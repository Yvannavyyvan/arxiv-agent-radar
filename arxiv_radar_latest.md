# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-20 19:29:15 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](http://arxiv.org/abs/2611.26553v1)
**arXiv ID:** `2611.26553v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26553v1) | **Published:** 2026-11-19
**Authors:** Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)valid...
2. **Key Technical Contributions:** our contributions:
• Controlled Replication of Security Incidents Reported
in Media. We introduce ROGUE-AI, the first framework
that tests a reported agent incident by rebuilding it offline
together with a matched control that lacks only the blamed
cause. Agents repeated the reported mistake in 18% to 33%
of runs, against at most 1% in the controls (§3, §6).
• Multi-Agent Replication Pipeline. We build the pipeline
from Claude-, Gemini- and GPT-based specialist agents,
which find and verify reports, build each replication, and di-
agnose and fix failed replications. Because these agents can
fail like those they test, each judgment has an independent
3. **Methodology & Architecture:** Categories: cs.CR, cs.AI, cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models](http://arxiv.org/abs/2611.26531v1)
**arXiv ID:** `2611.26531v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26531v1) | **Published:** 2026-11-19
**Authors:** Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipel...
2. **Key Technical Contributions:** From Abstract: ine cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. For each model, an LLM generates and shortlists cross features from a combinatorial candidate space, and all features are then ranked by se
3. **Methodology & Architecture:** Categories: cs.IR, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
We presented an agentic system that optimizes the features of every
model it manages in an ads ranking fleet under serving and shared
pipeline-cost constraints. A single LLM, fine-tuned on feature out-
comes across the fleet, generates cross features; the LLM Researcher
finds gains by rebalancing volume across feature categories rather
than only scaling it up; and trimming keeps shared pipeline cost
within budget. On production models, the system improves NE by
0.75 0.80 0.85 0.90 0.95 1.00 1.05 1.10
Inference QPS relative to baseline
−1.0
−0.5
0.0
0.5
1.0
1.5
ΔNE vs. baseline (%)
faster and better
(higher QPS, lower NE)1200/789/47/90
150/50/15/15
Baseline (300/100/30/30)
Dominated trial
Pareto frontier
(a) NE vs. serving QPS.
1 
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](http://arxiv.org/abs/2611.26613v1)
**arXiv ID:** `2611.26613v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26613v1) | **Published:** 2026-11-19
**Authors:** Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succee...
2. **Key Technical Contributions:** From Abstract: d nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an intent-grounded critique framework in which the policy agent states a local intent alongside each action,
3. **Methodology & Architecture:** Categories: cs.RO, cs.CL, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](http://arxiv.org/abs/2611.26601v1)
**arXiv ID:** `2611.26601v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26601v1) | **Published:** 2026-11-19
**Authors:** Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports an...
2. **Key Technical Contributions:** From Abstract: d disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correctness, its availability and the strength of its evidence. We use this framework to systematize the p
3. **Methodology & Architecture:** Categories: cs.CR, cs.AI, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity](http://arxiv.org/abs/2611.26565v1)
**arXiv ID:** `2611.26565v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26565v1) | **Published:** 2026-11-19
**Authors:** Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. As a result,...
2. **Key Technical Contributions:** From Abstract:  it remains unclear whether current policies truly understand physics or merely interpolate from their training data. We address this gap through the lens of dynamic extrinsic dexterity and introduce PhyDEX, a throwing benchmark in which a robot must infer an object's mass, center of mass, and frict
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Backtracking Agent Applications Security Incidents](http://arxiv.org/abs/2611.26525v1)
**arXiv ID:** `2611.26525v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26525v1) | **Published:** 2026-11-19
**Authors:** Yicheng Cai, Taegyu Kim, Peng Liu

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are traj...
2. **Key Technical Contributions:** From Abstract: ectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstraction layer, while the CEP candidates are function calls at the app code execution layer. Due to this se
3. **Methodology & Architecture:** Categories: cs.CR, cs.AI, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](http://arxiv.org/abs/2611.26617v1)
**arXiv ID:** `2611.26617v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26617v1) | **Published:** 2026-11-19
**Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for...
2. **Key Technical Contributions:** From Abstract:  both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI, cs.LG, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Future Work
O2LaF learns transferable latent actions from unlabeled videos, but several challenges remain.
Structure and interpretability of latent actions. Although our learned actions transfer across visual
contexts and embodiments, their underlying structure remains poorly understood. Beyond quantitative
probing, interpreting individual latent actions still largely relies on inspecting their corresponding reference
videos. Learning more interpretable, compositional, and appearance-invariant action representations remains
an important direction for future work.
Toward decision-making world models. O2LaF learns latent actions that explain visual transitions
and control future video generation. However, its dynamics are optimized for visual
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [RL Post-Training in Diffusion Transformers Is Activation Steering](http://arxiv.org/abs/2611.26627v1)
**arXiv ID:** `2611.26627v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26627v1) | **Published:** 2026-11-19
**Authors:** Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that...
2. **Key Technical Contributions:** From Abstract:  improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately simple parameterization: a fixed set of steering vectors added to the block outputs of the frozen base 
3. **Methodology & Architecture:** Categories: cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning](http://arxiv.org/abs/2611.26562v1)
**arXiv ID:** `2611.26562v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26562v1) | **Published:** 2026-11-19
**Authors:** Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly, Catherine E. Hagen, Jason T. Lewis et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia...
2. **Key Technical Contributions:** From Abstract:  grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-aware multiple instance learning for slide-level classification as non-dysplastic Barrett's esophagus (N
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PlayCraft: Designing Engaging Games from Agent Play Experience](http://arxiv.org/abs/2611.26624v1)
**arXiv ID:** `2611.26624v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.26624v1) | **Published:** 2026-11-19
**Authors:** Weihao Cheng

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its...
2. **Key Technical Contributions:** From Abstract:  detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After
3. **Methodology & Architecture:** Categories: cs.AI, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-19. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
