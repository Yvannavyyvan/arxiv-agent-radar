# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-13 19:01:37 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](http://arxiv.org/abs/2611.17294v1)
**arXiv ID:** `2611.17294v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17294v1) | **Published:** 2026-11-12
**Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and ...
2. **Key Technical Contributions:** From Abstract: GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level scheduling across interconnected Macs. Each agent retains its workspace and private development envi
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.CL, cs.DC. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Goal Encoding in LLMs](http://arxiv.org/abs/2611.17297v1)
**arXiv ID:** `2611.17297v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17297v1) | **Published:** 2026-11-12
**Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior ...
2. **Key Technical Contributions:** CONTRIBUTIONS
Internally an autoregressive transformer language model M has L layers. We write the residual
stream at layer ℓ and position t as hℓ t = hℓ−1 t + mℓ t + P j aℓj t , where mℓ t is the output of the MLP and
aℓj t is the contribution of the j-th attention head. Setting aside normalization and positional encoding,
an attention head’s contribution to the residual stream is
aℓj t =

X
i≤t
Attn(qt, K)ivi

 W ℓj O , Attn(qt, K) = softmax
 qtK ⊤ √dhead  (1)
with query qt = hℓ−1 t W ℓj Q and keys K = {k1, ...kt}, where ki = hℓ−1 i W ℓj K . Affinity of query and
key states determine the mixture over the value states vi = hℓ−1 i W ℓj V , which is then projected with
the output weights W ℓj O and added to the residual stream.
2.2 SEQ
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** LIMITATIONS
Selection of goal attributes. We operationalize goals through three attributes drawing from Bratman
(1987)’s planning theory: pre-commitment, plasticity and persistence (Section 1). The literature also
describes other goal attributes such as pro-activeness (whether an agent sets its own goals rather than
only responding to its environment; Wooldridge & Jennings (1995); Barandiaran et al. (2009)), and
deliberate adoption (the agent decides whether to pursue a goal at all; Bratman (1987); Frankfurt
(1971)). We have not included these attributes in this study, as it is unclear how to operationalize
them in LLMs.
Persistence. We focus on temporal persistence, the retention of a goal-encoding throughout its
execution across multiple 
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](http://arxiv.org/abs/2611.17267v1)
**arXiv ID:** `2611.17267v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17267v1) | **Published:** 2026-11-12
**Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed g...
2. **Key Technical Contributions:** From Abstract: eographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. LiveGeo places geographic tasks within this evolving environment, requiring agents to actively acquire 
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** conclusion 
that the trip cannot finish within 56 minutes.
Why this failure. The updated evidence reaches the explanation 
and arithmetic, yet the actual Boolean decision retains the earlier 
answer.
Ground truth: feasible: false. The updated trip exceeds 56 
minutes.
Figure 45: Decision Inertia in Task-Only Mobility Planning
(Claude Opus 5). The traffic update changes the route calculation
and written conclusion, but the final Boolean feasibility judgment
remains true.
53
Constraint-Preserving Replanning Failure: re-
pairing one dependency leaves another unre-
solved.
Figure 46 shows Grok 4.5 responding to The But-
tery’s closure by selecting Flat Iron Victoria for
eight diners. The model explicitly notices that
Flat Iron’s maximum party s
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research](http://arxiv.org/abs/2611.17332v1)
**arXiv ID:** `2611.17332v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17332v1) | **Published:** 2026-11-12
**Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document...
2. **Key Technical Contributions:** From Abstract:  which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace 
3. **Methodology & Architecture:** Categories: cs.CL, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](http://arxiv.org/abs/2611.17323v1)
**arXiv ID:** `2611.17323v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17323v1) | **Published:** 2026-11-12
**Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested ...
2. **Key Technical Contributions:** From Abstract: in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and studying how agents navigate this space under limited supervision. We find that even under weak feedba
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces](http://arxiv.org/abs/2611.17314v1)
**arXiv ID:** `2611.17314v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17314v1) | **Published:** 2026-11-12
**Authors:** Abigail L. Tenenbaum, R. Thomas McCoy

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes...
2. **Key Technical Contributions:** From Abstract:  a network to many related functions to facilitate its subsequent learning of similar functions. Prior work has shown that these meta-learned networks can learn new functions rapidly, but how they do so remains unclear. To investigate their internal structure, we take inspiration from classic work d
3. **Methodology & Architecture:** Categories: cs.LG, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](http://arxiv.org/abs/2611.17280v1)
**arXiv ID:** `2611.17280v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17280v1) | **Published:** 2026-11-12
**Authors:** Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that info...
2. **Key Technical Contributions:** From Abstract: rmation by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information. We demonstrate this threat by training two open-weight models to infer gender and age-group labels
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems](http://arxiv.org/abs/2611.17239v1)
**arXiv ID:** `2611.17239v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17239v1) | **Published:** 2026-11-12
**Authors:** Hannah Li

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** In interactive systems where users engage with LLMs, users are adaptive and, after observing LLM responses, can change their prompting strategy, as well as the type and difficulty of subsequent tasks. Thus model responses can influence the set of prompts on which the model is subsequently evaluated....
2. **Key Technical Contributions:** From Abstract:  We study the implications of this user adaptivity and prompt endogeneity for the evaluation of LLMs. We define two classes of estimands for comparing models: the common-distribution effect, which compares model performance on the same distribution of prompts, and the induced-distribution effect, wh
3. **Methodology & Architecture:** Categories: stat.ME, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](http://arxiv.org/abs/2611.17287v1)
**arXiv ID:** `2611.17287v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17287v1) | **Published:** 2026-11-12
**Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this reg...
2. **Key Technical Contributions:** From Abstract: ime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry makes standard RLVR unreliable, because reinforcing verified positives can directly reward shortcuts 
3. **Methodology & Architecture:** Categories: cs.LG, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Learning When Diffusion Language Models Should Regenerate](http://arxiv.org/abs/2611.17320v1)
**arXiv ID:** `2611.17320v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.17320v1) | **Published:** 2026-11-12
**Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error u...
2. **Key Technical Contributions:** From Abstract: sually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a verifier that predicts whether a partially generated sequence will reach a correct answer. Trained on the final correctness of the model's own trajectories, DiVR decides when to regenerate a block and w
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-12. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
