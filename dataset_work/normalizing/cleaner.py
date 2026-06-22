import json
import re

# Character-level normalization mappings
NORMALIZATION_MAP = {
    "ि": "ी",
    "ु": "ू",
    "ॅ": "े",
    "श": "स",
    "ष": "स",
    "ृ": "रि",
    "ऋ": "रि",
    "ँ": "ं",
    "ई": "इ",
    "ऊ": "उ",
    "ै": "े",
    "ौ": "ो",
    "ण": "न",
}

# Regex for fast replacement
pattern = re.compile("|".join(map(re.escape, NORMALIZATION_MAP.keys())))

def normalize_nepali(text):
    """
    Apply Dirghikaran normalization from the paper.
    """
    return pattern.sub(lambda m: NORMALIZATION_MAP[m.group(0)], text)

# Load dataset
with open(
    "/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_test.json",
    "r",
    encoding="utf-8",
) as f: 
    data = json.load(f)

# Normalize comments in-place
for item in data:
    if "Comment" in item and isinstance(item["Comment"], str):
        item["Comment"] = normalize_nepali(item["Comment"])

# Save normalized dataset
with open(
    "/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_test_normalized.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Normalization complete.")