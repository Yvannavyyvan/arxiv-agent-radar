# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-04 19:11:55 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation](http://arxiv.org/abs/2611.05319v1)
**arXiv ID:** `2611.05319v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05319v1) | **Published:** 2026-11-03
**Authors:** Zhen Tao, Xun Zhou, Xuhui Chen, Ziyue Qiao, Qingqiang Sun

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based recommendation as an ag...
2. **Key Technical Contributions:** From Abstract: entic-communication process in four stages: BUILD a self-description, TRANSMIT it along the collaborative graph, UNDERSTAND the other side, and SYNC it from the next interaction. This formulation reveals three unresolved communication challenges: the item side never produces a comparable self-descri
3. **Methodology & Architecture:** Categories: cs.IR, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](http://arxiv.org/abs/2611.05376v1)
**arXiv ID:** `2611.05376v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05376v1) | **Published:** 2026-11-03
**Authors:** Hao Fei

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, f...
2. **Key Technical Contributions:** From Abstract: ail to find the right words, and face hard choices without the benefit of their own history, because the machine that could help stands outside the situation. As AI moves into the physical world, attention has settled on one kind of intelligent individual, the embodied robot; we argue that the era o
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Adversarial Speculative Reasoning Improves Long Horizon Agents](http://arxiv.org/abs/2611.05345v1)
**arXiv ID:** `2611.05345v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05345v1) | **Published:** 2026-11-03
**Authors:** Hongyin Luo, Wei Fang, Lijie Yang, Owen Stepan, Daniel Suit et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this view does not hold ...
2. **Key Technical Contributions:** contributions:
1. We show that speculative verification is lossless in distri-
bution but not uniform in numerical precision. Noise grows
with slot position inside a verification block, appearing in
two frontier models with different draft architectures.
2. We recast the draft model from an accelerator into an
allocator of context precision. Draft acceptance decides
which tokens are committed through low-noise residual
sampling, a degree of freedom that is traditionally treated
as irrelevant.
3. We introduce reverse-direction preference training of the
draft at decision points, so that the target model writes the
decisions that shape a long-horizon trajectory.
4. We improve end-to-end success on long-horizon software-
engineering agentic ta
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
Speculative decoding has been typically viewed purely as a
systems optimization to improve the decoding speed since
rejection sampling does not change the target distribution.
We argue that the draft can decide what tokens in the context
are encoded more accurately. An adversarial draft model
Adversarial Speculative Reasoning Improves Long Horizon Agents11
utilizes this feature to improve reasoning capability. At deci-
sion points it proposes reasoning draft that the target model
should reject, so the target encodes critical decisions more
precisely from the start of a verification block, while every-
where else the draft stays an ordinary high-acceptance draft.
With adversarial draft models, GLM-5.3 and DeepSeek-
V4.1-Flash gain
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers](http://arxiv.org/abs/2611.05304v1)
**arXiv ID:** `2611.05304v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05304v1) | **Published:** 2026-11-03
**Authors:** Minsoo Cheong, Sungjoo Yoo

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively r...
2. **Key Technical Contributions:** From Abstract: educes parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows linearly with the number of loop steps and becomes the main memory bottleneck. We observe that the KV cache of looped models is highly redundant along the loop axis and that the loop steps
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](http://arxiv.org/abs/2611.05320v1)
**arXiv ID:** `2611.05320v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05320v1) | **Published:** 2026-11-03
**Authors:** Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration e...
2. **Key Technical Contributions:** From Abstract: pisode of the robot in the target scene and rebuilds the task in simulation: it writes the scene, an expert controller, and a success judge. The simulator supplies exact actions, and a video model conditioned on real images renders each rollout as photographic video, generating all camera views toge
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution](http://arxiv.org/abs/2611.05313v1)
**arXiv ID:** `2611.05313v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05313v1) | **Published:** 2026-11-03
**Authors:** Dian Jin, Jinluan Yang, Kairong Han, Baohong Li, Zijing Hu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and accelerate policy learn...
2. **Key Technical Contributions:** From Abstract: ing. However, self-generated memories often contain noisy supervision and functionally entangled, redundant, or conflicting knowledge, making direct distillation difficult. Under limited training budgets, these issues can hinder knowledge internalization and even degrade performance. To address this
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments](http://arxiv.org/abs/2611.05361v1)
**arXiv ID:** `2611.05361v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05361v1) | **Published:** 2026-11-03
**Authors:** Zhipeng Zhong, Matthew Coombes, Cunjia Liu

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner surveys. We present a LiDARbased reference-generation pipeline for evaluating the zero-shot performa...
2. **Key Technical Contributions:** From Abstract: nce of feed-forward visual-geometry models alongside conventional structure-from-motion (SfM) methods. The pipeline reuses camera images, LiDAR scans, and reference poses from existing multi-sensor localization datasets to generate per-view depth maps and visible reference point clouds. To address v
3. **Methodology & Architecture:** Categories: cs.CV, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](http://arxiv.org/abs/2611.05372v1)
**arXiv ID:** `2611.05372v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05372v1) | **Published:** 2026-11-03
**Authors:** Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depe...
2. **Key Technical Contributions:** From Abstract: nds on hand-tuned controllers, and training data on physical robots are costly to collect. We present PolicyIK, a goal-conditioned reinforcement learning policy for high-precision IK. It updates joint-position references from pose feedback and observes its accumulated reference relative to the measu
3. **Methodology & Architecture:** Categories: cs.RO, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Suppressing Misaligned Behaviors in Language Models, Durably](http://arxiv.org/abs/2611.05358v1)
**arXiv ID:** `2611.05358v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05358v1) | **Published:** 2026-11-03
**Authors:** Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the b...
2. **Key Technical Contributions:** From Abstract: ehavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure co
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection](http://arxiv.org/abs/2611.05340v1)
**arXiv ID:** `2611.05340v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.05340v1) | **Published:** 2026-11-03
**Authors:** Omar Nusrat

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration or a monitor-unit (MU) calculation can affect every patient treated with it. MedPhysBench has ten seeded generators of calculation items in radiation therapy, di...
2. **Key Technical Contributions:** From Abstract: agnostic imaging, nuclear medicine and radiation protection, up to clinical tasks such as a TG-51 calibration worksheet. Reference answers come from code implementing the governing protocols, and a grader converts units and applies tolerance bands. From the same inputs, separate checking items test 
3. **Methodology & Architecture:** Categories: physics.med-ph, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-03. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
