# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-06 06:26:32 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](http://arxiv.org/abs/2610.06830v1)
**arXiv ID:** `2610.06830v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06830v1) | **Published:** 2026-10-05
**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essentia...
2. **Key Technical Contributions:** From Abstract: l. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performance, cost, and latency largely underexplored. To address this challenge, we present \textbf{MemPilot
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Recursive Video In-Context Learning for Agentic Robot](http://arxiv.org/abs/2610.06843v1)
**arXiv ID:** `2610.06843v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06843v1) | **Published:** 2026-10-05
**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, Yuzhang Shang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration video shows it, but fits poorly into an agent's context. The full video slows every turn, fixed keyfram...
2. **Key Technical Contributions:** contributions:
• We introducevideo in-context learningto tool-
using robot agents: their text memory cannot
record what a successful execution looks like,
but a demonstration video shows it frame by
frame (§3.1).
• We propose Recursive Video In-Context
Learning (RV-ICL), which lets the agent look
only at the part of the demonstration its cur-
rent step needs, by giving itrecursive access
to a hierarchy built from the demonstration’s
sub-events (§3).
• On LIBERO-PRO,RV-ICLraises the success
rate of HarnessVLA from 92.6% to 96.5%,
above every baseline, and on LIBERO-Plus
from 86.7% to 95.8% across seven kinds of
perturbation. On the long LIBERO-10 tasks it
gains up to 12 points, where keyframes or the
whole video of the same demonstration gai
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CL, cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling](http://arxiv.org/abs/2610.06829v1)
**arXiv ID:** `2610.06829v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06829v1) | **Published:** 2026-10-05
**Authors:** Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and ...
2. **Key Technical Contributions:** From Abstract: cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language verification questions about its own rollouts; a Compositional Conformal Certifier keeps only question 
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Learning to Read the Contextual Tokens in Diffusion Transformers](http://arxiv.org/abs/2610.06844v1)
**arXiv ID:** `2610.06844v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06844v1) | **Published:** 2026-10-05
**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, Daniel Cohen-Or, Or Patashnik

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a fra...
2. **Key Technical Contributions:** From Abstract: mework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Large Language Model (LLM), allowing the LLM to answer questions about the emerging image directly from
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI, cs.GR, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification](http://arxiv.org/abs/2610.06790v1)
**arXiv ID:** `2610.06790v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06790v1) | **Published:** 2026-10-05
**Authors:** Je Yang, Ivan Lobov, Thomas Karpati

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual. Although Large Language Models (LLMs) have made rapid inroads into Electronic Design Automation (E...
2. **Key Technical Contributions:** From Abstract: DA), approximately 74.6% of existing studies target static Register-Transfer Level (RTL) code generation, leaving post-simulation verification and interactive waveform debugging largely untouched. We introduce Back-to-the-Future (BTTF), an end-to-end agentic framework that closes this infrastructura
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search](http://arxiv.org/abs/2610.06782v1)
**arXiv ID:** `2610.06782v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06782v1) | **Published:** 2026-10-05
**Authors:** Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev, Danil Taranets, Dmitrii Stoianov et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so b...
2. **Key Technical Contributions:** From Abstract: ackend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning followed by GSPO on a recall reward. Averaged over seven English and Russian benchmarks with gold evidenc
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline](http://arxiv.org/abs/2610.06852v1)
**arXiv ID:** `2610.06852v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06852v1) | **Published:** 2026-10-05
**Authors:** Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang, Hsi-An Chen, Chun-Wei Tuan Mu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different aspect ratio on the same computational graph, where any silently broken connection misrepresents the...
2. **Key Technical Contributions:** From Abstract:  method. We formulate aspect-ratio-adaptive flowchart relayout as a distinct task: given a raster flowchart and a target ratio, produce a structurally faithful, hallucination-free, editable layout. Existing methods fail characteristically: image-to-image models stretch blocks and reject extreme rati
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](http://arxiv.org/abs/2610.06805v1)
**arXiv ID:** `2610.06805v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06805v1) | **Published:** 2026-10-05
**Authors:** Wancong Zhang, Basile Terver, Michael Rabbat, Yann LeCun, Randall Balestriero

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training ...
2. **Key Technical Contributions:** our contributions:
1. We introduce an end-to-end training method for hierarchical JEPA world models (§2).
2. We show that when factors in the data evolve at separated timescales, higher levels discard
fast detail they cannot predict over their horizons and retain slower, predictable state (§3).
3. We show that H-JEPA’s hierarchical planning outperforms single-level planning at a fraction
of the test-time compute (§4.1). We identify two complementary mechanisms: hierarchical
latent spaces let higher-level planners score progress at the goal’s own level of abstraction,
while temporal decomposition breaks long-horizon tasks into easier subproblems (§4.2).
4. With an inverse-dynamics term, the method extends to DROID, a real-robot manipulation

3. **Methodology & Architecture:** Categories: cs.LG, cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Deep Learning for Sleep Heart Rate Estimation from Accelerometers: Toward Population-Scale Cardiac Insight Without Optical Sensors](http://arxiv.org/abs/2610.06823v1)
**arXiv ID:** `2610.06823v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06823v1) | **Published:** 2026-10-05
**Authors:** Tanbin Islam Rohan, Pranjol Sen Gupta, Tanusree Debi, Nazmus Sakib

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We present SeqSmoother, a transformer-based temporal corrector for sleep heart rate (HR) estimation from wri...
2. **Key Technical Contributions:** From Abstract: st accelerometry. SeqSmoother combines spectral descriptors with an intermediate Nightbeat-derived frequency anchor and a physics-motivated sub-harmonic feature designed to identify harmonic frequency lock-on. All inference-time features are derived from wrist accelerometry, while ECG is used only t
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** FUTURE WORK 
First, formal model -performance inference uses the first 13 
completed folds of a pre -generated frozen participant order, 
not all 38 usable recordings. No test participant was added, 
removed, replaced, or selected based on held-out performance, 
and the scientific configuration remained fixed during evidence 
accumulation. The all-38-recording pass verifies preprocessing 
applicability only and is not treated as 38-fold model evidence. 
External replication and broader participant -level testing re -
main desirable. 
Second, the official Nightbeat comparison uses the official 
algorithm under the unified 60-s/15-s protocol rather than 
reproducing every detail behind the published 0.88 bpm result. 
Third, 93.68% of SeqSmoot
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](http://arxiv.org/abs/2610.06801v1)
**arXiv ID:** `2610.06801v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.06801v1) | **Published:** 2026-10-05
**Authors:** Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang, Ye Huang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle ...
2. **Key Technical Contributions:** From Abstract: comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided by this analysis, we propose Meta-Cached Sparse Attention (MC-Sparse), a training-free framework th
3. **Methodology & Architecture:** Categories: cs.CV, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-05. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
