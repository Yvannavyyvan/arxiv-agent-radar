# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-07 18:14:26 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?](http://arxiv.org/abs/2610.08775v1)
**arXiv ID:** `2610.08775v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08775v1) | **Published:** 2026-10-06
**Authors:** Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities ...
2. **Key Technical Contributions:** From Abstract: into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets. Agents choose their own approach, such as training a small model or
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning](http://arxiv.org/abs/2610.08761v1)
**arXiv ID:** `2610.08761v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08761v1) | **Published:** 2026-10-06
**Authors:** Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute i...
2. **Key Technical Contributions:** From Abstract: n embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales verification through the co-evolution of the policy, training curriculum, and judge. The Policy Improv
3. **Methodology & Architecture:** Categories: cs.AI, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Future Work
While the judge evaluation set evolves with the policy to capture newly exposed failure patterns, the current
framework retains a fixed policy evaluation set as a consistent anchor for measuring improvement across
iterations. Future work could preserve a fixed held-out test set for comparable reporting while introducing an
adaptive policy evaluation set that co-evolves with the policy and judge to provide increasingly informative
signals for failure discovery and curriculum construction. The framework also still relies on reasoning-annotated
data: although the reference-free VeriFine-Judge can filter low-quality reasoning during training, the reference
reasoning used for policy evaluation remains human-verified. A natural extens
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](http://arxiv.org/abs/2610.08773v1)
**arXiv ID:** `2610.08773v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08773v1) | **Published:** 2026-10-06
**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current def...
2. **Key Technical Contributions:** CONTRIBUTIONS
1. ADVSIM2REAL, a two-stage framework that co-evolves a task curriculum, an injection adver-
sary, and a web agent inside a frozen web world model, so that both tasks and attacks track the
current agent.
2. The success-flip reward, which replays an accepted clean run to the injection step and credits
the adversary only when the continuation fails, so that failures the agent makes on its own earn
nothing.
3. A benchmark of 150 form-filling web tasks in five skill strata, with protected fields and forbidden
controls, a reactive adversary that chooses when and what to inject, and a deterministic browser
check of the submitted form; we release it with all checkpoints and trajectories.
4. Evidence that the curriculum stage buys cap
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas](http://arxiv.org/abs/2610.08781v1)
**arXiv ID:** `2610.08781v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08781v1) | **Published:** 2026-10-06
**Authors:** Ziyu Chen, Yilun Zhao, Jiashuo Sun, Yiling Ma, Manasi Patwardhan et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-grounded ideation remains challenging, as existing approaches based on prompting or feedback lack st...
2. **Key Technical Contributions:** contributions
build on prior work [Jurgens et al., 2018, Lo et al., 2020]. Specifically, we assemble a corpus of approximately
14K papers spanning machine learning and natural science. Leveraging LLMs, we first extract the core intellectual
contribution of each work, then retrospectively trace its most influential prior studies, and further reverse-engineer
the implicit anchor linking foundational literature to subsequent research innovations. By exploiting the inherent
provenance structure of academic publications, this pipeline produces high-quality structured training signals, and a
study with the original authors confirms that the mined prior works closely reflect the literature they credit for their
ideas.
To determine whether anchor-d
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Sherpa: Teaching LLMs to Teach Adaptively](http://arxiv.org/abs/2610.08778v1)
**arXiv ID:** `2610.08778v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08778v1) | **Published:** 2026-10-06
**Authors:** Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what g...
2. **Key Technical Contributions:** From Abstract: ood teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address this, we introduce Sherpa, a multi-turn reinforcement learning framework that instantiates multiple s
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [DepthWorld: 3D World Model for Robot Manipulation](http://arxiv.org/abs/2610.08780v1)
**arXiv ID:** `2610.08780v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08780v1) | **Published:** 2026-10-06
**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look...
2. **Key Technical Contributions:** contributions:
1.We introduce a calibration pipelinefor recovering metric depth and accurate multi-view ex-
trinsics from any multi-view stereo teleoperation collection with a known URDF. The pipeline
combines learned stereo depth with a joint factor graph optimization that pools all episodes of
the same physical robot to recover its shared kinematic parameters (joint offsets, hand-eye cal-
ibration) alongside per-scene extrinsics. Applied to DROID [18], this yieldsDROID-3D—a
calibrated 3D corpus providing dense metric depth and recalibrated multi-view extrinsics for
over 70,000 episodes.
2.We train DepthWorld, a Stable Video Diffusion-based world model that jointly predicts multi-
view RGB and depth via spatial latent tiling that leaves th
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Mission-Aware Attestation Envelopes for Time-Critical Autonomous Action: A Hardware-in-the-Loop V2I Study](http://arxiv.org/abs/2610.08771v1)
**arXiv ID:** `2610.08771v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08771v1) | **Published:** 2026-10-06
**Authors:** Dimitrios Nikou, Nikolaos Kekatos, Sophia Petridou, Stylianos Basagiannis

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** An autonomous system that asks for a privileged physical action is usually gated on integrity evidence: a platform proves what it is running, and the request is granted or refused on that basis. Such a gate is normally treated as a predicate, yet the evidence behind it has an age, the decision that ...
2. **Key Technical Contributions:** From Abstract: consumes it has a latency, and the physical system that waits for it has a deadline. We formulate mission-aware attestation as a runtime assurance contract that holds only when integrity is valid, the evidence is fresh enough, and the decision completes inside a budget derived from the current physi
3. **Methodology & Architecture:** Categories: cs.CR, cs.RO, eess.SY. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
Integrity evidence is normally treated as a predicate, and it is not one. It is
generated at a moment, it ages, the decision that consumes it costs time, and
the physical process that waits for that decision has a horizon. We formulated
mission-aware attestation as a contract over those three quantities, showed that
the resulting four outcomes separate failures a binary gate reports identically
or not at all, and showed that the two margins interact: below a threshold on
the freshness bound, lateness is unobservable because every late decision is also
stale.
On a hardware-in-the-loop platform in which a simulator supplies the physi-
cal state and a TPM-backed roadside unit supplies the evidence, combining the
two yields a region 
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation](http://arxiv.org/abs/2610.08743v1)
**arXiv ID:** `2610.08743v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08743v1) | **Published:** 2026-10-06
**Authors:** Wenwen Si, Honghao Wei

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which adapts the retained action set using critic scores and an online threshold. The threshold is update...
2. **Key Technical Contributions:** From Abstract: d from binary feedback indicating whether the set contains an action in a proxy target. We prove a deterministic bound on the observed proxy miss rate along adaptive trajectories. To quantify the effect of pruning on reward, we derive an exact decomposition of value loss into filtering and selection
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation](http://arxiv.org/abs/2610.08784v1)
**arXiv ID:** `2610.08784v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08784v1) | **Published:** 2026-10-06
**Authors:** Kun Song, Yiming Wang, Yilin Chen, Tianyi Ding, Jiaxin Tian et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Pretrained robotic policies can suffer substantial performance degradation under out-of-distribution (OOD) conditions encountered during deployment, motivating post-training through real-world interaction. However, reinforcement-learning (RL)-based post-training typically requires substantial enviro...
2. **Key Technical Contributions:** From Abstract: nment interactions, a burden that is especially significant in manipulation, where each trial can be slow, costly, or destructive. Therefore, we present PEARS, a physics-prior-guided hybrid RL framework for sample-efficient online adaptation of pretrained policies with tactile feedback. After each e
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Neural Petri flows for chemical reactions](http://arxiv.org/abs/2610.08750v1)
**arXiv ID:** `2610.08750v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.08750v1) | **Published:** 2026-10-06
**Authors:** Jose Eduardo Escrig Molina, Daniel Probst

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Petri nets have been used to describe chemical processes such as reactions.They map well to chemistry: Places are the bonds between atoms and the free valence of each atom, a token is a unit of bond order, a transition forms or breaks a bond, the conserved quantities are the valence budgets of the a...
2. **Key Technical Contributions:** From Abstract: toms, and the enabling rule is the valence rule. These semantics are not guaranteed by learned models of reactions or neural networks that are built on Petri nets that use the net as a scaffold for message passing. Here, we ask what architecture remains a Petri net for every value of its weights. We
3. **Methodology & Architecture:** Categories: cs.LG, physics.chem-ph, q-bio.QM. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
