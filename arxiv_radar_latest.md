# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-19 19:49:11 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Learning to Interact in Multi-Agent Self-Play for Controllable Autonomous Driving Scenario Generation](http://arxiv.org/abs/2611.24876v1)
**arXiv ID:** `2611.24876v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24876v1) | **Published:** 2026-11-18
**Authors:** Beyazit Yalcinkaya, Ethan Pronovost, Maximilian Naumann, Marcell Vazquez-Chanlatte

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large-scale, multi-agent self-play trains robust driving policies effectively in simulation, but controlling these models to generate specific, safety-critical edge cases remains a key challenge. Existing goal-conditioned self-play frameworks rely primarily on static map-location goals and fail to r...
2. **Key Technical Contributions:** From Abstract: eliably produce complex agent interactions such as aggressive tailgating or adversarial cut-offs. These agent interactions are necessary for rigorous autonomous vehicle (AV) testing. To address this, we present an extended multi-agent self-play framework that introduces agent-relative dynamic goals.
3. **Methodology & Architecture:** Categories: cs.RO, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
We extend goal-conditioned multi-agent self-play with
agent-relative goals. This addition is opt-in, introducing min-
imal interface changes without altering the core reward struc-
ture or training algorithm. Training on a mixture of static and
agent-relative goals yields a single controllable policy capable
of executing novel behaviors while maintaining baseline capa-
bilities. Consequently, these lightweight additions yield more
controllable policies capable of executing a broader spectrum
of scenarios relevant to AV testing.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration](http://arxiv.org/abs/2611.24915v1)
**arXiv ID:** `2611.24915v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24915v1) | **Published:** 2026-11-18
**Authors:** Zhaocheng Yu, Kui Jiang, Jing Cao, Yiang Chen, Xiaocheng Feng et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on tas...
2. **Key Technical Contributions:** From Abstract: k-dependent yet overlapping channel responses in the shared model. An offline task-prior search uses activation and gradient statistics to group channels with similar response profiles, then searches task-specific modulation coefficients over non-representative channels while leaving representative 
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
We presented PrismRestore, a compact agentic image
restoration framework built upon a shared-backbone tool-
box. By leveraging task-specific channel modulation, our
offline prior search constructs multiple callable restoration
actions from a single frozen all-in-one model, substantially
reducing toolbox storage overhead. A GRPO-trained pol-
icy enables adaptive action composition according to evolv-
ing image states, with quality-grouped and process-aware
rewards supporting sequential optimization. Extensive ex-
periments on synthetic and real-world benchmarks demon-
strate improved restoration performance over the evaluated
all-in-one baselines and competitive restoration quality rel-
8
ative to multi-model agents, alongside red
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](http://arxiv.org/abs/2611.24924v1)
**arXiv ID:** `2611.24924v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24924v1) | **Published:** 2026-11-18
**Authors:** Jiahang Lin, Jiahao Chen, Yiding Wang, Shichun Liu, Chengjun Pan et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the harness and benchmar...
2. **Key Technical Contributions:** contributions:
• We propose AHE-Beta, a harness evolution framework centered on user requirements. It combines
user-driven evaluation, team-based modification, and requirement-driven selection to identify
unmet needs, develop general fixes, and merge changes that resolve verified requirements.
• We show that requirement-centered harness evolution improves pass@1, user rating, and token
efficiency on held-out tasks. AHE-Beta raises pass@1 from 21.9% to 33.3% over Base Harness,
surpassing Claude Code, Meta-Harness, and AHE. Gains across all four domains and transfer to
other models without further evolution support the generality of the evolved harness.
3. **Methodology & Architecture:** Categories: cs.SE, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling](http://arxiv.org/abs/2611.24849v1)
**arXiv ID:** `2611.24849v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24849v1) | **Published:** 2026-11-18
**Authors:** Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole, William Stern

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask ...
2. **Key Technical Contributions:** From Abstract: whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scalable judges for automatic relevance labeling. Specifically, ExecJudges uses a frontier LLM to turn as
3. **Methodology & Architecture:** Categories: cs.IR, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Decomposing SGD Dynamics in Neural Networks: Teacher-Induced Spikes and Variance Inflation](http://arxiv.org/abs/2611.24908v1)
**arXiv ID:** `2611.24908v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24908v1) | **Published:** 2026-11-18
**Authors:** Samet Demir, Zafer Dogan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We study two-layer neural networks trained by stochastic gradient descent (SGD) on a multi-index teacher model, focusing on how first-layer parameters orthogonal to the teacher subspace affect generalization. We decompose the first-layer weights into a signal component aligned with the teacher and a...
2. **Key Technical Contributions:** From Abstract: n orthogonal complement, and analyze their joint SGD dynamics together with the second layer in the proportional limit. We show that although SGD updates to the complement are initially isotropic, the training dynamics induce teacher-dependent spectral spikes in the complement Gram matrix. This emer
3. **Methodology & Architecture:** Categories: stat.ML, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** conclusion
with T ◦-stopping removed.
The self-consistency
1 + τ Kτ (
p
B(m) + 1) + δ ≤ B(m), 2 + τ Kτ ( √ B∗ + 1) + δ ≤ B∗, (88)
is solvable at constants B(m), B∗ = O((τ Kτ )2 + δ2 + 1) (LHS grows only as √ B). Telescoping
the w- and u-recursions and bounding the martingale by δ on the high-probability event yields
wT (m) ∧t ≤ B(m) and uT (r) ∧t ≤ B∗ for all t ≤ Tmax. Since wT (m) > B(m) if T (m) < Tmax, and
likewise for u, this gives T (m) = T (r) = Tmax. With w0 = O(1/n) from ∥mi,0∥2 ∼ χ2 k⋆ /n and
u0 = 1 + o(1) from ∥f ⊥ i,0∥2 ∼ χ2 n−k⋆ /n, w0 ≤ 1 and u0 ≤ 2 with probability 1 − o(1).
Conclusion. Setting Bτ := Cτ + B(m) + B∗ — a constant depending only on
(τ, α, ηa, ηf , λ, k⋆, Lg , ∥g∥∞, ∥σ∥∞, ∥σ′∥∞, ∥σ′′∥∞, Ksg) — proves the lemma, es
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [On Evaluating User Simulators for Interactive Agents](http://arxiv.org/abs/2611.24892v1)
**arXiv ID:** `2611.24892v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24892v1) | **Published:** 2026-11-18
**Authors:** Hengguang Zhou, I-Hung Hsu, Li Chen, Priyanshi Shrivastava, Anastasios Angelopoulos et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This uncertainty makes it dif...
2. **Key Technical Contributions:** From Abstract: ficult to interpret simulator evaluation. To understand what a high benchmark score tells us about simulator quality, we (meta-)evaluate the metrics themselves. To instantiate this meta-evaluation, we deliberately perturb simulated replays to induce failures such as altered goals, omitted constraint
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Choosing What to Observe: Budget-Paired Counterfactual Audits for Credible Evaluation of Visual Agents](http://arxiv.org/abs/2611.24867v1)
**arXiv ID:** `2611.24867v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24867v1) | **Published:** 2026-11-18
**Authors:** Ruiqi Liu, Jinming Li, Mo Wang, Yang Lu, Yanlan Kang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Visual agents that read dense documents must ration a finite observation budget across candidate regions, yet answer accuracy conflates where an agent looks, how it adapts to the reads that remain, and how it an?swers once observation stops. We introduce budget-paired counterfactual audits, an evalu...
2. **Key Technical Contributions:** contributions:
• Budget- and value-paired counterfactual tests that separate horizon-sensitive planning from fixed-role
heuristics under identical public evidence.
• Exact trajectory return accounting that decomposes end-to-end accuracy loss into stepwise acquisition
loss and terminal decision loss.
• An empirical audit across controlled decisions, complete rollouts and natural forms, showing that
later-read routing dominates policy loss and that natural-document gains depend on reference definitions
and whole-image comparators.
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling](http://arxiv.org/abs/2611.24940v1)
**arXiv ID:** `2611.24940v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24940v1) | **Published:** 2026-11-18
**Authors:** Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent lat...
2. **Key Technical Contributions:** From Abstract: ent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight instead predicts the future directly in the visual token space in which its VLM perceives the present. C
3. **Methodology & Architecture:** Categories: cs.RO, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws](http://arxiv.org/abs/2611.24877v1)
**arXiv ID:** `2611.24877v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24877v1) | **Published:** 2026-11-18
**Authors:** Zhiyu Liu, Xinyu Yang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the three promises where the answers could be checked. From the International Stroke Trial we trained fo...
2. **Key Technical Contributions:** From Abstract: ur kinds of model (logistic regression, explainable boosting machine, gradient-boosted trees, neural network) for two outcomes on patients randomised earlier, planted one flaw in each of 24 copies (an under-predicted subgroup, a reversed risk factor or an implausible step) and mixed them with the 8 
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Unified Law for Visual Tasks (The Four Laws of Computer Vision)](http://arxiv.org/abs/2611.24917v1)
**arXiv ID:** `2611.24917v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.24917v1) | **Published:** 2026-11-18
**Authors:** Sen Fang, Yalin Feng, Yancheng Zhang, Yanxin Zhang, Zonglin Lyu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Our starting point is an inspiration and hypothesis: if the wo...
2. **Key Technical Contributions:** From Abstract: rld information is encoded into image, which we call World Snapshots, then image processing is world processing, and image generation is World Snapshot generation. Furthermore, if all visual and visualization tasks can be reformulated as generation tasks, then a unified method, World Snapshot Models
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-18. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
