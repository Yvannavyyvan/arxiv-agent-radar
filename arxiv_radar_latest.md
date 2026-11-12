# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-12 19:23:40 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](http://arxiv.org/abs/2611.14492v1)
**arXiv ID:** `2611.14492v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14492v1) | **Published:** 2026-11-10
**Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrac...
2. **Key Technical Contributions:** From Abstract: e, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind ea
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG, cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](http://arxiv.org/abs/2611.14511v1)
**arXiv ID:** `2611.14511v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14511v1) | **Published:** 2026-11-10
**Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across ...
2. **Key Technical Contributions:** From Abstract: diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical signals. To investigate automated ranking, we introduce PyriteRep, a structured representation of molecu
3. **Methodology & Architecture:** Categories: cs.LG, q-bio.QM. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](http://arxiv.org/abs/2611.14493v1)
**arXiv ID:** `2611.14493v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14493v1) | **Published:** 2026-11-10
**Authors:** Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based ...
2. **Key Technical Contributions:** Contributions
Agentic systems exhibit stochastic behavior [2] and execute com-
plex multi-step workflows involving tool usage, SQL generation,
and human interaction [4] that resist simple correctness checks.
Three evaluation paradigms have emerged (LLM-as-a-Judge, de-
terministic heuristics, and hybrid approaches), yet no systematic
comparison exists of how they perform across stability, detection,
and discovery for agentic systems.
We present a three-phase comparative evaluation of three frame-
works: Strands Evals (trace-based LLM judge), PromptFoo (text-only
LLM judge with red-teaming), and Agenta (deterministic heuristics).
We evaluate on two supply chain analytics agents and address three
research questions:
• RQ1 (Stability):How stabl
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL, cs.LG, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](http://arxiv.org/abs/2611.14519v1)
**arXiv ID:** `2611.14519v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14519v1) | **Published:** 2026-11-10
**Authors:** Emre Kutlusan, Yongmin Li

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whos...
2. **Key Technical Contributions:** From Abstract: e configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what determines this. We adapted a foundation model, DINOv2, with strategies ranging from tuning only its bias
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](http://arxiv.org/abs/2611.14515v1)
**arXiv ID:** `2611.14515v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14515v1) | **Published:** 2026-11-10
**Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way...
2. **Key Technical Contributions:** From Abstract:  to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information 
3. **Methodology & Architecture:** Categories: cs.LG, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking](http://arxiv.org/abs/2611.14477v1)
**arXiv ID:** `2611.14477v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14477v1) | **Published:** 2026-11-10
**Authors:** Arjun Rao, Nishant Gopinath

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Text-to-SQL systems over large pooled catalogs must first retrieve the tables a question needs. We compare against the published table recall of RASL, which uses Claude 3.5 models to extract keywords and select tables, on pooled BIRD, Spider, and Fiben catalogs. FERN (Feature-Engineered Ranking with...
2. **Key Technical Contributions:** From Abstract:  No generative LLM) instead fuses three frozen retrievers into 100 candidates, describes each with up to 120 features, and reorders them with LightGBM rankers fitted once on BIRD's training questions. On Spider, where it was not fitted, its candidate pool alone reaches RASL's published recall at fif
3. **Methodology & Architecture:** Categories: cs.IR, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](http://arxiv.org/abs/2611.14514v1)
**arXiv ID:** `2611.14514v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14514v1) | **Published:** 2026-11-10
**Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternati...
2. **Key Technical Contributions:** From Abstract: ve the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence 
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Accurate predictions of properties of energetic materials with tabular foundation models](http://arxiv.org/abs/2611.14462v1)
**arXiv ID:** `2611.14462v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14462v1) | **Published:** 2026-11-10
**Authors:** Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen, Dennis Christensen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also subst...
2. **Key Technical Contributions:** From Abstract: antially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given hand-crafted molecular descriptors and when they are given learned representations from Chemprop's m
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](http://arxiv.org/abs/2611.14504v1)
**arXiv ID:** `2611.14504v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14504v1) | **Published:** 2026-11-10
**Authors:** Adi Mashiach

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-lig...
2. **Key Technical Contributions:** From Abstract: and sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at hierarchical levels of resolution: functional (mechanism of action), residue (binding site localization, including orthosteric/allosteric discrimination), and bond (covalent versus non-covalen
3. **Methodology & Architecture:** Categories: cs.LG, q-bio.BM. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game](http://arxiv.org/abs/2611.14487v1)
**arXiv ID:** `2611.14487v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.14487v1) | **Published:** 2026-11-10
**Authors:** Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the...
2. **Key Technical Contributions:** From Abstract:  format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must rediscover the paper's core idea by asking yes-or-no questions. Built from 200 ICML 2026 papers, Re-Search tracks how a model's idea evolves as it asks questions and receives binary o
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-10. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
