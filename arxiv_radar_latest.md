# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-26 18:01:58 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](http://arxiv.org/abs/2610.32971v1)
**arXiv ID:** `2610.32971v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32971v1) | **Published:** 2026-10-23
**Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, Jiaying Xu, Shangding Gu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusab...
2. **Key Technical Contributions:** From Abstract: ility and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, offline, and safe RL algorithms under a unified interface for substantially improved reusability, to
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning](http://arxiv.org/abs/2610.32978v1)
**arXiv ID:** `2610.32978v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32978v1) | **Published:** 2026-10-23
**Authors:** Yuhan Liu, Lianhui Qin, Shenji Wan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrang...
2. **Key Technical Contributions:** From Abstract: ements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We introduce SceneBloom, an agentic framework that combines visual layout sampling with contract-guided 3D compilation. A hierarchical sampler uses diffusion priors to generate furniture arrangements within f
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning](http://arxiv.org/abs/2610.32951v1)
**arXiv ID:** `2610.32951v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32951v1) | **Published:** 2026-10-23
**Authors:** Yijing Ke, Tianle Cai, Ruosong Wang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning for large language models often uses separate systems for inference and training. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the entire inference an...
2. **Key Technical Contributions:** From Abstract: d training stacks, change global precision, or modify the learning algorithm. We ask whether aligning selected parts of the execution stack can stabilize BF16 RL while other implementation differences remain. We align training-side rounding locations with inference in three regions---RoPE, SwiGLU, a
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox](http://arxiv.org/abs/2610.32955v1)
**arXiv ID:** `2610.32955v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32955v1) | **Published:** 2026-10-23
**Authors:** Federico Lucca

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a...
2. **Key Technical Contributions:** From Abstract:  measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered hypotheses, human labels in the agent's review loop) that yields ground truth before any training. On 739 real Italian/English emails labelled by the owner (231 unbiased, 500 adversarially sampled), w
3. **Methodology & Architecture:** Categories: cs.CL, cs.HC, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Limitations
Single user, single inbox, two languages. What would not
transfer to another user is clear from the components: the
baseline’s weights (they encode this owner’s senders and
vocabulary and must be retrained from that user’s labels),
the contact graph (empty for a new user until contacts re-
cur, which is why coverage, not accuracy, is the quantity
to watch), the class priors (70–82%bassahere) and any
confidence threshold. What should transfer is the protocol it-
self, the zero-shot behaviour of the decision models, and the
finding that the sender’s relationship is a graph property; the
second inbox needed to test this is the obvious next study;
the owner reviewed labels proposed by model annotators
rather than labelling from scra
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations](http://arxiv.org/abs/2610.32891v1)
**arXiv ID:** `2610.32891v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32891v1) | **Published:** 2026-10-23
**Authors:** Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, Gunel Jahangirova, Hugo Araujo et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large Language Models (LLMs) are increasingly used to optimize code for performance. This practice often assumes that improvements in execution speed naturally translate into overall lower energy consumption. We challenge this assumption empirically by measuring whether performance-optimized code pr...
2. **Key Technical Contributions:** From Abstract: oduced by LLM self-refinement pipelines is also energy-efficient relative to canonical human reference solutions, and whether the energy cost of the optimization process can be offset by subsequent execution-time savings. We evaluate 11 open-source models across four decoding configurations on all 1
3. **Methodology & Architecture:** Categories: cs.SE, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
This paper presented a systematic measurement study of
the energy economics of LLM-based code self-optimization,
covering inference and execution cost across 11 open-source
models, four decoding configurations, and 1,000 EffiBench
problems. The central question was whether performance-
optimized code produced by LLM self-refinement is also
energy-efficient relative to canonical solutions.
Optimized code consumes more execution energy than the
canonical reference in 42 of 44 model-variant pairs; the two
exceptions achieve only marginal gains, with break-even points
requiring millions of executions. Performance optimization
and energy efficiency are not aligned even within the refine-
ment trajectory: more than half of all configur
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](http://arxiv.org/abs/2610.32969v1)
**arXiv ID:** `2610.32969v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32969v1) | **Published:** 2026-10-23
**Authors:** Amber Xie, Jiawei Fu, Xiaofeng Guo, Carmelo Sferrazza, Guanya Shi et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to...
2. **Key Technical Contributions:** From Abstract:  collect, but their motions must be estimated and retargeted to the robot, and they do not directly provide robot actions. In this paper, we introduce DexPort, a portable data-collection interface for high-DoF robot hands. It uses the same hand hardware for collection and deployment, avoiding a hand
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** future work
may explore extending them with additional skills learned in
simulation, such as other in-hand manipulation skills, learned
grasps, and more.
ACKNOWLEDGMENT
The authors would like to thank Keyshawn King and
V olodymyr Behma for data collection and support, and
Andrew Wright for initial hardware designs. We also thank
Tingfan Wu, Anas Houssaini, Jensen Gao, and the FAR team
for feedback and support.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [RynnUnify: Towards Unified Embodied Brain](http://arxiv.org/abs/2610.32965v1)
**arXiv ID:** `2610.32965v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32965v1) | **Published:** 2026-10-23
**Authors:** Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We introduce RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-horizon visual planning through interleaved video--language reasoning. With capabilities spanning spatial reasoning, physical prediction, and grounding, RynnUnify connects an understanding of t...
2. **Key Technical Contributions:** From Abstract: he physical world with visual anticipation of how it evolves across successive subtasks. Building on these capabilities, we further develop an agentic extension through reinforcement learning to selectively use video predictions for reasoning about unobserved states and interaction outcomes. We also
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms](http://arxiv.org/abs/2610.32945v1)
**arXiv ID:** `2610.32945v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32945v1) | **Published:** 2026-10-23
**Authors:** Yuhang Ji, Fasheng Xu, Tianjun Feng

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language model (LLM) platforms introducing advertising must decide how much capability ad revenue should fund and what consumers should pay to avoid ads. We study a monopolistic platform that jointly chooses costly response quality, advertising intensity, and subscription prices when advertisi...
2. **Key Technical Contributions:** From Abstract: ng reduces user value but better service raises advertising returns. Three findings follow. First, when partly ad-supported and ad-free plans coexist, advertising can finance useful service for consumers who receive none under pure subscription. Lower effective quality in middle plans weakens the al
3. **Methodology & Architecture:** Categories: econ.TH, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ZENO: Nonlinear filtering with Zakai Equation Neural Operators](http://arxiv.org/abs/2610.32926v1)
**arXiv ID:** `2610.32926v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32926v1) | **Published:** 2026-10-23
**Authors:** Aaditya Prasad, Steven W. Flavell, Brian DePasquale

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differential equation (SPDE) th...
2. **Key Technical Contributions:** From Abstract: at combines the forward Kolmogorov operator (known as the Fokker-Planck equation) with observed likelihood updates. Although solving these high-dimensional SPDEs is often impossible analytically and intractable numerically, advances in operator learning and physics-informed machine learning have mad
3. **Methodology & Architecture:** Categories: cs.LG, q-bio.NC. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-23. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Yalda-Embedding: Open Development of a Competitive Persian Retrieval Model](http://arxiv.org/abs/2610.32933v1)
**arXiv ID:** `2610.32933v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.32933v1) | **Published:** 2026-10-23
**Authors:** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Despite advances in multilingual text representations, effective dense retrieval for Persian remains constrained by the limited availability of language-specific training resources and compact embedding models. We present Yalda Embedding, a 595.8-million-parameter Persian retrieval model adapted fro...
2. **Key Technical Contributions:** From Abstract: m Qwen3-Embedding-0.6B using more than one million query-document pairs. On eight Persian retrieval tasks from FaMTEB, the model achieves the highest macro-average among the evaluated 0.6B models, scoring 0.5488 and outperforming Qwen3-Embedding-0.6B and F2LLM-v2-0.6B on every task. It also approach
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
We introduced YALDA-EMBEDDING, an openly developed
Persian retrieval model adapted from Qwen3-Embedding-
0.6B on more than one million query–document pairs. On
eight FaMTEB retrieval tasks, it achieves the highest mean
among the evaluated 0.6B models (0.5488) and outperforms
both same-scale decoder-based baselines on every task. It
approaches Qwen3-Embedding-4B, winning on four tasks and
tying on one, with a macro-average gap of 0.0075.
The two-stage ablation documents the progression from
contrastive training to relational distillation. The final distilled
model improves every task over the non-distilled recipe and
raises its mean from 0.4813 to 0.5488 while retaining the
same inference architecture. By releasing weights, traini
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
