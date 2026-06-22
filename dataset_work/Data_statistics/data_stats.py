import json
import re
from pathlib import Path
import pandas as pd
import numpy as np

def load_to_dataframe(file_path, phase_name):
    """Loads a JSON dataset and converts it into a structured DataFrame with engineered text features."""
    path = Path(file_path)
    if not path.exists():
        print(f"⚠️ Warning: File not found at {path.absolute()}")
        return None
        
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    df["Phase"] = phase_name
    
    # Feature Engineering for Text Statistics
    df["Char_Count"] = df["Comment"].apply(lambda x: len(str(x)))
    df["Word_Count"] = df["Comment"].apply(lambda x: len(str(x).split()))
    
    # Simple regex tracking for high-density emoji matching
    # Captures standard emoji blocks found in social media texts
    emoji_pattern = re.compile(r"[\u2000-\u3300|\ud83c-\ud83e][\ud000-\udfff]*", flags=re.UNICODE)
    df["Has_Emoji"] = df["Comment"].apply(lambda x: 1 if emoji_pattern.search(str(x)) else 0)
    
    return df

def calculate_vocabulary_stats(df):
    """Computes distinct token sets to calculate lexical diversity ratios."""
    all_words = []
    df["Comment"].apply(lambda x: all_words.extend(str(x).lower().split()))
    
    total_tokens = len(all_words)
    unique_tokens = len(set(all_words))
    # Type-Token Ratio (TTR) measures vocabulary richness (Closer to 1 = More diverse vocabulary)
    lexical_diversity = unique_tokens / total_tokens if total_tokens > 0 else 0
    
    return total_tokens, unique_tokens, lexical_diversity

def run_pipeline_statistics(dataset_map):
    """Iterates through dataset paths, compiles descriptive statistics, and prints a comparative report."""
    dfs = []
    for label, path in dataset_map.items():
        df = load_to_dataframe(path, label)
        if df is not None:
            dfs.append(df)
            
    if not dfs:
        print("❌ No data frames could be recovered. Check file pathways.")
        return
        
    print("==========================================================================")
    print("       📊 COMPREHENSIVE PIPELINE DATASET STATISTICS REPORT                ")
    print("==========================================================================\n")
    
    for df in dfs:
        phase = df["Phase"].iloc[0]
        total_rows = len(df)
        print(f"--- [ {phase.upper()} ] (Total Records: {total_rows}) ---")
        
        # 1. Target Label Configurations
        print("\n📍 Target Label Distribution Balance:")
        if "Label_Binary" in df.columns:
            binary_counts = df["Label_Binary"].value_counts()
            binary_pct = df["Label_Binary"].value_counts(normalize=True) * 100
            print("   • Binary Classes:")
            for idx in binary_counts.index:
                print(f"     - {idx}: {binary_counts[idx]} ({binary_pct[idx]:.2f}%)")
                
        if "Label_Multiclass" in df.columns:
            multi_counts = df["Label_Multiclass"].value_counts()
            multi_pct = df["Label_Multiclass"].value_counts(normalize=True) * 100
            print("   • Multiclass Subcategories:")
            for idx in multi_counts.index:
                print(f"     - {idx}: {multi_counts[idx]} ({multi_pct[idx]:.2f}%)")
                
        # 2. Sequence Length Distribution Analysis
        print("\n📏 Sequence Length Statistics:")
        print(f"   • Word Distribution  -> Mean: {df['Word_Count'].mean():.2f} | Median: {df['Word_Count'].median()} | Max: {df['Word_Count'].max()} | Std: {df['Word_Count'].std():.2f}")
        print(f"   • Char Distribution  -> Mean: {df['Char_Count'].mean():.2f} | Median: {df['Char_Count'].median()} | Max: {df['Char_Count'].max()} | Std: {df['Char_Count'].std():.2f}")
        
        # 3. Vocabulary Richness Metrics
        tot_tok, uniq_tok, lex_div = calculate_vocabulary_stats(df)
        print("\n🔤 Lexical Features & Vocabulary Volume:")
        print(f"   • Total Runtime Tokens : {tot_tok}")
        print(f"   • Unique Vocabulary Size: {uniq_tok}")
        print(f"   • Lexical Diversity TTR : {lex_div:.4f}")
        
        # 4. Phase-Specific Perturbation Diagnostics
        emoji_pct = (df["Has_Emoji"].sum() / total_rows) * 100
        print(f"   • Emojis Density Profile: {emoji_pct:.2f}% of comments contain emojis")
        print("-" * 74 + "\n")

# --- EXECUTION RUNTIME ---
if __name__ == "__main__":
    # Path routing lookup configurations
    base_dir = "/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset"
    
    target_datasets = {
        "Phase 1: Raw Training Set": f"/home/sahild/Quantum/official_quantum/Mid-term Report/nepali-offensive-lang-detection-dataset//train.json",
        "Phase 1: Raw Testing Set": f"/home/sahild/Quantum/official_quantum/Mid-term Report/nepali-offensive-lang-detection-dataset//test.json",
        "Phase 2: Normalized Training Set": f"dataset/updated_train.json",
        "Phase 2: Normalized Testing Set": f"dataset/updated_test.json",
        "Phase 3: Expanded Training Set": f"/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_train.json",
        "Phase 3: Expanded Testing Set": f"/home/sahild/Quantum/May-2026/Series/13-june-2026/dataset/dataset/expand_test.json",
    }
    
    run_pipeline_statistics(target_datasets)