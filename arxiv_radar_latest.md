# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-22 16:24:44 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](http://arxiv.org/abs/2610.30113v1)
**arXiv ID:** `2610.30113v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30113v1) | **Published:** 2026-10-21
**Authors:** Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (...
2. **Key Technical Contributions:** From Abstract: LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a benchmark and public leaderboard for end-to-end quantitative research on real A-share market data. A model constructs features and stock-scoring code, receives feedback only on 2022-
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.CE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](http://arxiv.org/abs/2610.30103v1)
**arXiv ID:** `2610.30103v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30103v1) | **Published:** 2026-10-21
**Authors:** Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi, Mahbub E Sobhani, Shubhashis Roy Dipta

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of ...
2. **Key Technical Contributions:** From Abstract: each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the same surface. To remove the textbook cues that enable recall, we build it with AgentGAN, an adversa
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](http://arxiv.org/abs/2610.30132v1)
**arXiv ID:** `2610.30132v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30132v1) | **Published:** 2026-10-21
**Authors:** Zhennan Wan, Jianfei Chen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL,...
2. **Key Technical Contributions:** From Abstract:  and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target
3. **Methodology & Architecture:** Categories: cs.CL, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](http://arxiv.org/abs/2610.30108v1)
**arXiv ID:** `2610.30108v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30108v1) | **Published:** 2026-10-21
**Authors:** Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multim...
2. **Key Technical Contributions:** From Abstract: odal task reasoning with physical action and revise decisions from the resulting feedback. This raises a central question: what changes when a multimodal agent moves from computer-use to robot-use? We introduce PAPAV, a unified capability-centric framework of five recurring functions: Perceive the c
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV, cs.MA, cs.MM. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Environment Duels: A Microcosm of LLM Co-Evolution](http://arxiv.org/abs/2610.30116v1)
**arXiv ID:** `2610.30116v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30116v1) | **Published:** 2026-10-21
**Authors:** Shibo Jin, Zhiqiu Xu, Yiling Zou, Shangyu Gong, Mayur Naik

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce Environment Duels, ...
2. **Key Technical Contributions:** From Abstract: a dynamic agentic benchmark that evaluates both capabilities on interactive environments. Each model writes environments, each with a privileged hint, aiming for tasks that capable solvers fail without the hint and pass with it. Across nine frontier LLMs, solving and authoring prove to be distinct s
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Agentic World Action Models](http://arxiv.org/abs/2610.30136v1)
**arXiv ID:** `2610.30136v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30136v1) | **Published:** 2026-10-21
**Authors:** Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. W...
2. **Key Technical Contributions:** From Abstract: e introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and action prediction. We jointly model code, future video, and robot actions as three coupled generative streams within a unified mixture-of-transformers architecture. Within this architec
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation](http://arxiv.org/abs/2610.30097v1)
**arXiv ID:** `2610.30097v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30097v1) | **Published:** 2026-10-21
**Authors:** Likui Zhang, Zhe Zhu, Zhihao Zhan, Yibo Bai, Hanlin Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typical...
2. **Key Technical Contributions:** From Abstract: ly suffer from delayed and biased credit assignment due to trajectory-level sparse rewards, while imbalanced subtask mastery creates bottlenecks that limit overall performance. To address these challenges, we propose AtomicRL, an RL post-training framework that leverages atomic task structures for r
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation](http://arxiv.org/abs/2610.30128v1)
**arXiv ID:** `2610.30128v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30128v1) | **Published:** 2026-10-21
**Authors:** Zhanshuo Cao, Jiakai Tang, Yuqi Zhou, Sunhao Dai, Jun Xu

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Existing sequential recommenders usually allocate a fixed computational budget to every item in a user's interaction history, regardless of the item's contribution to the final prediction. We challenge this de facto design with two diagnostic findings. (1) Non-uniform computational need: items withi...
2. **Key Technical Contributions:** From Abstract: n the same sequence vary drastically in how much computation they require. Most converge after shallow processing while a critical minority only stabilizes at full depth. (2) Suboptimality of fixed allocation: given oracle access to the target item, a non-uniform depth assignment consistently outran
3. **Methodology & Architecture:** Categories: cs.IR, cs.AI, cs.CL, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Asymmetric On-Policy Distillation Learns In-Context Exploration](http://arxiv.org/abs/2610.30105v1)
**arXiv ID:** `2610.30105v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30105v1) | **Published:** 2026-10-21
**Authors:** Sriyash Poddar, Yanda Bao, Jacob Krantz, Matthew Chang, Xavier Puig et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Sequential decision-making under partial observability is difficult because agents must explore to infer hidden, task-relevant information before acting effectively. Learning such information-gathering behaviors tabula rasa via online reinforcement learning is sample-inefficient, whereas offline imi...
2. **Key Technical Contributions:** contributions:
1. We present ASTEROID, a simple student–teacher distillation framework that enables in-context
exploration and test-time improvement learned solely from privileged experts.
2. We evaluate our method across 11 environments, including navigation in realistic household
simulators and real-world robot manipulation, where it outperforms RL and supervised baselines
under fixed exploration budgets while using two orders of magnitude fewer training interactions.
3. We show that learned policies exhibit efficient real-world exploration and, under appropriate
assumptions, recover posterior sampling with error linear rather than quadratic in context length.
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](http://arxiv.org/abs/2610.30089v1)
**arXiv ID:** `2610.30089v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.30089v1) | **Published:** 2026-10-21
**Authors:** Ruotong Liao, Meikel Kokowski, Xiaoxiao Sun, Yongqin Xian, Laura Bravo Sánchez et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Today's multimodal assistants are typically prompted to interpret the visual evidence presented to them. To offload the cognitive burden of remembering across long horizons, wearable assistants should instead proactively acquire and maintain useful memory as the user's surroundings evolve. Doing so ...
2. **Key Technical Contributions:** contributions:
•Formulation.We poseproactive memoryfor egocentric assistants: deciding from the
visual stream when to intervene and what to remember. It has three core components,
streaming egocentric perception, proactive initiative, and co-existent background operation,
framing it as object-centric ambient memory with ameasurable memory lifecycle.
•Evaluation protocol.We design a protocol built on multi-level proactiveness, three
ambient-memory tasks, and a question answering dataset that tests the quality of proactive
memory; evaluation metrics score jointly on timing and semantics of proactive initiatives.
•Benchmarking.We benchmark proprietary, open-source, video-language, and streaming
models on both daily and scientific scenarios and
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-21. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
