# Model Evaluation

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
