# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-08 18:15:54 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models](http://arxiv.org/abs/2610.10478v1)
**arXiv ID:** `2610.10478v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10478v1) | **Published:** 2026-10-07
**Authors:** Tan Yu, Alexander Bukharin, Khushi Bhardwaj, Jennifer Williams, Zirui Liu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** How can we predict which base checkpoint is worth an expensive round of agentic post-training? End-to-end pass@$K$ tests whether successful behavior already appears in a base model's distribution, but it is a poor fit for agentic coding: many base checkpoints cannot reliably produce the well-formed ...
2. **Key Technical Contributions:** From Abstract: tool invocation required to complete a task end-to-end. Single-shot or short-horizon tasks avoid these tool-calling failures by collapsing a multi-step interaction into a fixed prompt and a single patch, but they sidestep the core capability we care about: maintaining coherent state over many tool-u
3. **Methodology & Architecture:** Categories: cs.AI, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [SciExam for ENSO: Can AI Agents Build Climate Models?](http://arxiv.org/abs/2610.10513v1)
**arXiv ID:** `2610.10513v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10513v1) | **Published:** 2026-10-07
**Authors:** Yinling Zhang, Langchen Liu, Dongbin Xiu, Xueyan Zou, Xu Kuang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Language-model agents are increasingly asked to carry out open-ended scientific research, yet their results are usually graded against a known answer, a rubric, or a language-model reviewer, none of which can tell whether a new scientific model is valid. The AI Science Exam for El Nino-Southern Osci...
2. **Key Technical Contributions:** From Abstract: llation (SciExam for ENSO) is a benchmark in which agents build low-order stochastic models of ENSO, the dominant mode of interannual climate variability, from real observations. Within a six-hour budget, agents process the observations, write their own diagnostics, which are then frozen, and develo
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG, physics.ao-ph. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Decoupling Exploration from Optimization in RLVR](http://arxiv.org/abs/2610.10536v1)
**arXiv ID:** `2610.10536v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10536v1) | **Published:** 2026-10-07
**Authors:** Saif Punjwani, Micah Goldblum

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augm...
2. **Key Technical Contributions:** From Abstract: enting RLVR with strong novelty incentives has seen limited success and can degrade model quality. Because verifiable rewards supervise only a narrow slice of the model's knowledge and behavior, such degradations are difficult to recover from. Instead, we decouple exploration from optimization in a 
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory](http://arxiv.org/abs/2610.10533v1)
**arXiv ID:** `2610.10533v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10533v1) | **Published:** 2026-10-07
**Authors:** Hongru Cai, Ran Wei, Wenjie Wang, Chengfa Wu, Ning Song et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Conditional memory architectures such as DeepSeek Engram use input n-grams to look up learned embeddings, expanding the capacity of large language models (LLMs) with limited additional computation. Beyond model scaling, this architecture has demonstrated the potential to decouple factual knowledge s...
2. **Key Technical Contributions:** From Abstract: torage from general-purpose computation, offering a promising route to updating factual knowledge while keeping the Transformer backbone fixed. Realizing this potential is challenging because different expressions of a fact may activate different n-gram embeddings, while updating shared embeddings c
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Label-free cell counting and viability prediction with brightfield imaging and deep learning](http://arxiv.org/abs/2610.10473v1)
**arXiv ID:** `2610.10473v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10473v1) | **Published:** 2026-10-07
**Authors:** Amir Reza Vazifeh, Christian Zeigler, Sornanathan Meyyappan, Richard Jeske, Jason W. Fleischer

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Cell viability assessment is a core requirement in cell culture systems, with critical applications in biopharmaceutical manufacturing and drug development. Conventionally, it is measured by adding membrane-impermeable dyes to a sample (a process called staining), which allows compromised cell membr...
2. **Key Technical Contributions:** From Abstract: anes to be distinguished from intact ones. However, staining has several limitations: (a) chemical agents can perturb normal cellular processes of the cells being measured, (b) it is often ambiguous to assign viability to individual cells whose membrane integrity is only partially compromised. (c) p
3. **Methodology & Architecture:** Categories: cs.CV, q-bio.CB. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](http://arxiv.org/abs/2610.10479v1)
**arXiv ID:** `2610.10479v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10479v1) | **Published:** 2026-10-07
**Authors:** Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR)...
2. **Key Technical Contributions:** From Abstract: , a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an agent recovers metric scale, iteratively refines the scene using visual feedback, and checks task-r
3. **Methodology & Architecture:** Categories: cs.RO, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Long-WAM: Scaling the Context of World-Action Models](http://arxiv.org/abs/2610.10528v1)
**arXiv ID:** `2610.10528v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10528v1) | **Published:** 2026-10-07
**Authors:** Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Real-time robot control demands enough visual history to infer motion and task progress, but processing that history can delay action. We present Long-WAM, a model-system framework for scaling the context of causal world-action models under real-time control constraints. Our central finding is that ...
2. **Key Technical Contributions:** From Abstract: access to history is not the same as using it: longer histories pay off far more when the video foundation is pretrained autoregressively (AR). We first learn causal prediction from robot and egocentric videos without action labels, then preserve this history-to-future structure during world-action 
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing](http://arxiv.org/abs/2610.10507v1)
**arXiv ID:** `2610.10507v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10507v1) | **Published:** 2026-10-07
**Authors:** Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, ...
2. **Key Technical Contributions:** From Abstract: in many tasks, the evidence required for a solution is not explicitly present in any single source item. Instead, it must be derived through filtering, aggregation, or computation across multiple source items. In this work, we introduce RECAST (Routing Evidence through Computation, Access, and Synth
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution](http://arxiv.org/abs/2610.10498v1)
**arXiv ID:** `2610.10498v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10498v1) | **Published:** 2026-10-07
**Authors:** Python Song, Zhixuan Liang, Kelsey Fu, Mengdi Wang, Junfeng Yang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic ha...
2. **Key Technical Contributions:** From Abstract: rnesses can adapt around the model, but current self-evolving harnesses use robot trials inefficiently when deciding which code and skill changes to pursue. We introduce EmbodiedRSI, a self-evolving agentic harness that autonomously decides where to explore next and turns the resulting physical inte
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
EmbodiedRSI shows that a self-evolving agentic harness can gain lasting value from each physical trial by
using the outcome to select the next experiment, refine code and skills together, and retain experience for
later adaptation. Across simulated benchmarks and real-robot tasks, EmbodiedRSI improves generalization
and learning efficiency, and transfers the simulation-evolved harness to physical execution. More broadly,
continual robot learning can take place in the harness around a frozen robot foundation model when physical
evidence shapes both the next experiment and the knowledge carried into future tasks.
Limitations.Code-as-policy and agentic harness methods learn executable behavior from physical trajectories
without upda
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [RoboJEPA: Scaling Robotic Latent World Models](http://arxiv.org/abs/2610.10515v1)
**arXiv ID:** `2610.10515v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.10515v1) | **Published:** 2026-10-07
**Authors:** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we pr...
2. **Key Technical Contributions:** From Abstract: esent RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to pre
3. **Methodology & Architecture:** Categories: cs.AI, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-07. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
