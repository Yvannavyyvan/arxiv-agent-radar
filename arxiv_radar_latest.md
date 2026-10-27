# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-27 17:10:38 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution](http://arxiv.org/abs/2610.35733v1)
**arXiv ID:** `2610.35733v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35733v1) | **Published:** 2026-10-26
**Authors:** Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies that balance competing objectives, such as helpfulness versus honesty in safety and alignment, or s...
2. **Key Technical Contributions:** From Abstract: peed versus energy in robotics. The optimal policy can vary sharply with objective-weighting combinations, and the extent of this variation depends crucially on the degree of conflict among objectives, making per-preference policy learning sample-inefficient. In this paper, we introduce objective-co
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.MA, cs.RO, stat.ML. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](http://arxiv.org/abs/2610.35767v1)
**arXiv ID:** `2610.35767v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35767v1) | **Published:** 2026-10-26
**Authors:** Tingzhu Bi, Xun Zhang, Jinglin Li, Ping Wang, Meng Ma

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design beats letting a cap...
2. **Key Technical Contributions:** From Abstract: able model investigate on its own. We compare three simple harnesses that prescribe none of the model's calls (one call over an evidence package, a SQL agent and the Codex coding agent) with five published LLM RCA agents and with statistical and causal methods on RCAtlas, 90 validated cases from eig
3. **Methodology & Architecture:** Categories: cs.AI, cs.DC, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](http://arxiv.org/abs/2610.35817v1)
**arXiv ID:** `2610.35817v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35817v1) | **Published:** 2026-10-26
**Authors:** Benjamin Pikus, Daniel Saunders, Mircea Mironenco, Salman Mohammadi, Mathew Mathew et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot via a simple tool h...
2. **Key Technical Contributions:** From Abstract: arness. We use a pretrained 27B parameter model to bootstrap world understanding and reasoning, followed by supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move the robot. Without any real-world robot data during training, ZAP reaches 96.7% success on real-world tasks, m
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [A Unified Arena for LLM Agents across Diverse Eurogame](http://arxiv.org/abs/2610.35773v1)
**arXiv ID:** `2610.35773v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35773v1) | **Published:** 2026-10-26
**Authors:** Fengrui Zhang, Xiang Li, Ruomeng Ding, Jiayi Yuan, Yuchen Huang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution frameworks leave unclear whi...
2. **Key Technical Contributions:** From Abstract: ch competitive advantages persist across settings. We introduce DECE (Diverse Eurogame Competitive Environments), a unified arena spanning ten Eurogames with shared interfaces and evaluation protocols. These games combine lasting strategic commitments, competition over shared resources, and multiple
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](http://arxiv.org/abs/2610.35832v1)
**arXiv ID:** `2610.35832v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35832v1) | **Published:** 2026-10-26
**Authors:** Yifei Yao, Yude Zou, Guanbo Jiao, Xing Gao, Ning Gao et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be thoroughly evaluated. I...
2. **Key Technical Contributions:** From Abstract: n this report, we evaluate GPT-6-Astra on EBench as the core of an agent that controls a robot through an agent harness under the same visual and proprioceptive observation protocol as post-trained policies. We study two agent configurations: direct control, in which the agent generates waypoint com
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](http://arxiv.org/abs/2610.35829v1)
**arXiv ID:** `2610.35829v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35829v1) | **Published:** 2026-10-26
**Authors:** Amine Lbath, Massih-Reza Amini

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulnerabilities by working...
2. **Key Technical Contributions:** From Abstract:  as a security expert would: they run analysis tools, explore the surrounding code, test hypotheses and weigh the evidence before forming their own judgement. This reasoning, however, spans many model calls, so that each verdict takes minutes of compute, far too long for real-time screening. Faster 
3. **Methodology & Architecture:** Categories: cs.CR, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
REVAdetects vulnerabilities by probing an LLM’s internal
representations of a function and its security context in a single
forward pass. On PrimeVul’s held-out test set, it matches or
exceeds agentic detectors run on the same LLM, with fewer
false positives, in about one second per function and at a small
fraction of their cost. An LLM’s internal representations thus
carry more information about vulnerabilities than its verdicts,
and reading them enables real-time screening of every function
as it is written.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models](http://arxiv.org/abs/2610.35804v1)
**arXiv ID:** `2610.35804v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35804v1) | **Published:** 2026-10-26
**Authors:** Aidar Myrzakhan, Zhiqiang Shen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response. Efficient generation depends not only on which tokens are easy to predict, but also on how committing to them helps predict the remaining positions. A high...
2. **Key Technical Contributions:** From Abstract: ly predictable token may provide little useful context, while revealing a less predictable token can help several other positions become predictable sooner. We propose dSpark, a new schedule distillation-based framework for learning when to commit tokens for faster diffusion language generation. To 
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [I-HITL: Inalienable Human-in-the-Loop](http://arxiv.org/abs/2610.35835v1)
**arXiv ID:** `2610.35835v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35835v1) | **Published:** 2026-10-26
**Authors:** Samuel Breckenridge, Dani Vilardell, Wenhao Wang, Fan Zhang, Ari Juels

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly. We introduce the concept of inalienable h...
2. **Key Technical Contributions:** From Abstract: uman-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harness) compromised by the agent. A strong I-HITL protocol additionally ensures such approval even when an
3. **Methodology & Architecture:** Categories: cs.CR, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO](http://arxiv.org/abs/2610.35716v1)
**arXiv ID:** `2610.35716v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35716v1) | **Published:** 2026-10-26
**Authors:** Shurun Li, Michael Hua Wang, Haibo Zeng, Long Wang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning with verifiable rewards trains on cheap checks, such as unit tests, that a policy can learn to game, while a stronger check is too expensive to run on every rollout. We study how to spend a limited strong-verifier budget in GRPO, separating which weakly passing rollouts to aud...
2. **Key Technical Contributions:** From Abstract: it from what reward a caught hack receives. At a fixed policy state with centered advantages, the expected update depends on a design only through each rollout's marginal audit probability and correction; reflecting a caught hack's reward about the failure reward negates the advantages of an all-hac
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-26. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Learning Force-Reactive Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.35862v1)
**arXiv ID:** `2610.35862v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.35862v1) | **Published:** 2026-10-26
**Authors:** Sihang Li, Xiaofeng Guo, Jinkun Cao, Charlie Cheng, Ruihan Yang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Many everyday tasks require controlling contact force as well as motion. On a humanoid, this force must often be coordinated across both hands and the whole body, and cannot be specified by kinematic trajectories alone. Therefore, we present FLORE, a framework for learning force-reactive humanoid lo...
2. **Key Technical Contributions:** From Abstract: co-manipulation. We collect robot-free demonstrations using two force-sensing UMI-style handheld grippers for hand motion and contact wrenches, and wearable trackers for body motion. A force-reactive diffusion policy takes vision, proprioception, and measured wrenches as input, then predicts actions
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.LG, eess.SY. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
We presented FLORE, a framework for learning
force-reactive humanoid loco-manipulation from robot-free
demonstrations that record both motion and contact wrench.
Our hybrid compliance whole-body controller tracks the
learned force commands, allowing the humanoid to sustain
contact, coordinate both hands, and apply force while walk-
ing and balancing. On three tasks, the force-reactive policy
succeeds in 80% of rollouts, compared with 26.7% for a
position-only policy. By making force a shared interface
between demonstrations, policies, and whole-body control,
FLOREextends robot-free imitation learning to contact-rich
skills that motion alone cannot specify.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
