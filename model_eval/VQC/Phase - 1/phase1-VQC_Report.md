# VQC Training Report

Date: 2026-03-31
Project: Hybrid mBERT + VQC for Nepali Hate Speech Classification

## 1) Scope and Inputs

This report is built from:

- Training notebook/script: vqc/vqc_nepali_optimized.ipynb
- Experiment outputs in:
  - vqc/Graphs/take-1
  - vqc/Graphs/take-2
  - vqc/Graphs/take-3
  - vqc/Graphs/take-4
- Model checkpoints in:
  - vqc/models/take-1/vqc_nepali_hate.pt
  - vqc/models/take-2/vqc_nepali_hate.pt
  - vqc/models/take-3/vqc_nepali_hate.pt
  - vqc/models/take-4/vqc_nepali_hate.pt

Artifacts found:
- 4 take folders with classification_metrics.csv
- 3 take folders with training_history.json (takes 2, 3, 4)
- Curves, confusion matrices, class-distribution plots in all takes
- overfitting_monitor.png available in takes 2 and 3
- training_overview.* additionally available in take 4

## 2) Model and Training Pipeline (from script)

## 2.1 Architecture

Hybrid architecture:

1. Frozen mBERT encoder (bert-base-multilingual-cased) extracts CLS embedding (768)
2. Deep projection head: 768 -> 256 -> 64 -> n_qubits (tanh)
3. Variational quantum layer (PennyLane TorchLayer)
4. Residual classical path around quantum layer
5. Concatenation of quantum output and residual features
6. Classifier head: (2 x n_qubits) -> 32 -> num_classes

Configured quantum design in the optimized notebook:
- n_qubits = 6
- n_layers = 3
- quantum parameters = 6 x 3 x 3 = 54
- measurement: Pauli-Z expectation per qubit
- device: default.qubit with backprop for batched compatibility

Observed model size printout in notebook:
- Total / trainable params: 215062 / 215062
- Classical params: 215008
- Quantum params: 54

## 2.2 Loss, Optimization, and Regularization

- Loss: Focal Loss (gamma = 2.0) with effective-number class weighting and label smoothing
- Optimizer: AdamW with split learning rates
  - Classical: LR = 5e-4
  - Quantum: LR = 2.5e-5 (LR x 0.05)
- Scheduler: ReduceLROnPlateau (factor 0.5, patience 3)
- Gradient clipping: max_norm = 1.0
- Gradient accumulation supported (default 2; higher in low-end mode)
- Early stopping configured with patience = 10
- Oversampling enabled with capped ratio (MAX_OVERSAMPLE_RATIO = 5)

## 2.3 Data Profile and Imbalance

Common test support (all takes):
- NO: 895
- OO: 487
- OR: 49
- OS: 19

The dataset is strongly imbalanced, with OR and OS as minority classes.

## 3) Quantitative Results by Take

Metric source: each take's classification_metrics.csv.

| Take | Accuracy (Weighted Recall) | Macro F1 | Weighted F1 | NO F1 | OO F1 | OR F1 | OS F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Take-1 | 71.03% | 0.3419 | 0.6847 | 0.8008 | 0.5669 | 0.0000 | 0.0000 |
| Take-2 | 53.86% | 0.2361 | 0.4727 | 0.7574 | 0.0000 | 0.1324 | 0.0545 |
| Take-3 | 33.59% | 0.1257 | 0.1689 | 0.0000 | 0.5028 | 0.0000 | 0.0000 |
| Take-4 | 61.93% | 0.2247 | 0.5151 | 0.7580 | 0.1408 | 0.0000 | 0.0000 |

### Key ranking by overall accuracy

1. Take-1: 71.03%
2. Take-4: 61.93%
3. Take-2: 53.86%
4. Take-3: 33.59%

### Key ranking by macro F1 (class-balance aware)

1. Take-1: 0.3419
2. Take-2: 0.2361
3. Take-4: 0.2247
4. Take-3: 0.1257

Important: all runs struggle badly on minority classes OR and OS. Even the best overall run still has OR/OS F1 = 0.

## 4) Training Dynamics (from history files and plots)

## 4.1 Take-2 (history available)
- Epochs run: 8
- Best validation accuracy: 53.86% at epoch 4
- Train loss decreases steadily (1.64 -> 1.40)
- Validation loss stays high and nearly flat (around 1.74 to 1.79)
- Validation accuracy is unstable (approx 30% to 54%)

Interpretation:
- Model learns some train signal but generalization is weak and noisy.
- Confusion plot shows spread into NO/OR/OS, but OO class is effectively not learned (OO F1 = 0).

## 4.2 Take-3 (history available)
- Epochs run: 6
- Best validation accuracy: 33.59% at epoch 1
- Train loss decreases, but validation loss worsens (up to ~1.87)
- Validation accuracy collapses to near-random/degenerate behavior in multiple epochs

Interpretation:
- Strong class-collapse symptoms.
- Confusion matrix indicates near single-class prediction behavior (dominant prediction to OO).
- This is the most unstable and least useful run.

## 4.3 Take-4 (history available)
- Epochs run: 14
- Best validation accuracy: 61.93% at epoch 4
- Train loss quickly drops then plateaus (~0.42)
- Validation loss remains low (~0.31 to 0.33)
- Validation accuracy shows bimodal switching: around 4% in some epochs and around 61.7% in others

Interpretation:
- Optimization appears numerically stable, but decision behavior is unstable and threshold-like.
- Confusion and per-class bars show concentration on NO/OO with OR/OS still not recognized.
- Likely partial class-collapse or decision-boundary instability rather than clean convergence.

## 4.4 Take-1 (no training_history.json)
- Final metrics are strongest overall (71.03% accuracy, 0.6847 weighted F1)
- Confusion/per-class plots show performance concentrated in NO and OO
- OR and OS remain unlearned (both F1 = 0)

Interpretation:
- Best aggregate score among recorded takes, but still fails minority-class detection.

## 5) What the Plots Show Across Runs

## 5.1 Confusion matrices
Common pattern across takes:
- Correct predictions are dominated by NO (and partly OO in some runs)
- OR and OS are mostly mapped into majority classes
- Some runs collapse to predicting a single class for most/all samples

## 5.2 Per-class metric bars
- NO is consistently strongest
- OO varies significantly by take
- OR and OS are near-zero in almost all takes

## 5.3 Class-distribution plots
- Test distribution is always heavily imbalanced (NO and OO dominate)
- Training distribution differs by take depending on oversampling strength
- Even with oversampling, minority transfer to test performance is limited

## 5.4 Loss/accuracy curves and overfitting monitors
- Several runs show widening train-val behavior mismatch or oscillatory validation trajectories
- Validation accuracy jumps suggest unstable decision boundaries or collapse/recovery cycles

## 6) Checkpoint and Artifact Notes

Checkpoint file sizes:
- take-1: 48 KB
- take-2: 48 KB
- take-3: 1184 KB
- take-4: 2548 KB

Observation:
- Large size variation likely indicates differences in what was serialized per run (for example, minimal state dict versus broader checkpoint payload).

## 7) Overall Findings

1. Best top-line result is Take-1 (71.03% accuracy), but it still ignores minority classes OR and OS.
2. Take-4 is the most complete artifact set and appears to correspond to the optimized script design, but still suffers minority-class failure and oscillatory validation behavior.
3. Take-3 shows clear collapse to degenerate predictions and should not be used as baseline.
4. Across all takes, macro performance remains low because minority classes are not being learned robustly.

## 8) Actionable Recommendations

## 8.1 Data and sampling
- Move from simple capped oversampling to class-balanced batch sampling each step.
- Add targeted augmentation for OR and OS (text-level paraphrase, synonym, noise, emoji/context-preserving variants).
- Verify label quality for OR/OS; small noisy classes can destroy minority learning.

## 8.2 Objective and calibration
- Keep focal loss, but tune gamma and alpha using macro-F1 on validation as selection metric.
- Remove/reduce label smoothing for minority-sensitive runs if it suppresses rare-class margins.
- Add per-class threshold calibration on validation outputs (instead of plain argmax only).

## 8.3 Training stability
- Save and evaluate by best macro-F1 (not only best validation accuracy).
- Add deterministic seeds and stratified folds for variance control.
- Track and alert per-epoch prediction entropy and class histogram to catch collapse early.

## 8.4 Architecture and quantum block
- Run ablations:
  - Frozen mBERT + classical head only
  - Frozen mBERT + projection + residual (no quantum)
  - Full hybrid model
- If hybrid does not improve macro-F1 against strong classical baselines, simplify and prioritize robust minority handling.

## 9) Recommended Deployment Candidate

Current best candidate: Take-1 for top-line accuracy only.

However, for any safety-critical hate-speech use case, none of the current runs are production-ready because OR and OS detection is effectively missing. A new model selection target should prioritize macro-F1 and per-class recall floors, not only overall accuracy.

## 10) Files Used

- vqc/vqc_nepali_optimized.ipynb
- vqc/Graphs/take-1/classification_metrics.csv
- vqc/Graphs/take-2/classification_metrics.csv
- vqc/Graphs/take-2/training_history.json
- vqc/Graphs/take-3/classification_metrics.csv
- vqc/Graphs/take-3/training_history.json
- vqc/Graphs/take-4/classification_metrics.csv
- vqc/Graphs/take-4/training_history.json
- Plot artifacts under each take folder in vqc/Graphs
- Checkpoints under vqc/models/take-1 to take-4

## 11) Graphs and Plots

The following figures are embedded directly from the experiment output folders.

### Take-1

#### Accuracy Curve
![Take-1 Accuracy Curve](vqc/Graphs/take-1/accuracy_curve.png)

#### Loss Curve
![Take-1 Loss Curve](vqc/Graphs/take-1/loss_curve.png)

#### Combined Loss and Accuracy Curves
![Take-1 Loss and Accuracy Curves](vqc/Graphs/take-1/loss_accuracy_curves.png)

#### Confusion Matrix
![Take-1 Confusion Matrix](vqc/Graphs/take-1/confusion_matrix.png)

#### Normalized Confusion Matrix
![Take-1 Normalized Confusion Matrix](vqc/Graphs/take-1/confusion_matrix_normalized.png)

#### Per-Class Metrics
![Take-1 Per-Class Metrics](vqc/Graphs/take-1/per_class_metrics.png)

#### Class Distribution
![Take-1 Class Distribution](vqc/Graphs/take-1/class_distribution.png)

### Take-2

#### Accuracy Curve
![Take-2 Accuracy Curve](vqc/Graphs/take-2/accuracy_curve.png)

#### Loss Curve
![Take-2 Loss Curve](vqc/Graphs/take-2/loss_curve.png)

#### Combined Loss and Accuracy Curves
![Take-2 Loss and Accuracy Curves](vqc/Graphs/take-2/loss_accuracy_curves.png)

#### Overfitting Monitor
![Take-2 Overfitting Monitor](vqc/Graphs/take-2/overfitting_monitor.png)

#### Confusion Matrix
![Take-2 Confusion Matrix](vqc/Graphs/take-2/confusion_matrix.png)

#### Normalized Confusion Matrix
![Take-2 Normalized Confusion Matrix](vqc/Graphs/take-2/confusion_matrix_normalized.png)

#### Per-Class Metrics
![Take-2 Per-Class Metrics](vqc/Graphs/take-2/per_class_metrics.png)

#### Class Distribution
![Take-2 Class Distribution](vqc/Graphs/take-2/class_distribution.png)

### Take-3

#### Accuracy Curve
![Take-3 Accuracy Curve](vqc/Graphs/take-3/accuracy_curve.png)

#### Loss Curve
![Take-3 Loss Curve](vqc/Graphs/take-3/loss_curve.png)

#### Combined Loss and Accuracy Curves
![Take-3 Loss and Accuracy Curves](vqc/Graphs/take-3/loss_accuracy_curves.png)

#### Overfitting Monitor
![Take-3 Overfitting Monitor](vqc/Graphs/take-3/overfitting_monitor.png)

#### Confusion Matrix
![Take-3 Confusion Matrix](vqc/Graphs/take-3/confusion_matrix.png)

#### Normalized Confusion Matrix
![Take-3 Normalized Confusion Matrix](vqc/Graphs/take-3/confusion_matrix_normalized.png)

#### Per-Class Metrics
![Take-3 Per-Class Metrics](vqc/Graphs/take-3/per_class_metrics.png)

#### Class Distribution
![Take-3 Class Distribution](vqc/Graphs/take-3/class_distribution.png)

### Take-4

#### Accuracy Curve
![Take-4 Accuracy Curve](vqc/Graphs/take-4/accuracy_curve.png)

#### Loss Curve
![Take-4 Loss Curve](vqc/Graphs/take-4/loss_curve.png)

#### Combined Loss and Accuracy Curves
![Take-4 Loss and Accuracy Curves](vqc/Graphs/take-4/loss_accuracy_curves.png)

#### Training Overview
![Take-4 Training Overview](vqc/Graphs/take-4/training_overview.png)

#### Confusion Matrix
![Take-4 Confusion Matrix](vqc/Graphs/take-4/confusion_matrix.png)

#### Normalized Confusion Matrix
![Take-4 Normalized Confusion Matrix](vqc/Graphs/take-4/confusion_matrix_normalized.png)

#### Per-Class Metrics
![Take-4 Per-Class Metrics](vqc/Graphs/take-4/per_class_metrics.png)

#### Class Distribution
![Take-4 Class Distribution](vqc/Graphs/take-4/class_distribution.png)
