# Quantum-Enhanced BERT for Nepali Offensive Speech Detection

**A Hybrid Classical-Quantum Machine Learning Approach for Low-Resource NLP**

This repository contains the implementation framework, experimental design, and research documentation for the project **"Quantum-Enhanced BERT Model for Offensive Speech Detection and Analysis in Nepali Language"**. 

This project integrates the contextual representational power of transformer models (BERT) with **Variational Quantum Circuits (VQCs)** to dramatically improve text classification performance in low-resource language environments.

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

## Limitations & Technical Challenges

* **Hardware Noise:** Modern Quantum simulators and early Noisy Intermediate-Scale Quantum (NISQ) real hardware are prone to qubit decoherence, readout errors, and strict circuit depth boundaries.
* **Scope Boundary:** This iteration addresses textual inputs in the native Devanagari script (and localized Romanized strings) only. Multi-modal entries (memes, voice clips, video) are out of scope.

---


## Ethical Considerations & Regulations

Data transparency and integrity remain absolute priorities. All training datasets gathered from digital spheres are completely anonymized to shield individual identities. This project is executed strictly in compliance with data privacy boundaries, structural institutional ethics reviews, and acts directly toward supporting Nepal's digital transformation and cyber resilience priorities.

---

## Notable Academic References

1. Niraula, N. B., et al. (2021). *Offensive Language Detection in Nepali Social Media*. Proceedings of the Workshop on Online Abuse and Harms (WOAH).
2. Yu, W., et al. (2024). *Application of Quantum Recurrent Neural Network in Low Resource Language Text Classification*. IEEE Transactions on Quantum Engineering.
3. Davidson, T., et al. (2017). *Automated Hate Speech Detection and the Problem of Offensive Language*. International Conference on Web and Social Media (ICWSM).