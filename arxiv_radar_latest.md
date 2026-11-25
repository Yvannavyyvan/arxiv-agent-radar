# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-25 20:55:15 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design](http://arxiv.org/abs/2611.33093v1)
**arXiv ID:** `2611.33093v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33093v1) | **Published:** 2026-11-24
**Authors:** Guangyuan Wang, Chengran Li, Minchen Luo, Jichen Feng, Mengdi Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardwa...
2. **Key Technical Contributions:** From Abstract: re correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable register-transfer-level (RTL) code against an executable integer reference that specifies the outputs and the stored state at every decoding step. They debug against public tests under fixed b
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](http://arxiv.org/abs/2611.33098v1)
**arXiv ID:** `2611.33098v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33098v1) | **Published:** 2026-11-24
**Authors:** Lingwei Gu, Jimmy Lin

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks to a small language m...
2. **Key Technical Contributions:** From Abstract: odel, or SLM, that runs on hardware one already owns. To test it, we build Delegent, a simple and effective agent harness built on Claude Code, in which the frontier model stays in charge of every task but hands focused subtasks, such as investigating code, running tests, and searching a corpus, to 
3. **Methodology & Architecture:** Categories: cs.AI, cs.IR. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics](http://arxiv.org/abs/2611.33078v1)
**arXiv ID:** `2611.33078v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33078v1) | **Published:** 2026-11-24
**Authors:** Yisrael Clark, Guy Katz

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall...
2. **Key Technical Contributions:** From Abstract:  pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-Proof operates by deterministically obtaining a pool of candidate translations via semantic analysis tools, such as the English Resource Grammar and Minimal Recursion Semantics; then
3. **Methodology & Architecture:** Categories: cs.CL, cs.LO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](http://arxiv.org/abs/2611.33145v1)
**arXiv ID:** `2611.33145v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33145v1) | **Published:** 2026-11-24
**Authors:** Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, m...
2. **Key Technical Contributions:** From Abstract: aking it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-act
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions](http://arxiv.org/abs/2611.33111v1)
**arXiv ID:** `2611.33111v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33111v1) | **Published:** 2026-11-24
**Authors:** Yuxing Liu, Wei Zuo, Walid Krichene, Tong Zhang, Li Zhang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization. The speedup relies on the acceptance probability of d...
2. **Key Technical Contributions:** From Abstract: raft tokens in target verification, which is directly related to the gap $\|p-q\|_1$ between the target distribution $p$ and the draft distribution $q$. In this paper, we study draft calibration of speculative decoding to improve the speedup of speculative decoding, where we employ post-hoc methods 
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents](http://arxiv.org/abs/2611.33144v1)
**arXiv ID:** `2611.33144v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33144v1) | **Published:** 2026-11-24
**Authors:** Feixiang Ruan, Guodong Lv, Kewei Zhang, Wenbo Huang, Yintianrun Zhang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding...
2. **Key Technical Contributions:** From Abstract:  agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the succes
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Neural Implicit Representation for Bathymetry Estimation using Sidescan Sonar Imagery](http://arxiv.org/abs/2611.33118v1)
**arXiv ID:** `2611.33118v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33118v1) | **Published:** 2026-11-24
**Authors:** Tianxiang Lin, Sacchin Sundar, Fenghao Liu, Onur Bagoren, Katherine A. Skinner

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Bathymetry measurement and estimation is critical for understanding the structure of underwater environments. While multibeam echosounders (MBES) provide accurate depth measurements, their deployment on surface vessels limits spatial resolution in deep water. Sidescan sonar (SSS), in contrast, can b...
2. **Key Technical Contributions:** From Abstract: e deployed on autonomous underwater vehicles (AUVs) to operate closer to the seafloor, enabling high-resolution acoustic imaging. However, the inherent ambiguity in measurements and the limited observation coverage of sonar datasets degrade the performance of state-of-the-art methods for underwater 
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** FUTURE WORK
We proposed a neural implicit reconstruction framework
for bathymetry estimation using SSS imagery. Through
experiments on both synthetic and real-world datasets, we
demonstrated that our method achieves improved accuracy
on bathymetry estimation compared to the existing approach.
For future work, we see multiple promising directions.
First, we will explore incorporating sonar noise and pose
error in the neural rendering pipeline to improve results on
real data. Second, since our current process handles one sonar
ping at a time, we will transition from single-ping processing
to batch training to fully leverage our GPU hardware. This
will enable parallel processing of multiple pings, boosting
data throughput to work toward an eff
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [CANON: Agent-Assisted Construction of Canonical Differential Equations for Feynman Integrals](http://arxiv.org/abs/2611.33100v1)
**arXiv ID:** `2611.33100v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33100v1) | **Published:** 2026-11-24
**Authors:** Dong-shan Jian, Yuanche Liu, Yan-qing Ma, Bo-xuan Shi, Yu Wu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** The construction of canonical basis is an important procedure in the calculation of multi-loop Feynman integrals via the canonical differential equation methods. Currently, there are various different methods for this purpose. Among them, no single method is universally applicable. Thus, obtaining a...
2. **Key Technical Contributions:** From Abstract:  valid basis often requires repeated attempts and verification. In this paper, we present CANON, an agent-assisted framework designed to make this search-and-verification process more convenient and more efficient. In this workflow, the agent selects methods and calls the corresponding tools to revi
3. **Methodology & Architecture:** Categories: hep-ph, cs.MA, hep-th. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [OmniAct: One Policy, One Million Embodiments](http://arxiv.org/abs/2611.33158v1)
**arXiv ID:** `2611.33158v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33158v1) | **Published:** 2026-11-24
**Authors:** Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how dif...
2. **Key Technical Contributions:** From Abstract: ferences in robot morphology should shape manipulation strategies. We introduce OmniAct, a cross-embodiment manipulation policy that conditions directly on each robot's kinematics in a specific scene to produce embodiment-specific behavior. This kinematic graph represents the robot's joint positions
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification](http://arxiv.org/abs/2611.33143v1)
**arXiv ID:** `2611.33143v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.33143v1) | **Published:** 2026-11-24
**Authors:** Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities unde...
2. **Key Technical Contributions:** From Abstract: r robot motion and collision constraints. Independent checks use simulation state and episode records to assess outcomes and task requirements, with stronger checks of geometry, coverage, or placement. It comprises 250 manually validated tasks across 11 types in five groups and 27 indoor environment
3. **Methodology & Architecture:** Categories: cs.RO, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-24. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
