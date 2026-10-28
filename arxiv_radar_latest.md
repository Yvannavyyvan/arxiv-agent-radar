# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-28 17:44:39 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](http://arxiv.org/abs/2610.37609v1)
**arXiv ID:** `2610.37609v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37609v1) | **Published:** 2026-10-27
**Authors:** Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organ...
2. **Key Technical Contributions:** From Abstract: izing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Environment-aware Scheduling), an online scheduler that learns from rollout history. EnvSched assigns sc
3. **Methodology & Architecture:** Categories: cs.LG, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](http://arxiv.org/abs/2610.37648v1)
**arXiv ID:** `2610.37648v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37648v1) | **Published:** 2026-10-27
**Authors:** Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which e...
2. **Key Technical Contributions:** From Abstract: xplicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts 
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](http://arxiv.org/abs/2610.37649v1)
**arXiv ID:** `2610.37649v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37649v1) | **Published:** 2026-10-27
**Authors:** Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without bei...
2. **Key Technical Contributions:** From Abstract: ng told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary physics. The evaluated LLMs act as explorers, manipulating objects and building tools to investigate t
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](http://arxiv.org/abs/2610.37624v1)
**arXiv ID:** `2610.37624v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37624v1) | **Published:** 2026-10-27
**Authors:** Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is ...
2. **Key Technical Contributions:** From Abstract: confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant facts is crossed while their text is held fixed (480 tasks). Across Qwen2.5-7B, Llama-3.1-8B, and t
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL, cs.MA, cs.SI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](http://arxiv.org/abs/2610.37592v1)
**arXiv ID:** `2610.37592v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37592v1) | **Published:** 2026-10-27
**Authors:** Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck, Prashant Doshi

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on information they will not ...
2. **Key Technical Contributions:** From Abstract: have when they act, an information gap between training and execution. It widens under partial observability, observation noise, and openness, where the set of agents and tasks present changes during an episode. Existing methods transfer centralized guidance in one direction only, removing or distil
3. **Methodology & Architecture:** Categories: cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [VideoLVR: Latent Visual Reasoning over Grounded Video Evidence](http://arxiv.org/abs/2610.37613v1)
**arXiv ID:** `2610.37613v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37613v1) | **Published:** 2026-10-27
**Authors:** Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability...
2. **Key Technical Contributions:** From Abstract:  to reason over video content. Existing approaches maintain visual grounding during reasoning in two main ways: they either refer to evidence using textual coordinates, which specify symbolic locations rather than the visual content itself, or reinsert cropped regions or frames into the multimodal c
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](http://arxiv.org/abs/2610.37666v1)
**arXiv ID:** `2610.37666v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37666v1) | **Published:** 2026-10-27
**Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning fro...
2. **Key Technical Contributions:** From Abstract: m them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thou
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](http://arxiv.org/abs/2610.37657v1)
**arXiv ID:** `2610.37657v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37657v1) | **Published:** 2026-10-27
**Authors:** Igor Shilov, Xiaoxue Yang, Alexander Panfilov, Evgenii Kortukov, Matthieu Meeus et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted conten...
2. **Key Technical Contributions:** From Abstract: t without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it against SecAlign++, a state-of-the-art finetuning-based defense, and ASIDE, a defense that, like ours, builds instruction-data separation into the model architecture. We show that HoS 
3. **Methodology & Architecture:** Categories: cs.LG, cs.CL, cs.CR. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices](http://arxiv.org/abs/2610.37599v1)
**arXiv ID:** `2610.37599v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37599v1) | **Published:** 2026-10-27
**Authors:** Kailai Feng, Haoxiang Rao, Yuxiang Wei, Bo Chen, Junsong Li et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Developing on-device image models requires considering practical user needs, task types and device resource constraints. However, existing benchmarks provide limited guidance on identifying capability gaps between on-device models and server-side models. We introduce MoI-Bench, a benchmark grounded ...
2. **Key Technical Contributions:** From Abstract: in mobile user needs, comprising 64 subtasks and 1150 samples. It defines 16 operations, such as removal and replacement, and eight visual target categories covering content such as portraits and text. These form two orthogonal axes whose applicable combinations define specific tasks, such as removi
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [GEPA-Curator: Curated Learning for Self Improving Agents](http://arxiv.org/abs/2610.37651v1)
**arXiv ID:** `2610.37651v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.37651v1) | **Published:** 2026-10-27
**Authors:** Zack Yu, Nicholas Lee, Minjae Lee, Lakshya Agarwal, Luca Manolache et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitatio...
2. **Key Technical Contributions:** From Abstract: ns, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to the prompt optimizer for better performance. We introduce GEPA-Curator, a framework that augments the
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-27. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
