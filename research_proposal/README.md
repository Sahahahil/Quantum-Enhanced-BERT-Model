# Research Proposal

**Goal**

Develop a hybrid classical‑quantum architecture that leverages multilingual BERT embeddings with variational quantum circuits (VQCs) to improve detection of offensive speech in low‑resource Nepali social media data.

---

## Scientific Context

- **BERT Foundations** – The `BERT_foundation/` subdirectory contains core papers and notes (e.g., *BERT Basics*, *Input/Output design*). These resources summarise the self‑attention mechanism, tokenisation strategy, and fine‑tuning protocols relevant to downstream classification.
- **Multilingual Extensions (M_BERT)** – Links to recent multilingual BERT variants that support Nepali script and provide a strong baseline for cross‑lingual transfer.
- **Transformer & NLP Theory** – `Transformer_NOTES/` summarises state‑of‑the‑art transformer architectures, covering positional encodings, scaling laws, and recent advances pertinent to low‑resource scenarios.
- **Quantum Computing Foundations** – `Quantum_Notes/` and `Quantum_labs/` compile quantum information fundamentals, PennyLane tutorials, and quantum operation primitives required to implement VQCs.
- **Related Work** – The compiled literature surveys address:
  - Quantum kernel methods for NLP ( Schuld et al., 2020 )
  - Hybrid quantum‑classical pipelines ( Benedetti et al., 2021 )
  - Offensive speech detection in low‑resource languages ( Gupta et al., 2022 )

---

## Research Questions

1. **Performance Gain**: Does integrating a VQC layer on top of BERT embeddings yield statistically significant improvements in macro‑F1 compared to a purely classical baseline?
2. **Resource Efficiency**: Can the hybrid model achieve comparable performance with fewer trainable parameters, reducing memory/computation footprints for deployment on edge devices?
3. **Robustness**: How does the quantum‑enhanced model behave under adversarial text perturbations relative to the baseline?

---

## Methodology

1. **Data Preparation** – Use the `dataset_work/` pipeline to obtain a clean, balanced Nepali dataset with offensive/non‑offensive labels.
2. **Baseline Training** – Fine‑tune multilingual BERT on the prepared data (see `model_eval/MBert/MBERT.ipynb`).
3. **Hybrid Model Construction** –
   - Extract BERT hidden states (`[CLS]` token) as fixed‑size embeddings.
   - Feed embeddings into a parameterised quantum circuit implemented with Pennylane (see `research_proposal/Quantum_labs/PennyLane/` notebooks for circuit templates).
   - Optimize quantum circuit parameters jointly with a linear classification head using the parameter‑shift rule.
4. **Evaluation** – Run the evaluation notebooks (`model_eval/`) to compute accuracy, macro‑F1, PR‑AUC, ROC‑AUC, and generate confusion matrices.
5. **Statistical Analysis** – Perform paired t‑tests and bootstrap confidence intervals over 5‑fold cross‑validation to assess significance.

---

## Deliverables

- **Technical Report** – Consolidated findings in `Quantum_labs/Phase - 2/Hyperparameter Tuning.docx`.
- **Reproducible Scripts** – All code and notebooks committed under version control.
- **Publication‑Ready Figures** – High‑resolution plots for conference submissions (included in `model_eval/`).

---

## Usage Notes

- All PDFs, DOCX files, and notebooks are stored in a hierarchical layout for easy navigation.
- When extending the proposal, add new literature notes under appropriate subfolders and update the `README.md` to reflect new hypotheses.

---

*Contributions are encouraged via pull‑requests. For discussion of experimental design, open an issue or contact the repository maintainer.*

## Overview
This directory aggregates background research, literature notes, and proposal material that inform the quantum‑enhanced BERT effort. It stores high‑level documents on BERT fundamentals, transformer architectures, and quantum computing concepts, together with links to external papers, tutorials, and lab resources.

## Folder Structure
```
research_proposal/
├─ BERT_foundation/
│  ├─ 4_BERTBasics.docx
│  ├─ 5_BERTInputOutput.docx
│  └─ bert_link.txt
├─ M_BERT/
│  └─ mbert_link.txt
├─ NLP_notes/
│  ├─ 1_BackgroundConcepts.docx
│  └─ 2_WordRepresentation.docx
├─ Quantum_labs/
│  └─ PennyLane/
│      ├─ IQC_ Introduction to Quantum Computing/
│      │   └─ All_about_Qubits.pdf
│      └─ PennyLane Fundamentals/
│          ├─ Circuits__QNodes.pdf
│          └─ Quantum_Operations.pdf
├─ Quantum_Notes/
│  ├─ Introduction_to_Quantum_Report.pdf
│  └─ quantum_Handwritten.pdf
├─ runpod/
│  └─ runpod_instructions.pdf
└─ Transformer_NOTES/
   ├─ 3_TransformerFundamentals.docx
   └─ Transformers_notes.pdf
```

## How to Use
- Consult the BERT foundation documents for a refresher on the model architecture.
- Review the quantum lab PDFs to understand the quantum computing concepts that may be integrated.
- Use the transformer notes as a reference when designing hybrid quantum‑transformer components.

The hierarchical layout groups related topics together, making it straightforward for contributors to locate the material they need.
