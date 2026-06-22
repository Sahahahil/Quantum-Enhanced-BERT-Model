# Dataset Work

**Purpose**

The `dataset_work` directory implements a fully reproducible data pipeline for the Nepali offensive speech detection task. Each subdirectory corresponds to a distinct processing stage, allowing independent execution or full‑pipeline runs.

---

## Pipeline Stages

| Subdirectory | Role | Key Artifacts |
|--------------|------|----------------|
| `original_dataset/` | Stores the untouched raw Nepali corpus (JSON) and licensing information. | `*.json`, `LICENSE.txt` |
| `annotation_report/` | Manually annotated train/test splits with offensive labels. | `*.json` |
| `cleaned_dataset/` | Scripts remove HTML artefacts, non‑UTF8 characters, and language‑specific noise. Logs (`log.txt`) record removal statistics. | `log.txt`, cleaned copies |
| `normalizing/` | Applies Nepali‑specific Unicode normalisation (NFKC) and token‑level normalisation (e.g., handling of diacritics). | Normalised CSV/JSON files |
| `balanced_datasets/` | Implements class‑balancing via under‑sampling, over‑sampling, and SMOTE. Generates diagnostic plots (`*.png`). | `*.py`, `*.png` |
| `expanded_dataset/` | Augments data through back‑translation and synonym replacement. Includes augmentation logs. | `expand_*.json`, `log.txt` |
| `formatting/` | Utilities for round‑tripping between CSV and JSON, preserving schema integrity. | `csv_to_json.py`, `json_to_csv.py` |
| `translating/` | Stores translated variants of the dataset (e.g., English translations) and associated metadata. | `*.json`, `info.txt` |

---

## Typical Usage Workflow

```bash
# 1. Copy raw data
cp path/to/raw/*.json dataset_work/original_dataset/

# 2. Clean data
python dataset_work/cleaning/clean_data.py

# 3. Normalise Unicode representations
python dataset_work/normalizing/normalize.py

# 4. Balance classes
python dataset_work/balanced_datasets/balance.py

# 5. Optional augmentation
python dataset_work/expanded_dataset/augment.py
```

Each script writes a concise `log.txt` in its folder, providing traceability for downstream experiments.

---

## Extending the Pipeline

- **Custom preprocessing**: Add a new module under `dataset_work/` and update the master `pipeline.sh` (if present).
- **Logging standards**: Follow the `key: value` format used in existing logs for seamless aggregation.
- **Reproducibility**: Seed any stochastic operation with `--seed 42` to ensure deterministic outputs across runs.

---

*All artefacts are versioned; commit any new scripts or logs to maintain a complete provenance chain.*

## Overview
This directory gathers everything related to the data pipeline for the project. It holds the original raw datasets, intermediate processed versions, and the scripts used to clean, normalize, balance, expand, and convert the data. Log files are kept alongside each step to provide a simple audit trail.

## Folder Structure
```
dataset_work/
├─ annotation_report/        # JSON files containing annotated data splits
├─ balanced_datasets/       # Scripts and visual reports for class‑balancing
├─ cleaned_dataset/          # Logs from the cleaning stage
├─ Data_statistics/          # Scripts that compute basic statistics and their outputs
├─ expanded_dataset/        # Expanded versions of the original data and related documentation
├─ formatting/              # Utilities for converting between CSV and JSON
├─ normalizing/             # Normalization scripts and normalized data copies
├─ original_dataset/        # The untouched source data and licensing information
└─ translating/              # Translated versions of the dataset and accompanying notes
```

## Typical Usage
- Run the cleaning script to generate a cleaned copy.
- Use the normalizing utilities to produce a consistent format.
- Apply balancing scripts if class distribution needs adjustment.
- Expand or translate the dataset as required for downstream experiments.

The layout is intentionally modular so that each processing stage can be executed independently or in sequence.

