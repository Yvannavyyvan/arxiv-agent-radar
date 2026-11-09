# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-09 21:49:16 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [On Agentic Manipulation Policies](http://arxiv.org/abs/2611.09892v1)
**arXiv ID:** `2611.09892v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09892v1) | **Published:** 2026-11-06
**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze age...
2. **Key Technical Contributions:** From Abstract: ntic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the 
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can Agentic Systems Close the Gap in Radiology with Production AI Tools?](http://arxiv.org/abs/2611.09836v1)
**arXiv ID:** `2611.09836v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09836v1) | **Published:** 2026-11-06
**Authors:** Aubin Charley, Julien Khlaut, Charles Corbière, Pierre Manceron, Corentin Dancette et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Radiology AI has developed along two paths: specialized models that perform well on narrow tasks but cover few clinical findings, and generalist models that address a broader range of tasks but remain prone to hallucination and inaccurate measurements. Combining the two through agentic systems offer...
2. **Key Technical Contributions:** From Abstract: s a route towards comprehensive radiology reporting, but published systems are tied to one modality or body part. We describe a radiology agentic framework that standardizes how an orchestrator calls modular tools to produce a structured report, and use it to measure what such a system can do with t
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Limitations
PARROT reports are fictional, which gives scale and privacy but is not a proxy for real-world
clinical situations [10]. Evaluation is text-only and every tool call is simulated from the reference
report, so tool error is excluded by design and broad classes return more than real detectors
would. The held-out runs use 100 reports, enough for the direction of the effect but not to rank
the cutoffs. The catalog is a snapshot (FDA decisions to March 2026) built with LLM extraction
and consolidation, and the main orchestrator is one model; absolute numbers will move with the
model.
Can Agentic Systems Close the Gap in Radiology? 13
5 Conclusion
Agentic systems can already compose today’s cleared radiology tools into a report, and thi
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse](http://arxiv.org/abs/2611.09891v1)
**arXiv ID:** `2611.09891v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09891v1) | **Published:** 2026-11-06
**Authors:** Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very...
2. **Key Technical Contributions:** From Abstract:  efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for constructing robust CPU-executable agentic reasoning caches (ARCs) from LLM reasoning traces. ARCs show on-par performance with frontier LLMs across a range of difficult mathematical a
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Video-Coder: Reinforcing Agentic Coding for Video Generation](http://arxiv.org/abs/2611.09894v1)
**arXiv ID:** `2611.09894v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09894v1) | **Published:** 2026-11-06
**Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Code...
2. **Key Technical Contributions:** From Abstract: r, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals to downstream video generators. To support this paradigm, we design a dedicated data pipeline and c
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ZeoBench: A Benchmark for Self-Supervised Learning on 3D Zeolite Representations](http://arxiv.org/abs/2611.09880v1)
**arXiv ID:** `2611.09880v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09880v1) | **Published:** 2026-11-06
**Authors:** Aaron Sun, Yachan Liu, Ping Yang, Peng Bai, Subhransu Maji

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Zeolites are an important class of porous crystalline materials with broad applications in gas storage, separations, and catalysis. Although hundreds of thousands of experimentally realized and hypothetical zeolite structures are known, identifying materials optimized for a target application remain...
2. **Key Technical Contributions:** contributions:
1. We introduce ZeoBench, a benchmark for SSL on dense 3D grids of all-silica zeolites, built
from 331k real and hypothetical zeolite structures, with fixed train/validation/test splits.
2. We standardize six existing downstream adsorption-property prediction tasks with label-
budget splits, evaluation metrics, and linear-probe and fine-tuning protocols.
3. We benchmark four SSL objectives, out-of-domain 3D volumetric pretraining, ImageNet-
pretrained 2D backbones adapted to 3D, hand-crafted descriptors, and supervised baselines.
4. We show that in-domain SSL substantially improves low-label adsorption prediction, with
contrastive methods producing the strongest frozen representations and SSL initialization
improving fine-tun
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning](http://arxiv.org/abs/2611.09872v1)
**arXiv ID:** `2611.09872v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09872v1) | **Published:** 2026-11-06
**Authors:** Haoyu Wang, Ru Wang, Yuanyuan Wang, Jiaxian Guo, Mingming Gong

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its ...
2. **Key Technical Contributions:** From Abstract: error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the downstream effects of finite-rollout variation. We propose \emph{Prompt-Conditional Distributionall
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Computer-Use Agents Are Embodied Generalists](http://arxiv.org/abs/2611.09847v1)
**arXiv ID:** `2611.09847v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09847v1) | **Published:** 2026-11-06
**Authors:** Pranjal Aggarwal, Sean Welleck

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** In many areas of AI, general-purpose models have increasingly replaced handcrafted methods and specialized architectures. We argue that embodied AI is poised for a similar shift. Our key claim is that embodied tasks can be formulated as interaction with digital software. Specifically, we build softw...
2. **Key Technical Contributions:** From Abstract: are that renders an agent's view of a physical environment on a screen and provides controls for acting in it. A computer-use agent (CUA) can then perform embodied tasks through the same screenshots and keyboard and mouse actions that it uses to operate ordinary software. Using a single CUA design a
3. **Methodology & Architecture:** Categories: cs.LG, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Scenario Orchestration for Closed-loop Policy Evaluation of Autonomous Driving](http://arxiv.org/abs/2611.09888v1)
**arXiv ID:** `2611.09888v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09888v1) | **Published:** 2026-11-06
**Authors:** Frieda Rong, Zhaoyue Wang, Veer Kapadia, Vishaka Rajani, Aren A. Babikian et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Scenario-based simulation is central to evaluating autonomous-driving policies, but a scenario scripted before execution (i.e., with predetermined, fixed actor routes and speeds) may not preserve its intended interaction once the tested ego policy responds in closed loop. Scripted scenarios cannot a...
2. **Key Technical Contributions:** From Abstract: dapt to unanticipated ego behavior, while learned traffic actors may remain reactive without reliably realizing a particular scenario intent. We introduce a scenario orchestrator that continuously monitors the joint traffic state and adapts non-ego actors through re-timing, re-routing, and role reas
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
Closed-loop policy evaluation is subject to closed-loop
drift. A scenario scripted before execution with predeter-
mined actor routes, speeds, or behaviors may not preserve
its intended interaction once the ego policy responds in
closed loop. Reactive actors are not enough, nor are scenario
triggers. We address this gap with a scenario orchestrator
that continuously monitors the joint traffic state and jointly
adapts non-ego actors through re-timing, re-routing, and role
reassignment, solving a constrained optimization at each step
so that the intended interaction remains attainable while
interventions stay limited and traffic remains feasible.
Experiments in CARLA, across scenario families and
ego policies, show that this orches
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation](http://arxiv.org/abs/2611.09864v1)
**arXiv ID:** `2611.09864v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09864v1) | **Published:** 2026-11-06
**Authors:** Xun Tu, Minghao Zou, Karthik Desingh

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains ch...
2. **Key Technical Contributions:** From Abstract: allenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often require accurate dynamics models, or through learning-based methods, which reduce this requirement but
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
We presented a task-aware grasp selection framework for
prehensile goal-conditioned large-object loco-manipulation.
By training one unified manipulation policy across multiple
initial grasp configurations, the learned critic captures the
long-horizon utility of different grasp configurations. Dis-
tilling these values into a lightweight grasp utility network
enables the robot to select a suitable grasp before physical
interaction without explicitly estimating privileged physi-
cal properties of the object. Simulation results demonstrate
improved rearrangement success over fixed and randomly
selected grasp configurations. Future work will extend the
evaluation to additional household objects and real-world
deployment on the SPOT p
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [BEV3SR: Evidence-Aware 3D Spatial Reasoning from Video](http://arxiv.org/abs/2611.09816v1)
**arXiv ID:** `2611.09816v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.09816v1) | **Published:** 2026-11-06
**Authors:** Fan Zhu, Rui Yu

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** 3D spatial reasoning from video remains challenging for VLMs because videos provide sequential, view-local observations rather than persistent metric scene records. Many questions must be answered in a query-specified perspective rather than the observed camera viewpoint, and prompting with a fixed ...
2. **Key Technical Contributions:** From Abstract: set of RGB views may miss sparse or occluded visual cues. To address these gaps, we introduce BEV3SR, a training-free and backbone-agnostic framework for RGB-D videos with camera parameters. BEV3SR turns video observations into queryable metric bird's-eye-view (BEV) scene memory and formalizes each 
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-06. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
