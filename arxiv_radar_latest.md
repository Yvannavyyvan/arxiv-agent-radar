# arXiv AI & Computer Science Research Radar
**Generated:** 2026-10-13 18:44:10 UTC
**Target Categories:** cs.AI, cs.LG, cs.CL, cs.CV, cs.RO, cs.MA, cs.NE, stat.ML, cs.SE, cs.CR, cs.DC, cs.IR
**High-Yield Papers Analyzed:** 10

---

### [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](http://arxiv.org/abs/2610.13889v1)
**arXiv ID:** `2610.13889v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13889v1) | **Published:** 2026-10-09
**Authors:** Weiliang Chen, Song Liao

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics)...
2. **Key Technical Contributions:** From Abstract: , a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This 
3. **Methodology & Architecture:** Categories: cs.AI, cs.IR. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Conclusion
We introduced RATED, a reliability-aware tool retrieval framework
that combines DRAGON encoders fine-tuned with contrastive learn-
ing and contextual bandit re-ranking from execution feedback. On
Table 3: Inference latency at batch size 1 (ms).
Method Avg. Latency P95 LatencyΔOverhead
DRAGON encode only 3.223 4.269 –
ToolRL-like Batch GRPO 17.839 28.921 +14.616
RATED (w/o Feedback) 3.248 4.274 +0.025
RATED (w/ Global MAB) 3.331 4.351 +0.108
RATED (Full) 3.395 4.391 +0.172
EcoAgent, RATED achieves strong in-domain retrieval and remains
competitive on real-world queries. Under injected tool failures,
it reduces fault selection to 2.5–2.9% FSR,7 .3× lower than static
DRAGON, with only 0.172 ms added latency over encode-only in-
fere
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](http://arxiv.org/abs/2610.13947v1)
**arXiv ID:** `2610.13947v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13947v1) | **Published:** 2026-10-09
**Authors:** Xudong Cai, Ruijie Zhu, Haoliang Shang, Ruining Li, Marc Pollefeys et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articr...
2. **Key Technical Contributions:** From Abstract: aft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-free motion, stability under gravity, and accurate mass and material properties. Furthermore, we constr
3. **Methodology & Architecture:** Categories: cs.CV. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation](http://arxiv.org/abs/2610.13862v1)
**arXiv ID:** `2610.13862v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13862v1) | **Published:** 2026-10-09
**Authors:** Fabio Hübel, Adam Lilja, Yue Yin, Siming He, Claire Tomlin et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Deploying language-model agents onboard mobile robots requires task reasoning and responsive execution within limited compute and memory. We propose BT-Agent, an onboard architecture combining LLM-driven task decisions with predefined behavior-tree (BT) skills. These skills enforce execution conditi...
2. **Key Technical Contributions:** From Abstract: ons and return structured failure feedback. We demonstrate fully onboard operation with a 9B model on a quadruped across five task categories. Intervention tests show that local checks stop ongoing navigation without waiting for another model decision, while the agent remains active to retry or repo
3. **Methodology & Architecture:** Categories: cs.RO. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** CONCLUSION
Onboard trials demonstrate BT-Agent’s combination of
task reasoning and reactive execution: the agent coordinates
multi-step tasks, while local BT checks enforce execution
conditions and interrupt motion without waiting for another
model decision. Smaller models benefit most from harness
support, while useful components depend on the task and
inference cost. Text enables inexpensive development, and
simulator trials expose skill and decision failures.
A. Limitations and Future Work
The Actor can sequence and parameterize available skills,
but their implementations and guards stay fixed at runtime.
This supports review and testing before deployment, but new
capabilities require skill authoring and platform-specific in-
tegration. 
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](http://arxiv.org/abs/2610.13886v1)
**arXiv ID:** `2610.13886v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13886v1) | **Published:** 2026-10-09
**Authors:** Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional fai...
2. **Key Technical Contributions:** From Abstract: lures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions or decompose harmful objectives specified by humans or LLMs into seemingly benign action combination
3. **Methodology & Architecture:** Categories: cs.AI. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness](http://arxiv.org/abs/2610.13918v1)
**arXiv ID:** `2610.13918v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13918v1) | **Published:** 2026-10-09
**Authors:** Daniel Szelogowski

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale bi...
2. **Key Technical Contributions:** From Abstract: ophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothalamic leaky integrate-and-fire spiking neural network. We formalize five clinical cohorts across an id
3. **Methodology & Architecture:** Categories: cs.NE, cs.ET, cs.LG, q-bio.NC. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems](http://arxiv.org/abs/2610.13870v1)
**arXiv ID:** `2610.13870v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13870v1) | **Published:** 2026-10-09
**Authors:** Pascal Sowietzki, Steffen Holter, Yannick Metz, Emil Kasper, Raphael Baur et al.

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** To balance task performance and computational cost, agentic workflows can use a lower-cost model for execution and selectively consult a stronger model. In such executor-advisor systems, the executor decides when to seek advice, making escalation depend on self-assessment, although current language ...
2. **Key Technical Contributions:** From Abstract: models struggle to detect where their own reasoning fails. The need for stronger reasoning emerges during execution and varies across workflow phases. We introduce ARIA, a meta-controller that learns when to consult by balancing task success against consultation cost. Our approach formulates consult
3. **Methodology & Architecture:** Categories: cs.MA. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Constructive Bounds for the Topological Expressivity of Neural Networks](http://arxiv.org/abs/2610.13931v1)
**arXiv ID:** `2610.13931v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13931v1) | **Published:** 2026-10-09
**Authors:** Kosio Beshkov

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** The expressivity of a neural network $Φ$ describes the class of functions that a network can express. The term topological expressivity refers to a family of measures particularly suited to understand binary classification and is often formulated in terms of the Betti numbers of a decision boundary ...
2. **Key Technical Contributions:** Our contributions
The previously mentioned studies of the topology of neural
representations are empirical or methodological in nature
and do not explicitly relate their results to any notion of
expressivity of a network. In this paper we provide, what
is to our knowledge, the first architectural bounds on the
topology of the representations of ReLU neural networks.
We attempt to classify networks by the Betti numbers that
they can generate given that the data comes from some
contractible compact set in Rd. Instead of evaluating the
Betti numbers for a network with a given architecture, we
approach the problem in reverse and provide upper bounds
on the size of the architecture that can generate particular
Betti numbers.
We construct a set o
3. **Methodology & Architecture:** Categories: math.AT, cs.LG. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Structural Automata for Neural Semantic Parsing](http://arxiv.org/abs/2610.13896v1)
**arXiv ID:** `2610.13896v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13896v1) | **Published:** 2026-10-09
**Authors:** Xiao Zhang

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Neural semantic parsers generate meaning representations token by token, yet well-formedness depends on references, scope, and graph relations that unfold during generation. Constrained decoding prevents locally invalid tokens but does not guarantee that a valid prefix can be completed within a fixe...
2. **Key Technical Contributions:** From Abstract: d output-length limit. We investigate structural automata at three stages of DRS parsing (decoding, post hoc processing, and training) and additionally evaluate decoding on AMR. For decoding, we introduce accepting-path decoding (APD), which maintains a verified completion within the remaining lengt
3. **Methodology & Architecture:** Categories: cs.CL. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [Can Language Models Play the Wikipedia Game?](http://arxiv.org/abs/2610.13948v1)
**arXiv ID:** `2610.13948v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13948v1) | **Published:** 2026-10-09
**Authors:** Alexander Hickey, Joanna Knight, James Bishop

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. I...
2. **Key Technical Contributions:** From Abstract: n the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We construct very large local graphs of Wikipedia pages and of paper citations using OpenAlex and provide co
3. **Methodology & Architecture:** Categories: cs.AI, cs.IR. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---

### [AI Models Can Provably Hide Arbitrary Capabilities](http://arxiv.org/abs/2610.13928v1)
**arXiv ID:** `2610.13928v1` | **PDF:** [View PDF](https://arxiv.org/pdf/2610.13928v1) | **Published:** 2026-10-09
**Authors:** Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt

#### 5-Point Executive Dossier:
1. **Core Problem & Thesis:** Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural...
2. **Key Technical Contributions:** Contributions
• We propose a novel class of attacks that hide arbitrary computations within model weights
with cryptographic guarantees under the stated assumptions.
• We provide implementations of our proof-of-concept constructions as model organisms
in PyTorch, along with a framework for embedding arbitrary algorithms as differentiable
circuits in modern architectures. This framework may serve as infrastructure for future
interpretability and red-teaming research.
• We empirically evaluate elicitation methods on our models. We also demonstrate how to
differentiate genuine elicitation from overelicitation using circuits that are theoretically hard
to learn via gradient descent.
3. **Methodology & Architecture:** Categories: cs.LG, cs.CR. Focused on AI architecture, computational models, and algorithmic implementation.
4. **Key Results & Findings:** Published on 2026-10-09. Detailed empirical evaluation provided in full manuscript.
5. **Limitations & Radar Notes:** Assessed against specific benchmark environments; real-world scalability and safety guarantees require ongoing evaluation.

---
