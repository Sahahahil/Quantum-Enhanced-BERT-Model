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

# Regex for fast normalization replacement
normalization_pattern = re.compile(
    "|".join(map(re.escape, NORMALIZATION_MAP.keys()))
)

# Emoji removal regex
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # geometric shapes extended
    "\U0001F800-\U0001F8FF"  # supplemental arrows
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA00-\U0001FA6F"  # chess, symbols
    "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended
    "\U00002700-\U000027BF"  # dingbats
    "\U00002600-\U000026FF"  # miscellaneous symbols
    "\U0000FE0F"             # variation selector
    "\U0000200D"             # zero-width joiner
    "]+",
    flags=re.UNICODE,
)


def normalize_nepali(text):
    """
    Apply Dirghikaran normalization.
    """
    return normalization_pattern.sub(
        lambda m: NORMALIZATION_MAP[m.group(0)], text
    )


def remove_emojis(text):
    """
    Remove emojis and related Unicode symbols.
    """
    return emoji_pattern.sub("", text)


# Load dataset
with open(
    "/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/original_dataset/test (1).json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

# Process comments
for item in data:
    if "Comment" in item and isinstance(item["Comment"], str):
        text = item["Comment"]
        text = remove_emojis(text)      # Remove emojis
        text = normalize_nepali(text)   # Apply normalization
        item["Comment"] = text.strip()

# Save processed dataset
with open(
    "/home/sahild/Quantum/ForGithub/Quantum-Enhanced-BERT-Model/dataset_work/emoji-scene/original_test_Noemo.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Normalization and emoji removal complete.")