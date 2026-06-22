
import json
import random
import re
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def resolve_path(path_str):
    return Path(path_str)

out_dir = resolve_path("outputs_improved")
out_dir.mkdir(exist_ok=True)

def get_synthetic_data(num_samples=100):
    base_comments = [
        "आज जीउदै छौ कसलाई के थाहा छ", "हास्ने बित्तिकै मन प्रसन्न हुन्छ",
        "सुरुमा सोचिने बित्तिकै …", "ज्याने गोलिमाल ...",
        "तिमीलाई थाहा छ यो कस्तो गरिबीको दिखाव हो",
        "अटल बीहारी अवीवाहीत थीए छोरी कहाँ बाट हुँन्छ", "समुदायको बिचलन ..."
    ]
    fillers = ["भए पनि", "साथै", "पनि", "जसरी", "ठीकै", "ब्युँज"]
    emojis = ["😂", "😡", "🤬", "🤢", "🙈", "😏"]
    
    metadata_pool = [
        {"Label_Binary": "NOFF", "Label_Multiclass": "NO"},
        {"Label_Binary": "OFF",  "Label_Multiclass": "OO"},
        {"Label_Binary": "OFF",  "Label_Multiclass": "OR"},
        {"Label_Binary": "OFF",  "Label_Multiclass": "OS"}
    ]
    
    synthetic = []
    for _ in range(num_samples):
        base = random.choice(base_comments)
        filler_noise = random.choice(fillers) if random.random() > 0.4 else ""
        emoji_noise = random.choice(emojis) if random.random() > 0.3 else ""
        
        comment_tokens = [base]
        if filler_noise: comment_tokens.append(filler_noise)
        if emoji_noise: comment_tokens.append(emoji_noise)
        final_comment = " ".join([t for t in comment_tokens if t])
        
        meta = random.choice(metadata_pool)
        synthetic.append({
            "ID": f"mock-{random.randint(100000, 999999)}",
            "Comment": final_comment,
            "Label_Binary": meta["Label_Binary"],
            "Label_Multiclass": meta["Label_Multiclass"]
        })
    return synthetic

# --- GRAPH VISUALIZATION PIPELINE ---
def plot_distributions(train_data, test_data, save_dir):
    """
    Generates a suite of 4 distinct visualization charts to review 
    the text properties and label mechanics across splits.
    """
    df_train = pd.DataFrame(train_data)
    df_train['Split'] = 'Train'
    df_test = pd.DataFrame(test_data)
    df_test['Split'] = f'Test (30% Subsample, N={len(test_data)})'
    df_all = pd.concat([df_train, df_test], axis=0)
    
    df_all['Word_Count'] = df_all['Comment'].apply(lambda x: len(str(x).split()))
    df_all['Char_Count'] = df_all['Comment'].apply(lambda x: len(str(x)))
    
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('📊 Multi-Dimensional Dataset Analytics Report (Subsampled Test)', fontsize=18, fontweight='bold')

    # GRAPH TYPE 1: Split-stratified Multiclass Countplot (Bar Chart)
    sns.countplot(data=df_all, x='Label_Multiclass', hue='Split', ax=axes[0, 0], palette='Set2')
    axes[0, 0].set_title('1. Multiclass Categorical Target Balance', fontsize=13, fontweight='bold')
    axes[0, 0].set_xlabel('Multiclass Label (NO, OO, OR, OS)')
    axes[0, 0].set_ylabel('Sample Frequency')

    # GRAPH TYPE 2: Crossed Hierarchical Facet Matrix (Stripplot)
    sns.stripplot(data=df_all, x='Label_Multiclass', y='Word_Count', hue='Label_Binary', 
                  ax=axes[0, 1], dodge=True, alpha=0.7, palette='tab10', size=7)
    axes[0, 1].set_title('2. Token Volumes Across Class Classifications', fontsize=13, fontweight='bold')
    axes[0, 1].set_xlabel('Multiclass Categories')
    axes[0, 1].set_ylabel('Words Per Comment String')

    # GRAPH TYPE 3: KDE Density Distribution (Kernel Density Estimation)
    sns.kdeplot(data=df_all, x='Char_Count', hue='Split', fill=True, common_norm=False, 
                ax=axes[1, 0], palette='crest', alpha=0.5, linewidth=2)
    axes[1, 0].set_title('3. Character Length Density Profiles', fontsize=13, fontweight='bold')
    axes[1, 0].set_xlabel('Total Character Array Count')
    axes[1, 0].set_ylabel('Probability Density')

    # GRAPH TYPE 4: Whiskered Outlier Boxplot
    sns.boxplot(data=df_all, x='Split', y='Word_Count', ax=axes[1, 1], palette='vlag', width=0.4)
    axes[1, 1].set_title('4. Text Length Quartile & Outlier Dispersion', fontsize=13, fontweight='bold')
    axes[1, 1].set_xlabel('Data Split Profile')
    axes[1, 1].set_ylabel('Word Length Distributions')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    report_path = Path(save_dir) / "dataset_analytics_report.png"
    plt.savefig(report_path, dpi=300)
    plt.close()
    print(f"📊 Matrix of graphs rendered and saved to: {report_path}")

# --- PATH AND ENVIRONMENT EXECUTION ---
train_json_path = resolve_path("/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_train.json")
test_json_path  = resolve_path("/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_test.json")

if not train_json_path.exists() or not test_json_path.exists():
    print("⚠️ Dataset files not found. Generating compliant synthetic instances...")
    train_json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(train_json_path, "w", encoding="utf-8") as f:
        json.dump(get_synthetic_data(150), f, indent=2, ensure_ascii=False)
    with open(test_json_path, "w", encoding="utf-8") as f:
        json.dump(get_synthetic_data(100), f, indent=2, ensure_ascii=False)
    print("✅ Schema-compliant synthetic baseline created.")

# Load full structural matrices
with open(train_json_path, 'r', encoding='utf-8') as f:
    train_samples = json.load(f)
with open(test_json_path, 'r', encoding='utf-8') as f:
    full_test_samples = json.load(f)

# --- 30% RANDOM SUBSAMPLING BLOCK ---
# Using a fixed seed for reproducible test evaluation slices
df_test_full = pd.DataFrame(full_test_samples)
df_test_subsampled = df_test_full.sample(frac=0.30, random_state=42)
test_samples = df_test_subsampled.to_dict(orient='records')

print(f"Loaded {len(train_samples)} train entries.")
print(f"Subsampled test set down to 30%: {len(test_samples)} rows selected out of {len(full_test_samples)} total.")

# Execute downstream graph suite using the sliced test dataset
plot_distributions(train_samples, test_samples, out_dir)