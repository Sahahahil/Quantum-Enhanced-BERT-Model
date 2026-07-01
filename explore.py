import json
import csv
import os

print("Loading train.json...")
with open('dataset_work/original_dataset/train.json', 'r', encoding='utf-8') as f:
    train_data = json.load(f)
print(f"Train entries: {len(train_data)}")

print("Loading test (1).json...")
with open('dataset_work/original_dataset/test (1).json', 'r', encoding='utf-8') as f:
    test_data = json.load(f)
print(f"Test entries: {len(test_data)}")

# Combine for analysis
all_data = train_data + test_data

# Count binary labels
binary_counts = {}
multiclass_counts = {}
for entry in all_data:
    b = entry['Label_Binary']
    m = entry['Label_Multiclass']
    binary_counts[b] = binary_counts.get(b, 0) + 1
    multiclass_counts[m] = multiclass_counts.get(m, 0) + 1

print("\nBinary label counts:")
for k, v in sorted(binary_counts.items()):
    print(f"  {k}: {v}")

print("\nMulticlass label counts:")
for k, v in sorted(multiclass_counts.items()):
    print(f"  {k}: {v}")

# Check ID pattern
ids = [entry['ID'] for entry in all_data]
print(f"\nSample IDs: {ids[:5]}")
# Check length and chars
if ids:
    sample = ids[0]
    print(f"ID length: {len(sample)}")
    print(f"ID chars: {set(sample)}")
