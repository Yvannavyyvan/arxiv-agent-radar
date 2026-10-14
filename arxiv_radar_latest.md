# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-14 16:17:16 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [ChunkAct: Action Chunking for Agentic Robotics](http://arxiv.org/abs/2610.18874v1)
**arXiv ID:** `2610.18874v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18874v1) | **Published:** 2026-10-13
**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficie...
2. **Key Technical Contributions:** From Abstract: ncy. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present Chunk
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.CL, cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Hybrid Reasoning Agents](http://arxiv.org/abs/2610.18861v1)
**arXiv ID:** `2610.18861v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18861v1) | **Published:** 2026-10-13
**Authors:** Jiaru Zou, Yunzhe Qi, Sirui Chen, Federico Bianchi, Shang Zhu et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge ...
2. **Key Technical Contributions:** From Abstract: these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the ag
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](http://arxiv.org/abs/2610.18868v1)
**arXiv ID:** `2610.18868v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18868v1) | **Published:** 2026-10-13
**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, Nanyun Peng, Kai-Wei Chang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely fo...
2. **Key Technical Contributions:** From Abstract: r lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce Tev-Gym, the first long-horizon agent training dataset with verifiable, dense, progressive rewards -
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.CV, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](http://arxiv.org/abs/2610.18862v1)
**arXiv ID:** `2610.18862v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18862v1) | **Published:** 2026-10-13
**Authors:** Minghao Luo, Liang Chen

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heurist...
2. **Key Technical Contributions:** From Abstract: ics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a training-free decoding method in which a much smaller reasoning model steers the large one towards brevity. The small model reads the large model's CoT so far twice, once prompted to be brief 
3. **Methodology & Architecture:** Categories: cs.CL, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs](http://arxiv.org/abs/2610.18858v1)
**arXiv ID:** `2610.18858v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18858v1) | **Published:** 2026-10-13
**Authors:** Aimon Rahman, Joymallya Chakraborty, Vidit Bansal, Abhishek Dan

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Multimodal large language models have advanced rapidly, but most remain optimized for single-image inputs. Multi-image reasoning is costly because each image adds many visual tokens, increasing encoding and attention demands. Existing techniques that address the above issue, including visual token p...
2. **Key Technical Contributions:** From Abstract: runing, token merging, visual token compression, learned resampling, hierarchical compression, retrieval-augmented visual reasoning, and memory-based architectures, have largely been designed for single-image scenarios, where redundancy is primarily spatial and local. Multi-image reasoning introduce
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](http://arxiv.org/abs/2610.18869v1)
**arXiv ID:** `2610.18869v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18869v1) | **Published:** 2026-10-13
**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and...
2. **Key Technical Contributions:** From Abstract:  24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain b
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
In the evaluated configurations, approach-aware episode
conditioning improves mean success over plain BC, and
constant-tag FT improves mean success after conditioned
pretraining under both tested inference protocols. Condition-
ing favors episode labels and filtering favors chunk labels on
average, with model-dependent reversals. The study covers a
shared tabletop simulation setting, with real-world validation
using one VLA in a reference workspace. Testing larger pre-
training budgets and additional workspaces and embodiments
would clarify how broadly the findings transfer. Initialization
and trainable modules vary across VLAs, so the comparisons
do not isolate the causes of their different method rankings.
Matched controls coul
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence](http://arxiv.org/abs/2610.18867v1)
**arXiv ID:** `2610.18867v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18867v1) | **Published:** 2026-10-13
**Authors:** Wenyi Li, Yizhe Chi, Youjie Zheng, Chunyu Liu, Xiaoqiu Wang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Bringing general-purpose agents into the physical world calls for an executable representation of physical intelligence. Compared with vision-language-action (VLA) models, which map observations and language instructions directly to actions, code makes control logic explicit and reusable. Code can s...
2. **Key Technical Contributions:** From Abstract: erve not only as a policy representation but also as the workspace in which the agent solves a task. Rather than following a prescribed workflow of planning, execution, and verification, the agent can autonomously inspect the state, revise and execute code, and use feedback to choose the next step. 
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AutoAgent0: An Agentic Runtime for Safe Closed-Loop Driving](http://arxiv.org/abs/2610.18866v1)
**arXiv ID:** `2610.18866v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18866v1) | **Published:** 2026-10-13
**Authors:** Jiageng Liu, Seth Z. Zhao, Zewei Zhou, Alejandro Huerta, Aidan Bayer-Calvert et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Safe autonomous driving requires more than accurate planning at a single frame: it demands reliable closed-loop execution in dynamic environments. Although end-to-end driving policies have advanced rapidly, the accumulated closed-loop errors, especially in unseen scenarios, can push vehicles into st...
2. **Key Technical Contributions:** From Abstract: ates from which the same policy struggles to recover. We address the challenge by treating closed-loop driving safety as a test-time execution problem. We introduce AutoAgent0, an agentic runtime and harness framework that augments existing driving experts with complementary detection skills, rule-b
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards](http://arxiv.org/abs/2610.18853v1)
**arXiv ID:** `2610.18853v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18853v1) | **Published:** 2026-10-13
**Authors:** Yuante Li, Junwei Quan, Kai Qiu, Kate Zhang, Yicheng Tao

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in pract...
2. **Key Technical Contributions:** contributions
from tokens whose ratios move beyond the clipping
range.
In our multi-step GRPO experiments, three phe-
nomena appear together under the square-root rule:
➀ Progress slows with batch size.Larger rollout
batches learn more slowly per sample. ➁ Failure
keeps time in samples.Without the clip, larger
batches collapse after the same number of sam-
ples as smaller ones, despite taking far fewer op-
timizer steps. ➂ Clipping helps larger batches
most.Although clipping is often viewed as a bot-
tleneck on learning (Qi et al., 2026; Yang et al.,
2026a), its stabilizing effect is strongest for the
larger batches. Figure 1 visualizes this split into
two clocks: progress becomes increasingly sample-
inefficient with larger rollout batches
3. **Methodology & Architecture:** Categories: cs.LG, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](http://arxiv.org/abs/2610.18843v1)
**arXiv ID:** `2610.18843v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.18843v1) | **Published:** 2026-10-13
**Authors:** Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the rob...
2. **Key Technical Contributions:** From Abstract: ot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height, and gripper pads. Each axis has five severity lev
3. **Methodology & Architecture:** Categories: cs.RO, cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-13. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
