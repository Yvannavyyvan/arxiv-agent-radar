# arXiv AI & Computer Science Research Radar
**Generated:** 2026-11-16 21:29:09 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [Imitation Bootstrapped Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2611.18543v1)
**arXiv ID:** `2611.18543v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18543v1) | **Published:** 2026-11-13
**Authors:** Tony H. Zhang, Connor Mattson, Daniel S. Brown

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Demonstrations are an effective way to accelerate single-agent reinforcement learning (RL), but extending this idea to multi-agent reinforcement learning (MARL) is non-trivial as it is difficult and often impossible for a single person to teleoperate multiple agents simultaneously. Round-Robin Behav...
2. **Key Technical Contributions:** From Abstract: ior Cloning (R2BC) addresses this by letting a single demonstrator control one agent at a time while the others execute their current policies. However, the resulting imitation policies are limited by the quality of the demonstrations. We propose Imitation Bootstrapped Multi-Agent Reinforcement Lear
3. **Methodology & Architecture:** Categories: cs.AI, cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** limitations
that we believe could lead to exciting avenues for future work.
First, all results are in simulation, and the human study uses a
single demonstrator on a single task. Future work should evaluate
IBMARL on real robots and with several demonstrators of varying
skill. Second, we assume the team reward is known. While this is a
standard assumption in MARL, we note that a reward learned from
human preferences [8] could easily replace the ground-truth reward
without changing our method. Importantly, this could let a single
8
person supply both the demonstrations and the reward. Third, the
IL policy is frozen once RL begins. In the future, the demonstrator
could keep teaching during RL and leverage the learned critics to
find where the
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination](http://arxiv.org/abs/2611.18514v1)
**arXiv ID:** `2611.18514v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18514v1) | **Published:** 2026-11-13
**Authors:** Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Mechanistic Interpretability (MI) has made significant progress in explaining the internal computations of Large Language Models (LLMs); however, these advances have yet to demonstrate comparable success in explaining the decision-making processes of LLM-based agents. This paper examines the challen...
2. **Key Technical Contributions:** From Abstract: ges MI tools face when applied to realistic agentic failures. We focus on one such failure: web agents hallucinating actions that are not available on a website. We apply a series of mechanistic analyzes to Qwen2.5-7B-Instruct as it interacts with live websites. We find that a linear probe trained o
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents](http://arxiv.org/abs/2611.18493v1)
**arXiv ID:** `2611.18493v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18493v1) | **Published:** 2026-11-13
**Authors:** Sandip Nandi, Aishwarya Bose, Apurba Bose, Soovadeep Bakshi

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Autonomous trading agents need controls that prevent problematic orders without making legitimate tasks impractical. We study this aspect of agentic compliance with TradeGauntlet, a replayable limit-order-book simulator that separates detection, prevention, and execution cost. In 1,680 simulated ses...
2. **Key Technical Contributions:** From Abstract: sions with Claude Haiku 5.5 and Sonnet 5.5, all conduct alerts were self-matches. Gates eliminated those alerts by rejecting self-crossing orders, while the aggregate-gate condition reduced Sonnet's two-sided fills by about 15%. A conduct reminder reduced Sonnet's alert rate but reduced Haiku's fill
3. **Methodology & Architecture:** Categories: cs.MA, cs.AI, cs.CE. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Training Reasoning Models in Simulation to Natively Use Real Robots](http://arxiv.org/abs/2611.18562v1)
**arXiv ID:** `2611.18562v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18562v1) | **Published:** 2026-11-13
**Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that...
2. **Key Technical Contributions:** From Abstract:  an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the model observes the environment, reasons in a chain of thought, and generates the next end-effector po
3. **Methodology & Architecture:** Categories: cs.RO, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL](http://arxiv.org/abs/2611.18533v1)
**arXiv ID:** `2611.18533v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18533v1) | **Published:** 2026-11-13
**Authors:** Zelin He, Siyu Zhu, Jacob Helwig, Yujian Liu, Li An et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agentic reinforcement learning (RL) increasingly relies on a harness, the scaffold around the model that decides what it sees of its own interaction and what guidance it receives. Most existing approaches train under a hand-written harness that stays fixed throughout. However, an effective harness d...
2. **Key Technical Contributions:** From Abstract: epends on the domain, the data and the model, and keeps changing as the model trains. We introduce ModHarness-RL, which recasts the harness as programs that are learned from data and evolve as the model trains with RL. ModHarness-RL records the interaction as structured State, a set of typed blocks,
3. **Methodology & Architecture:** Categories: cs.AI, cs.CL, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models](http://arxiv.org/abs/2611.18494v1)
**arXiv ID:** `2611.18494v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18494v1) | **Published:** 2026-11-13
**Authors:** Dhruv Dixit, Khushi Patel, Congcong Xu, Min Song

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Small language models are attractive for local, low-cost, and privacy-sensitive deployment, but they remain unreliable on mathematical reasoning tasks that require decomposition, exact computation, tool use, and verification. We introduce \textbf{ARCHER}: \textbf{A}ction-trace \textbf{R}einforcement...
2. **Key Technical Contributions:** From Abstract:  for \textbf{C}alculator-grounded \textbf{H}ierarchical \textbf{E}xecutable \textbf{R}easoning, a two-stage framework for training small language models (SLMs) to produce executable and auditable reasoning trajectories. In the first stage, ARCHER compiles free-form chain-of-thought rationales into t
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [WeightBench: Evaluating Language Models as Weight-Space Programmers](http://arxiv.org/abs/2611.18553v1)
**arXiv ID:** `2611.18553v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18553v1) | **Published:** 2026-11-13
**Authors:** Aayush Marasini, Barsat Khadka, Nick Rahimi

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Recent work shows that large language models (LLMs) can operate directly on the parameters of other neural networks. They can read what a network was trained to do, fix a network that fails, and write working networks from scratch, all without gradient descent. This capability has been termed Weight...
2. **Key Technical Contributions:** From Abstract: -Space Programming (WSP). Exploring this new paradigm systematically requires a robust benchmark. We introduce WEIGHTBENCH, a benchmark that evaluates LLMs of increasing capability on 42 WSP tasks across five tracks: reading, fixing and writing weights, recognizing edits that are impossible, and dat
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval](http://arxiv.org/abs/2611.18516v1)
**arXiv ID:** `2611.18516v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18516v1) | **Published:** 2026-11-13
**Authors:** Dayoon Ko, Yichuan Wang, Soyeong Jeong, Joseph E. Gonzalez, Gunhee Kim et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Screen history can serve as searchable visual memory for people and agents, but unlike an offline corpus, it must be encoded and indexed as each screenshot arrives. OCR-based indexing is fast but loses visual information; visual encoding takes over two seconds. Yet screens change incrementally: most...
2. **Key Technical Contributions:** From Abstract:  pixels repeat within and across screenshots. This raises a question: do visual encoders need to recompute their representations from scratch for every new screenshot? We present StreamEmbed, a system for incremental visual embedding that exploits this redundancy. Guided solely by pixel differences,
3. **Methodology & Architecture:** Categories: cs.CV, cs.IR, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Agentic induction of common data elements and information extraction from sarcoma case report abstracts](http://arxiv.org/abs/2611.18506v1)
**arXiv ID:** `2611.18506v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18506v1) | **Published:** 2026-11-13
**Authors:** Daniel Reichenpfader, Kwaku Appiagyei, Manovah Nadarajah, Ahmed Reda Bahr, Irina Filchenko et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Common data elements (CDEs) support clinical data comparability but are usually defined manually. We investigated whether large language model agents could derive a CDE schema from sarcoma case report abstracts and apply it at scale. An agent proposed 72,909 candidate CDEs from 24,588 PubMed abstrac...
2. **Key Technical Contributions:** From Abstract: ts; agentic consolidation yielded 1,570 CDEs. We retained 53 supported by at least 50 abstracts and attempted evidence-linked extraction across the corpus. Processing succeeded for all retained CDEs in 79.2% of abstracts, including responses indicating non-mention. Two human reviewers approved 83.0%
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Disturbance-Aware Informative Planning in Spatiotemporal Environments](http://arxiv.org/abs/2611.18505v1)
**arXiv ID:** `2611.18505v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2611.18505v1) | **Published:** 2026-11-13
**Authors:** Kaleb Ben Naveed, Haejoon Lee, Anouck Girard, Dimitra Panagou

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Autonomous robots are widely used for persistent monitoring of spatiotemporal environments, where quantities of interest (QoI) change across space and time and require repeated measurements. In practice, robot motion can be affected by external disturbances that vary across the environment. When suc...
2. **Key Technical Contributions:** From Abstract: h external disturbances are not considered in trajectory optimization, it can lead to inaccurate predictions of robot motion and, consequently, the information acquired about the QoI during execution. However, estimating disturbances throughout the environment can be inefficient, as disturbances in 
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-11-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
