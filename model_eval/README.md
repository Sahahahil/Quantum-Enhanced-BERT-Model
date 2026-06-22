# Model Evaluation

**Scope**

The `model_eval` directory captures the full experimental evaluation pipeline for all model variants explored in this project (classical BERT baselines, multilingual BERT, and quantum‑enhanced hybrids).

---

## Evaluation Architecture

1. **Notebook Driver** – Each major model family (e.g., `MBert`, `NepBERT`) provides a Jupyter notebook (`*.ipynb`) that:
   - Loads the processed dataset produced by `dataset_work/`.
   - Instantiates the model architecture (standard BERT, multilingual BERT, or VQC‑augmented MBERT).
   - Trains with a fixed random seed (`seed=42`) and logs training curves.
   - Generates predictions on a held‑out test split.
2. **Metrics Computation** – After inference, the notebook computes:
   - **Accuracy**
   - **Macro‑averaged F1**
   - **Precision‑Recall AUC**
   - **ROC AUC**
   - Confusion matrices for each class.
3. **Visualization** – Plots are saved under subfolders (`confusion_matrices/`, `pr_curves/`, `roc_curves/`, `comparison/`). All images are PNG for lossless rendering.
4. **Reporting** – Summary CSV/JSON files (`*_metrics.csv`, `summary_table.csv`) aggregate per‑class and macro metrics for downstream analysis.

---

## Directory Layout

```
model_eval/
├─ MBert/
│   ├─ MBERT.ipynb                # Core evaluation notebook
│   ├─ comparison/                # Accuracy / F1 comparison plots
│   ├─ confusion_matrices/         # PNG confusion matrices per classifier
│   ├─ pr_curves/                 # Precision‑Recall curves
│   └─ roc_curves/                # ROC curves
├─ NepBERT/
│   ├─ hate_speech_evaluation.png  # Overall evaluation visual
│   ├─ hate_speech_metrics.csv     # Detailed per‑class metrics
│   └─ summary_table.csv           # Aggregated results table
└─ VQC/
    ├─ Phase - 1/
    │   ├─ Combined_Quantum_VQC.pdf
    │   └─ phase1-VQC_Report.md
    └─ Phase - 2/
        ├─ Hyperparameter Tuning.docx
        ├─ part_1_quantum_create_embeddings.ipynb
        └─ part_2_improved.ipynb
```

---

## Reproducibility Checklist

- **Random Seeds**: All notebooks set `torch.manual_seed(42)` and `numpy.random.seed(42)`.
- **Environment Capture**: `requirements.txt` pins exact library versions; the notebook logs the `pip freeze` output to `environment.txt`.
- **Data Versioning**: The notebook reads from the immutable `dataset_work` commit hash, ensuring consistent inputs.
- **Artifact Tracking**: Every generated plot or CSV is committed back to the repository (see commit history) for full provenance.

---

## Running an Evaluation

```bash
# Activate environment
source .venv/bin/activate

# Launch the MBERT evaluation notebook
jupyter notebook model_eval/MBert/MBERT.ipynb
```

Execute all cells sequentially; the final cells will write metrics and plots to the appropriate subfolders.

---

## Extending the Suite

- **New Model Variants** – Add a sibling directory under `model_eval/` with its own notebook and follow the same metric/reporting conventions.
- **Custom Metrics** – Extend the notebook's metric block with additional functions (e.g., Matthews correlation coefficient) and add columns to the summary CSV.
- **Batch Evaluation** – Use the provided `run_all_evals.sh` script (if present) to loop over all model directories automatically.

---

*All evaluation artefacts are version‑controlled to provide a complete audit trail for research reproducibility.*

## Overview
This folder contains all artifacts produced when evaluating the various BERT‑based models in the project. It includes Jupyter notebooks that drive the evaluation pipelines and the resulting visualizations such as confusion matrices, precision‑recall curves, ROC curves, and comparative performance plots.

## Folder Structure
```
model_eval/
├─ MBert/
│  ├─ MBERT.ipynb                # Notebook driving MBERT evaluation
│  ├─ comparison/                # Comparative plots (accuracy, F1, etc.)
│  ├─ confusion_matrices/         # Confusion matrix images for each classifier
│  ├─ pr_curves/                  # Precision‑Recall curve images
│  └─ roc_curves/                 # ROC curve images
├─ NepBERT/
│  ├─ hate_speech_evaluation.png  # Overall evaluation image
│  ├─ hate_speech_metrics.csv     # Metric values per class
│  └─ summary_table.csv           # Summary of results
└─ VQC/
   ├─ Phase - 1/
   │   ├─ Combined_Quantum_VQC.pdf
   │   └─ phase1-VQC_Report.md
   └─ Phase - 2/
       ├─ Hyperparameter Tuning.docx
       ├─ part_1_quantum_create_embeddings.ipynb
       └─ part_2_improved.ipynb
```

## Typical Workflow
- Open the notebook for the model you wish to evaluate.
- Execute the cells to reproduce the evaluation and generate the plots.
- Review the images in the subfolders to compare model performance across metrics.

All visual assets are kept alongside the notebooks that generated them for easy traceability.
