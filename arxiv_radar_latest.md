# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-18 19:49:04 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Do LLM Agents Still Need to Be Told How to Self-Improve?](http://arxiv.org/abs/2611.23219v1)
**arXiv ID:** `2611.23219v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23219v1) | **Published:** 2026-11-17
**Authors:** Shobhita Sundaram, Cansu Sancaktar, Phillip Isola

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-im...
2. **Key Technical Contributions:** From Abstract: prove? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for context-based optimization. Using the setting of gameplay as a testbed, a frozen LLM agent is given a comp
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching](http://arxiv.org/abs/2611.23229v1)
**arXiv ID:** `2611.23229v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23229v1) | **Published:** 2026-11-17
**Authors:** Giannis Daras, Marios Papachristou, Adam Klivans, Antonio Torralba, Constantinos Daskalakis

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Collecting large-scale, diverse, and high-quality post-training datasets for autoregressive language models is challenging. Consequently, Supervised Fine-Tuning (SFT) is typically applied to datasets significantly smaller than those used for pre-training, which leads to overfitting and the catastrop...
2. **Key Technical Contributions:** From Abstract: hic forgetting of the tails of the data distribution. To prevent this collapse, we introduce Ambient SFT, a principled framework for leveraging imperfect predictions to augment the fine-tuning set. In our method, a "frozen" version of the pre-trained model serves as a noisy teacher that the fine-tun
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [VIVID: Beyond Static Multi-Image Reasoning with Localized Visual Differences and Textual Entity Dynamics in Video MLLMs](http://arxiv.org/abs/2611.23153v1)
**arXiv ID:** `2611.23153v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23153v1) | **Published:** 2026-11-17
**Authors:** Chengqian Ma, Yuanze Zeng, Hongyu Wang, Mingfeng Lin, YiCheng Xiao et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Video question answering under tight frame budgets requires preserving localized motion and event order, yet current video multimodal large language models (MLLMs) reduce comprehension to static multi-image reasoning by discarding unselected frames and encoding keyframes independently: (1) Spatially...
2. **Key Technical Contributions:** From Abstract: , whole-frame pooling dilutes small moving targets into static backgrounds; (2) Temporally, dropping intermediate frames or averaging tokens erases inter-frame motion, confusing direction, speed, and order. We propose VIVID (Visual Inter-frame Variations and Individual Dynamics), which moves beyond 
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents](http://arxiv.org/abs/2611.23202v1)
**arXiv ID:** `2611.23202v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23202v1) | **Published:** 2026-11-17
**Authors:** Viet K. Nguyen, Mohammad I. Husain

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, exec...
2. **Key Technical Contributions:** From Abstract: ution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZTA), and remote attestation. ATI establishes federated trust through peer organizational certificate 
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
Secure collaboration among autonomous AI agents requires
trust mechanisms that extend beyond traditional network au-
thentication and API credentials. Although Public Key Infras-
tructure (PKI) provides a foundation for establishing crypto-
graphic identities, agentic AI introduces additional require-
ments, including verification of model and prompt integrity,
fine-grained tool authorization, cross-organizational trust, and
accountability for autonomous actions. To address these re-
quirements, we introduced the Agent Trust Infrastructure
(ATI), a framework-independent architecture comprising five
complementary security planes enforced through a reference
monitor operating outside the agent’s language model.
Our experimental eva
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU](http://arxiv.org/abs/2611.23205v1)
**arXiv ID:** `2611.23205v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23205v1) | **Published:** 2026-11-17
**Authors:** Mehmet Altan Toksöz

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 sign...
2. **Key Technical Contributions:** From Abstract: al-processing MATLAB subtasks, using low-rank adaptation (LoRA) and quantized LoRA (QLoRA) on the integrated GPU (iGPU) of a laptop, and deploy the 8-bit integer (int8) models with the adapters through OpenVINO. On held-out variants scored by deterministic checkers, the pass rate rises from 18/66 to
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI, cs.SE, eess.SP. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models](http://arxiv.org/abs/2611.23228v1)
**arXiv ID:** `2611.23228v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23228v1) | **Published:** 2026-11-17
**Authors:** Rui Ning, Om Chabra, Hari Balakrishnan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gate...
2. **Key Technical Contributions:** From Abstract: d DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frames normally requires re-running the entire window through the model. We observe that the recurrent up
3. **Methodology & Architecture:** Categories: cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Learning Grounded Reasoning from Human Gaze](http://arxiv.org/abs/2611.23209v1)
**arXiv ID:** `2611.23209v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23209v1) | **Published:** 2026-11-17
**Authors:** Gabriel Sarch, Declan Campbell, Nicholas Budny, Kia Ghods, Katerina Fragkiadaki et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes nois...
2. **Key Technical Contributions:** From Abstract: e and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be effectively leveraged to improve visual reasoning in VLMs, while maintaining alignment with human behavior. We collect 7,109 human gaze trials from a diverse and challenging set of visual rea
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Higher-Scoring Coding Models Did Not Get More Work Done](http://arxiv.org/abs/2611.23216v1)
**arXiv ID:** `2611.23216v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23216v1) | **Published:** 2026-11-17
**Authors:** Yining Hua

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done. On June 12, 2026, a U.S. export control directive banned access to Claude Fable 5 for 19 days, which forced users to ...
2. **Key Technical Contributions:** From Abstract: switch to other models. During this time, most former Fable 5 users switched to Opus 4.8 (11 points lower on SWE-Bench Pro compared to Fable 5). We treat this suspension as a natural experiment, where the people and projects stayed the same and only the model changed, so we could isolate the effect 
3. **Methodology & Architecture:** Categories: cs.SE, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition](http://arxiv.org/abs/2611.23192v1)
**arXiv ID:** `2611.23192v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23192v1) | **Published:** 2026-11-17
**Authors:** Almog Anschel, Sarah Keren

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous trajectories rely on an e...
2. **Key Technical Contributions:** From Abstract: xplicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous trajectory prefixes where such knowledge is most needed. We present WoRD (Waypoint Recognition with Diffu
3. **Methodology & Architecture:** Categories: cs.AI, cs.LG, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Inference after coding agents](http://arxiv.org/abs/2611.23174v1)
**arXiv ID:** `2611.23174v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.23174v1) | **Published:** 2026-11-17
**Authors:** Florian Gunsilius, David Van Dijcke, Kaspar Wüthrich

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Empirical research is changing rapidly as AI coding agents are becoming increasingly proficient in every step of it, from writing code to manipulating data. We argue that while the potential of coding agents for science is vast, their use in hypothesis testing poses a substantial threat to classical...
2. **Key Technical Contributions:** From Abstract:  inference, as these agents enable a supercharged form of selective inference. In particular, we argue that coding agents carrying out empirical research introduce a new type of post-selection inference that combines human-like, open-ended search over an implicit space of estimators with programmati
3. **Methodology & Architecture:** Categories: stat.ME, cs.AI, econ.EM. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-17. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
