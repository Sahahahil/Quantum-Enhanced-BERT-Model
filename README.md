# Quantum‑Enhanced BERT for Nepali Offensive Speech Detection

**Repository Overview**

This project implements a hybrid classical‑quantum machine‑learning pipeline for low‑resource Nepali offensive speech detection. It combines multilingual BERT embeddings with variational quantum circuits (VQCs) to explore quantum advantage in NLP classification.

---

## Architecture

- **Data Ingestion & Pre‑processing** – Raw Nepali social‑media posts are cleaned, normalised, balanced, and optionally augmented. See `dataset_work/` for the modular stages.
- **Feature Extraction** – Tokenisation and embedding extraction using `transformers` (multilingual BERT). Embeddings are fed to a classical dense classifier or projected into a quantum feature space via Pennylane‑Qiskit VQC layers.
- **Quantum Layer** – Parameterised quantum circuits implemented with Pennylane; gradient‑based optimisation via the parameter‑shift rule.
- **Classification Head** – Final logits are produced by a hybrid classifier (classical + quantum) and evaluated with standard metrics.

---

## Repository Structure

```
Quantum-Enhanced-BERT-Model/
├─ dataset_work/          # Data pipeline scripts & logs
│   ├─ original_dataset/ # Raw source data
│   ├─ cleaning/          # Cleaning utilities
│   ├─ normalizing/       # Normalisation scripts
│   ├─ balancing/         # Class‑balancing tools
│   └─ augmentation/     # Data‑augmentation modules
├─ model_eval/            # Evaluation notebooks, metrics, visualisations
│   ├─ MBert/             # Baseline BERT evaluation
│   ├─ NepBERT/           # Alternative model results
│   └─ VQC/               # Quantum‑circuit experiments
├─ research_proposal/     # Literature survey & proposal documents
├─ requirements.txt       # Python dependencies
├─ README.md              # (this file)
└─ LICENSE                # License
```

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your‑username>/Quantum-Enhanced-BERT-Model.git
   cd Quantum-Enhanced-BERT-Model
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare the data**
   - Place raw JSON datasets in `dataset_work/original_dataset/`.
   - Execute the processing scripts in logical order (`cleaning → normalizing → balancing → augmentation`). Each script logs progress to its respective folder.
5. **Run the evaluation notebook**
   ```bash
   jupyter notebook model_eval/MBert/MBERT.ipynb
   ```
   The notebook reproduces the full training/evaluation pipeline, including optional quantum circuit execution.

---

## Evaluation Methodology

- **Metrics**: Accuracy, macro‑averaged F1, Precision‑Recall AUC, ROC‑AUC.
- **Cross‑validation**: 5‑fold stratified split on the processed dataset.
- **Statistical Significance**: Paired t‑test between classical and hybrid models.
- **Reproducibility**: Random seeds are fixed (`seed=42`) and all intermediate artefacts (confusion matrices, PR/ROC curves) are versioned under `model_eval/`.

---

## References & Further Reading

- *Pennylane Documentation*: https://pennylane.ai
- *Qiskit Documentation*: https://qiskit.org
- *BERT Paper*: Devlin et al., 2018
- *Quantum Machine Learning Survey*: Schuld & Petruccione, 2021

---

*Contributions are welcome via pull‑requests. For questions, open an issue or contact the repository owner.*

*Hybrid classical‑quantum machine‑learning pipeline for low‑resource NLP*  

---

## 📖 Overview

This repository provides a reproducible research framework that combines **pre‑trained multilingual BERT embeddings** with **variational quantum circuits (VQCs)** to classify Nepali social‑media text as offensive or non‑offensive. The codebase is deliberately modular: data preparation, feature engineering, model training, and evaluation are each encapsulated in separate directories.

---

## 📂 Repository Structure

```
Quantum-Enhanced-BERT-Model/
├─ dataset_work/                 # Data acquisition, cleaning, normalisation, and synthetic augmentation
│   ├─ annotation_report/        # Annotated train / test splits (JSON)
│   ├─ balanced_datasets/       # Class‑balancing utilities & diagnostic plots
│   ├─ cleaned_dataset/          # Logs generated during cleaning steps
│   ├─ Data_statistics/          # Scripts that compute basic corpus statistics
│   ├─ expanded_dataset/         # Expanded/augmented versions of the original data
│   ├─ formatting/               # CSV ↔ JSON conversion helpers
│   ├─ normalizing/              # Nepali‑specific character normalisation
│   ├─ original_dataset/        # Raw source files and licence information
│   └─ translating/              # Translated variants of the dataset
├─ model_eval/                  # Evaluation notebooks, plots, and result artefacts
│   ├─ MBert/                    # MBERT evaluation notebook & visualisations
│   ├─ NepBERT/                  # Alternative model results
│   └─ VQC/                      # Quantum‑circuit experiments (PDF reports & notebooks)
├─ research_proposal/           # Background literature, proposal notes, and quantum lab resources
│   ├─ BERT_foundation/         # Core BERT concepts and input‑output design docs
│   ├─ M_BERT/                  # Links to specialised BERT variants
│   ├─ NLP_notes/                # Word‑representation and background theory
│   ├─ Quantum_labs/             # PennyLane tutorials and quantum‑operations PDFs
│   ├─ Quantum_Notes/            # High‑level quantum reports and handwritten sketches
│   ├─ runpod/                   # Instructions for cloud‑based training runs
│   └─ Transformer_NOTES/        # Transformer fundamentals and related papers
├─ requirements.txt             # Python dependencies for the whole project
├─ README.md                    # (this file)
└─ LICENSE                      # Project licence
```

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your‑username>/Quantum-Enhanced-BERT-Model.git
   cd Quantum-Enhanced-BERT-Model
   ```
2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```
3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare the data**
   - Place the raw Nepali dataset (JSON files) under `dataset_work/original_dataset/`.
   - Run the data‑pre‑processing scripts in `dataset_work/` in the order they appear (cleaning → normalising → balancing → expanding). Each script prints a short status line and writes logs to its respective folder.
5. **Run the evaluation notebook**
   ```bash
   jupyter notebook model_eval/MBert/MBERT.ipynb
   ```
   The notebook will load the prepared data, train the MBERT baseline, optionally invoke the VQC layers, and generate the plots saved under `model_eval/MBert/`.

---

## 📦 Dependencies

All required packages are listed in `requirements.txt`. The core stack includes:
- **pandas**, **numpy** – data handling
- **matplotlib**, **seaborn** – visualisation
- **torch**, **transformers** – BERT model implementation
- **pennylane**, **qiskit** – quantum circuit simulation
- **jupyter** – notebook environment

Optional packages for extended experiments (e.g., GPU acceleration, advanced quantum back‑ends) can be installed as needed.

---


*For any questions or to discuss collaboration opportunities, please open an issue or contact the repository owner.*