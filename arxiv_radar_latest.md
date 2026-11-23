# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-23 23:10:55 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning](http://arxiv.org/abs/2611.27915v1)
**arXiv ID:** `2611.27915v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27915v1) | **Published:** 2026-11-20
**Authors:** Chi Yan, Guoyang Zhao, Wentao Yuan, Yixiao Ge, Yanning Zhou et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints...
2. **Key Technical Contributions:** From Abstract: . This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are grounded in visual evidence or driven primarily by semantic priors. In contrast, calibrated stereo provides explicit cross-view geometry that resolves this ambiguity and offers a more re
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [TEA-Bench-BR: Can Coding Agents Turn a Branching Clinical Specification into Correct Code?](http://arxiv.org/abs/2611.27895v1)
**arXiv ID:** `2611.27895v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27895v1) | **Published:** 2026-11-20
**Authors:** Marcio Andre de Souza Estevam

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Coding agents increasingly implement rules written by domain experts, and bugs in such code are silent: it runs and returns a plausible answer. We introduce TEA-Bench-BR, a benchmark built on the Brazilian pathway for early autism (TEA) screening: three fictitious instruments with the structure of r...
2. **Key Technical Contributions:** From Abstract: eal ones, a multi-professional referral flow, and export to FHIR R4 with the national RNDS profiles, all specified in Portuguese. A generator samples each task's parameters (144 tasks, 6,798 hidden cases), and the hidden cases kill all 1,955 non-equivalent mutants of the reference. With Gemma 4 as t
3. **Methodology & Architecture:** Categories: cs.SE, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers](http://arxiv.org/abs/2611.27901v1)
**arXiv ID:** `2611.27901v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27901v1) | **Published:** 2026-11-20
**Authors:** Zunhai Su, Keyu Fan, Ruishan Guo, Zhongzhu Zhou, Jingzehua Xu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Streaming visual geometry transformers retain historical key-value (KV) states as cross-view geometric memory, but growing caches constrain long-sequence inference. We systematically characterize KV quantization in streaming geometry and uncover two linked challenges: Nonuniform Geometric Sensitivit...
2. **Key Technical Contributions:** From Abstract: y and Cache-Geometry Mismatch. Quantization sensitivity varies across precision choices and cache locations, while perturbed retrieval changes geometry-head inputs and propagates through subsequent predictions and KV writes. Guided by these findings, we propose QuantStream3D, to our knowledge the fi
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform](http://arxiv.org/abs/2611.27953v1)
**arXiv ID:** `2611.27953v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27953v1) | **Published:** 2026-11-20
**Authors:** Guillem Fustier-Castillo, Ruben Ribes-Serrano, Javier Naranjo-Alcazar, Vicent Ortiz-Castello, Pedro Zuccarello

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Neuromorphic sensing and computing offer a promising alternative to conventional deep learning pipelines for mobile robots, where perception must run continuously under tight latency and energy constraints. However, most neuromorphic solutions are still evaluated offline or on isolated benchmarks, a...
2. **Key Technical Contributions:** From Abstract: nd their integration into complete robotic systems remains largely unexplored. In this technical report, a four-wheel rover platform is presented that combines three real-time perception pipelines: a classical audio tagging pipeline based on Pretrained Audio Neural Networks (PANNs) running on an NVI
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Model Carving: Training Transformers That Optimize Their Own Topology](http://arxiv.org/abs/2611.27962v1)
**arXiv ID:** `2611.27962v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27962v1) | **Published:** 2026-11-20
**Authors:** Kaden Zheng, Pratyusha Sharma

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Machine learning has largely kept separate the choice of architecture and the process of training. A classic Transformer, for instance, trains a fixed set of attention and MLP sublayers at every layer, in the same order, and optimizes the weights within. This uniformity is a convention rather than a...
2. **Key Technical Contributions:** From Abstract:  principled design choice, and it is likely suboptimal: the best architecture for a given task may be smaller, more efficient, and far from uniform. We believe that, ideally, training itself should shape the model's topology. To this end, we introduce Model Carving, which learns both a Transformer's
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning](http://arxiv.org/abs/2611.27978v1)
**arXiv ID:** `2611.27978v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27978v1) | **Published:** 2026-11-20
**Authors:** Hari Sitaula, Joseph Opitz

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features. We benchmark three model families, namely linear regression, vanilla recurrent neural networks (RNN)...
2. **Key Technical Contributions:** From Abstract: , and long short-term memory networks (LSTM), within a unified preprocessing and chronological evaluation pipeline. A central contribution of this work is a methodological audit of common practices in the deep-learning-for-stock-prediction literature. We identify three sources of result inflation th
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [SUAF: Spectral Universal Advantage Features for Zero-Shot Policy Improvement](http://arxiv.org/abs/2611.27919v1)
**arXiv ID:** `2611.27919v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27919v1) | **Published:** 2026-11-20
**Authors:** Huaze Tang, Runqing Miao, Tianren Peng, Lam Nguyen, Chao Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reward-independent representations enable reinforcement learning agents to reuse knowledge across tasks, but limited representation capacity raises three fundamental questions: what statistical dependence should these representations capture, which components of that dependence should be retained fo...
2. **Key Technical Contributions:** From Abstract: r policy improvement, and how does discarding the remaining components affect decision-making? We address these questions through canonical dependence analysis. For a reference policy, we construct an action-centered, positive-lag canonical dependence matrix (CDM) that isolates the additional predic
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search](http://arxiv.org/abs/2611.27910v1)
**arXiv ID:** `2611.27910v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27910v1) | **Published:** 2026-11-20
**Authors:** Aadharsh Kannan, Robert Bruckner, Philip A. Bernstein

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Business data systems must determine whether records refer to the same entity and retrieve records satisfying requests whose decisive properties are implicit. As agents act on these records, both tasks require auditable reasons. Dense embeddings perform well but offer opaque coordinates, cannot be f...
2. **Key Technical Contributions:** From Abstract: iltered by meaning, and require corpus re-encoding to add new properties. We propose interpretable embeddings built from decision columns: each column stores a decision model's calibrated answer to a natural-language question, with outcomes yes, no, or not stated. A record's embedding is its answers
3. **Methodology & Architecture:** Categories: cs.IR, cs.AI, cs.DB. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Interactive Semi-Parametric On-Track Learning for Vehicle Dynamics in Autonomous Racing](http://arxiv.org/abs/2611.27932v1)
**arXiv ID:** `2611.27932v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27932v1) | **Published:** 2026-11-20
**Authors:** Jungbin Kim, Youngim Nam, Cheolhyeon Kwon

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Autonomous racing requires an accurate vehicle dynamics model near the limits of handling, yet a mismatch between the nominal and actual dynamics inevitably remains. To reduce this mismatch, existing methods learn from on-track data, i.e., data collected while the vehicle drives on the track under r...
2. **Key Technical Contributions:** From Abstract: acing conditions, by adapting the physical parameters of the nominal model or by learning a residual that captures the remaining mismatch. However, these on-track learning methods typically handle either the physical parameters or the residual separately, which restricts their ability to resolve the
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
This paper has presented an interactive framework for
semi-parametric dynamics learning from on-track data in
autonomous racing. The framework recursively updates the
physical parameters via NLS and the residual model via sparse
GP regression in turn under a single shared prediction-error
objective. To account for their mutual dependence, each update
is guided by the latest update of the other model. Since
an update of either model is accepted only if it does not
increase the shared objective, the objective never increases
and is guaranteed to converge over the recursion. Numerical
simulations and hardware experiments on a 1/10-scale vehicle
showed that the proposed framework outperforms the base-
lines, given the same limited on
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](http://arxiv.org/abs/2611.27889v1)
**arXiv ID:** `2611.27889v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.27889v1) | **Published:** 2026-11-20
**Authors:** Vasco Portilheiro, Samuel Liebana, Andrew Saxe, Peter Orbanz

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution o...
2. **Key Technical Contributions:** From Abstract: ver represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization is taken to zero. In certain cases, we show that the zero-regularization and infinite-time limits c
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-20. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
