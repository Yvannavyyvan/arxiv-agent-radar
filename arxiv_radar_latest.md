# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-25 15:22:14 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)
**arXiv ID:** `2610.31650v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31650v1) | **Published:** 2026-10-22
**Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an ...
2. **Key Technical Contributions:** From Abstract: executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](http://arxiv.org/abs/2610.31656v1)
**arXiv ID:** `2610.31656v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31656v1) | **Published:** 2026-10-22
**Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from ...
2. **Key Technical Contributions:** From Abstract: past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation 
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Cost-Aware Abstention for LLM-Based IT Ticket Classification](http://arxiv.org/abs/2610.31657v1)
**arXiv ID:** `2610.31657v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31657v1) | **Published:** 2026-10-22
**Authors:** Sachin Gupta

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a...
2. **Key Technical Contributions:** From Abstract:  public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on cali
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
We presented a reproducible empirical framework for asking
whether automatic ticket routing is cost-preferred under stated
assumptions. On one public corpus and primary illustrative
(0,1,5)costs, a calibration-selected TF-IDF + LR policy
reduces held-out modeled cost by 38.1 %; in a post-hoc 16-
setting cost analysis, frozen calibration-selected policies beat
both always-route and always-defer in 14 settings. The fixed
break-even rule defers every ticket for seven prompted LLM
conditions and routes only 19/1,000 for Haiku few-shot. Iso-
tonic lowers ECE but generally does not improve correctness
ranking. The result is a scoped deployment warning, not a
universal ranking of model families. Separating prediction,
confidence, reject
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](http://arxiv.org/abs/2610.31624v1)
**arXiv ID:** `2610.31624v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31624v1) | **Published:** 2026-10-22
**Authors:** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the ...
2. **Key Technical Contributions:** From Abstract: first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforcement learning with verifiable rewards (RLVR) make a model more likely to express instrumental-converge
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](http://arxiv.org/abs/2610.31636v1)
**arXiv ID:** `2610.31636v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31636v1) | **Published:** 2026-10-22
**Authors:** Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compi...
2. **Key Technical Contributions:** From Abstract: les each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four phenomena. The largest is a machine-generated content farm of 1,408,437 documents (5.32%) that passe
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](http://arxiv.org/abs/2610.31667v1)
**arXiv ID:** `2610.31667v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31667v1) | **Published:** 2026-10-22
**Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes th...
2. **Key Technical Contributions:** From Abstract: e candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based methods assign a score to each partial solution and discard those predicted to ultimately lead to an i
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](http://arxiv.org/abs/2610.31670v1)
**arXiv ID:** `2610.31670v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31670v1) | **Published:** 2026-10-22
**Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a...
2. **Key Technical Contributions:** From Abstract:  shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-f
3. **Methodology & Architecture:** Categories: cs.CV, cs.LG, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [BrickWright: Agentic Creation of Physically Feasible Brick Builds](http://arxiv.org/abs/2610.31651v1)
**arXiv ID:** `2610.31651v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31651v1) | **Published:** 2026-10-22
**Authors:** Ava Pun, Kevin Dai, Sally Chen, Maxwell Jones, Ruixuan Liu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for a...
2. **Key Technical Contributions:** From Abstract: ssembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds, we present BrickWright, a framework for generating physically feasible brick builds from text or im
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution](http://arxiv.org/abs/2610.31644v1)
**arXiv ID:** `2610.31644v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31644v1) | **Published:** 2026-10-22
**Authors:** Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez, Luigi Di Stefano

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the othe...
2. **Key Technical Contributions:** From Abstract: r hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimental evaluation focused on deploying LRs with gigapixel imagery. GigaBench includes images collected, a
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](http://arxiv.org/abs/2610.31639v1)
**arXiv ID:** `2610.31639v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.31639v1) | **Published:** 2026-10-22
**Authors:** Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling ...
2. **Key Technical Contributions:** our contributions:
1We use the term “causal” throughout this work to denote strict procedural dependence (i.e., subsequent
reasoning steps are strictly conditioned on the related prior steps) rather than formal statistical causal inference
or structural causal models. This scoping is stated in full in
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-22. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
