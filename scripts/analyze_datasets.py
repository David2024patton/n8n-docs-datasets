#!/usr/bin/env python3
"""
n8n Dataset Analyzer

Analyzes n8n workflow training datasets to provide statistics,
detect duplicates, and identify patterns.

Usage:
    python analyze_datasets.py [dataset_file]
    python analyze_datasets.py  # Analyzes all datasets
"""

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Any
import hashlib


def load_dataset(filepath: Path) -> List[Dict]:
    """Load and parse a dataset JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing {filepath.name}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error loading {filepath.name}: {e}")
        return None


def extract_workflow(example: Dict) -> Dict:
    """Extract workflow JSON from assistant message."""
    try:
        messages = example.get('messages', [])
        for msg in messages:
            if msg.get('role') == 'assistant':
                content = msg.get('content', '')
                return json.loads(content)
    except:
        return None
    return None


def analyze_dataset(filepath: Path) -> Dict[str, Any]:
    """Analyze a single dataset file."""
    print(f"\n{'='*60}")
    print(f"📊 Analyzing: {filepath.name}")
    print(f"{'='*60}")
    
    data = load_dataset(filepath)
    if data is None:
        return None
    
    stats = {
        'filename': filepath.name,
        'total_examples': len(data),
        'file_size_mb': filepath.stat().st_size / (1024 * 1024),
        'duplicates': 0,
        'node_types': Counter(),
        'workflow_patterns': Counter(),
        'unique_hashes': set(),
        'duplicate_examples': []
    }
    
    # Analyze each example
    for idx, example in enumerate(data):
        # Check for duplicates using hash
        example_str = json.dumps(example, sort_keys=True)
        example_hash = hashlib.md5(example_str.encode()).hexdigest()
        
        if example_hash in stats['unique_hashes']:
            stats['duplicates'] += 1
            stats['duplicate_examples'].append(idx)
        else:
            stats['unique_hashes'].add(example_hash)
        
        # Extract workflow to analyze nodes
        workflow = extract_workflow(example)
        if workflow:
            nodes = workflow.get('nodes', [])
            for node in nodes:
                node_type = node.get('type', 'unknown')
                stats['node_types'][node_type] += 1
                
            # Identify workflow patterns (source -> target apps)
            if len(nodes) >= 2:
                source_type = nodes[0].get('type', '').split('.')[-1]
                target_type = nodes[-1].get('type', '').split('.')[-1]
                pattern = f"{source_type} → {target_type}"
                stats['workflow_patterns'][pattern] += 1
    
    # Print statistics
    print(f"\n📈 Statistics:")
    print(f"   Total Examples: {stats['total_examples']:,}")
    print(f"   File Size: {stats['file_size_mb']:.2f} MB")
    print(f"   Unique Examples: {stats['total_examples'] - stats['duplicates']:,}")
    print(f"   Duplicates: {stats['duplicates']:,} ({stats['duplicates']/stats['total_examples']*100:.1f}%)")
    
    print(f"\n🔧 Top 10 Node Types:")
    for node_type, count in stats['node_types'].most_common(10):
        short_name = node_type.split('.')[-1]
        print(f"   {short_name:30s} {count:>5,} uses")
    
    print(f"\n🔀 Top 10 Workflow Patterns:")
    for pattern, count in stats['workflow_patterns'].most_common(10):
        print(f"   {pattern:40s} {count:>4,} workflows")
    
    if stats['duplicates'] > 0:
        print(f"\n⚠️  Duplicate Example Indices (first 10):")
        for idx in stats['duplicate_examples'][:10]:
            print(f"   Index {idx}")
        if len(stats['duplicate_examples']) > 10:
            print(f"   ... and {len(stats['duplicate_examples']) - 10} more")
    
    return stats


def create_deduped_dataset(filepath: Path, output_path: Path):
    """Create a deduplicated version of the dataset."""
    data = load_dataset(filepath)
    if data is None:
        return
    
    unique_data = []
    seen_hashes = set()
    
    for example in data:
        example_str = json.dumps(example, sort_keys=True)
        example_hash = hashlib.md5(example_str.encode()).hexdigest()
        
        if example_hash not in seen_hashes:
            unique_data.append(example)
            seen_hashes.add(example_hash)
    
    # Write deduplicated data
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, indent=2)
    
    original_count = len(data)
    deduped_count = len(unique_data)
    removed = original_count - deduped_count
    
    print(f"\n✅ Created deduplicated file: {output_path.name}")
    print(f"   Original: {original_count:,} examples")
    print(f"   Deduplicated: {deduped_count:,} examples")
    print(f"   Removed: {removed:,} duplicates ({removed/original_count*100:.1f}%)")


def main():
    """Main analysis function."""
    # Find datasets directory
    datasets_dir = Path(__file__).parent.parent / 'datasets'
    
    if not datasets_dir.exists():
        print(f"❌ Datasets directory not found: {datasets_dir}")
        return
    
    # Get dataset files
    if len(sys.argv) > 1:
        dataset_files = [datasets_dir / sys.argv[1]]
    else:
        dataset_files = sorted(datasets_dir.glob('dataset_*.json'))
    
    if not dataset_files:
        print("❌ No dataset files found")
        return
    
    print(f"\n🔍 n8n Dataset Analyzer")
    print(f"Found {len(dataset_files)} dataset file(s)")
    
    all_stats = []
    for filepath in dataset_files:
        stats = analyze_dataset(filepath)
        if stats:
            all_stats.append(stats)
    
    # Summary across all datasets
    if len(all_stats) > 1:
        print(f"\n{'='*60}")
        print(f"📊 Overall Summary")
        print(f"{'='*60}")
        total_examples = sum(s['total_examples'] for s in all_stats)
        total_duplicates = sum(s['duplicates'] for s in all_stats)
        total_size_mb = sum(s['file_size_mb'] for s in all_stats)
        
        print(f"   Total Files: {len(all_stats)}")
        print(f"   Total Examples: {total_examples:,}")
        print(f"   Total Duplicates: {total_duplicates:,}")
        print(f"   Total Size: {total_size_mb:.2f} MB")
        print(f"   Duplicate Rate: {total_duplicates/total_examples*100:.1f}%")
    
    # Offer to create deduplicated versions
    print(f"\n{'='*60}")
    create_deduped = input("Create deduplicated versions? (y/n): ").strip().lower()
    
    if create_deduped == 'y':
        for filepath in dataset_files:
            if filepath.exists():
                output_path = filepath.parent / f"{filepath.stem}_deduped.json"
                create_deduped_dataset(filepath, output_path)
        print("\n✅ Deduplication complete!")
    
    print(f"\n{'='*60}")
    print("Analysis complete! 🎉")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
