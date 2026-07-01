import json
import csv
import os
import random
import string

def load_ids_and_labels(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def apply_changes(data, csv_path):
    # Build mapping from ID to new labels
    changes = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            eid = row['ID']
            # Only apply if confidence is high? We'll apply all for now.
            changes[eid] = {
                'Label_Binary': row['Final_Binary'],
                'Label_Multiclass': row['Final_Multiclass']
            }
    # Apply changes
    for entry in data:
        eid = entry['ID']
        if eid in changes:
            entry['Label_Binary'] = changes[eid]['Label_Binary']
            entry['Label_Multiclass'] = changes[eid]['Label_Multiclass']
    return data

def balance_binary(data):
    # Count binary labels
    counts = {}
    for entry in data:
        b = entry['Label_Binary']
        counts[b] = counts.get(b, 0) + 1
    print(f"Current binary counts: {counts}")
    # Determine minority class
    if len(counts) < 2:
        return data
    # Find class with fewer samples
    minority_class = min(counts, key=lambda k: counts[k])
    majority_class = max(counts, key=lambda k: counts[k])
    needed = counts[majority_class] - counts[minority_class]
    print(f"Minority class: {minority_class} ({counts[minority_class]}), need {needed} more to balance.")
    if needed <= 0:
        return data
    # Collect samples of minority class
    minority_samples = [e for e in data if e['Label_Binary'] == minority_class]
    # We'll duplicate some of them, modifying ID slightly
    new_entries = []
    for i in range(needed):
        src = random.choice(minority_samples)
        # Create a copy
        new_entry = src.copy()
        # Generate new ID similar pattern: 6 lowercase letters
        while True:
            new_id = ''.join(random.choices(string.ascii_lowercase, k=6))
            # Ensure not colliding with existing IDs (optional)
            if new_id not in [e['ID'] for e in data]:
                break
        new_entry['ID'] = new_id
        # Keep labels same (minority class)
        new_entries.append(new_entry)
    data.extend(new_entries)
    print(f"Added {len(new_entries)} new entries.")
    return data

def main():
    base_dir = '/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/original_dataset'
    train_json = os.path.join(base_dir, 'train.json')
    test_json = os.path.join(base_dir, 'test (1).json')
    train_csv = '/home/sahild/Quantum/official_quantum/Mid-term Report/july_changes/reason_to_change_train.csv'
    test_csv = '/home/sahild/Quantum/official_quantum/Mid-term Report/july_changes/reason_to_change_test.csv'
    
    # Process train
    print("Processing train...")
    train_data = load_ids_and_labels(train_json)
    train_data = apply_changes(train_data, train_csv)
    # Balance
    train_data = balance_binary(train_data)
    # Save
    os.makedirs('/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/2nd_expand', exist_ok=True)
    out_train = '/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/2nd_expand/new_expand_train.json'
    with open(out_train, 'w', encoding='utf-8') as f:
        json.dump(train_data, f, ensure_ascii=False, indent=2)
    print(f"Saved train to {out_train}")
    
    # Process test
    print("\nProcessing test...")
    test_data = load_ids_and_labels(test_json)
    test_data = apply_changes(test_data, test_csv)
    test_data = balance_binary(test_data)
    out_test = '/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/2nd_expand/new_expand_test.json'
    with open(out_test, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    print(f"Saved test to {out_test}")

if __name__ == '__main__':
    main()
