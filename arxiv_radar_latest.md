# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-10 19:09:29 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2611.12856v1)
**arXiv ID:** `2611.12856v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12856v1) | **Published:** 2026-11-09
**Authors:** Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of sy...
2. **Key Technical Contributions:** From Abstract: stem structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as wor
3. **Methodology & Architecture:** Categories: cs.CL, cs.SE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](http://arxiv.org/abs/2611.12886v1)
**arXiv ID:** `2611.12886v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12886v1) | **Published:** 2026-11-09
**Authors:** Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the ev...
2. **Key Technical Contributions:** From Abstract: idence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the observation state, rather than only the output distribution, as an object of alignment. First, Ground-Drop-GRPO (GD-GRPO) trains spatial and temporal specialists with evidence-aware rewards 
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](http://arxiv.org/abs/2611.12872v1)
**arXiv ID:** `2611.12872v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12872v1) | **Published:** 2026-11-09
**Authors:** Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined representations, whic...
2. **Key Technical Contributions:** From Abstract: h may miss relevant memories and overlook heterogeneous evidence needs across queries. We introduce \textbf{\hivemem}, a multimodal memory framework that interleaves \textbf{\textsc{H}}or\textbf{\textsc{i}}zontal Memory Expansion with \textbf{\textsc{Ve}}rtical Evidence Composition. For horizontal m
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning](http://arxiv.org/abs/2611.12825v1)
**arXiv ID:** `2611.12825v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12825v1) | **Published:** 2026-11-09
**Authors:** Jihwan Jeong, Guy Tennenholtz, Yinlam Chow, Chih-Wei Hsu, Craig Boutilier

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** AI systems must often maintain bounded memory of unbounded interaction histories. However, optimizing the memory representation, and its updates, for downstream task utility is difficult for standard reinforcement learning (RL) due to severe credit assignment bottlenecks induced by sparse, delayed r...
2. **Key Technical Contributions:** From Abstract: ewards. We introduce MaxIM (Maximally Informative Incremental Memory), a framework that formulates incremental summarization as a capacity-constrained, information-theoretic reward-shaping problem. Grounded in value suboptimality bounds, we show that bounding sequential information loss motivates ma
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Limitations
G.1 Broader Impacts
MaxIM introduces a principled approach to bounded memory management in streaming environments.
On the positive side, this framework enhances the reliability of long-horizon AI agents by actively
suppressing hallucinations and enforcing factual grounding through recursive consistency. This is
particularly beneficial for high-stakes applications requiring persistent context—such as educational
tutoring, accessibility tools, and medical or legal document analysis—where unbounded context
scaling is computationally prohibitive.
However, the capability to persistently track dynamically evolving latent states (such as user emotions
or implicit intents, as demonstrated in our WildChat experiments) poses potential pri
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [World In-Context Learning for Agentic Robot Manipulation](http://arxiv.org/abs/2611.12885v1)
**arXiv ID:** `2611.12885v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12885v1) | **Published:** 2026-11-09
**Authors:** Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the wor...
2. **Key Technical Contributions:** From Abstract: ld the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in 
3. **Methodology & Architecture:** Categories: cs.CV, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Mitigating Agentic Deception via Evaluation-Side Partially Observable Games](http://arxiv.org/abs/2611.12835v1)
**arXiv ID:** `2611.12835v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12835v1) | **Published:** 2026-11-09
**Authors:** Hanxiao Li, Shutong Liu, Yongjia Ma, Jiaming Ji, Juntao Dai et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfu...
2. **Key Technical Contributions:** From Abstract: lness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial observability by predefined evaluator latent belief space or one-shot monitoring, which do not extend to free-form language space and vulnerable to stronger deceptions that evade simple monitor
3. **Methodology & Architecture:** Categories: cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs](http://arxiv.org/abs/2611.12883v1)
**arXiv ID:** `2611.12883v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12883v1) | **Published:** 2026-11-09
**Authors:** Zhaoying Pan, Shenyu Lu, Jun Hui Wong, Junyi Chai, Xiaoqian Wang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We...
2. **Key Technical Contributions:** From Abstract:  identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow visual or textual evidence. Building on this, we introduce a lightweight, training-free intervention that biases these heads toward a designated trusted modality at inference time. 
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [DreamLander: A 6-DOF World Model based Reinforcement Learning Planetary Lander](http://arxiv.org/abs/2611.12824v1)
**arXiv ID:** `2611.12824v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12824v1) | **Published:** 2026-11-09
**Authors:** George Nehma, Patrick Quinn, Madhur Tiwari, Camilo Riano-Rios

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Soft powered descent landings are becoming evermore important in the field of space exploration and scientific advancement, because of their ability to deliver mission critical payloads, both highly accurately and safely. The high efficiency restriction on planetary landings due to the severely limi...
2. **Key Technical Contributions:** From Abstract: ted fuel supply results in the need for optimal guidance trajectories and control. Model based reinforcement learning is proving to be an important tool in simplifying the highly complex process of generating optimal guidance trajectories and control. In this work, we present DreamLander, a state of
3. **Methodology & Architecture:** Categories: cs.RO, math.OC. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
In this work we present DreamLander, a DreamerV3 based MBRL framework capable of a highly precise and
efficient planetary landing control policy. It has shown to capably learn the dynamics of the EDL problem and then
formulate a control policy capable of landing the vehicle with pinpoint accuracy. The model trains efficiently on data
provided in simulation and with the latent imagination it produces. We demonstrated its capability to successfully solve
the EDL over a large range of initial conditions, and learn a policy that is intuitive. The model based nature of this
framework also enables the further inclusion of safety based algorithms to be included so that undesired states can
be avoided, further demonstrating the capabilit
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [How Well Does AI Peer Review Work? A Benchmark Built from 100 Planted Errors](http://arxiv.org/abs/2611.12820v1)
**arXiv ID:** `2611.12820v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12820v1) | **Published:** 2026-11-09
**Authors:** Paul Litvak

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** One hundred known errors were planted into 10 open-access psychology papers, and the modified papers were then run through frontier models and two commercial AI review tools. The best single system caught 71 of the 100 errors, while the worst caught 30. Pooling every system's output caught 93. Model...
2. **Key Technical Contributions:** From Abstract: s are only partly correlated in the errors they find, which makes ensembling a big lever for finding issues in papers. Seven errors could not be caught by any system, and all seven were omissions: information deleted from a paper rather than mistakes inserted into it. Refine.ink contributes more uni
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
AI peer review is here whether we like it or not. AI-generated science is also here and will increasingly be a larger 
and larger portion of new scientific knowledge. That knowledge will quickly outstrip the ability of humans to 
evaluate it. Amidst that new knowledge (especially at first), there are going to be a considerable number of mistakes. 
We need to start thinking very carefully about how to surmount the evaluation and human expert attention 
bottleneck. Training the next generation of scientists with the requisite domain expertise, critical thinking, and AI-
native thinking is essential if we have any hope of avoiding being drowned in all the new information, or of 
preventing it from being riddled with errors and mista
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Automated Knowledge Acquisition Pipeline for Disassembly Instructions: A Comparison of NLP and Generative AI Frameworks](http://arxiv.org/abs/2611.12816v1)
**arXiv ID:** `2611.12816v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.12816v1) | **Published:** 2026-11-09
**Authors:** Tim Schnieders, Tareq Maximilian Gabriel Ahrari, Oliver Petrovic, Christian Brecher

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** The push towards circularity and Re-X principles presents a challenge to SMEs, particularly due to increasing product complexity that impedes the adoption of disassembly automation. This paper introduces and compares two frameworks for extracting disassembly instructions from unstructured informatio...
2. **Key Technical Contributions:** From Abstract: n sources, such as disassembly manuals. Our goal is to transform natural language text into a structured, curated and machine-readable format. We implemented and tested a rule-based Natural Language Processing (NLP) framework against a generative AI framework leveraging LLMs. The performance of both
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
