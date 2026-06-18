# Quantum-Enhanced BERT for Nepali Offensive Speech Detection

**A Hybrid Classical-Quantum Machine Learning Approach for Low-Resource NLP**

This repository contains the implementation framework, experimental design, and research documentation for the project **"Quantum-Enhanced BERT Model for Offensive Speech Detection and Analysis in Nepali Language"**. 

Developed as a research initiative at the **Department of Computer Engineering, Khwopa College of Engineering (Bhaktapur)**, this project integrates the contextual representational power of transformer models (BERT) with **Variational Quantum Circuits (VQCs)** to dramatically improve text classification performance in low-resource language environments.

---

## Project Overview

The proliferation of offensive and hateful language on social media is a critical societal challenge. For low-resource languages like Nepali, traditional deep learning and classical transformer models often underperform due to severe data scarcity, complex dialectal variations, and cultural nuances.

This project introduces a **hybrid classical-quantum framework** that:
1. Extracts high-quality contextual text embeddings using pre-trained multilingual transformers (e.g., `mBERT`, `IndicBERT`).
2. Map these embeddings into high-dimensional quantum states via **Variational Quantum Circuits (VQCs)**.
3. Leverages quantum properties like **superposition and entanglement** to discover complex, non-linear semantic relationships using less data.

### Key Highlights
* **Target Domain:** Automated Offensive Speech Detection & Content Moderation.
* **Language Focus:** Nepali (including colloquial scripts and social media dialects).
* **Core Architecture:** Pre-trained BERT + Variational Quantum Circuit (VQC) + Classical Linear Classifier.
* **Primary Frameworks:** Qiskit, PennyLane, Hugging Face Transformers, PyTorch/TensorFlow.

---

## Architecture & Methodology

+-------------------------------------------------------------+
|                     INPUT NEPALI TEXT                       |
|  "त्यो मान्छे एकदम नराम्रो छ..." (Social Media Posts)        |
+------------------------------+------------------------------+
|
v
+-------------------------------------------------------------+
|               PREPROCESSING & TOKENIZATION                  |
|    - Noise Removal, Normalization, & Subword Tokenization    |
+------------------------------+------------------------------+
|
v
+-------------------------------------------------------------+
|                 CLASSICAL EMBEDDING LAYER                   |
|     - Pre-trained Transformer Feature Extraction (BERT)     |
+------------------------------+------------------------------+
| (High-Dimensional Vectors)
v
+-------------------------------------------------------------+
|                 QUANTUM FEATURE ENCODING                   |
|     - Mapping Vectors to Quantum States (Superposition)     |
+------------------------------+------------------------------+
|
v
+-------------------------------------------------------------+
|              VARIATIONAL QUANTUM CIRCUIT (VQC)              |
|        - Quantum Feature Maps & Parameterized Gates         |
+------------------------------+------------------------------+
| (Measurement / Expectation)
v
+-------------------------------------------------------------+
|                 CLASSICAL CLASSIFICATION                    |
|      - Softmax Layer -> [Offensive / Non-Offensive]         |
+-------------------------------------------------------------+


1. **Data Engineering:** Sourcing and manually annotating real-world Nepali social media text (Twitter, Facebook, forums). Augmentation via back-translation and synonym replacement.
2. **Quantum Feature Optimization:** Parameterized quantum layers are jointly updated with classical weights using hybrid gradient descent optimization.

---

## Research Implementation Timeline

The project execution is planned across a **20-week timeline**:

| Phase | Task Description | Duration |
| :--- | :--- | :--- |
| **Phase 1** | Literature Review & Problem Definition | Weeks 1–2 |
| **Phase 2** | Data Collection, Normalization & Annotation | Weeks 3–5 |
| **Phase 3** | Baseline Transformer Model Fine-Tuning | Weeks 6–8 |
| **Phase 4** | Variational Quantum Circuit (VQC) Integration | Weeks 9–12 |
| **Phase 5** | Hybrid System Joint Training & Optimization | Weeks 13–15 |
| **Phase 6** | Performance Evaluation & Ablation Analysis | Weeks 16–17 |
| **Phase 7** | Documentation, Reporting & Paper Drafting | Weeks 18–19 |
| **Phase 8** | Project Review & Final Submission | Week 20 |

---

## Budget & Resource Allocation

The total estimated operational budget for the project is **NPR 50,000**, distributed as follows:

| Category | Description | Amount (NPR) |
| :--- | :--- | :--- |
| **Data Logistics** | Social media scraping, manual labeling, and linguistic verification. | रू 8,000 |
| **Compute Infrastructure** | Cloud-based GPU runtimes (AWS / Google Colab Pro) for BERT base models. | रू 15,000 |
| **Quantum Software Simulation**| Commercial frameworks and local HPC execution for Qiskit/PennyLane. | रू 6,000 |
| **Research Assistance** | Compensations for text annotators and regional language experts. | रू 8,000 |
| **Evaluation Metrics** | Multi-variant ablation benchmarking and systematic cross-testing. | रू 5,000 |
| **Documentation & Reporting**| Physical asset printing, slide compilation, and publishing costs. | रू 4,000 |
| **Contingency Fund** | Unforeseen computational run extensions or pipeline adjustments (10%). | रू 4,000 |
| **Total** | | **NPR 50,000** |

---

## Limitations & Technical Challenges

* **Hardware Noise:** Modern Quantum simulators and early Noisy Intermediate-Scale Quantum (NISQ) real hardware are prone to qubit decoherence, readout errors, and strict circuit depth boundaries.
* **Scope Boundary:** This iteration addresses textual inputs in the native Devanagari script (and localized Romanized strings) only. Multi-modal entries (memes, voice clips, video) are out of scope.

---

## Project Investigators

Developed by the research cohort at the **Department of Computer Engineering, Khwopa College of Engineering, Bhaktapur, Nepal**:

* **Naresh Khatri**
* **Anish Baral**
* **Uddav Rajbhandari**

---

## Ethical Considerations & Regulations

Data transparency and integrity remain absolute priorities. All training datasets gathered from digital spheres are completely anonymized to shield individual identities. This project is executed strictly in compliance with data privacy boundaries, structural institutional ethics reviews, and acts directly toward supporting Nepal's digital transformation and cyber resilience priorities.

---

## Notable Academic References

1. Niraula, N. B., et al. (2021). *Offensive Language Detection in Nepali Social Media*. Proceedings of the Workshop on Online Abuse and Harms (WOAH).
2. Yu, W., et al. (2024). *Application of Quantum Recurrent Neural Network in Low Resource Language Text Classification*. IEEE Transactions on Quantum Engineering.
3. Davidson, T., et al. (2017). *Automated Hate Speech Detection and the Problem of Offensive Language*. International Conference on Web and Social Media (ICWSM).