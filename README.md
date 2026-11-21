# Awesome AI Harness

An agent harness is the software around a language model that turns it into an agent: the loop that calls the model, the tools it acts through, the context it sees, where its actions run, what it remembers, and the checks, permissions and orchestration around it.
This list is generated from the verified reference database of the survey *Agent Harnesses: Architecture, Measured Effects, and Design Trade-offs* (forthcoming on arXiv).
It holds 892 papers and resources the survey cites or codes as core harness work, and 421 open-source repositories checked against the GitHub API.

Entries are kept in [`data/`](data/) and the README is rebuilt by `python3 scripts/build_readme.py`; see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [The nine-part anatomy](#the-nine-part-anatomy)
- [Papers](#papers)
  - [Surveys and anatomies](#surveys-and-anatomies)
  - [By anatomy part](#by-anatomy-part)
  - [By use case](#by-use-case)
- [Harness repositories](#harness-repositories)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Security](#security)
- [Courses and learning](#courses-and-learning)

## The nine-part anatomy

| Part | What it does | Papers |
|---|---|---:|
| [Control loop](#control-loop) | Runs the turn cycle: call the model, dispatch actions, decide when to stop. | 81 |
| [Context manager](#context-manager) | Builds what the model sees each turn: prompts, instruction files, retrieval, compaction. | 78 |
| [Action interface](#action-interface) | Tools and protocols through which the model acts: function calls, code, GUI, MCP. | 81 |
| [Execution environment](#execution-environment) | Where actions run: sandbox, container, VM, filesystem, network policy. | 29 |
| [State and memory](#state-and-memory) | What persists outside the context window: transcripts, checkpoints, memory, skills. | 96 |
| [Verification and feedback](#verification-and-feedback) | Checks fed back into the loop: tests, critics, self-review, evaluators. | 43 |
| [Governance](#governance) | Who may do what: permissions, approvals, guardrails, human oversight, audit. | 13 |
| [Orchestration](#orchestration) | More than one loop: subagents, teams, workflows, agent-to-agent protocols. | 60 |
| [Observability and extension](#observability-and-extension) | Telemetry, traces, the human interface, hooks and plugins. | 17 |

## Papers

### Surveys and anatomies

- [A Comprehensive Survey of Agent Distillation across Models, Artifacts, and Harnesses](https://arxiv.org/abs/2609.36630) - Ziluowen Luo et al. (2026). arXiv:2609.36630
- [A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2605.07358) - Yingli Zhou et al. (2026). arXiv:2605.07358
- [A Systematic Survey of Agentic Skills: Architecture, Lifecycle, and Security](https://arxiv.org/abs/2608.29596) - Sanket Badhe et al. (2026). arXiv:2608.29596
- [A Technical Taxonomy of LLM Agent Communication Protocols](https://arxiv.org/abs/2606.19135) - Linus Sander et al. (2026). arXiv:2606.19135
- [A Theory of Reliable Self-Evolution for Agent Harnesses](https://arxiv.org/abs/2609.08175) - Qianshu Cai et al. (2026). arXiv:2609.08175
- [Agent Harness Engineering: A Survey](https://openreview.net/forum?id=3hXEPbG0dh) - Junjie Li et al. (2026).
- [Agent Harness for Large Language Model Agents: A Survey](https://doi.org/10.20944/preprints202604.0428.v3) - Qianyu Meng et al. (2026). doi:10.20944/preprints202604.0428.v3
- [Agentic Societies Need a Social Harness](https://arxiv.org/abs/2609.17527) - Tapan Chugh et al. (2026). arXiv:2609.17527
- [AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents](https://arxiv.org/abs/2605.13357) - Hailin Zhong, Shengxin Zhu (2026). arXiv:2605.13357
- [AI Harness: Certification under Proposal-Conditioned Information for Foundation-Model Agents](https://arxiv.org/abs/2609.32184) - Hailin Zhong, Shengxin Zhu (2026). arXiv:2609.32184
- [Anatomy of an Agent Harness: Decisions, Invariants and Corner Cases](https://arxiv.org/abs/2611.19960) - Resham Joshi (2026). arXiv:2611.19960
- [Audit the Scaffold, Not the Checkpoint: A Stationarity Dichotomy for Recursive Self-Improvement in Agentic Coding](https://arxiv.org/abs/2609.34924) - Sebastian Bobadilla-Suarez, Bob Suh, Ryan Fortin (2026). arXiv:2609.34924
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](https://arxiv.org/abs/2608.05179) - Tianyu Ding et al. (2026). arXiv:2608.05179
- [Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration - A Single-Operator Case Study](https://arxiv.org/abs/2611.06946) - Lei Hua (2026). arXiv:2611.06946
- [Code as Agent Harness](https://arxiv.org/abs/2605.18747) - Xuying Ning et al. (2026). arXiv:2605.18747
- [Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance](https://arxiv.org/abs/2610.16015) - Quanyan Zhu (2026). arXiv:2610.16015
- [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/abs/2607.25408) - Debjyoti Paul (2026). arXiv:2607.25408
- [Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries](https://arxiv.org/abs/2607.10113) - Yubo Li (2026). arXiv:2607.10113
- [Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](https://arxiv.org/abs/2609.02309) - Bizhe Bai et al. (2026). arXiv:2609.02309
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224) - Chenyu Zhou et al. (2026). arXiv:2604.08224
- [From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents](https://arxiv.org/abs/2606.04990) - Yiqi Wang et al. (2026). arXiv:2606.04990
- [From Capability to Assurance in Autonomous Penetration-Testing Harnesses: A Framework and Reference Implementation](https://arxiv.org/abs/2609.22664) - Joas Antonio dos Santos Barbosa (2026). arXiv:2609.22664
- [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](https://arxiv.org/abs/2605.26112) - Shangding Gu (2026). arXiv:2605.26112
- [From Prompt to Harness: Coderlet from Scratch](https://arxiv.org/abs/2608.09480) - Mengfan Li (2026). arXiv:2608.09480
- [From Question Answering to Task Completion: A Survey on Agent System and Harness Design](https://arxiv.org/abs/2606.20683) - Jianyuan Guo et al. (2026). arXiv:2606.20683
- [From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents](https://arxiv.org/abs/2603.22386) - Ling Yue et al. (2026). arXiv:2603.22386
- [Harness Engineering as Categorical Architecture](https://arxiv.org/abs/2605.12239) - Bogdan Banu (2026). arXiv:2605.12239
- [Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime](https://doi.org/10.20944/preprints202603.1756.v2) - Chaoyue He et al. (2026). doi:10.20944/preprints202603.1756.v2
- [Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer](https://arxiv.org/abs/2606.09416) - Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park (2026). arXiv:2606.09416
- [Harnesses for Inference-Time Alignment over Execution Trajectories](https://arxiv.org/abs/2605.21516) - Boyuan Wang et al. (2026). arXiv:2605.21516
- [Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](https://arxiv.org/abs/2611.22299) - Deep Shah, Nehal Kathrotia (2026). arXiv:2611.22299
- [Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515) - Benjamin Rombaut (2026). arXiv:2604.03515
- [LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns](https://doi.org/10.3390/fi18060326) - Yiwen Zhu et al. (2026). doi:10.3390/fi18060326
- [Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures](https://arxiv.org/abs/2607.28802) - Harsh Raj et al. (2026). arXiv:2607.28802
- [Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings](https://arxiv.org/abs/2607.13918) - Jiangang Han (2026). arXiv:2607.13918
- [Reconfigurable Action Theories: A Formal Foundation for Dynamically Composable Agent Harnesses](https://arxiv.org/abs/2611.12300) - Jianmin Ji (2026). arXiv:2611.12300
- [SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills](https://arxiv.org/abs/2611.23990) - Nami Cho, Shailja Gupta (2026). arXiv:2611.23990
- [Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813) - Chuyang Wei et al. (2026). arXiv:2610.18813
- [SOK: A Taxonomy of Attack Vectors and Defense Strategies for Agentic Supply Chain Runtime](https://arxiv.org/abs/2602.19555) - Xiaochong Jiang et al. (2026). arXiv:2602.19555
- [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) - Yunbei Zhang et al. (2026). arXiv:2605.23950
- [Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines](https://arxiv.org/abs/2606.24598) - Yimo Lin, Zhen Zhang, Yibin Li (2026). arXiv:2606.24598
- [Towards Agentic Robots: Model, Data, Environment, and Harness](https://arxiv.org/abs/2610.20442) - Chonghan Qin et al. (2026). arXiv:2610.20442
- [Towards Portable Specification of the Agent Harness](https://arxiv.org/abs/2610.40917) - Nicolas Gertler, Claudio Novelli, Luciano Floridi (2026). arXiv:2610.40917
- [Towards Reliable AI Data Scientists: Data Agents with Workflow Harnesses](https://arxiv.org/abs/2609.35255) - Huachi Zhou et al. (2026). arXiv:2609.35255
- [Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191) - Liaoyuan Fan et al. (2026). arXiv:2610.40191
- [What makes a harness a harness: necessary and sufficient conditions for an agent harness](https://arxiv.org/abs/2606.10106) - Sanderson Oliveira de Macedo (2026). arXiv:2606.10106
- [Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255) - Jian Mu, Ruibo Shen, Yao Shu (2026). arXiv:2610.37255
- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407) - Jinyuan Fang et al. (2025). arXiv:2508.07407
- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) - Lingrui Mei et al. (2025). arXiv:2507.13334
- [A Survey of Data Agents: Emerging Paradigm or Overstated Hype?](https://arxiv.org/abs/2510.23587) - Yizhang Zhu et al. (2025). arXiv:2510.23587
- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) - Huan-ang Gao et al. (2025). arXiv:2507.21046
- [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) - Apostol Vassilev et al. (2025).
- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) - Asaf Yehudai et al. (2025). arXiv:2503.16416
- [AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways](https://arxiv.org/abs/2406.02630) - Zehang Deng et al. (2024). arXiv:2406.02630
- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) - Dang Nguyen et al. (2024). arXiv:2412.13501
- [Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279) - Chaoyun Zhang et al. (2024). arXiv:2411.18279
- [Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of Foundation Model Based Agents](https://arxiv.org/abs/2408.02205) - Md Shamsujjoha et al. (2024). arXiv:2408.02205
- [The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies](https://arxiv.org/abs/2407.19354) - Feng He et al. (2024). arXiv:2407.19354
- [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935) - Changle Qu et al. (2024). arXiv:2405.17935
- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452) - Zhiruo Wang et al. (2024). arXiv:2403.15452
- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://arxiv.org/abs/2406.01297) - Ryo Kamoi et al. (2024). arXiv:2406.01297
- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Lei Wang et al. (2023). arXiv:2308.11432
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) - Zhiheng Xi et al. (2023). arXiv:2309.07864

### By anatomy part

#### Control loop

- [A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion](https://arxiv.org/abs/2610.19999) - Palvika Bansal, Rittika Jindal, Ruichong Wang (2026). arXiv:2610.19999
- [Adaptive-GEPA: Make Your Harness Fit Heterogeneous Requests](https://arxiv.org/abs/2609.38762) - Tianyu Chen et al. (2026). arXiv:2609.38762
- [Agentic Routing: The Harness-Native Data Flywheel](https://arxiv.org/abs/2607.11399) - Xinchen Liu et al. (2026). arXiv:2607.11399
- [AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses](https://arxiv.org/abs/2608.12307) - Cheng Qian et al. (2026). arXiv:2608.12307
- [An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798) - Kehui Yao et al. (2026). arXiv:2610.28798
- [Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts](https://arxiv.org/abs/2609.18366) - Guojun Zhu et al. (2026). arXiv:2609.18366
- [BAGEN: Are LLM Agents Budget-Aware?](https://arxiv.org/abs/2606.00198) - Yuxiang Lin et al. (2026). arXiv:2606.00198
- [Bounded Loops: Pre-Run Spend Bounds, Proved Termination, and Verified Completion for Agent Harnesses](https://arxiv.org/abs/2609.27871) - Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj (2026). arXiv:2609.27871
- [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](https://arxiv.org/abs/2610.21453) - Zixuan Wang et al. (2026). arXiv:2610.21453
- [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134) - Zhou Yu et al. (2026). arXiv:2609.09134
- [Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1](https://arxiv.org/abs/2607.06764) - Kabir Moghe, Peter Chin (2026). arXiv:2607.06764
- [DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds](https://arxiv.org/abs/2608.06113) - Kishanthan Thangarajah, Boyuan Chen, Ahmed E. Hassan (2026). arXiv:2608.06113
- [Diagnosing and Mitigating Context Rot in Long-horizon Search](https://arxiv.org/abs/2606.29718) - Shijie Xia et al. (2026). arXiv:2606.29718
- [Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution](https://arxiv.org/abs/2609.38108) - Subba Reddy Oota et al. (2026). arXiv:2609.38108
- [Does The Way You Plan Matter? An Empirical Study of Planning Representations for LLM Web Agents](https://arxiv.org/abs/2605.29927) - Alejandra Zambrano et al. (2026). arXiv:2605.29927
- [Does Your Agent Need to Know Its Budget? A Placebo-Controlled Experiment on LLM Coding Agents](https://arxiv.org/abs/2611.21614) - Iftesam Nabi et al. (2026). arXiv:2611.21614
- [DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents](https://arxiv.org/abs/2609.40306) - Haoyuan Deng et al. (2026). arXiv:2609.40306
- [Effective Harness Engineering for Algorithm Discovery with Coding Agents](https://arxiv.org/abs/2605.15221) - Yoichi Ishibashi, Taro Yano, Masafumi Oyamada (2026). arXiv:2605.15221
- [Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution](https://arxiv.org/abs/2610.23782) - Changshu Liu et al. (2026). arXiv:2610.23782
- [EvoX: Rethinking the Agent Harness as a Runtime Policy](https://arxiv.org/abs/2611.15006) - Haoyang Zhang et al. (2026). arXiv:2611.15006
- [Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767) - Tingzhu Bi et al. (2026). arXiv:2610.35767
- [Fyan: A Human--AI Harness with Semantic Auditing for Document-Level Formalization](https://arxiv.org/abs/2609.39228) - Wei Zhao et al. (2026). arXiv:2609.39228
- [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760) - Laizhen Li et al. (2026). arXiv:2609.26760
- [Guava: Distilling Frontier VLMs into a Compact Agent through a Robotic Manipulation Harness](https://arxiv.org/abs/2606.18363) - Haowen Liu et al. (2026). arXiv:2606.18363
- [Harness Annealing: Learning to Act with Less External Control](https://arxiv.org/abs/2610.01235) - Yingxuan Yang, Huacan Chai, Ying Wen (2026). arXiv:2610.01235
- [Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity](https://arxiv.org/abs/2609.26891) - Zhening Li et al. (2026). arXiv:2609.26891
- [Harness Engineering for Predictable Agentic Systems: An Empirical Study of Deterministic Execution Constraints](https://arxiv.org/abs/2608.26197) - Saransh Dhage (2026). arXiv:2608.26197
- [Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses from 0.75B to 4.7B](https://arxiv.org/abs/2611.21407) - Hao Wang, Ting Huang (2026). arXiv:2611.21407
- [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](https://arxiv.org/abs/2609.01481) - Haoyang Yan et al. (2026). arXiv:2609.01481
- [HarnessMDP: Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning](https://arxiv.org/abs/2607.05458) - Haiwen Yi, Xinyuan Song (2026). arXiv:2607.05458
- [HarnessMM: Recursive Self-Improvement for Harness Token Efficiency](https://arxiv.org/abs/2610.32813) - Yuhua Jiang et al. (2026). arXiv:2610.32813
- [HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery](https://arxiv.org/abs/2610.17370) - Yingzi Ma et al. (2026). arXiv:2610.17370
- [How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents](https://arxiv.org/abs/2609.20474) - Yukun Zhang, Kemu Xu, Yishen Chen (2026). arXiv:2609.20474
- [How Much Heavy Lifting Can an Agent Harness Do?: Measuring the LLM's Residual Role in a Planning Agent](https://arxiv.org/abs/2604.07236) - Sungwoo Jung, Seonil Son (2026). arXiv:2604.07236
- [Improving Environment-Agnostic Agents: The Role of Scaffolding](https://arxiv.org/abs/2610.22289) - Sergey Rodionov (2026). arXiv:2610.22289
- [It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers](https://arxiv.org/abs/2605.26731) - Yong-eun Cho (2026). arXiv:2605.26731
- [It's Not the Size: Harness Design Determines Operational Stability in Small Language Models](https://arxiv.org/abs/2605.12129) - Yong-eun Cho (2026). arXiv:2605.12129
- [JoMoHa: Joint Model--Harness Optimization with Reinforcement Learning](https://arxiv.org/abs/2611.11499) - Xudong Wu et al. (2026). arXiv:2611.11499
- [Knowing When to Stop: The Evidence-Action Gap in Coding Agents](https://arxiv.org/abs/2610.31895) - Tianyu Chen et al. (2026). arXiv:2610.31895
- [Learning to Design SR Solvers: Harness Optimization for Symbolic Regression](https://arxiv.org/abs/2610.16966) - Qian Li et al. (2026). arXiv:2610.16966
- [LLM-as-Code: Agentic Programming for Agent Harness](https://arxiv.org/abs/2606.15874) - Junjia Qi et al. (2026). arXiv:2606.15874
- [LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling](https://arxiv.org/abs/2605.14186) - Qi Cao et al. (2026). arXiv:2605.14186
- [MerLean-Prover: A Recursive Looping Harness for Lean 4 Theorem Proving](https://arxiv.org/abs/2605.26959) - Jinzheng Li, Zeru Zhu, Yuanjie Ren (2026). arXiv:2605.26959
- [Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks](https://arxiv.org/abs/2610.02001) - Hao Wang, Ting Huang (2026). arXiv:2610.02001
- [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](https://arxiv.org/abs/2609.14857) - Siwei Wu et al. (2026). arXiv:2609.14857
- [More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding](https://arxiv.org/abs/2605.05716) - Ming Liu (2026). arXiv:2605.05716
- [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723) - Linyue Pan et al. (2026). arXiv:2603.25723
- [One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models](https://arxiv.org/abs/2608.10178) - Siqi Yang et al. (2026). arXiv:2608.10178
- [OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents](https://arxiv.org/abs/2608.05013) - Jingsheng Zheng et al. (2026). arXiv:2608.05013
- [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524) - Hyunin Lee et al. (2026). arXiv:2607.15524
- [Separable Pathways for Causal Reasoning: How Architectural Scaffolding Enables Hypothesis-Space Restructuring in LLM Agents](https://arxiv.org/abs/2604.20039) - John Alderete et al. (2026). arXiv:2604.20039
- [StarCodex: Dynamic Coding Harness for Starlink Measurement Analysis and Experiment Automation](https://arxiv.org/abs/2607.15541) - Pengcheng Luo et al. (2026). arXiv:2607.15541
- [StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments](https://arxiv.org/abs/2608.24804) - Esakkivel Esakkiraja et al. (2026). arXiv:2608.24804
- [Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study](https://arxiv.org/abs/2606.04056) - Sajjad Khan (2026). arXiv:2606.04056
- [Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports](https://arxiv.org/abs/2607.15684) - Jingyi Chen et al. (2026). arXiv:2607.15684
- [VideoEvolve: Evolving Agent Harnesses for Video Temporal Grounding](https://arxiv.org/abs/2610.01766) - Bingjun Luo et al. (2026). arXiv:2610.01766
- [Visual Harness Scales General VLMs to Medical Images](https://arxiv.org/abs/2611.22815) - Shaowen Wan et al. (2026). arXiv:2611.22815
- [What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491) - Kaiser Sun et al. (2026). arXiv:2610.34491
- [When May an Agent Stop? Evidence-Carrying Termination for Tool-Using LLMs](https://arxiv.org/abs/2608.23623) - Jason Liu (2026). arXiv:2608.23623
- [Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) - Xin Ding et al. (2026). arXiv:2608.16590
- [Budget-Aware Tool Use Enables Effective Agent Scaling](https://arxiv.org/abs/2511.17006) - Tengxiao Liu et al. (2025). arXiv:2511.17006
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - Justin Young (2025).
- [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) - Thomas Kwa et al. (2025). arXiv:2503.14499
- [mini-swe-agent (GitHub repository)](https://github.com/SWE-agent/mini-swe-agent) - SWE-agent (2025).
- [The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs](https://arxiv.org/abs/2509.09677) - Akshit Sinha et al. (2025). arXiv:2509.09677
- [Building effective AI agents](https://www.anthropic.com/engineering/building-effective-agents) - Erik S., Barry Zhang (2024).
- [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://arxiv.org/abs/2407.07086) - Logan Cross et al. (2024). arXiv:2407.07086
- [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](https://arxiv.org/abs/2402.01817) - Subbarao Kambhampati et al. (2024). arXiv:2402.01817
- [On the Brittle Foundations of ReAct Prompting for Agentic Large Language Models](https://arxiv.org/abs/2405.13966) - Mudit Verma, Siddhant Bhambri, Subbarao Kambhampati (2024). arXiv:2405.13966
- [Planning in Strawberry Fields: Evaluating and Improving the Planning and Scheduling Capabilities of LRM o1](https://arxiv.org/abs/2410.02162) - Karthik Valmeekam et al. (2024). arXiv:2410.02162
- [TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622) - Jian Xie et al. (2024). arXiv:2402.01622
- [Tree Search for Language Model Agents](https://arxiv.org/abs/2407.01476) - Jing Yu Koh et al. (2024). arXiv:2407.01476
- [ADaPT: As-Needed Decomposition and Planning with Language Models](https://arxiv.org/abs/2311.05772) - Archiki Prasad et al. (2023). arXiv:2311.05772
- [On the Planning Abilities of Large Language Models : A Critical Investigation](https://arxiv.org/abs/2305.15771) - Karthik Valmeekam et al. (2023). arXiv:2305.15771
- [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091) - Lei Wang et al. (2023). arXiv:2305.04091
- [ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323) - Binfeng Xu et al. (2023). arXiv:2305.18323
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) - Shunyu Yao et al. (2023). arXiv:2305.10601
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) - Jason Wei et al. (2022). arXiv:2201.11903
- [MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning](https://arxiv.org/abs/2205.00445) - Ehud Karpas et al. (2022). arXiv:2205.00445
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - Shunyu Yao et al. (2022). arXiv:2210.03629
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) - Rich Sutton (2019).

#### Context manager

- [A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption](https://arxiv.org/abs/2608.25241) - Yegor Denisov-Blanch et al. (2026). arXiv:2608.25241
- [AGENTS.md](https://agents.md/) - AGENTS.md contributors (2026).
- [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804) - Run-Ze Fan et al. (2026). arXiv:2609.20804
- [Benchmarks Are Surprisingly Compaction-Friendly](https://arxiv.org/abs/2610.31778) - Jeanne Salle et al. (2026). arXiv:2610.31778
- [Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2609.34649) - Weiyuan Li et al. (2026). arXiv:2609.34649
- [Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents](https://arxiv.org/abs/2609.32961) - Ritul Satish et al. (2026). arXiv:2609.32961
- [Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/abs/2603.05344) - Nghi D. Q. Bui (2026). arXiv:2603.05344
- [Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving](https://arxiv.org/abs/2610.06597) - Jiaqi Zhao et al. (2026). arXiv:2610.06597
- [CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation](https://arxiv.org/abs/2610.39244) - Minmao Wang et al. (2026). arXiv:2610.39244
- [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/abs/2604.10352) - Mofasshara Rafique, Laurent Bindschaedler (2026). arXiv:2604.10352
- [CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks](https://arxiv.org/abs/2611.25673) - Jiayi Chen et al. (2026). arXiv:2611.25673
- [Compact-Bench: Measuring What Context Compaction Costs Long-Horizon Coding Agents](https://arxiv.org/abs/2610.31710) - Ruopei Sun et al. (2026). arXiv:2610.31710
- [Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes](https://arxiv.org/abs/2607.13071) - Hiroki Tamba (2026). arXiv:2607.13071
- [Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses](https://arxiv.org/abs/2610.41172) - Zhichang Yu et al. (2026). arXiv:2610.41172
- [Context Has a Price: Adding and Removing Context for LLM Coding Agents under Prefix Caching](https://arxiv.org/abs/2611.22238) - Zerui Yang et al. (2026). arXiv:2611.22238
- [Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses](https://arxiv.org/abs/2610.36114) - Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan (2026). arXiv:2610.36114
- [Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223) - Yiwei Zha et al. (2026). arXiv:2611.03223
- [Do Coding Agents Follow AGENTS.md? The Effect of Policy Wording on Instruction Compliance](https://arxiv.org/abs/2611.04367) - Rikuto Tsuchida et al. (2026). arXiv:2611.04367
- [Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories](https://arxiv.org/abs/2607.27250) - Prakhar Khatri (2026). arXiv:2607.27250
- [Do They Do as They Are Told? Investigating Coding Agents' Adherence to Explicit Instructions in Context Files](https://arxiv.org/abs/2611.13709) - Gianmario Voria et al. (2026). arXiv:2611.13709
- [Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2601.06007) - Elias Lumer et al. (2026). arXiv:2601.06007
- [EmoHarness: Boosting Multimodal Emotion Understanding with Meta-Harness Evolving](https://arxiv.org/abs/2611.11994) - Fenghai Li et al. (2026). arXiv:2611.11994
- [EnactOpt: Diagnosis-Guided Harness Evolution for Embodied Agents](https://arxiv.org/abs/2610.14977) - ZhiYuan Feng et al. (2026). arXiv:2610.14977
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) - Thibaud Gloaguen et al. (2026). arXiv:2602.11988
- [FermiLink: An Agent Harness for Multidomain Scientific Simulations](https://arxiv.org/abs/2604.03460) - Gang Meng et al. (2026). arXiv:2604.03460
- [Guardrails Beat Guidance: A Large-Scale Study of Rules, Skills, and Persistent Configuration for Coding Agents](https://arxiv.org/abs/2604.11088) - Xing Zhang et al. (2026). arXiv:2604.11088
- [HARBOR: Automated Harness Optimization](https://arxiv.org/abs/2604.20938) - Biswa Sengupta, Jinhua Wang (2026). arXiv:2604.20938
- [Harness Engineering for Agentic AI Coding Tools: An Exploratory Study](https://arxiv.org/abs/2602.14690) - Matthias Galster et al. (2026). arXiv:2602.14690
- [Harness Tokenomics: A Router for the Enterprise Agentic Control Plane](https://arxiv.org/abs/2609.28919) - Ted Kwartler, Alan Aqrawi, Arian Abbasi (2026). arXiv:2609.28919
- [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/abs/2606.12882) - Xiaoxuan Wang et al. (2026). arXiv:2606.12882
- [Herding CATs: ALARA for Agent Harness Engineering in Portable Composable Multi-Agent Teams](https://arxiv.org/abs/2603.20380) - Christopher J. Agostino, Nayan D'Souza (2026). arXiv:2603.20380
- [How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context in LLM-Driven Vulnerability Discovery](https://arxiv.org/abs/2610.28802) - Ganni Galea Curmi, Ben Wilde (2026). arXiv:2610.28802
- [Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables](https://arxiv.org/abs/2605.10039) - Damon McMillan (2026). arXiv:2605.10039
- [Latent Harness: Compiling Agent Behaviors into Post-Block Activation Shifts](https://arxiv.org/abs/2611.01415) - Ran Li et al. (2026). arXiv:2611.01415
- [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528) - Haiwen Yi, Xinyuan Song (2026). arXiv:2607.04528
- [MedicalHarness: A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks](https://arxiv.org/abs/2610.05778) - Ziqing Wang, Lili Zhao, Kaize Ding (2026). arXiv:2610.05778
- [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052) - Yoonho Lee et al. (2026). arXiv:2603.28052
- [Methodological Harness in Agentic Software Engineering: An Empirical Study on Mining Software Repositories](https://arxiv.org/abs/2609.32014) - Jessica Díaz, Jorge Pérez, Sergio Gil-Borrás (2026). arXiv:2609.32014
- [ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL](https://arxiv.org/abs/2611.18533) - Zelin He et al. (2026). arXiv:2611.18533
- [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/abs/2601.20404) - Jai Lal Lulla et al. (2026). arXiv:2601.20404
- [Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness](https://arxiv.org/abs/2608.20389) - Kevin Dela Rosa (2026). arXiv:2608.20389
- [Same Model, Different Harness: Different Coding-Agent Results](https://arxiv.org/abs/2608.26218) - Sydney Lewis (2026). arXiv:2608.26218
- [Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents](https://arxiv.org/abs/2610.34817) - Ying Zhang et al. (2026). arXiv:2610.34817
- [Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix](https://arxiv.org/abs/2610.30571) - Xiaonan Xu, Wenjing Wu (2026). arXiv:2610.30571
- [System Optimizations for Cost-Efficient Agent Harnesses](https://arxiv.org/abs/2611.12122) - Jongseok Park et al. (2026). arXiv:2611.12122
- [Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations](https://arxiv.org/abs/2608.17433) - Liangtao Lin et al. (2026). arXiv:2608.17433
- [Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests](https://arxiv.org/abs/2606.13449) - Ali Arabat, Mohammed Sayagh (2026). arXiv:2606.13449
- [TRACER: A Multimodal Harness for Patient Care in Hospitals](https://arxiv.org/abs/2610.21266) - Zane Durante et al. (2026). arXiv:2610.21266
- [TTHE: Test-Time Harness Evolution](https://arxiv.org/abs/2607.08124) - Jun Nie et al. (2026). arXiv:2607.08124
- [Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution](https://arxiv.org/abs/2609.37950) - Bingjun Luo, Jialin Guo, Siqi Li (2026). arXiv:2609.37950
- [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](https://arxiv.org/abs/2608.24302) - Guoyang Xu, Hao Chen (2026). arXiv:2608.24302
- [VidHarness: Evolving Agent Harnesses for Cost-Efficient Long Video Understanding](https://arxiv.org/abs/2609.38413) - Susan Liang, Jianmin Wu, Daxiang Dong (2026). arXiv:2609.38413
- [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200) - Qiushi Han et al. (2026). arXiv:2610.02200
- [WHALE: A Simple Recipe for Joint Harness-Weight Optimization](https://arxiv.org/abs/2609.00196) - Haechan Kim et al. (2026). arXiv:2609.00196
- [What Open-Source Projects Tell Their Coding Agents: A Census of AGENTS.md and CLAUDE.md](https://arxiv.org/abs/2610.31715) - Pawel Zarzycki (2026). arXiv:2610.31715
- [When the harness decides success: state that cannot be re-observed](https://arxiv.org/abs/2610.26632) - Raimondas Lencevicius (2026). arXiv:2610.26632
- [Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents](https://arxiv.org/abs/2609.02889) - Michael Nguyen et al. (2026). arXiv:2609.02889
- [Which Part of the Context Layer Does the Work? Separating Semantic Content from Retrieval Scaffolding in Text-to-SQL Agents](https://arxiv.org/abs/2609.22259) - Qing Ye (2026). arXiv:2609.22259
- [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095) - Kushal Chakrabarti (2026). arXiv:2608.11095
- [Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost](https://arxiv.org/abs/2611.03852) - Anton Hristov (2026). arXiv:2611.03852
- [Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://arxiv.org/abs/2511.12884) - Worawalan Chatlatanagulchai et al. (2025). arXiv:2511.12884
- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699) - Rui Ye et al. (2025). arXiv:2510.24699
- [Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases](https://arxiv.org/abs/2512.10398) - Sherman Wong et al. (2025). arXiv:2512.10398
- [Context as a Tool: Context Management for Long-Horizon SWE-Agents](https://arxiv.org/abs/2512.22087) - Shukai Liu et al. (2025). arXiv:2512.22087
- [Decoding the Configuration of AI Coding Agents: Insights from Claude Code Projects](https://arxiv.org/abs/2511.09268) - Helio Victor F. Santos et al. (2025). arXiv:2511.09268
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Anthropic (2025).
- [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Anthropic (2025).
- [FocusAgent: Simple Yet Effective Ways of Trimming the Large Context of Web Agents](https://arxiv.org/abs/2510.03204) - Imene Kerboua et al. (2025). arXiv:2510.03204
- [General Modular Harness for LLM Agents in Multi-Turn Gaming Environments](https://arxiv.org/abs/2507.11633) - Yuxuan Zhang et al. (2025). arXiv:2507.11633
- [NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167) - Ali Modarressi et al. (2025). arXiv:2502.05167
- [Scaling Long-Horizon LLM Agent via Context-Folding](https://arxiv.org/abs/2510.11967) - Weiwei Sun et al. (2025). arXiv:2510.11967
- [The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management](https://arxiv.org/abs/2508.21433) - Tobias Lindenbauer et al. (2025). arXiv:2508.21433
- [Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models](https://arxiv.org/abs/2402.14848) - Mosh Levy, Alon Jacoby, Yoav Goldberg (2024). arXiv:2402.14848
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) - Nelson F. Liu et al. (2023). arXiv:2307.03172
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) - Charles Packer et al. (2023). arXiv:2310.08560
- [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://arxiv.org/abs/2311.04934) - In Gim et al. (2023). arXiv:2311.04934
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) - Patrick Lewis et al. (2020). arXiv:2005.11401
- [Prompt caching - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) - Anthropic.

#### Action interface

- [Action-Space Shaping for LLM Agents: Measuring and Mitigating Tool-Schema Bias](https://arxiv.org/abs/2609.34971) - Yinhong Liu et al. (2026). arXiv:2609.34971
- [Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents](https://arxiv.org/abs/2605.22166) - Tianshi Xu, Huifeng Wen, Meng Li (2026). arXiv:2605.22166
- [Agentic Harness for Real-World Compilers](https://arxiv.org/abs/2603.20075) - Yingwei Zheng et al. (2026). arXiv:2603.20075
- [AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness](https://arxiv.org/abs/2606.10577) - Yijian Li et al. (2026). arXiv:2606.10577
- [An Empirical Study of Model Context Protocol Applications](https://arxiv.org/abs/2607.25635) - Muhammad Hamza Arshad Majeed, May Mahmoud, Sarah Nadi (2026). arXiv:2607.25635
- [An LLM-Agnostic, MAVLink-Based Drone Command and Control Interface and Agentic Harness Using the Model Context Protocol](https://arxiv.org/abs/2601.15486) - Javier Noé Ramos Silva, Peter J. Burke (2026). arXiv:2601.15486
- [Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory](https://arxiv.org/abs/2610.39446) - Kai Sheng et al. (2026). arXiv:2610.39446
- [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112) - Chengcheng Wang et al. (2026). arXiv:2611.01112
- [Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses](https://arxiv.org/abs/2609.05736) - Cen Mia Zhao et al. (2026). arXiv:2609.05736
- [ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning](https://arxiv.org/abs/2610.28282) - Qi Wang et al. (2026). arXiv:2610.28282
- [CODESTRUCT: Code Agents over Structured Action Spaces](https://arxiv.org/abs/2604.05407) - Myeongsoo Kim et al. (2026). arXiv:2604.05407
- [Constrained Decoding: Harmful or Beneficial? Revisiting Its Impact on LLM Performance](https://arxiv.org/abs/2610.35328) - Ngoc Trinh Hung Nguyen et al. (2026). arXiv:2610.35328
- [Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740) - Pengze Li et al. (2026). arXiv:2610.17740
- [CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910) - Dongjie Cheng et al. (2026). arXiv:2610.21910
- [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](https://arxiv.org/abs/2608.18613) - Yutong Cheng et al. (2026). arXiv:2608.18613
- [DeltaHarness: Self-Evolving Harnesses for Resource-Adaptive Tool Execution](https://arxiv.org/abs/2611.21688) - Lecheng Yan et al. (2026). arXiv:2611.21688
- [From Tool Orchestration to Code Execution: A Study of MCP Design Choices](https://arxiv.org/abs/2602.15945) - Yuval Felendler et al. (2026). arXiv:2602.15945
- [Function calling \| OpenAI API](https://platform.openai.com/docs/guides/function-calling) - OpenAI (2026).
- [Harness Compilation: Which Decisions Should a Small Vision-Language Model Keep?](https://arxiv.org/abs/2610.11231) - Minhao Fan et al. (2026). arXiv:2610.11231
- [Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives](https://arxiv.org/abs/2609.01736) - Haibo Jin et al. (2026). arXiv:2609.01736
- [Harness-G: A Graph-Structured Harness for Search Agents](https://arxiv.org/abs/2607.27652) - Yanning Hou et al. (2026). arXiv:2607.27652
- [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) - Xin Wang et al. (2026). arXiv:2609.29166
- [HexaShell: A Universal Harness for Robot Coding Agents in Simulation and the Real World](https://arxiv.org/abs/2610.23479) - Hongcheng Gao et al. (2026). arXiv:2610.23479
- [Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents](https://arxiv.org/abs/2610.41432) - Haoqing Wang et al. (2026). arXiv:2610.41432
- [I-PTC: Interactive Programmatic Tool Calling for Stateful Tool-Augmented Agents](https://arxiv.org/abs/2611.01446) - Huanzhi Mao et al. (2026). arXiv:2611.01446
- [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/abs/2605.15184) - Sahil Sen et al. (2026). arXiv:2605.15184
- [Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616) - Yuyang Bai, Yu Wang, Yu Zhang (2026). arXiv:2610.18616
- [Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction](https://arxiv.org/abs/2610.37046) - Haoyu Yao et al. (2026). arXiv:2610.37046
- [Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents](https://arxiv.org/abs/2610.34298) - Zhenning Shi, Liang Pang, Yongqi Li (2026). arXiv:2610.34298
- [Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents](https://arxiv.org/abs/2609.39982) - Minki Kang et al. (2026). arXiv:2609.39982
- [Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions](https://arxiv.org/abs/2602.14878) - Mohammed Mehedi Hasan et al. (2026). arXiv:2602.14878
- [Policy as Code: A Coroutine-Bridge Harness for Fast-Reasoning Reliability on CAR-bench](https://arxiv.org/abs/2609.29251) - Ivan Matveev (2026). arXiv:2609.29251
- [Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](https://arxiv.org/abs/2610.29812) - Mohammed Saqlain (2026). arXiv:2610.29812
- [Rethinking Tool Design for Agentic RCA: A Controlled Empirical Study](https://arxiv.org/abs/2610.05009) - Yu Luo et al. (2026). arXiv:2610.05009
- [RoboHarness: A Simple Harness Outperforms VLA and World Action Models](https://arxiv.org/abs/2610.14018) - Bince Qu, Wei Chen, Bo Zhang (2026). arXiv:2610.14018
- [Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem](https://arxiv.org/abs/2609.14119) - Obada Kraishan (2026). arXiv:2609.14119
- [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519) - Haozhe Liu et al. (2026). arXiv:2609.20519
- [SRHarness: A Harness for Agentic Symbolic Regression](https://arxiv.org/abs/2609.35501) - Zihan Yu et al. (2026). arXiv:2609.35501
- [The Cost of Saying Hello: An Empirical Study of Handshake Overhead in AI Agent Communication Protocols](https://arxiv.org/abs/2610.30151) - Pranav Varshney (2026). arXiv:2610.30151
- [The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior](https://arxiv.org/abs/2608.11386) - Xiangzhe Xu et al. (2026). arXiv:2608.11386
- [The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447) - Kyungmin Kim et al. (2026). arXiv:2606.25447
- [The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task](https://arxiv.org/abs/2608.08654) - Marc Alier Forment et al. (2026). arXiv:2608.08654
- [Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555) - Antonio Ken Iannillo et al. (2026). arXiv:2610.32555
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/abs/2607.25718) - Xinyi Hong et al. (2026). arXiv:2607.25718
- [Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem](https://arxiv.org/abs/2610.05319) - Tingxuan Tang, Zilong Chen, Yue Xiao (2026). arXiv:2610.05319
- [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](https://arxiv.org/abs/2611.17797) - Haolin Yang et al. (2026). arXiv:2611.17797
- [When Does Restricting a Coding Agent to execute_code Help? A Regime $\times$ Agent-Design Ablation](https://arxiv.org/abs/2607.10569) - Hong Yang, Qi Yu, Travis Desell (2026). arXiv:2607.10569
- [When Harness Beats Scale, and When Reading Beats Both](https://arxiv.org/abs/2609.34366) - Ivan Bondarenko, Nikolay O. Nikitin (2026). arXiv:2609.34366
- [When Interfaces Speak: Data-Aware Generative UI Harness for Active Interaction](https://arxiv.org/abs/2610.11123) - Xiaolong Li et al. (2026). arXiv:2610.11123
- [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095) - Jiapeng Li (2026). arXiv:2609.29095
- [Which Metadata Matters for LLM Tool Selection in MCP? Evidence from Controlled Factor-Level Interventions](https://arxiv.org/abs/2610.14334) - Xiaofan Li, Fengchun Qiao, Xing Gao (2026). arXiv:2610.14334
- [Code execution with MCP for efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp) - Anthropic (2025).
- [JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models](https://arxiv.org/abs/2501.10868) - Saibo Geng et al. (2025). arXiv:2501.10868
- [MCP-Zero: Active Tool Discovery for Autonomous LLM Agents](https://arxiv.org/abs/2506.01056) - Xiang Fei, Xiawu Zheng, Hao Feng (2025). arXiv:2506.01056
- [Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers](https://arxiv.org/abs/2506.13538) - Mohammed Mehedi Hasan et al. (2025). arXiv:2506.13538
- [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563) - Hongrui Jia et al. (2025). arXiv:2510.24563
- [RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation](https://arxiv.org/abs/2505.03275) - Tiantian Gan, Qiyao Sun (2025). arXiv:2505.03275
- [Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models](https://arxiv.org/abs/2503.01763) - Zhengliang Shi et al. (2025). arXiv:2503.01763
- [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://proceedings.mlr.press/v267/patil25a.html) - Shishir G Patil et al. (2025).
- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) - Yujia Qin et al. (2025). arXiv:2501.12326
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) - Anthropic (2025).
- [$τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) - Shunyu Yao et al. (2024). arXiv:2406.12045
- [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://arxiv.org/abs/2410.13825) - Ke Yang et al. (2024). arXiv:2410.13825
- [Beyond Browsing: API-Based Web Agents](https://arxiv.org/abs/2410.16464) - Yueqi Song et al. (2024). arXiv:2410.16464
- [Computer use, Claude 3.5 Sonnet, and Claude 3.5 Haiku](https://www.anthropic.com/news/3-5-models-and-computer-use) - Anthropic (2024).
- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) - Xingyao Wang et al. (2024). arXiv:2402.01030
- [Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models](https://arxiv.org/abs/2408.02442) - Zhi Rui Tam et al. (2024). arXiv:2408.02442
- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243) - Boyu Gou et al. (2024). arXiv:2410.05243
- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203) - Yadong Lu et al. (2024). arXiv:2408.00203
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) - Tianbao Xie et al. (2024). arXiv:2404.07972
- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) - Kanzhi Cheng et al. (2024). arXiv:2401.10935
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) - John Yang et al. (2024). arXiv:2405.15793
- [ToolGen: Unified Tool Retrieval and Calling via Generation](https://arxiv.org/abs/2410.03439) - Renxi Wang et al. (2024). arXiv:2410.03439
- [TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks](https://arxiv.org/abs/2401.12869) - Zhiruo Wang, Daniel Fried, Graham Neubig (2024). arXiv:2401.12869
- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) - Shishir G. Patil et al. (2023). arXiv:2305.15334
- [Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126) - Tianle Cai et al. (2023). arXiv:2305.17126
- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441) - Jianwei Yang et al. (2023). arXiv:2310.11441
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - Timo Schick et al. (2023). arXiv:2302.04761
- [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789) - Yujia Qin et al. (2023). arXiv:2307.16789
- [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) - Luyu Gao et al. (2022). arXiv:2211.10435
- [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/abs/2211.12588) - Wenhu Chen et al. (2022). arXiv:2211.12588

#### Execution environment

- [An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657) - Robert Sorab Stanley et al. (2026). arXiv:2604.19657
- [AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction](https://arxiv.org/abs/2606.23449) - Shanhui Zhao et al. (2026). arXiv:2606.23449
- [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417) - E. Kelly Buchanan et al. (2026). arXiv:2611.08417
- [Can You Undo It? Reversibility Classes for AI Agent Actions](https://arxiv.org/abs/2611.22075) - Deepak Waghmare, Shaad Sufi (2026). arXiv:2611.22075
- [ClawGym II: Exploring Black-Box RL on Agent Harness](https://arxiv.org/abs/2608.16798) - Huatong Song et al. (2026). arXiv:2608.16798
- [HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention](https://arxiv.org/abs/2610.06563) - Han Luo et al. (2026). arXiv:2610.06563
- [Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI](https://arxiv.org/abs/2609.38143) - Cheng Qian et al. (2026). arXiv:2609.38143
- [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](https://arxiv.org/abs/2608.17393) - Yiming Du et al. (2026). arXiv:2608.17393
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557) - Xiao Yu et al. (2026). arXiv:2607.21557
- [PUDA: An AI-Native Hardware Harness for Self-Driving Laboratories](https://arxiv.org/abs/2607.26464) - Zekun Ren et al. (2026). arXiv:2607.26464
- [Readie: Low-Latency Code Sandboxes for AI Agents](https://arxiv.org/abs/2611.22171) - Arjun Sivaraman et al. (2026). arXiv:2611.22171
- [Returning to Development States: When Full Sandbox Snapshots Help Coding Agents](https://arxiv.org/abs/2610.13841) - Daniel Thi Graviet, Tanmay Shah (2026). arXiv:2610.13841
- [RippleCP: Measuring Counterfactual Checkpoint Advantage in Coding Agents](https://arxiv.org/abs/2610.09088) - Mayur Akewar, Ravi Ranjan (2026). arXiv:2610.09088
- [SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS](https://arxiv.org/abs/2610.02456) - Dimitrios Prasakis (2026). arXiv:2610.02456
- [Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines](https://arxiv.org/abs/2611.11344) - Chentao Cao et al. (2026). arXiv:2611.11344
- [ceLLMate: Sandboxing Browser AI Agents](https://arxiv.org/abs/2512.12594) - Luoxi Meng et al. (2025). arXiv:2512.12594
- [DeepResearchGym: A Free, Transparent, and Reproducible Evaluation Sandbox for Deep Research](https://arxiv.org/abs/2505.19253) - João Coelho et al. (2025). arXiv:2505.19253
- [Making Claude Code safer with sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) - Anthropic (2025).
- [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) - Anthropic (2025).
- [The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents](https://arxiv.org/abs/2511.03690) - Xingyao Wang et al. (2025). arXiv:2511.03690
- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) - Christopher Rawles et al. (2024). arXiv:2405.14573
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299) - Michele Tufano et al. (2024). arXiv:2403.08299
- [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741) - Xingyao Wang et al. (2024). arXiv:2407.16741
- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://arxiv.org/abs/2409.08264) - Rogerio Bonatti et al. (2024). arXiv:2409.08264
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) - Carlos E. Jimenez et al. (2023). arXiv:2310.06770
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) - Shuyan Zhou et al. (2023). arXiv:2307.13854
- [Blending containers and virtual machines: a study of firecracker and gVisor](https://doi.org/10.1145/3381052.3381315) - Anjali, Tyler Caraza-Harter, Michael M. Swift (2020). doi:10.1145/3381052.3381315
- [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) - Alexandru Agache et al. (2020).
- [gVisor: Application Kernel for Containers](https://github.com/gvisor/gvisor) - gVisor Authors (2018).

#### State and memory

- [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](https://arxiv.org/abs/2609.29204) - Junyi Tang et al. (2026). arXiv:2609.29204
- [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770) - Zewen Liu et al. (2026). arXiv:2606.01770
- [AEL: Evolving Agent Harness in Open-Ended Environments](https://arxiv.org/abs/2604.21725) - Wujiang Xu et al. (2026). arXiv:2604.21725
- [Agentic Interpretation: Harness-Governed Evidence Construction for Software Agents](https://arxiv.org/abs/2610.23996) - Yifeng He et al. (2026). arXiv:2610.23996
- [An Empirical Study of Agent Skills' Downstream Utility](https://arxiv.org/abs/2610.08875) - Yu Cheng et al. (2026). arXiv:2610.08875
- [Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses](https://arxiv.org/abs/2606.08348) - Xiaojun Wu et al. (2026). arXiv:2606.08348
- [Causal Improvement Graph for Agentic Harness Optimization](https://arxiv.org/abs/2610.05039) - Junjie Zhang et al. (2026). arXiv:2610.05039
- [Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents](https://arxiv.org/abs/2611.17696) - Luyao Wang et al. (2026). arXiv:2611.17696
- [Cochise: A Reference Harness for Autonomous Penetration Testing](https://arxiv.org/abs/2605.11671) - Andreas Happe, Jürgen Cito (2026). arXiv:2605.11671
- [CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://arxiv.org/abs/2610.25078) - Jiaqi Su et al. (2026). arXiv:2610.25078
- [COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709) - Zongxia Li et al. (2026). arXiv:2607.01709
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) - Seth Karten et al. (2026). arXiv:2605.09998
- [Delivered, Not Used: Evaluating Agent Memory at Its Point of Use](https://arxiv.org/abs/2611.01718) - Changran Xu, Zeju Li, Qiang Xu (2026). arXiv:2611.01718
- [Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents](https://arxiv.org/abs/2607.20972) - Swapnanil Saha (2026). arXiv:2607.20972
- [DeltaBox: Millisecond-Scale Sandbox Checkpoint and Rollback for Stateful AI Agents](https://arxiv.org/abs/2605.22781) - Yunpeng Dong et al. (2026). arXiv:2605.22781
- [Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Traces](https://arxiv.org/abs/2608.10319) - Shuyan Huang, Kai Du, Andrew Lan (2026). arXiv:2608.10319
- [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071) - Tianxin Wei et al. (2026). arXiv:2608.15071
- [EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts](https://arxiv.org/abs/2611.03868) - Xinyi Xu et al. (2026). arXiv:2611.03868
- [EvoHarness-RL: Learning Runtime Harness Coordination for Self-Evolving Agents](https://arxiv.org/abs/2608.05446) - Xuying Ning et al. (2026). arXiv:2608.05446
- [Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference](https://arxiv.org/abs/2606.05922) - Wenbo Pan et al. (2026). arXiv:2606.05922
- [Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation](https://arxiv.org/abs/2610.33024) - Zhihao Yang et al. (2026). arXiv:2610.33024
- [EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses](https://arxiv.org/abs/2608.28363) - Tanmay Sah et al. (2026). arXiv:2608.28363
- [ExpHarness: Model-Agnostic Experience Learning through a Trainable Harness](https://arxiv.org/abs/2605.30712) - Tao Feng et al. (2026). arXiv:2605.30712
- [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](https://arxiv.org/abs/2606.17642) - Pianran Guo et al. (2026). arXiv:2606.17642
- [GenMem: Generative Symbolic Memory for Self-Evolving Harness](https://arxiv.org/abs/2609.34633) - Xinke Jiang et al. (2026). arXiv:2609.34633
- [GitHarness: Git Init Your Harness Working Memory for Perpetual User Requirements](https://arxiv.org/abs/2609.36789) - Zhibang Yang et al. (2026). arXiv:2609.36789
- [Harness Continual Learning: Continual Adaptation Beyond Model Parameters](https://arxiv.org/abs/2608.19013) - Borui Kang et al. (2026). arXiv:2608.19013
- [Harness Engineering for Software Engineering via Modular Executable Dev-Primitives](https://arxiv.org/abs/2610.07832) - Haibo Jin et al. (2026). arXiv:2610.07832
- [Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents](https://arxiv.org/abs/2609.36892) - Zeyu Gan, Zixuan Gong, Yong Liu (2026). arXiv:2609.36892
- [Harness Evolution Hits a Ceiling: When Weight Training Should Begin](https://arxiv.org/abs/2610.11655) - Yuan Tian et al. (2026). arXiv:2610.11655
- [Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents](https://arxiv.org/abs/2608.15008) - Wei-Chieh Huang et al. (2026). arXiv:2608.15008
- [Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621) - Minhua Lin et al. (2026). arXiv:2605.30621
- [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373) - Pengcheng Jiang et al. (2026). arXiv:2606.02373
- [Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724) - Zhen Bi et al. (2026). arXiv:2610.34724
- [HELIX: Model-Harness Co-evolution for Recursive Self-Improvement](https://arxiv.org/abs/2608.13951) - Tianyu Fan, Chao Huang (2026). arXiv:2608.13951
- [HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation](https://arxiv.org/abs/2604.18791) - Zijian Zeng et al. (2026). arXiv:2604.18791
- [HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization](https://arxiv.org/abs/2610.40023) - Jianghan Zhu et al. (2026). arXiv:2610.40023
- [HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup](https://arxiv.org/abs/2611.18443) - Xiang Li et al. (2026). arXiv:2611.18443
- [HERD: Harness-Evolving Recursive Distillation for Continual Learning](https://arxiv.org/abs/2610.31401) - Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu (2026). arXiv:2610.31401
- [How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub](https://arxiv.org/abs/2611.04456) - Jinjun Huang et al. (2026). arXiv:2611.04456
- [Incremental Open-Ended Deep Research with Structured Harness](https://arxiv.org/abs/2610.11566) - Meilin Chen, Hongyuan Bao (2026). arXiv:2610.11566
- [Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](https://arxiv.org/abs/2610.30755) - Zhengye Bao et al. (2026). arXiv:2610.30755
- [JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents](https://arxiv.org/abs/2607.23588) - Yunlong Lin et al. (2026). arXiv:2607.23588
- [Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs](https://arxiv.org/abs/2609.28530) - Zeyu Lou et al. (2026). arXiv:2609.28530
- [Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent](https://arxiv.org/abs/2611.15268) - Yujia Zhang et al. (2026). arXiv:2611.15268
- [KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](https://arxiv.org/abs/2610.27417) - Zhikang Chen et al. (2026). arXiv:2610.27417
- [L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](https://arxiv.org/abs/2610.19591) - Carson Eisenach et al. (2026). arXiv:2610.19591
- [LiteEvo: Automated, Cost-Efficient Harness Evolution for Generalization to Unseen Tasks](https://arxiv.org/abs/2609.33146) - Euntae Choi, Sumin Song, Sungjoo Yoo (2026). arXiv:2609.33146
- [Living-Harness Is an Interactive-Agent Evolver](https://arxiv.org/abs/2607.26598) - Yuetian Du et al. (2026). arXiv:2607.26598
- [LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://arxiv.org/abs/2608.01964) - Ziyu Ma et al. (2026). arXiv:2608.01964
- [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493) - Di Wu et al. (2026). arXiv:2605.12493
- [LVMH: A Meta-Optimization Harness for Long-Video Agent Memory](https://arxiv.org/abs/2610.23904) - Liwei Che et al. (2026). arXiv:2610.23904
- [M$^\star$: Every Task Deserves Its Own Memory Harness](https://arxiv.org/abs/2604.11811) - Wenbo Pan et al. (2026). arXiv:2604.11811
- [MaLiang-Harness: A Programmable Path to Image and Video Generation](https://arxiv.org/abs/2609.34309) - Haoyu Zhao et al. (2026). arXiv:2609.34309
- [Recurrent Harness for Agentic Continual Learning](https://arxiv.org/abs/2610.12668) - Yuxin Xiao et al. (2026). arXiv:2610.12668
- [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876) - Zhaochen Yu et al. (2026). arXiv:2608.24876
- [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378) - Seungyeon Kim et al. (2026). arXiv:2609.33378
- [Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis](https://arxiv.org/abs/2610.03548) - Wenlong Zhang et al. (2026). arXiv:2610.03548
- [Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation](https://arxiv.org/abs/2609.38024) - Jaewon Chu et al. (2026). arXiv:2609.38024
- [RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060) - Zhuoran Li et al. (2026). arXiv:2603.24060
- [Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers](https://arxiv.org/abs/2609.00546) - Zhenyu Zhao, Roy Zhao (2026). arXiv:2609.00546
- [SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction](https://arxiv.org/abs/2609.05511) - Bowei He et al. (2026). arXiv:2609.05511
- [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) - Peidong Wang et al. (2026). arXiv:2608.11350
- [Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators](https://arxiv.org/abs/2605.22343) - Chengcheng Wang et al. (2026). arXiv:2605.22343
- [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671) - Zhiwei Li, Yong Hu (2026). arXiv:2606.08671
- [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency](https://arxiv.org/abs/2603.29919) - Yudong Gao et al. (2026). arXiv:2603.29919
- [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670) - Xiangyi Li et al. (2026). arXiv:2602.12670
- [SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses](https://arxiv.org/abs/2604.03088) - Le Chen et al. (2026). arXiv:2604.03088
- [StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling](https://arxiv.org/abs/2608.15089) - Ziheng Qin et al. (2026). arXiv:2608.15089
- [Stratum: Repository Memory for Coding Agents Beyond the Context Window](https://arxiv.org/abs/2610.36153) - Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan (2026). arXiv:2610.36153
- [StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](https://arxiv.org/abs/2607.11388) - Wenyi Wu et al. (2026). arXiv:2607.11388
- [SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?](https://arxiv.org/abs/2603.15401) - Tingxu Han et al. (2026). arXiv:2603.15401
- [Teaching the Harness: Student-Aware Skill Transfer for LLM Agents](https://arxiv.org/abs/2611.13144) - Chang Liu, Bo Wu (2026). arXiv:2611.13144
- [Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness](https://arxiv.org/abs/2611.22432) - Siqi Lai, Haitao Li, Hao Liu (2026). arXiv:2611.22432
- [VideoEvoHarness: Self Evolving Agent Harness from Unlabeled Videos for Video Understanding](https://arxiv.org/abs/2610.15389) - Weixin Xu et al. (2026). arXiv:2610.15389
- [What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory](https://arxiv.org/abs/2611.03930) - Chih-Hsuan Yang et al. (2026). arXiv:2611.03930
- [Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving](https://arxiv.org/abs/2507.06229) - Xiangru Tang et al. (2025). arXiv:2507.06229
- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) - Qizheng Zhang et al. (2025). arXiv:2510.04618
- [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952) - Mirac Suzgun et al. (2025). arXiv:2504.07952
- [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257) - Yuanzhe Hu, Yu Wang, Julian McAuley (2025). arXiv:2507.05257
- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857) - Tianxin Wei et al. (2025). arXiv:2511.20857
- [HaluMem: Evaluating Hallucinations in Memory Systems of Agents](https://arxiv.org/abs/2511.03506) - Ding Chen et al. (2025). arXiv:2511.03506
- [LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866) - Jizhan Fang et al. (2025). arXiv:2510.18866
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) - Prateek Chhikara et al. (2025). arXiv:2504.19413
- [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) - Yuyang Hu et al. (2025). arXiv:2512.13564
- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) - Siru Ouyang et al. (2025). arXiv:2509.25140
- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079) - Boyuan Zheng et al. (2025). arXiv:2504.07079
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) - Preston Rasmussen et al. (2025). arXiv:2501.13956
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) - Zora Zhiruo Wang et al. (2024). arXiv:2409.07429
- [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) - Adyasha Maharana et al. (2024). arXiv:2402.17753
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) - Di Wu et al. (2024). arXiv:2410.10813
- [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) - Andrew Zhao et al. (2023). arXiv:2308.10144
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - Joon Sung Park et al. (2023). arXiv:2304.03442
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Noah Shinn et al. (2023). arXiv:2303.11366
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) - Guanzhi Wang et al. (2023). arXiv:2305.16291
- [Specification - Agent Skills](https://agentskills.io/specification) - Agent Skills project.

#### Verification and feedback

- [A Domain-Specific Harness for End-to-End Automation of Optimization Research](https://arxiv.org/abs/2608.07407) - Heechang Kim, Ernest K. Ryu, Shuvomoy Das Gupta (2026). arXiv:2608.07407
- [Action Verification through Conjecture and Refutation for Language Model Agents](https://arxiv.org/abs/2611.02950) - Minhyeon Oh et al. (2026). arXiv:2611.02950
- [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](https://arxiv.org/abs/2608.09857) - Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai (2026). arXiv:2608.09857
- [AutoHarness: improving LLM agents by automatically synthesizing a code harness](https://arxiv.org/abs/2603.03329) - Xinghua Lou et al. (2026). arXiv:2603.03329
- [Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test](https://arxiv.org/abs/2608.13228) - Saveliy Batruin (2026). arXiv:2608.13228
- [Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild](https://arxiv.org/abs/2610.04921) - Yifan Xiong et al. (2026). arXiv:2610.04921
- [Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation](https://arxiv.org/abs/2611.18471) - Disha Sheshanarayana, Sai Linisha Reddy Goli (2026). arXiv:2611.18471
- [Done Is Not Correct: Measuring Silent Failures and Self-Verification Calibration When LLM Agents Take CAD Actions](https://arxiv.org/abs/2611.10063) - Carson Rodrigues, Clive Rodrigues, Aravind Reddy G (2026). arXiv:2611.10063
- [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028) - Joongho Ahn, Moonsoo Kim (2026). arXiv:2607.08028
- [GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution](https://arxiv.org/abs/2610.00948) - Geyi Yang et al. (2026). arXiv:2610.00948
- [Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF)](https://arxiv.org/abs/2604.17025) - Tianbao Zhang (2026). arXiv:2604.17025
- [Harness-agnostic detection and immunization of reward hacking in self-evolving language models](https://arxiv.org/abs/2609.04665) - Rongxin Yang et al. (2026). arXiv:2609.04665
- [HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770) - Zhuoshi Pan et al. (2026). arXiv:2610.26770
- [Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures](https://arxiv.org/abs/2611.20595) - Sajib Acharjee Dip, Brian Ouyang, Lala Motlhabi (2026). arXiv:2611.20595
- [Maestro Order: A Model-Agnostic Orchestration Harness](https://arxiv.org/abs/2606.23983) - Hidayet Aksu (2026). arXiv:2606.23983
- [MUSE: A Unified Agentic Harness for MLLMs](https://arxiv.org/abs/2606.03005) - Jianglin Lu et al. (2026). arXiv:2606.03005
- [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](https://arxiv.org/abs/2607.13083) - Su Wang et al. (2026). arXiv:2607.13083
- [ReFlect: An Effective Harness System for Complex Long-Horizon LLM Reasoning](https://arxiv.org/abs/2605.05737) - Fan Huang (2026). arXiv:2605.05737
- [Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents](https://arxiv.org/abs/2602.07900) - Zhi Chen et al. (2026). arXiv:2602.07900
- [Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577) - Zhengxin Zhang et al. (2026). arXiv:2610.34577
- [SBCO: Self-Supervised, Verifier-Grounded Harness Optimization For Planning Agents](https://arxiv.org/abs/2608.10157) - Vivek Kulkarni et al. (2026). arXiv:2608.10157
- [Scaling Laws for Agent Harnesses via Effective Feedback Compute](https://arxiv.org/abs/2605.29682) - Xuanliang Zhang et al. (2026). arXiv:2605.29682
- [Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection](https://arxiv.org/abs/2608.20169) - Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki (2026). arXiv:2608.20169
- [The Last Harness You'll Ever Build](https://arxiv.org/abs/2604.21003) - Haebin Seong et al. (2026). arXiv:2604.21003
- [Trace-to-Architecture: Capability Bottleneck Diagnosis for Harness Revision](https://arxiv.org/abs/2610.16725) - Wenfeng Wang et al. (2026). arXiv:2610.16725
- [Verifier-Guided Twelve-Tone Composition: A Generate-Verify-Repair Harness for Symbolic Music Generation](https://arxiv.org/abs/2607.11334) - Congren Dai et al. (2026). arXiv:2607.11334
- [Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609) - Tianyi Xu et al. (2026). arXiv:2610.17609
- [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](https://arxiv.org/abs/2608.27311) - Jinghan Xu et al. (2026). arXiv:2608.27311
- [Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents](https://arxiv.org/abs/2607.17641) - Yitao Wu et al. (2026). arXiv:2607.17641
- [Veritas: A Verifier Generation Harness for Agent Tasks](https://arxiv.org/abs/2611.13336) - Daoan Zhang et al. (2026). arXiv:2611.13336
- [VERSE: Verified Self-Evolving Optimizer for Agent Harnesses](https://arxiv.org/abs/2610.02616) - Zekai Wang et al. (2026). arXiv:2610.02616
- [Vestrum: Learning the Verification, Retrieval and Structure of Agent Harnesses from a Few Long Episodes](https://arxiv.org/abs/2609.33822) - Jayant Parashar et al. (2026). arXiv:2609.33822
- [What Do CAE Simulation Agents Really Need Beyond a Generic Harness?](https://arxiv.org/abs/2609.03718) - Jiasheng Shi, Tianhan Zhang (2026). arXiv:2609.03718
- [When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents](https://arxiv.org/abs/2610.00372) - Shuyao Xiao et al. (2026). arXiv:2610.00372
- [When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826) - Hao Chen et al. (2026). arXiv:2610.36826
- [Where Does Agent Reliability Come From? A Cross-Benchmark Decomposition of Verification Loops, Specialist Models, and Scaffolding in a Production Enterprise Agent](https://arxiv.org/abs/2607.17044) - Arunabh Dastidar (2026). arXiv:2607.17044
- [app.build: A Production Framework for Scaling Agentic Prompt-to-App Generation with Environment Scaffolding](https://arxiv.org/abs/2509.03310) - Evgenii Kniazev et al. (2025). arXiv:2509.03310
- [Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/abs/2503.15223) - You Wang, Michael Pradel, Zhongxin Liu (2025). arXiv:2503.15223
- [On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks](https://arxiv.org/abs/2402.08115) - Kaya Stechly, Karthik Valmeekam, Subbarao Kambhampati (2024). arXiv:2402.08115
- [Self-Reflection in LLM Agents: Effects on Problem-Solving Performance](https://arxiv.org/abs/2405.06682) - Matthew Renze, Erhan Guven (2024). arXiv:2405.06682
- [Can Large Language Models Really Improve by Self-critiquing Their Own Plans?](https://arxiv.org/abs/2310.08118) - Karthik Valmeekam, Matthew Marquez, Subbarao Kambhampati (2023). arXiv:2310.08118
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) - Aman Madaan et al. (2023). arXiv:2303.17651
- [CodeT: Code Generation with Generated Tests](https://arxiv.org/abs/2207.10397) - Bei Chen et al. (2022). arXiv:2207.10397

#### Governance

- [ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses](https://arxiv.org/abs/2606.25189) - Yusheng Zheng et al. (2026). arXiv:2606.25189
- [Agentao: A Policy-Governed Runtime Harness for Embeddable Tool-Using LLM Agents](https://arxiv.org/abs/2608.13574) - Bo Jin, Qiang Jiao, Xin Tong (2026). arXiv:2608.13574
- [Applying Anthropic Primitives at Large Enterprises: Harness Paradigm for Knowledge Work](https://arxiv.org/abs/2608.20622) - George Juraj Salapa (2026). arXiv:2608.20622
- [Auditable Authorization for LLM Agents: Empirical Evidence Across Model, Harness, and Workflow Layers](https://arxiv.org/abs/2611.19237) - Bangjie Deng et al. (2026). arXiv:2611.19237
- [Clinical Harness for Governable Medical AI Skill Ecosystems](https://arxiv.org/abs/2606.26494) - Tianhan Xu et al. (2026). arXiv:2606.26494
- [Distributing Security Controls Through Harness Engineering](https://arxiv.org/abs/2607.25890) - William Robert Gore (2026). arXiv:2607.25890
- [From Proposal to Verified Effect: Praxa, an Evidence-Bound Harness for Governed AI Agent Execution](https://arxiv.org/abs/2610.00015) - Stefan G. Creadore (2026). arXiv:2610.00015
- [Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents](https://arxiv.org/abs/2606.21856) - Wangxuan Fan, Xiaoyu Nie, Zhongxiang Dai (2026). arXiv:2606.21856
- [Safe, Persistent, and Evolving Agent Harness for Understanding Partially Observable Worlds](https://arxiv.org/abs/2610.11552) - Yisen Gao et al. (2026). arXiv:2610.11552
- [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786) - Qinghua Mao et al. (2026). arXiv:2609.02786
- [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885) - Wanying Qu et al. (2026). arXiv:2608.09885
- [The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate](https://arxiv.org/abs/2610.10629) - Ravil Akhtyamov (2026). arXiv:2610.10629
- [When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses](https://arxiv.org/abs/2611.09088) - Boming Xia et al. (2026). arXiv:2611.09088

#### Orchestration

- [A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717) - Xiaochen Chang (2026). arXiv:2610.36717
- [A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO](https://arxiv.org/abs/2606.27188) - Fabiana Fournier, Lior Limonad (2026). arXiv:2606.27188
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071) - Hu Wei (2026). arXiv:2604.18071
- [At Equal Inference Cost, Multi-Agent Structure Does Not Beat a Single Frozen Agent](https://arxiv.org/abs/2609.04217) - David Dylan et al. (2026). arXiv:2609.04217
- [Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help](https://arxiv.org/abs/2610.06069) - Akshit Anchan, Nayonika Sen (2026). arXiv:2610.06069
- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](https://arxiv.org/abs/2607.25825) - Jiarun Fu et al. (2026). arXiv:2607.25825
- [Compiling Deterministic Structure into SLM Harnesses](https://arxiv.org/abs/2604.17450) - Zan Kai Chong, Hiroyuki Ohsaki, Bryan Ng (2026). arXiv:2604.17450
- [Design and Cross-Domain Evaluation of an Agent Execution Harness](https://arxiv.org/abs/2610.25568) - Saurav Joshi et al. (2026). arXiv:2610.25568
- [DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration](https://arxiv.org/abs/2610.11299) - Yingda Shen et al. (2026). arXiv:2610.11299
- [Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction](https://arxiv.org/abs/2610.04137) - Som Sagar et al. (2026). arXiv:2610.04137
- [Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.19799) - Seojin Hwang, Youngmin Choi, Hwanhee Lee (2026). arXiv:2610.19799
- [Federation over Harness](https://arxiv.org/abs/2610.24007) - Dixi Yao, Tahseen Rabbani, Tian Li (2026). arXiv:2610.24007
- [From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills](https://arxiv.org/abs/2611.08905) - Wenkai Yu et al. (2026). arXiv:2611.08905
- [Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses](https://arxiv.org/abs/2608.29641) - Xinke Jiang et al. (2026). arXiv:2608.29641
- [Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination](https://arxiv.org/abs/2610.05382) - Shanyong Wang et al. (2026). arXiv:2610.05382
- [HarnessNet: Feedback-driven Hierarchical Joint Harness Evolution for Multi-agent Systems](https://arxiv.org/abs/2610.15221) - Zhaoyuan Qiu et al. (2026). arXiv:2610.15221
- [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396) - Jianing Wang et al. (2026). arXiv:2605.02396
- [How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) - Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé (2026). arXiv:2609.40303
- [MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution](https://arxiv.org/abs/2609.38349) - Prithwish Jana et al. (2026). arXiv:2609.38349
- [MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks](https://arxiv.org/abs/2611.15754) - Daniela Gottesman et al. (2026). arXiv:2611.15754
- [PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation](https://arxiv.org/abs/2605.05258) - Yuchen Wang, Zhongzhi Luan (2026). arXiv:2605.05258
- [QueenBee: A Recursively Self-Improving Harness for Communication Topology Design in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2606.27492) - Congjia Tian, Yuhang Yao, Jiaming Cui (2026). arXiv:2606.27492
- [RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models](https://arxiv.org/abs/2609.39551) - Zheng Chen et al. (2026). arXiv:2609.39551
- [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439) - EverMind AI (2026). arXiv:2609.33439
- [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643) - Elias Lumer et al. (2026). arXiv:2606.13643
- [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](https://arxiv.org/abs/2601.12307) - Jiawei Xu et al. (2026). arXiv:2601.12307
- [SemaClaw: A Step Towards General-Purpose Personal AI Agents through Harness Engineering](https://arxiv.org/abs/2604.11548) - Ningyan Zhu et al. (2026). arXiv:2604.11548
- [SKIMIX: Multi-Agent Harness-Time Scaling with Skill Mixture for Dynamic Harness Engineering](https://arxiv.org/abs/2607.27994) - Jia Luo (2026). arXiv:2607.27994
- [Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2609.09233) - Wasu Top Piriyakulkij et al. (2026). arXiv:2609.09233
- [Synthesizing Multi-Agent Harnesses for Vulnerability Discovery](https://arxiv.org/abs/2604.20801) - Hanzhi Liu et al. (2026). arXiv:2604.20801
- [Test-Time Compute Scales Better with Parallel Agent Teams](https://arxiv.org/abs/2611.09798) - Junlin Wang et al. (2026). arXiv:2611.09798
- [Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?](https://arxiv.org/abs/2605.28334) - Víctor Mayoral-Vilches et al. (2026). arXiv:2605.28334
- [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) - Aditya Oke et al. (2026). arXiv:2610.31831
- [Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060) - Priya Pitre et al. (2026). arXiv:2610.32060
- [Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution](https://arxiv.org/abs/2606.25514) - Yang Chen et al. (2026). arXiv:2606.25514
- [When Messages Go Wrong: Understanding Communication Faults in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.15459) - Jinhao Zhou et al. (2026). arXiv:2610.15459
- [When Sub-Agents Work in Parallel: The Promises and Pitfalls of Dynamic Concurrency in Long-Horizon Coding Tasks](https://arxiv.org/abs/2610.10263) - Han Li et al. (2026). arXiv:2610.10263
- [When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration](https://arxiv.org/abs/2609.36855) - Yaxin Gong et al. (2026). arXiv:2609.36855
- [Agent2Agent (A2A) Protocol Specification](https://a2a-protocol.org/latest/specification/) - The Linux Foundation (2025).
- [AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement](https://arxiv.org/abs/2502.00757) - J Rosser, Jakob Foerster (2025). arXiv:2502.00757
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents) - Anthropic (2025).
- [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://arxiv.org/abs/2508.17536) - Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li (2025). arXiv:2508.17536
- [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) - Walden Yan (2025).
- [FlowForge: Guiding the Creation of Multi-agent Workflows with Design Space Visualization as a Thinking Scaffold](https://arxiv.org/abs/2507.15559) - Pan Hao et al. (2025). arXiv:2507.15559
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) - Anthropic (2025).
- [Multi-agent Architecture Search via Agentic Supernet](https://arxiv.org/abs/2502.04180) - Guibin Zhang et al. (2025). arXiv:2502.04180
- [Single-agent or Multi-agent Systems? Why Not Both?](https://arxiv.org/abs/2505.18286) - Mingyan Gao et al. (2025). arXiv:2505.18286
- [Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity](https://arxiv.org/abs/2502.08788) - Hangfan Zhang et al. (2025). arXiv:2502.08788
- [Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate](https://arxiv.org/abs/2509.05396) - Andrea Wynn, Harsh Satija, Gillian Hadfield (2025). arXiv:2509.05396
- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) - Yubin Kim et al. (2025). arXiv:2512.08296
- [Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors](https://arxiv.org/abs/2504.04785) - Fan Nie et al. (2025). arXiv:2504.04785
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) - Mert Cemri et al. (2025). arXiv:2503.13657
- [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) - Jiayi Zhang et al. (2024). arXiv:2410.10762
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489) - Chunqiu Steven Xia et al. (2024). arXiv:2407.01489
- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) - Shengran Hu, Cong Lu, Jeff Clune (2024). arXiv:2408.08435
- [Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823) - Mingchen Zhuge et al. (2024). arXiv:2402.16823
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) - Qingyun Wu et al. (2023). arXiv:2308.08155
- [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) - Guohao Li et al. (2023). arXiv:2303.17760
- [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) - Chen Qian et al. (2023). arXiv:2307.07924
- [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) - Sirui Hong et al. (2023). arXiv:2308.00352

#### Observability and extension

- [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811) - Wendy Zheng et al. (2026). arXiv:2610.28811
- [Agent Harness Awareness: Turning Verified Telemetry into Operational Control for Tool-Using Agents](https://arxiv.org/abs/2611.05391) - Manu Agrawal, Shrey Nagpal (2026). arXiv:2611.05391
- [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/abs/2607.18754) - Kunlun Zhu et al. (2026). arXiv:2607.18754
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850) - Jiahang Lin et al. (2026). arXiv:2604.25850
- [FreeForm Harness: A Mobile-Native Agent Harness for Open and Composable Extensions](https://arxiv.org/abs/2611.04579) - Bo Zhang et al. (2026). arXiv:2611.04579
- [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324) - Mengzhuo Chen et al. (2026). arXiv:2606.06324
- [Harness Self-Evolution for Long-Horizon Terminal Agents](https://arxiv.org/abs/2610.27435) - Ruhan Wang et al. (2026). arXiv:2610.27435
- [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](https://arxiv.org/abs/2608.24271) - Zahra Seyedghorban et al. (2026). arXiv:2608.24271
- [On the Maintenance and Co-evolution of Agent Plugins: An Empirical Study of Claude Code Plugin Marketplaces](https://arxiv.org/abs/2608.28497) - Ahmed Hereiz et al. (2026). arXiv:2608.28497
- [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) - OpenTelemetry Authors (2026).
- [PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins](https://arxiv.org/abs/2609.32423) - Yaorui Shi et al. (2026). arXiv:2609.32423
- [Tracing the Messy Middle: A Runtime Transaction Schema for AI Coding Agents](https://arxiv.org/abs/2611.23234) - Yuelin Hou et al. (2026). arXiv:2611.23234
- [Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations](https://arxiv.org/abs/2610.08364) - Toby D. Pilditch et al. (2026). arXiv:2610.08364
- [Abduct, Act, Predict: Scaffolding Causal Inference for Automated Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2509.10401) - Alva West et al. (2025). arXiv:2509.10401
- [Interactive Debugging and Steering of Multi-Agent AI Systems](https://arxiv.org/abs/2503.02068) - Will Epperson et al. (2025). arXiv:2503.02068
- [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212) - Shaokun Zhang et al. (2025). arXiv:2505.00212
- [Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents](https://arxiv.org/abs/2411.03455) - Benjamin Rombaut et al. (2024). arXiv:2411.03455

#### Whole-harness systems

- [Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](https://arxiv.org/abs/2611.24924) - Jiahang Lin et al. (2026). arXiv:2611.24924
- [Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3](https://arxiv.org/abs/2610.30499) - Jens Lehmann, Sahar Vahdati (2026). arXiv:2610.30499
- [CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents](https://arxiv.org/abs/2609.22247) - Xinlu Zhang et al. (2026). arXiv:2609.22247
- [Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives](https://arxiv.org/abs/2609.38912) - Peng Kuang et al. (2026). arXiv:2609.38912
- [DemoEvolve: Demonstration-Guided Harness Evolution under Sparse Feedback](https://arxiv.org/abs/2605.24539) - Lirong Che et al. (2026). arXiv:2605.24539
- [Divide, Diagnose, and Compose: Optimizing Agentic Pipelines and Harnesses](https://arxiv.org/abs/2611.08723) - Divij Handa et al. (2026). arXiv:2611.08723
- [DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution](https://arxiv.org/abs/2607.26722) - Hanghui Guo et al. (2026). arXiv:2607.26722
- [Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents](https://arxiv.org/abs/2609.11677) - Ruiqing Yue et al. (2026). arXiv:2609.11677
- [Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization](https://arxiv.org/abs/2610.27889) - Younghyun Kim et al. (2026). arXiv:2610.27889
- [EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement](https://arxiv.org/abs/2608.04968) - Jun Nie et al. (2026). arXiv:2608.04968
- [Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815) - Jingzhe Liu et al. (2026). arXiv:2610.28815
- [Harness Learning Enables Generalizable Test-Time Adaptation](https://arxiv.org/abs/2609.35738) - Alvin Zhang et al. (2026). arXiv:2609.35738
- [Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458) - Fei Bai et al. (2026). arXiv:2610.29458
- [Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions](https://arxiv.org/abs/2607.03935) - Haochen Luo et al. (2026). arXiv:2607.03935
- [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276) - Shuai Shao et al. (2026). arXiv:2608.02276
- [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) - Haoran Ye et al. (2026). arXiv:2609.24974
- [Harness^2: Recursive Agent Harnessing for an Open World](https://arxiv.org/abs/2610.14224) - Ruiyao Xu et al. (2026). arXiv:2610.14224
- [HarnessBandit: Joint Learnability-Transferability Scheduling for Multi-Harness Agentic Reinforcement Learning](https://arxiv.org/abs/2609.13739) - Hongliang Wei et al. (2026). arXiv:2609.13739
- [HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution](https://arxiv.org/abs/2607.13683) - Xiaotian Luo et al. (2026). arXiv:2607.13683
- [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254) - Zhi Hong et al. (2026). arXiv:2611.06254
- [HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems](https://arxiv.org/abs/2606.01779) - Mingju Chen et al. (2026). arXiv:2606.01779
- [HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249) - Tingyang Chen et al. (2026). arXiv:2606.14249
- [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042) - Sudipta Paul et al. (2026). arXiv:2610.30042
- [Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses](https://arxiv.org/abs/2608.08466) - Tailin Zhou (2026). arXiv:2608.08466
- [HM-ROUTER: Joint Model and Harness Routing for Agentic Systems](https://arxiv.org/abs/2609.32213) - Hao Mark Chen et al. (2026). arXiv:2609.32213
- [JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution](https://arxiv.org/abs/2608.25593) - Guibin Zhang et al. (2026). arXiv:2608.25593
- [Learning from Research: Toward Lifelong Agent Harness Evolution](https://arxiv.org/abs/2609.40169) - Jingbo Yang et al. (2026). arXiv:2609.40169
- [MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2610.28201) - Yu Cui et al. (2026). arXiv:2610.28201
- [MESH-Harness: Self-Improving Agent Harnesses via Bandit-Guided Compositional Evolution](https://arxiv.org/abs/2610.05300) - Zhiwei Shang et al. (2026). arXiv:2610.05300
- [MoMHa: Multi-Objective Optimization of LLM Harnesses over Accuracy, Safety, and Tokens](https://arxiv.org/abs/2609.30967) - Subhojyoti Mukherjee, Md Mehrab Tanjim (2026). arXiv:2609.30967
- [More Programs or More Rolls? Separating Coverage from Specialization in LLM Harnesses](https://arxiv.org/abs/2609.35873) - Ziyang Xu et al. (2026). arXiv:2609.35873
- [Multi-Task Self-Evolving Harnesses with the Agent as Its Own Optimizer](https://arxiv.org/abs/2609.38372) - Qiankai Xu (2026). arXiv:2609.38372
- [ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost](https://arxiv.org/abs/2611.02079) - Xingzhi Qian et al. (2026). arXiv:2611.02079
- [RobustSGPO: Search-Space Control for Agent Harness Evolution](https://arxiv.org/abs/2609.09646) - Zibo Zhao et al. (2026). arXiv:2609.09646
- [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) - Peng Xia et al. (2026). arXiv:2609.24972
- [SHarP: Saliency-based Pruning of Agent Harnesses](https://arxiv.org/abs/2610.04178) - Xinyi Gao et al. (2026). arXiv:2610.04178
- [VACE: Validation-Gated Alternating Co-Evolution of Agent Models and Harnesses](https://arxiv.org/abs/2609.37105) - Jiexing Qi et al. (2026). arXiv:2609.37105
- [VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](https://arxiv.org/abs/2610.19424) - Zihao Lin et al. (2026). arXiv:2610.19424
- [When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483) - Shao Zhang et al. (2026). arXiv:2610.32483
- [Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?](https://arxiv.org/abs/2610.37276) - Sichun Luo et al. (2026). arXiv:2610.37276

### By use case

#### Software engineering

- [ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization](https://arxiv.org/abs/2610.00906) - Sungho Park et al. (2026). arXiv:2610.00906
- [Automatic Harness Evolution for Hardware Design Verification: Can LLMs Consolidate Gains Across Discovered Harnesses?](https://arxiv.org/abs/2609.28908) - Kidus Seyoum, Ajay Mittur (2026). arXiv:2609.28908
- [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](https://arxiv.org/abs/2608.23041) - Sungho Park et al. (2026). arXiv:2608.23041
- [Beyond the Model: Demystifying Harness Effects in Software Engineering Agents](https://arxiv.org/abs/2609.32459) - Haichuan Hu et al. (2026). arXiv:2609.32459
- [BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization](https://arxiv.org/abs/2611.09218) - Yuhao Tan et al. (2026). arXiv:2611.09218
- [CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469) - Jianwen Chen et al. (2026). arXiv:2610.36469
- [CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution](https://arxiv.org/abs/2610.10426) - Jixuan Chen et al. (2026). arXiv:2610.10426
- [DarwinX: Evolving Agent Harnesses Through Natural Selection](https://arxiv.org/abs/2608.07545) - Yifan Zhang et al. (2026). arXiv:2608.07545
- [Don't Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality](https://arxiv.org/abs/2607.03691) - Oussama Ben Sghaier et al. (2026). arXiv:2607.03691
- [Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/abs/2610.13025) - Chejian Xu et al. (2026). arXiv:2610.13025
- [Finding the Right Fit: Model-Harness Interactions across Agent Tasks](https://arxiv.org/abs/2610.00917) - Yixuan Li et al. (2026). arXiv:2610.00917
- [Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses](https://arxiv.org/abs/2610.15150) - Weichen Yu et al. (2026). arXiv:2610.15150
- [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems](https://arxiv.org/abs/2609.00006) - Paul Barbaste et al. (2026). arXiv:2609.00006
- [Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable](https://arxiv.org/abs/2607.13285) - Ruhan Wang et al. (2026). arXiv:2607.13285
- [Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite](https://arxiv.org/abs/2609.11987) - Mohsen Arjmandi (2026). arXiv:2609.11987
- [Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277) - Kangning Zhang et al. (2026). arXiv:2611.04277
- [HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses](https://arxiv.org/abs/2608.01918) - Luan Zhang et al. (2026). arXiv:2608.01918
- [How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation](https://arxiv.org/abs/2610.34938) - Christoph Treude, Sebastian Baltes (2026). arXiv:2610.34938
- [MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/abs/2607.14159) - Yue Huang et al. (2026). arXiv:2607.14159
- [Meta$^2$: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents](https://arxiv.org/abs/2611.05139) - Lingzhi Yuan et al. (2026). arXiv:2611.05139
- [Meta-Engineering Harnesses for AI-Native Software Production: A Contract-Driven Adversarial Verification Architecture with Early Deployment Report](https://arxiv.org/abs/2605.25665) - Satadru Sengupta, Tamunokorite Briggs, Ivan Myshakivskyi (2026). arXiv:2605.25665
- [Mixture of Self-Improving Branches For Agent Harness Optimization](https://arxiv.org/abs/2609.37834) - Haoyu Dong et al. (2026). arXiv:2609.37834
- [Multi-Harness Reinforcement Learning for Coding Agents: Training Gains and Harness Dependence](https://arxiv.org/abs/2609.04518) - Chenqian Le et al. (2026). arXiv:2609.04518
- [openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents](https://arxiv.org/abs/2608.27969) - Tao Yu et al. (2026). arXiv:2608.27969
- [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) - Seth Karten et al. (2026). arXiv:2608.23552
- [Prompt-Induced Waste in Coding Agents: Reasoning, Effort, Harness Design, and End-to-End Cost](https://arxiv.org/abs/2608.01347) - Sarel Weinberger, Amir Hozez (2026). arXiv:2608.01347
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227) - Yike Wang et al. (2026). arXiv:2607.12227
- [Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791) - Zhepei Wei et al. (2026). arXiv:2610.22791
- [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) - Hangfan Zhang et al. (2026). arXiv:2606.09498
- [SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation](https://arxiv.org/abs/2608.18565) - Yanlun Tu et al. (2026). arXiv:2608.18565
- [The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses](https://arxiv.org/abs/2608.23953) - Dai Jiahong (2026). arXiv:2608.23953
- [The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://arxiv.org/abs/2607.22585) - Naman Vats, Oleg Golev (2026). arXiv:2607.22585
- [Turbo Harness: Instance-Adaptive Harness Optimization](https://arxiv.org/abs/2609.40330) - Tunyu Zhang et al. (2026). arXiv:2609.40330
- [What Does a Harness Buy? Tokens, Mostly](https://arxiv.org/abs/2610.04433) - Yangze Liu, Zhongyi Han (2026). arXiv:2610.04433

#### Web and computer use

- [Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing](https://arxiv.org/abs/2610.33636) - Arsham Gholamzadeh Khoee et al. (2026). arXiv:2610.33636

#### Science and research

- [AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness](https://arxiv.org/abs/2610.05367) - Prithwish Jana et al. (2026). arXiv:2610.05367
- [Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling](https://arxiv.org/abs/2608.23653) - Zizhe Wang (2026). arXiv:2608.23653
- [CAX-Agent: A Lightweight Agent Harness for Reliable APDL Automation](https://arxiv.org/abs/2605.15218) - Chenying Lin et al. (2026). arXiv:2605.15218
- [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/abs/2607.22688) - Zhengyu Chen et al. (2026). arXiv:2607.22688
- [DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery](https://arxiv.org/abs/2610.23791) - Yuxing Chen et al. (2026). arXiv:2610.23791
- [KISS - Knowledge Infrastructure for Scientific Simulation: A Scaffolding for Agentic Earth Science](https://arxiv.org/abs/2605.17856) - Ziwei Li et al. (2026). arXiv:2605.17856
- [MarkovSim: an LLM Agent Harness with Bounded Context for Long-Horizon Computational Simulation](https://arxiv.org/abs/2610.35349) - Yeui-Lung Lei, Wen-Bo Chen, Pan Zhang (2026). arXiv:2610.35349
- [ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](https://arxiv.org/abs/2610.24744) - Jinxiang Xie et al. (2026). arXiv:2610.24744
- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983) - Honghao Lin et al. (2026). arXiv:2609.15983
- [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](https://arxiv.org/abs/2607.11423) - Junhao Ruan et al. (2026). arXiv:2607.11423

#### Data and ML engineering

- [AION: Next-Generation Tasks and Practical Harness for Time Series](https://arxiv.org/abs/2605.25045) - Tianxiang Zhan et al. (2026). arXiv:2605.25045
- [Automated Discovery Has No Universally Superior Harness](https://arxiv.org/abs/2607.18235) - Akshat Gupta et al. (2026). arXiv:2607.18235
- [DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://arxiv.org/abs/2608.28590) - Fan Liu, Hao Liu (2026). arXiv:2608.28590
- [RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization](https://arxiv.org/abs/2610.35316) - Jiawei Lu et al. (2026). arXiv:2610.35316
- [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) - Prannay Hebbar et al. (2026). arXiv:2605.27276

#### Embodied agents and robotics

- [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/abs/2606.14674) - Jixuan Chen et al. (2026). arXiv:2606.14674
- [Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560) - Jiarui Yuan et al. (2026). arXiv:2611.01560
- [EMHO: EMbodied Agent Harness Optimization via Experience Traces](https://arxiv.org/abs/2610.08432) - Hyun Jung Lee et al. (2026). arXiv:2610.08432
- [Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents](https://arxiv.org/abs/2609.39304) - Zhijie Wei et al. (2026). arXiv:2609.39304
- [TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216) - Kehong Gong et al. (2026). arXiv:2610.41216
- [Towards the Harness of Embodied Agents](https://arxiv.org/abs/2608.11246) - Qi Wang et al. (2026). arXiv:2608.11246

#### Enterprise and operations

- [Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation](https://arxiv.org/abs/2607.08938) - Chenyang Yang et al. (2026). arXiv:2607.08938
- [CORAL: An LLM-Native Harness for Production Recommender Systems](https://arxiv.org/abs/2609.02730) - Muhammad Rafay Azhar et al. (2026). arXiv:2609.02730
- [From General Agents to RCA Experts: A Self-Evolving Harness for Root Cause Analysis](https://arxiv.org/abs/2608.25661) - Haiyu Huang et al. (2026). arXiv:2608.25661
- [KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents](https://arxiv.org/abs/2610.39884) - Xinhua Miao et al. (2026). arXiv:2610.39884
- [Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design](https://arxiv.org/abs/2610.28380) - Gaotang Li et al. (2026). arXiv:2610.28380
- [Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434) - Shai Nahum Gefen et al. (2026). arXiv:2611.03434
- [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](https://arxiv.org/abs/2607.06906) - Muayad Sayed Ali et al. (2026). arXiv:2607.06906
- [Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763) - TaoLive AIGC LLM Team et al. (2026). arXiv:2608.15763

#### Healthcare

- [MammoClaw: Towards Skill-Evolving Agent Harness for Breast Cancer Mammography Analysis](https://arxiv.org/abs/2609.31789) - Krishna Kanth Nakka (2026). arXiv:2609.31789
- [What Does a Harness Repair? Four Preregistered Studies Around a Longevity-Tuned Language Model](https://arxiv.org/abs/2610.05533) - Bowen Xu, Boyu Chen (2026). arXiv:2610.05533

#### Finance

- [The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116) - Mehmet Murat Huyut (2026). arXiv:2611.06116

#### Creative media

- [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560) - Yaxin Luo et al. (2026). arXiv:2608.13560
- [AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation](https://arxiv.org/abs/2609.35530) - Yuta Oshima et al. (2026). arXiv:2609.35530
- [EvoGen-Harness: Learning Where and How to Evolve Image-Generation Harnesses](https://arxiv.org/abs/2610.00383) - Jiabin Luo et al. (2026). arXiv:2610.00383
- [VIVID: A Visual Harness for Agentic Video Editing](https://arxiv.org/abs/2611.20688) - Wenhan Yu et al. (2026). arXiv:2611.20688

#### Security operations

- [MetaVul: Agentic Harness Discovery for Vulnerability Detection](https://arxiv.org/abs/2610.40721) - Ira Ceka et al. (2026). arXiv:2610.40721

#### General and cross-domain

- [EnterpriseBench: Benchmarking LLM Agents on Enterprise-Level Strategic Reasoning and Decision-Making](https://arxiv.org/abs/2609.37658) - Min Yang et al. (2026). arXiv:2609.37658
- [From Delegation to Action Approval: An Exploratory Study of Developers' Practices in Collaborating with AI Coding Agents](https://arxiv.org/abs/2611.10058) - Yinan Wu et al. (2026). arXiv:2611.10058
- [Hidden in Plain Sight: an Empirical Study about The Instruction Stacks of Coding Agents](https://arxiv.org/abs/2610.37332) - Felipe de Sant'Anna Paixão et al. (2026). arXiv:2610.37332
- [How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions](https://arxiv.org/abs/2605.29442) - Ningzhi Tang et al. (2026). arXiv:2605.29442
- [SREGym: A Live Benchmark for AI SRE Agents with High-Fidelity Failure Scenarios](https://arxiv.org/abs/2605.07161) - Jackson Clark et al. (2026). arXiv:2605.07161
- [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868) - Mike A. Merrill et al. (2026). arXiv:2601.11868
- [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227) - Samuel Schmidgall et al. (2025). arXiv:2501.04227
- [AIDE: AI-Driven Exploration in the Space of Code](https://arxiv.org/abs/2502.13138) - Zhengyao Jiang et al. (2025). arXiv:2502.13138
- [An Illusion of Progress? Assessing the Current State of Web Agents](https://arxiv.org/abs/2504.01382) - Tianci Xue et al. (2025). arXiv:2504.01382
- [Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows](https://arxiv.org/abs/2509.04198) - Petr Průcha, Michaela Matoušková, Jan Strnad (2025). arXiv:2509.04198
- [CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions](https://arxiv.org/abs/2505.18878) - Kung-Hsiang Huang et al. (2025). arXiv:2505.18878
- [DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](https://arxiv.org/abs/2506.11763) - Mingxuan Du et al. (2025). arXiv:2506.11763
- [ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks](https://arxiv.org/abs/2502.05352) - Saurabh Jha et al. (2025). arXiv:2502.05352
- [MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692) - Jaehyun Nam et al. (2025). arXiv:2506.15692
- [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848) - Giulio Starace et al. (2025). arXiv:2504.01848
- [R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science](https://arxiv.org/abs/2505.14738) - Xu Yang et al. (2025). arXiv:2505.14738
- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/abs/2509.16941) - Xiang Deng et al. (2025). arXiv:2509.16941
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066) - Yutaro Yamada et al. (2025). arXiv:2504.08066
- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164) - Saaket Agashe et al. (2024). arXiv:2410.08164
- [Data Interpreter: An LLM Agent For Data Science](https://arxiv.org/abs/2402.18679) - Sirui Hong et al. (2024). arXiv:2402.18679
- [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703) - Liqiang Jing et al. (2024). arXiv:2409.07703
- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) - Boyuan Zheng et al. (2024). arXiv:2401.01614
- [Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks](https://arxiv.org/abs/2411.04468) - Adam Fourney et al. (2024). arXiv:2411.04468
- [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095) - Jun Shern Chan et al. (2024). arXiv:2410.07095
- [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080) - Ziru Chen et al. (2024). arXiv:2410.05080
- [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://arxiv.org/abs/2411.07763) - Fangyu Lei et al. (2024). arXiv:2411.07763
- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://arxiv.org/abs/2410.06703) - Ido Levy et al. (2024). arXiv:2410.06703
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) - Chris Lu et al. (2024). arXiv:2408.06292
- [TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161) - Frank F. Xu et al. (2024). arXiv:2412.14161
- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) - Hongliang He et al. (2024). arXiv:2401.13919
- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718) - Alexandre Drouin et al. (2024). arXiv:2403.07718
- [MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302) - Qian Huang et al. (2023). arXiv:2310.03302
- [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) - Jacky Liang et al. (2022). arXiv:2209.07753
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) - Michael Ahn et al. (2022). arXiv:2204.01691

### Foundations and other cited work

- [Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](https://arxiv.org/abs/2604.14228) - Jiacheng Liu et al. (2026). arXiv:2604.14228
- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) - Mitchell Hashimoto (2026).
- [Understanding the Architecture of Coding Agents: An Exploratory Study Using a Research Prototype](https://arxiv.org/abs/2608.10934) - Marco Tulio Valente (2026). arXiv:2608.10934
- [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](https://arxiv.org/abs/2601.04748) - Xiaoxiao Li (2026). arXiv:2601.04748
- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) - Maxime Robeyns, Martin Szummer, Laurence Aitchison (2025). arXiv:2504.15228
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) - Alexander Novikov et al. (2025). arXiv:2506.13131
- [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) - Jenny Zhang et al. (2025). arXiv:2505.22954
- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) - Lakshya A Agrawal et al. (2025). arXiv:2507.19457
- [Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies](https://arxiv.org/abs/2502.02533) - Han Zhou et al. (2025). arXiv:2502.02533
- [Recursive Language Models](https://arxiv.org/abs/2512.24601) - Alex L. Zhang, Tim Kraska, Omar Khattab (2025). arXiv:2512.24601
- [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs](https://arxiv.org/abs/2406.11695) - Krista Opsahl-Ong et al. (2024). arXiv:2406.11695
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) - Mert Yuksekgonul et al. (2024). arXiv:2406.07496
- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) - Omar Khattab et al. (2023). arXiv:2310.03714
- [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) - Yecheng Jason Ma et al. (2023). arXiv:2310.12931
- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) - Chengrun Yang et al. (2023). arXiv:2309.03409
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) - Akari Asai et al. (2023). arXiv:2310.11511
- [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) - Eric Zelikman et al. (2023). arXiv:2310.02304

## Harness repositories

Sorted by stars within each category. Stars and last push from the GitHub API.

### MCP servers, clients and registries

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 98.2k | MIT | 2026-11-17 | A collection of MCP servers. |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 92.1k | NOASSERTION | 2026-11-19 | Model Context Protocol Reference Servers |
| [upstash/context7](https://github.com/upstash/context7) | 65.1k | MIT | 2026-11-19 | Context7 Platform -- Up-to-date docs for AI agents |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 58.3k | Apache-2.0 | 2026-11-19 | Chrome DevTools for coding agents |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 39.9k | Apache-2.0 | 2026-11-18 | Playwright MCP server |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 35.0k | MIT | 2026-11-18 | Community plugin to control Blender 3D with any LLM of your choice. Not affiliated with the official Blender Foundation. |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 34.6k | MIT | 2026-11-19 | GitHub's official MCP Server |
| [oraios/serena](https://github.com/oraios/serena) | 31.5k | NOASSERTION | 2026-11-19 | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 28.7k | Apache-2.0 | 2026-11-19 | 🚀 The fast, Pythonic way to build MCP servers and clients. |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24.9k | MIT | 2026-11-17 | The official Python SDK for Model Context Protocol servers and clients |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 23.3k | MIT | 2026-11-19 | MCP server that lets Claude, ChatGPT, Cursor and other AI assistants operate n8n: debug, edit, validate, test and build workflows on any n8n instance |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | 17.7k | MIT | 2026-11-13 | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. |
| [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | 17.0k | MIT | 2026-11-19 | The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store. |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | 16.9k | Apache-2.0 | 2026-11-19 | MCP Toolbox for Databases is an open source MCP server for databases. |
| [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | 16.3k | MIT | 2026-11-15 | MCP server to provide Figma layout information to AI coding agents like Cursor |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 13.8k | NOASSERTION | 2026-11-19 | The official TypeScript SDK for Model Context Protocol servers and clients |
| [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | 13.5k | MIT | 2026-11-12 | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | 11.3k | NOASSERTION | 2026-11-18 | Deterministic testing tools for MCP servers |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | 11.0k | MIT | 2026-11-19 | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents. |
| [awslabs/mcp](https://github.com/awslabs/mcp) | 9.9k | Apache-2.0 | 2026-11-19 | Open source MCP Servers for AWS |
| [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.7k | NOASSERTION | 2026-11-19 | Specification and documentation for the Model Context Protocol |
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | 9.2k | MIT | 2026-11-19 | A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools. |
| [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.6k | Apache-2.0 | 2026-01-25 | Build effective agents using Model Context Protocol and simple workflow patterns |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | 7.5k | NOASSERTION | 2026-11-18 | A community driven registry service for Model Context Protocol (MCP) servers. |
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | 5.4k | NOASSERTION | 2026-11-17 | The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google. |
| [MCP-UI-Org/mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | 5.3k | Apache-2.0 | 2026-09-16 | UI over MCP. Create next-gen UI experiences with the protocol and SDK! |
| [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) | 4.9k | Apache-2.0 | 2026-11-19 | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins. |
| [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | 4.1k | NOASSERTION | 2026-11-17 | The official Rust SDK for the Model Context Protocol |
| [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) | 3.1k | NOASSERTION | 2026-11-10 | Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers |
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | 1.6k | MIT | 2026-10-26 | docker mcp CLI plugin / MCP Gateway |

### Browser and computer-use agents

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 203.8k | AGPL-3.0 | 2026-11-19 | Knowledge infrastructure to make your agents smarter. Search, scrape and 550+ data providers through one API. |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 121.5k | MIT | 2026-11-19 | Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API. |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 87.6k | Apache-2.0 | 2026-11-19 | Official Crawl4AI Cloud: a hosted web scraping, extraction, and search API for AI agents. Free API key, 1,000 credits a month, no card. Fully open source: this repo is the Apache-2.0 crawler that powers it, and you can self-host it. |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 52.8k | Apache-2.0 | 2026-11-19 | Browser automation CLI for AI agents |
| [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | 42.2k | AGPL-3.0 | 2026-11-19 | Lightpanda: the headless browser designed for AI and automation |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | 36.5k | Apache-2.0 | 2026-11-19 | The headless browser for AI agents and web scraping |
| [trycua/cua](https://github.com/trycua/cua) | 32.7k | MIT | 2026-11-19 | Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes, and benchmarks for training, evaluation, and data generation. |
| [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | 31.2k | Apache-2.0 | 2026-11-07 | Make Any Website into CLI & Use your logged-in browser by AI agent. |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | 29.7k | MIT | 2026-11-18 | JavaScript in-page GUI agent. Control web interfaces with natural language. |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | 27.7k | GPL-3.0 | 2026-11-17 | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. |
| [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | 26.6k | Apache-2.0 | 2026-03-06 | An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | 26.1k | MIT | 2026-11-19 | The SDK to extract data and interact with any site on the web. Get started with Claude Code, Codex, Eve, Mastra, and more. |
| [microsoft/OmniParser](https://github.com/microsoft/OmniParser) | 25.6k | CC-BY-4.0 | 2026-11-14 | A simple screen parsing tool towards pure vision based GUI agent |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 25.5k | Apache-2.0 | 2026-11-18 | Computer use CLI for AI agents |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 24.7k | MIT | 2026-11-11 | Fastest and cheapest web agent |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | 23.5k | AGPL-3.0 | 2026-11-19 | Automate browser based workflows with AI |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 21.1k | MIT | 2026-11-06 | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) | 15.6k | MIT | 2026-11-19 | See interfaces like a human. E2E testing in natural language. |
| [browseros-ai/BrowserOS](https://github.com/browseros-ai/BrowserOS) | 14.4k | AGPL-3.0 | 2026-11-19 | 🌐 The open-source Agentic browser; alternative to ChatGPT Atlas, Perplexity Comet, Dia. |
| [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser) | 14.3k | Apache-2.0 | 2026-11-17 | Open-source AI agent for web automation. Use your real, logged-in browser to automate daily tasks. |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | 13.0k | Apache-2.0 | 2026-11-13 | Agent S: the state-of-the-art open source computer use agents |
| [OthersideAI/self-operating-computer](https://github.com/OthersideAI/self-operating-computer) | 10.3k | MIT | 2026-10-19 | A framework to enable a multimodal model to operate a computer. |
| [microsoft/UFO](https://github.com/microsoft/UFO) | 10.2k | MIT | 2026-10-30 | UFO³: Weaving the Digital Agent Galaxy |
| [droidrun/mobilerun](https://github.com/droidrun/mobilerun) | 10.1k | MIT | 2026-11-18 | Automate your mobile devices with natural language commands - an LLM agnostic mobile Agent 🤖 |
| [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | 9.4k | MIT | 2026-11-03 | Mobile-Agent: The Powerful GUI Agent Family |
| [steel-dev/steel-browser](https://github.com/steel-dev/steel-browser) | 8.0k | Apache-2.0 | 2026-11-19 | 🔥 Open Source Browser API for AI Agents & Apps. Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure. |
| [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview) | 3.3k | Apache-2.0 | 2026-07-28 |  |
| [openai/openai-cua-sample-app](https://github.com/openai/openai-cua-sample-app) | 1.9k | MIT | 2026-10-19 | Learn how to use CUA (our Computer Using Agent) via the API on multiple computer environments. |

### Coding-agent harnesses and CLIs

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 284.1k | MIT | 2026-11-18 | DeepSeek Harness: Everything is a Plugin. |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 228.0k | MIT | 2026-11-19 | The open source coding agent. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 156.3k | none | 2026-11-19 | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 155.8k | MIT | 2026-11-19 | A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io |
| [openai/codex](https://github.com/openai/codex) | 135.9k | Apache-2.0 | 2026-11-19 | Lightweight coding agent that runs in your terminal |
| [earendil-works/pi](https://github.com/earendil-works/pi) | 122.9k | MIT | 2026-11-19 | AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108.9k | Apache-2.0 | 2026-11-19 | An open-source AI agent that brings the power of Gemini directly into your terminal. |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 93.8k | MIT | 2026-11-19 | 🙌 OpenHands: AI-Driven Development |
| [cline/cline](https://github.com/cline/cline) | 71.8k | Apache-2.0 | 2026-11-19 | Autonomous coding agent as an SDK, IDE extension, or CLI assistant. |
| [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 68.9k | Apache-2.0 | 2026-11-15 | A coding agent for open models like Kimi K3.1 and GLM 5.3 |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | 66.1k | AGPL-3.0 | 2026-11-19 | Warp is an agentic development environment, born out of the terminal. |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | 56.8k | Apache-2.0 | 2026-11-19 | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 51.9k | Apache-2.0 | 2026-11-19 | the runtime your coding agents live on |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 50.2k | Apache-2.0 | 2026-05-22 | aider is AI pair programming in your terminal |
| [codewhale-hq/Codewhale](https://github.com/codewhale-hq/Codewhale) | 41.2k | MIT | 2026-11-19 | An open-source coding agent for your terminal, written in Rust. It works with any model, can split one task across several agents, and every line of it is yours to read. |
| [continuedev/continue](https://github.com/continuedev/continue) | 36.5k | Apache-2.0 | 2026-11-18 | open-source coding agent |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 30.8k | Apache-2.0 | 2026-11-19 | An open-source AI coding agent that lives in your terminal. |
| [charmbracelet/crush](https://github.com/charmbracelet/crush) | 29.1k | NOASSERTION | 2026-11-19 | Glamourous agentic coding for all 💘 |
| [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | 28.1k | MIT | 2026-11-19 | Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent. |
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 27.8k | Apache-2.0 | 2026-09-29 | SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible. |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | 20.8k | MIT | 2026-11-16 | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. \[NeurIPS 2024\] |
| [plandex-ai/plandex](https://github.com/plandex-ai/plandex) | 15.9k | MIT | 2025-10-03 | Open source AI coding agent. Designed for large projects and real world tasks. |
| [bytedance/trae-agent](https://github.com/bytedance/trae-agent) | 12.2k | MIT | 2026-02-05 | Trae Agent is an LLM-based agent for general purpose software engineering tasks. |
| [github/copilot-cli](https://github.com/github/copilot-cli) | 11.4k | NOASSERTION | 2026-11-19 | GitHub Copilot CLI brings the power of Copilot coding agent directly to your terminal. |
| [mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) | 5.4k | Apache-2.0 | 2026-11-18 | Minimal CLI coding agent by Mistral |
| [aws/amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli) | 2.0k | Apache-2.0 | 2026-08-24 | ✨ Agentic chat experience in your terminal. Build applications using natural language. |

### Context engineering and skills collections

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | 327.9k | MIT | 2026-11-19 | Skills for Real Engineers. Straight from my .agents directory. |
| [obra/superpowers](https://github.com/obra/superpowers) | 321.8k | MIT | 2026-11-03 | An agentic skills framework & software development methodology that works. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 307.0k | MIT | 2026-11-17 | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 234.4k | none | 2026-04-20 | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [anthropics/skills](https://github.com/anthropics/skills) | 197.6k | none | 2026-11-16 | Public repository for Agent Skills |
| [github/spec-kit](https://github.com/github/spec-kit) | 150.6k | MIT | 2026-11-19 | 💫 Toolkit to help you get started with SDD or any other process! |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 150.5k | Apache-2.0 | 2026-11-17 | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 144.8k | GPL-3.0 | 2026-10-12 | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 142.1k | MIT | 2026-11-19 | Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 121.5k | Apache-2.0 | 2026-11-19 | why use many token when few token do trick. Skill + local proxy for coding agents: shorter answers, smaller tool output, every original recoverable. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 119.1k | MIT | 2026-11-18 | Production-grade engineering skills for AI coding agents. |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 87.2k | Apache-2.0 | 2026-11-19 | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 80.1k | Apache-2.0 | 2026-11-19 | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 78.1k | MIT | 2026-11-19 | Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 75.3k | MIT | 2026-11-19 | Spec-driven development (SDD) for AI coding assistants. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 71.8k | CC0-1.0 | 2026-11-19 | Leaked system prompts of ChatGPT, Claude, Gemini and more. The hidden system prompt of every popular chatbot, in full, every version since May 2025. Also Anthropic Claude Code, OpenAI Codex, Google Antigravity, xAI Grok, Meta Muse, Moonshot Kimi, Alibaba Qwen, Z.ai GLM ZCode, MiniMax, Cursor, Perplexity, DeepSeek and 30+ others. Updated daily. |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 69.2k | MIT | 2026-11-19 | from vibe coding to agentic engineering - practice makes claude perfect |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 55.5k | NOASSERTION | 2026-11-19 | Breakthrough Method for Agile Ai Driven Development |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 47.7k | Apache-2.0 | 2026-11-19 | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 40.1k | MIT | 2026-11-17 | The open agent skills tool - npx skills |
| [yamadashy/repomix](https://github.com/yamadashy/repomix) | 29.3k | MIT | 2026-11-18 | 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more. |
| [openai/skills](https://github.com/openai/skills) | 28.8k | none | 2026-10-28 | Skills Catalog for Codex |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 27.5k | Apache-2.0 | 2026-11-04 | Specification and documentation for Agent Skills |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 27.3k | NOASSERTION | 2025-09-21 | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | 25.6k | MIT | 2026-09-10 | AGENTS.md — a simple, open format for guiding coding agents |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 18.4k | MIT | 2026-10-12 | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context management. |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | 13.9k | MIT | 2026-03-16 | Context engineering is the new vibe coding - it's the way to actually make AI coding assistants work. Claude Code is the best for this so that's what this repo is centered around, but you can apply this strategy with any AI coding assistant! |
| [microsoft/apm](https://github.com/microsoft/apm) | 4.4k | Apache-2.0 | 2026-11-19 | Agent Package Manager |
| [humanlayer/advanced-context-engineering-for-coding-agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | 2.8k | none | 2026-10-16 |  |

### General agent frameworks and SDKs

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 394.8k | MIT | 2026-11-19 | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 264.7k | MIT | 2026-11-19 | The agent that grows with you |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 188.1k | NOASSERTION | 2026-11-19 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. |
| [langgenius/dify](https://github.com/langgenius/dify) | 161.5k | NOASSERTION | 2026-11-19 | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack. |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 156.8k | MIT | 2026-11-19 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows. |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 149.9k | MIT | 2026-11-19 | The agent engineering platform. |
| [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) | 59.0k | MIT | 2026-11-02 | No fortress, purely open ground.  OpenManus is Coming. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 53.0k | MIT | 2026-11-14 | LlamaIndex is the document processing platform for AI |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 48.0k | MIT | 2026-11-19 | Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 45.2k | MIT | 2026-11-19 | Build resilient agents. |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 43.2k | Apache-2.0 | 2026-11-19 | The self-managing agent platform |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 42.8k | GPL-3.0 | 2026-11-18 | The fastest, cheapest, most efficient open-source agent harness. Run more than 500 agents on a $10 VPS. |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.8k | MIT | 2026-11-19 | The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more.  Makers of the AG-UI Protocol |
| [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | 38.0k | Apache-2.0 | 2026-11-19 | Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities. |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | 31.4k | MIT | 2026-11-19 | The batteries-included agent harness. |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 31.2k | MIT | 2026-11-19 | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action. |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 30.8k | MIT | 2026-11-19 | A lightweight, powerful framework for multi-agent workflows |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 30.4k | Apache-2.0 | 2026-11-18 | 🤗 smolagents: a barebones library for agents that think in code. |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | 29.6k | NOASSERTION | 2026-11-19 | Mastra is the modern TypeScript framework for AI-powered applications and agents. |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28.8k | MIT | 2026-11-19 | Integrate cutting-edge LLM technology quickly and easily into your apps |
| [vercel/ai](https://github.com/vercel/ai) | 28.1k | NOASSERTION | 2026-11-19 | The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 27.1k | Apache-2.0 | 2026-11-19 | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems. |
| [google/adk-python](https://github.com/google/adk-python) | 22.3k | Apache-2.0 | 2026-11-19 | An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 21.3k | MIT | 2026-11-19 | How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end. |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | 9.3k | Apache-2.0 | 2026-11-19 | Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 8.6k | MIT | 2026-11-19 |  |
| [cloudflare/agents](https://github.com/cloudflare/agents) | 6.0k | MIT | 2026-11-19 | Build and deploy AI Agents on Cloudflare |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) | 4.0k | MIT | 2026-11-19 | A lightweight, powerful framework for multi-agent workflows and voice agents |
| [anthropics/claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript) | 1.9k | none | 2026-11-19 |  |

### Memory systems

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 118.4k | Apache-2.0 | 2026-11-19 | Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 69.2k | Apache-2.0 | 2026-11-18 | The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production. |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 62.0k | MIT | 2026-11-19 | Hindsight: Agent Memory That Learns |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | 60.6k | MIT | 2026-11-19 | The best-benchmarked open-source AI memory system. And it's free. |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 48.9k | MIT | 2026-11-19 | Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection. |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 42.5k | AGPL-3.0 | 2026-11-19 | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills. |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 40.8k | MIT | 2026-11-19 | \[EMNLP2025\] LightRAG: Simple and Fast Retrieval-Augmented Generation |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36.7k | MIT | 2026-11-16 | A modular graph-based Retrieval-Augmented Generation (RAG) system |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 33.4k | Apache-2.0 | 2026-11-19 | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 32.9k | Apache-2.0 | 2026-11-19 | Build Real-Time Knowledge Graphs for AI Agents |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 31.7k | MIT | 2026-11-19 | Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. |
| [tobi/qmd](https://github.com/tobi/qmd) | 31.2k | MIT | 2026-11-18 | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 31.0k | NOASSERTION | 2026-11-19 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks. |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | 30.5k | Apache-2.0 | 2026-11-18 | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [gastownhall/beads](https://github.com/gastownhall/beads) | 28.8k | MIT | 2026-11-19 | Beads - A memory upgrade for your coding agent |
| [letta-ai/letta](https://github.com/letta-ai/letta) | 25.5k | Apache-2.0 | 2026-10-18 | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 17.6k | NOASSERTION | 2026-10-03 | Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for enterprise, Memori works with the data infrastructure you already run, no rip-and-replace, and deploys across managed cloud, single-tenant cloud, VPC, and on-premises. |
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 14.6k | NOASSERTION | 2026-11-19 | Personal memory across agents |
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 13.9k | Apache-2.0 | 2026-11-19 | One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows. |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 12.5k | Apache-2.0 | 2026-11-19 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | 8.2k | AGPL-3.0 | 2026-11-19 | Memory library for building stateful agents |
| [getzep/zep](https://github.com/getzep/zep) | 5.0k | Apache-2.0 | 2026-11-17 | Zep \| Examples, Integrations, & More |
| [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) | 4.6k | AGPL-3.0 | 2026-11-18 | AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN |
| [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 4.1k | MIT | 2026-10-06 | \[NeurIPS'24\] HippoRAG is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents. RAG + Knowledge Graphs + Personalized PageRank. |
| [memodb-io/memobase](https://github.com/memodb-io/memobase) | 3.0k | Apache-2.0 | 2026-01-11 | User Profile-Based Long-Term Memory for AI Chatbot Applications. |
| [langchain-ai/langmem](https://github.com/langchain-ai/langmem) | 1.8k | MIT | 2026-11-16 |  |
| [xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval) | 1.2k | MIT | 2026-05-11 | Benchmarking Chat Assistants on Long-Term Interactive Memory (ICLR 2025) |
| [agiresearch/A-mem](https://github.com/agiresearch/A-mem) | 1.2k | MIT | 2025-12-12 | A-MEM: Agentic Memory for LLM Agents |

### Multi-agent orchestration

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 169.3k | MIT | 2026-11-09 | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
| [stablyai/orca](https://github.com/stablyai/orca) | 129.6k | MIT | 2026-11-19 | Orca lets you run a fleet of coding agents (e.g. Claude Code, Codex) with your own subscription. Available on desktop, mobile and remote runtime. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 115.0k | MIT | 2026-11-19 | The open-source app everyone uses to manage agents at work |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 82.1k | MIT | 2026-11-19 | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71.4k | MIT | 2026-01-21 | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 71.0k | NOASSERTION | 2026-11-19 | OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 61.1k | MIT | 2026-11-19 | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. |
| [multica-ai/multica](https://github.com/multica-ai/multica) | 56.7k | NOASSERTION | 2026-11-19 | Make humans and AI agents work as one team — open-source and self-hostable. |
| [wshobson/agents](https://github.com/wshobson/agents) | 42.7k | MIT | 2026-11-18 | Plugins, agents, skills, and commands for Claude Code, Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi, written once in Markdown and adapted to each tool by generators with validation and evals. |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 41.0k | MIT | 2026-11-19 | Teams-first Multi-agent orchestration for Claude Code |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 36.3k | Apache-2.0 | 2026-11-19 | Build and run agents you can see, understand and trust. |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | 34.8k | Apache-2.0 | 2026-11-06 | ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | 28.7k | Apache-2.0 | 2026-11-15 | Get 10X more out of Claude Code, Codex or any coding agent |
| [openai/symphony](https://github.com/openai/symphony) | 28.1k | Apache-2.0 | 2026-09-15 | Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents. |
| [a2aproject/A2A](https://github.com/a2aproject/A2A) | 26.6k | Apache-2.0 | 2026-11-18 | Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications. |
| [slopus/happy](https://github.com/slopus/happy) | 24.7k | MIT | 2026-11-19 | Orchestrate Claude, Codex and Grok in one app. Open-source (MIT), reuses the subscriptions you already pay for. |
| [snarktank/ralph](https://github.com/snarktank/ralph) | 22.3k | MIT | 2026-02-02 | Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. |
| [openai/swarm](https://github.com/openai/swarm) | 22.2k | MIT | 2026-04-15 | Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team. |
| [camel-ai/owl](https://github.com/camel-ai/owl) | 20.2k | none | 2026-11-16 | 🦉 OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | 18.8k | MIT | 2026-11-14 | Gas Town - multi-agent workspace manager |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 18.0k | Apache-2.0 | 2026-11-16 | 🐫 CAMEL: The first and the best multi-agent framework. Finding the Scaling Law of Agents. https://www.camel-ai.org |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | 10.1k | MIT | 2026-11-16 | MagenticLite is an experimental agent that works across the browser and local file system |
| [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad) | 8.8k | AGPL-3.0 | 2026-11-13 | Manage multiple AI terminal agents like Claude Code, Codex, OpenCode, and Amp. |
| [2FastLabs/agent-squad](https://github.com/2FastLabs/agent-squad) | 7.8k | Apache-2.0 | 2026-11-11 | Flexible and powerful framework for managing multiple AI agents and handling complex conversations |
| [kyegomez/swarms](https://github.com/kyegomez/swarms) | 7.4k | Apache-2.0 | 2026-11-19 | The Enterprise-Grade Multi-Agent Orchestration Framework. Website: https://swarms.ai |
| [ag2ai/ag2](https://github.com/ag2ai/ag2) | 5.1k | Apache-2.0 | 2026-11-19 | AG2 (formerly AutoGen): The Open-Source AgentOS.Join us at: https://discord.gg/sNGSwQME3x |
| [a2aproject/a2a-python](https://github.com/a2aproject/a2a-python) | 2.2k | Apache-2.0 | 2026-11-19 | Official Python SDK for the Agent2Agent (A2A) Protocol |
| [langchain-ai/langgraph-swarm-py](https://github.com/langchain-ai/langgraph-swarm-py) | 1.6k | MIT | 2026-10-28 | For your multi-agent needs |

### Observability and tracing

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 63.5k | NOASSERTION | 2026-11-19 | The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging \[Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM\] |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 37.6k | NOASSERTION | 2026-11-19 | 🪢 Open source AI engineering platform: AI Gateway, agent observability, evals, and prompt/skill management, built on OpenTelemetry. One open platform for every AI call and every agent. Self-host or use Langfuse Cloud. |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | 28.9k | Apache-2.0 | 2026-11-19 | The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize production-quality AI applications while controlling costs and managing access to models and data. |
| [comet-ml/opik](https://github.com/comet-ml/opik) | 23.5k | Apache-2.0 | 2026-11-19 | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards. |
| [ccusage/ccusage](https://github.com/ccusage/ccusage) | 19.5k | NOASSERTION | 2026-11-19 | npx ccusage |
| [raga-ai-hub/RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16.2k | Apache-2.0 | 2026-02-11 | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboard and advanced analytics with timeline and execution graph view |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 13.4k | MIT | 2026-05-25 | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly API. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 12.4k | NOASSERTION | 2026-11-19 | AI Observability & Evaluation |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | 11.9k | MIT | 2026-11-18 | Free, local tool to track AI coding token usage and cost across 37 tools and agents (Claude Code, Cursor, Codex, Gemini and more), by model, project, and task. npx codeburn |
| [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | 9.8k | NOASSERTION | 2026-11-19 | Observability and enforcement for AI agent harnesses. Capture every run and runtime reliability with policy enforcement. |
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | 9.8k | Apache-2.0 | 2026-11-19 | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys, budgets and MCP Code Mode. Works with any SDK or agent and adds under 200µs of overhead at 5k RPS. |
| [Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 8.8k | MIT | 2026-07-05 | Real-time Claude Code usage monitor with predictions and warnings |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | 8.1k | Apache-2.0 | 2026-09-29 | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, and monitor any AI-powered system or data pipeline. From tabular data to Gen AI. 100+ metrics. |
| [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer) | 7.8k | MIT | 2026-11-19 | Experience-Driven Black-Box Cost Control for Coding Agents |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | 7.5k | Apache-2.0 | 2026-11-19 | Open-source observability for your GenAI or LLM application, based on OpenTelemetry |
| [katanemo/plano](https://github.com/katanemo/plano) | 7.1k | Apache-2.0 | 2026-10-24 | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observability, agent orchestration, and guardrails so you stay focused on your agents core logic. |
| [Helicone/helicone](https://github.com/Helicone/helicone) | 6.3k | Apache-2.0 | 2026-11-17 | 🧊 Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23 🍓 |
| [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) | 6.0k | MIT | 2026-06-25 | Python SDK for AI agent monitoring, LLM cost tracking, benchmarking, and more. Integrates with most LLMs and agent frameworks including CrewAI, Agno, OpenAI Agents SDK, Langchain, Autogen, AG2, and CamelAI |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | 5.0k | Apache-2.0 | 2026-11-19 | Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company. |
| [Agenta-AI/agenta](https://github.com/Agenta-AI/agenta) | 4.9k | NOASSERTION | 2026-11-19 | Agenta is a workspace where you and your team build agents and automations. |
| [pydantic/logfire](https://github.com/pydantic/logfire) | 4.6k | MIT | 2026-11-19 | AI observability platform for production LLM and agent systems. |
| [lmnr-ai/lmnr](https://github.com/lmnr-ai/lmnr) | 3.5k | Apache-2.0 | 2026-11-19 | Laminar - open-source observability platform purpose-built for AI agents. YC S24. |
| [openlit/openlit](https://github.com/openlit/openlit) | 3.1k | Apache-2.0 | 2026-11-19 | Same agent, Smaller bill. The tools and infrastructure to get more work from your AI. Fewer tokens. Less compute. Lower cost. |
| [simonw/claude-code-transcripts](https://github.com/simonw/claude-code-transcripts) | 1.7k | Apache-2.0 | 2026-02-12 | Tools for publishing transcripts for Claude Code sessions |
| [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | 1.6k | none | 2026-02-08 | Real-time monitoring for Claude Code agents through simple hook event tracking. |
| [Arize-ai/openinference](https://github.com/Arize-ai/openinference) | 1.3k | Apache-2.0 | 2026-11-19 | OpenTelemetry Instrumentation for AI Observability |
| [wandb/weave](https://github.com/wandb/weave) | 1.2k | Apache-2.0 | 2026-11-18 | Weave is a toolkit for developing AI-powered applications, built by Weights & Biases. |

### Other awesome lists on agents

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 145.1k | Apache-2.0 | 2026-11-18 | 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 79.9k | none | 2026-09-18 | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 58.4k | NOASSERTION | 2026-11-19 | A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 53.9k | MIT | 2026-11-18 | The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞 |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 40.1k | MIT | 2026-11-06 | The 500 AI Agents Projects is a curated collection of AI agent use cases across various industries. It showcases practical applications and provides links to open-source projects for implementation, illustrating how AI agents are transforming sectors such as healthcare, finance, education, retail, and more. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 37.4k | MIT | 2026-11-15 | A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more. |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 31.0k | NOASSERTION | 2026-08-21 | A list of AI autonomous agents |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 26.7k | MIT | 2026-11-02 | A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15.9k | none | 2026-04-28 | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code |
| [kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain) | 9.6k | CC0-1.0 | 2026-11-11 | 😎 Awesome list of tools and projects with the awesome LangChain framework |
| [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | 8.8k | MIT | 2026-11-19 | A trilingual (繁中 / English / 简中) learning roadmap for agentic AI: from LLM basics to multi-agent systems, with 240+ curated resources and hands-on examples. 中文 AI agent 學習地圖。 |
| [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) | 8.3k | none | 2025-09-12 | The paper list of the 86-page SCIS cover paper "The Rise and Potential of Large Language Model Based Agents: A Survey" by Zhiheng Xi et al. |
| [yzfly/Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | 7.8k | MIT | 2026-11-14 | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients |
| [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) | 6.6k | MIT | 2026-06-07 | A collection of MCP clients. |
| [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | 6.5k | MIT | 2026-11-02 | A collection of 130+ specialized Codex subagents covering a wide range of development use cases. |
| [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | 6.5k | none | 2026-09-17 |  |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 6.4k | MIT | 2026-11-09 | Tutorials, Guides and Agent Skills Directories |
| [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | 5.2k | NOASSERTION | 2026-11-19 | Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration. |
| [nibzard/awesome-agentic-patterns](https://github.com/nibzard/awesome-agentic-patterns) | 5.1k | Apache-2.0 | 2026-11-16 | A curated catalogue of awesome agentic AI patterns |
| [walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | 4.8k | CC0-1.0 | 2026-11-09 | 🛠️ Awesome tools & guides for harness engineering. |
| [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | 3.3k | MIT | 2026-05-28 | 🔥 Comprehensive survey on Context Engineering: from prompt engineering to production-grade AI systems. hundreds of papers, frameworks, and  implementation guides for LLMs and AI agents. |
| [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) | 3.0k | none | 2026-11-18 | 🤖 Awesome list of AI Agents |
| [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) | 2.5k | CC0-1.0 | 2026-11-18 | List of agent orchestrators |
| [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | 2.0k | none | 2026-11-04 | An awesome list of Agent Harness engineering resources, including GitHub projects, tools, benchmarks, and practical guides. |
| [steel-dev/awesome-web-agents](https://github.com/steel-dev/awesome-web-agents) | 1.6k | NOASSERTION | 2026-11-10 | 🔥 A list of tools, frameworks, and resources for building AI web agents |
| [RyanAlberts/best-of-Agent-Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) | 1.6k | CC-BY-SA-4.0 | 2026-11-15 | 🏆 Ranked list of 187 AI agent harnesses, plus templates, playbooks, MCP, and learning resources. Rescored weekly. |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | 1.5k | none | 2026-11-16 | Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them. Covers open-source tools (Pi, OpenCode, Aider, Goose), platform agents (Claude Code, Codex, Gemini CLI), parallel runners, autonomous loops, and agent infrastructure. |
| [YennNing/Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) | 779 | MIT | 2026-05-20 | A curated list of papers and resources based on the survey "Code as Agent Harness" |
| [TsinghuaC3I/Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) | 668 | MIT | 2026-11-18 | A Collection of Papers about Memory for Language Agents |
| [AutoJunjie/awesome-agent-harness](https://github.com/AutoJunjie/awesome-agent-harness) | 537 | none | 2026-04-19 |  |

### Prompt/program optimisation and self-improving agents

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 42.0k | NOASSERTION | 2026-11-18 | An AI prompt optimizer for writing better prompts and getting better AI results. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 39.1k | MIT | 2026-11-19 | DSPy: The framework for programming—not prompting—language models |
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | 22.8k | NOASSERTION | 2026-11-19 | A self-improving RLM agent for coding workflows and long-running autonomous tasks. |
| [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | 19.2k | MIT | 2026-11-17 | SkillOpt is a text-space optimizer that trains reusable natural-language skills for frozen LLM agents through trajectory-driven edits, validation-gated updates, and deployable best_skill.md artifacts. |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 19.0k | MIT | 2026-11-12 | The absolute trainer to light up AI agents. |
| [EvoMap/evolver](https://github.com/EvoMap/evolver) | 8.7k | GPL-3.0 | 2026-11-19 | The GEP-powered self-evolving engine for AI agents. Auditable evolution with Genes, Capsules, and Events. \| evomap.ai |
| [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | 7.8k | Apache-2.0 | 2026-11-19 | Open-source implementation of AlphaEvolve |
| [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | 7.8k | Apache-2.0 | 2026-11-19 | Infrastructure for continually self‑improving agents |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | 7.5k | MIT | 2026-11-09 | Optimize prompts, code, and more with AI-powered Reflective Optimization |
| [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) | 7.0k | MIT | 2026-11-18 | 达尔文.skill —— 一个让你的Skill无限进化的系统：评估→改进→测试→保留或回滚 \| Autoresearch-inspired autonomous skill optimization for Claude Code. Evaluate, improve, test, keep or revert. |
| [Q00/ouroboros](https://github.com/Q00/ouroboros) | 6.4k | MIT | 2026-11-19 | Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more. |
| [rllm-org/rllm](https://github.com/rllm-org/rllm) | 5.9k | Apache-2.0 | 2026-10-16 | Democratizing Reinforcement Learning for LLMs |
| [areal-project/AReaL](https://github.com/areal-project/AReaL) | 5.9k | Apache-2.0 | 2026-11-19 | The RL Bridge for LLM-based Agent Applications. Made Simple & Flexible. |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | 4.2k | MIT | 2026-11-01 | AdalFlow: The library to build & auto-optimize LLM applications. |
| [microsoft/PromptWizard](https://github.com/microsoft/PromptWizard) | 4.0k | MIT | 2025-10-13 | Task-Aware Agent-driven Prompt Optimization Framework |
| [zou-group/textgrad](https://github.com/zou-group/textgrad) | 3.8k | MIT | 2025-07-25 | TextGrad: Automatic ''Differentiation'' via Text -- using large language models to backpropagate textual gradients. Published in Nature. |
| [ANative-Lab/EvoAgentX](https://github.com/ANative-Lab/EvoAgentX) | 3.4k | NOASSERTION | 2026-10-31 | 🚀 EvoAgentX: Building a Self-Evolving Ecosystem of AI Agents |
| [Eladlev/AutoPrompt](https://github.com/Eladlev/AutoPrompt) | 3.0k | Apache-2.0 | 2025-12-02 | A framework for prompt tuning using Intent-based Prompt Calibration |
| [facebookresearch/HyperAgents](https://github.com/facebookresearch/HyperAgents) | 2.9k | NOASSERTION | 2026-07-31 | Self-referential self-improving agents that can optimize for any computable task |
| [kayba-ai/agentic-context-engine](https://github.com/kayba-ai/agentic-context-engine) | 2.6k | Apache-2.0 | 2026-09-24 | 🧠 Make your agents learn from experience. Now available as a hosted solution at kayba.ai |
| [jennyzzt/dgm](https://github.com/jennyzzt/dgm) | 2.5k | Apache-2.0 | 2025-08-13 | Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents |
| [stanford-iris-lab/meta-harness](https://github.com/stanford-iris-lab/meta-harness) | 1.8k | MIT | 2026-11-05 | Official code for Meta-Harness (2603.28052) |
| [SakanaAI/ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) | 1.5k | Apache-2.0 | 2026-11-19 | ShinkaEvolve: Towards Open-Ended and Sample-Efficient Program Evolution 🧬 |
| [ace-agent/ace](https://github.com/ace-agent/ace) | 1.5k | Apache-2.0 | 2026-08-24 | Evolve your language agent with Agentic Context Engineering (ACE) |
| [microsoft/Trace](https://github.com/microsoft/Trace) | 766 | MIT | 2026-06-17 | End-to-end Generative Optimization for AI Agents |

### Research/science agents

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 100.3k | none | 2026-03-26 | AI agents running research on single-GPU nanochat training automatically |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 85.5k | MIT | 2026-11-19 | An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours. |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 57.7k | NOASSERTION | 2026-11-19 | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 42.1k | MIT | 2026-11-18 | An Open Source implementation of Notebook LM with more flexibility and features |
| [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | 38.2k | AGPL-3.0 | 2026-08-02 | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free. |
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | 31.9k | MIT | 2025-09-30 | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 30.8k | Apache-2.0 | 2026-11-12 | An autonomous agent that conducts deep research on any data using any LLM providers |
| [karpathy/llm-council](https://github.com/karpathy/llm-council) | 26.7k | none | 2025-11-22 | LLM Council works together to answer your hardest questions |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | 20.2k | Apache-2.0 | 2026-02-27 | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [dzhng/deep-research](https://github.com/dzhng/deep-research) | 19.9k | MIT | 2026-04-11 | An AI-powered research assistant that performs iterative, deep research on any topic by combining search engines, web scraping, and large language models.  The goal of this repo is to provide the simplest implementation of a deep research agent - e.g. an agent that can refine its research direction overtime and deep dive into a topic. |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 19.5k | MIT | 2026-11-19 | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent. |
| [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) | 18.4k | Apache-2.0 | 2026-06-14 | Get started with building Fullstack Agents using Gemini 2.5 and LangGraph |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | 16.9k | MIT | 2026-11-17 | "DeepCode: Open Agentic Coding (Agent Harness & Loop Engineering & Multi-Agent Orchestration)" |
| [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) | 15.4k | MIT | 2026-10-21 | Research and development (R&D) is crucial for the enhancement of industrial productivity, especially in the AI era, where the core aspects of R&D are mainly focused on data and models. We are committed to automating these high-value generic R&D processes through R&D-Agent, which lets AI drive data-driven AI. 🔗https://aka.ms/RD-Agent-Tech-Report |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 15.0k | NOASSERTION | 2025-12-19 | The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery 🧑‍🔬 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14.9k | MIT | 2026-08-19 | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 14.7k | MIT | 2026-10-11 | Comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude code/codex/gemini agent will be an AI research agent with full horsepower. Maintained by Orchestra Research. |
| [HKUDS/AutoAgent](https://github.com/HKUDS/AutoAgent) | 9.8k | MIT | 2025-10-16 | "AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework" |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 9.6k | Apache-2.0 | 2026-11-16 | High accuracy RAG for answering questions from scientific documents with citations |
| [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9.6k | MIT | 2026-11-19 | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Everything Local & Encrypted. |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | 7.5k | NOASSERTION | 2025-12-19 | The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search |
| [SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | 5.9k | MIT | 2025-08-20 | Agent Laboratory is an end-to-end autonomous research workflow meant to assist you as the human researcher toward implementing your research ideas |
| [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 5.9k | none | 2025-10-16 | \[NeurIPS2025\] "AI-Researcher: Autonomous Scientific Innovation" -- A production-ready version: https://novix.science/chat |
| [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | 4.9k | Apache-2.0 | 2026-11-15 | PaperOrchestra is a multi-agent framework for automated AI research paper writing. |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | 4.1k | Apache-2.0 | 2026-11-16 | Biomni: a general-purpose biomedical AI agent |
| [WecoAI/aideml](https://github.com/WecoAI/aideml) | 1.6k | MIT | 2026-10-16 | AIDE: an LLM agent for machine learning engineering - the research Weco grew out of. Referenced in OpenAI MLE-bench. |
| [Future-House/robin](https://github.com/Future-House/robin) | 760 | Apache-2.0 | 2026-04-21 | Robin: A multi-agent system for automating scientific discovery |
| [Future-House/aviary](https://github.com/Future-House/aviary) | 288 | Apache-2.0 | 2026-11-17 | A language agent gym with challenging scientific tasks |
| [gomesgroup/coscientist](https://github.com/gomesgroup/coscientist) | 214 | NOASSERTION | 2025-08-11 |  |

### Sandboxes and execution environments

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [apple/container](https://github.com/apple/container) | 52.0k | Apache-2.0 | 2026-11-13 | A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon. |
| [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker) | 38.1k | Apache-2.0 | 2026-11-18 | Secure and fast microVMs for serverless computing. |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 21.8k | Apache-2.0 | 2026-11-19 | OpenShell is the safe, private runtime for autonomous AI agents. |
| [gvisor/gvisor](https://github.com/gvisor/gvisor) | 20.1k | Apache-2.0 | 2026-11-19 | Application Kernel for Containers |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 17.6k | Apache-2.0 | 2026-11-19 | Secure, Fast, and Extensible Sandbox runtime for AI agents. |
| [coder/coder](https://github.com/coder/coder) | 17.4k | AGPL-3.0 | 2026-11-19 | Secure environments for developers and their agents |
| [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | 14.9k | Apache-2.0 | 2026-11-19 | Open-source, secure environment with real-world tools for enterprise-grade agents. |
| [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 13.4k | NOASSERTION | 2026-11-19 | Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. |
| [containers/bubblewrap](https://github.com/containers/bubblewrap) | 9.6k | NOASSERTION | 2026-10-14 | Low-level unprivileged sandboxing tool used by Flatpak and similar projects |
| [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | 9.2k | MIT | 2026-11-18 | Orchestrate sandboxed coding agents in TypeScript with sandcastle.run() |
| [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) | 9.1k | Apache-2.0 | 2026-11-19 | 🧱 easy, fast, programmable and local-first microVM runtime and library |
| [pydantic/monty](https://github.com/pydantic/monty) | 9.0k | MIT | 2026-11-19 | A secure Python sandbox, written in Rust, for code written by AI. |
| [anthropics/sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 7.2k | Apache-2.0 | 2026-11-13 | A lightweight sandboxing tool for enforcing filesystem and network restrictions on arbitrary processes at the OS level, without requiring a container. |
| [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | 7.1k | Apache-2.0 | 2026-11-19 | An embeddable, portable, branchable virtual machine to safely run Agents locally. |
| [e2b-dev/fragments](https://github.com/e2b-dev/fragments) | 6.4k | Apache-2.0 | 2026-11-18 | Open-source Next.js template for building apps that are fully generated by AI. By E2B. |
| [agent-infra/sandbox](https://github.com/agent-infra/sandbox) | 6.4k | Apache-2.0 | 2026-09-14 | All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container. |
| [nolabs-ai/nono](https://github.com/nolabs-ai/nono) | 5.0k | Apache-2.0 | 2026-11-19 | agent runtime security - zero trust, zero setup, zero latency agent sandboxing |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 4.7k | Apache-2.0 | 2026-11-18 | agent-sandbox enables easy management of isolated, stateful, singleton workloads, ideal for use cases like AI agent runtimes  and reinforcement learning (RL). |
| [vercel-labs/just-bash](https://github.com/vercel-labs/just-bash) | 4.5k | none | 2026-11-17 | Bash for Agents |
| [google/nsjail](https://github.com/google/nsjail) | 4.2k | Apache-2.0 | 2026-11-10 | A lightweight process isolation tool that utilizes Linux namespaces, cgroups, rlimits and seccomp-bpf syscall filters, leveraging the Kafel BPF language for enhanced security. |
| [dagger/container-use](https://github.com/dagger/container-use) | 4.1k | Apache-2.0 | 2026-11-14 | Development environments for coding agents. Enable multiple agents to work safely and independently with your preferred stack. |
| [boxlite-ai/boxlite](https://github.com/boxlite-ai/boxlite) | 2.7k | Apache-2.0 | 2026-11-19 | The micro-VM for AI agents — light enough to embed on your laptop, elastic enough to power an agentic cloud. |
| [e2b-dev/code-interpreter](https://github.com/e2b-dev/code-interpreter) | 2.4k | Apache-2.0 | 2026-11-18 | Python & JS/TS SDK for running AI-generated code/code interpreting in your AI app |
| [e2b-dev/desktop](https://github.com/e2b-dev/desktop) | 1.6k | Apache-2.0 | 2026-11-16 | E2B Desktop Sandbox for LLMs. E2B Sandbox with desktop graphical environment that you can connect to any LLM for secure computer use. |
| [cloudflare/sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) | 1.2k | NOASSERTION | 2026-11-10 | Run sandboxed code environments on Cloudflare's edge network |
| [vndee/llm-sandbox](https://github.com/vndee/llm-sandbox) | 1.1k | MIT | 2026-11-17 | Lightweight and portable LLM sandbox runtime (code interpreter) Python library. |
| [SWE-agent/SWE-ReX](https://github.com/SWE-agent/SWE-ReX) | 651 | MIT | 2026-11-16 | Sandboxed code execution for AI agents, locally or on the cloud. Massively parallel, easy to extend. Powering SWE-agent and more. |
| [modal-labs/modal-client](https://github.com/modal-labs/modal-client) | 540 | Apache-2.0 | 2026-11-19 | SDK libraries for Modal |

## Benchmarks and evaluation

### Papers and resources

- [Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard](https://arxiv.org/abs/2610.00651) - Michael Hardy et al. (2026). arXiv:2610.00651
- [AgentBug-Smith: Automatically Reproducing Real-World Harness Bugs in Agentic Systems](https://arxiv.org/abs/2609.37864) - Yiming Cheng et al. (2026). arXiv:2609.37864
- [AgentTorrent: A Dataset of Context and Harness Engineering Artifacts on GitHub](https://arxiv.org/abs/2611.15436) - Sebastian Baltes et al. (2026). arXiv:2611.15436
- [AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090) - Kaiyu Huang et al. (2026). arXiv:2610.18090
- [Auditing Agent Harness Safety](https://arxiv.org/abs/2605.14271) - Chengzhi Liu et al. (2026). arXiv:2605.14271
- [Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories](https://arxiv.org/abs/2610.01491) - Chengguang Gan et al. (2026). arXiv:2610.01491
- [Autonomous Active Directory Exploitation via Multi-Model Harness Orchestration: A Benchmark Study with NeuroSploit on GOAD](https://arxiv.org/abs/2610.04243) - Joas Antonio dos Santos Barbosa (2026). arXiv:2610.04243
- [BudgetBench: A Budget-Tiered Protocol and Pilot Harness for Memory Strategy Evaluation in Local Large Language Model Agents](https://arxiv.org/abs/2609.13149) - Aditya Karnam Gururaj Rao, Arjun Jaggi (2026). arXiv:2609.13149
- [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/abs/2606.12344) - Mengyu Zheng et al. (2026). arXiv:2606.12344
- [Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer Order Its Top Entries, and What to Measure Instead](https://arxiv.org/abs/2609.17394) - Fengshuo Liu et al. (2026). arXiv:2609.17394
- [Construct Validity of Coding Benchmarks for LLM-based Agentic Coding Tools](https://arxiv.org/abs/2611.05665) - Alexander Berndt et al. (2026). arXiv:2611.05665
- [CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?](https://arxiv.org/abs/2609.01600) - Damien Sileo, Dimitri Kachler (2026). arXiv:2609.01600
- [DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT](https://arxiv.org/abs/2611.10629) - Shijie Liu et al. (2026). arXiv:2611.10629
- [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368) - Jiaqi Shao et al. (2026). arXiv:2607.22368
- [Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://arxiv.org/abs/2610.20344) - Yuyao Ge et al. (2026). arXiv:2610.20344
- [EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses](https://arxiv.org/abs/2609.39284) - Zhixuan Tan et al. (2026). arXiv:2609.39284
- [Evaluating Agentic Harness Systems for Autonomous Computational Pathology](https://arxiv.org/abs/2607.02598) - Jie Lin et al. (2026). arXiv:2607.02598
- [Evaluating Agentic Learning Harness Capabilities Without Labels via the Scaling Hypothesis](https://arxiv.org/abs/2608.13608) - Aryan Luthra et al. (2026). arXiv:2608.13608
- [Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance](https://arxiv.org/abs/2609.37501) - Dipankar Sarkar (2026). arXiv:2609.37501
- [Evo-Bench: Can Language Models Improve Agent Harness?](https://arxiv.org/abs/2608.09096) - Lisheng Huang et al. (2026). arXiv:2608.09096
- [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280) - Zixuan Ke et al. (2026). arXiv:2609.04280
- [Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows](https://arxiv.org/abs/2605.27922) - Yilun Yao et al. (2026). arXiv:2605.27922
- [Harness-Delta Attribution: Dissecting Gains From Harness Evolution](https://arxiv.org/abs/2610.22466) - Wenxuan Ding et al. (2026). arXiv:2610.22466
- [Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents](https://arxiv.org/abs/2608.11727) - Zining Huang et al. (2026). arXiv:2608.11727
- [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](https://arxiv.org/abs/2609.01437) - Yuhao Wu et al. (2026). arXiv:2609.01437
- [HarnessOpt-Bench: Evaluating LLMs at Harness Optimization](https://arxiv.org/abs/2608.06301) - Varun Ursekar et al. (2026). arXiv:2608.06301
- [HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety](https://arxiv.org/abs/2608.17597) - Yajing Bai et al. (2026). arXiv:2608.17597
- [HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses](https://arxiv.org/abs/2608.06984) - Xiao Zhang et al. (2026). arXiv:2608.06984
- [Hearsay: Who Can Audit the Record a Deployed Agent Harness Writes?](https://arxiv.org/abs/2609.32495) - Jiahong Dai et al. (2026). arXiv:2609.32495
- [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750) - Longju Bai et al. (2026). arXiv:2604.22750
- [HPCAgent-Bench: A Framework for Sound Benchmarking of Code-Optimizing Agents, Harnesses, and Skills](https://arxiv.org/abs/2610.20673) - Yakup Koray Budanaz et al. (2026). arXiv:2610.20673
- [kw-bench: Breaking Frontier Harnesses on Real-World Tasks](https://arxiv.org/abs/2610.36405) - George Juraj Salapa (2026). arXiv:2610.36405
- [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/abs/2606.11686) - Sawyer Zhang, Alexander Wang, Sophie Lei (2026). arXiv:2606.11686
- [LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning](https://arxiv.org/abs/2609.38137) - Quang Hieu Pham et al. (2026). arXiv:2609.38137
- [LoopsBench: From Harness Engineering to Loop Engineering in Coding Agent Evaluation](https://arxiv.org/abs/2608.00267) - Han Li et al. (2026). arXiv:2608.00267
- [Noise Floor Audit for Agent Benchmarks](https://arxiv.org/abs/2608.22331) - Yihang Chen et al. (2026). arXiv:2608.22331
- [OctoBench: Benchmarking Scaffold-Aware Instruction Following in Repository-Grounded Agentic Coding](https://arxiv.org/abs/2601.10343) - Deming Ding et al. (2026). arXiv:2601.10343
- [On the estimation and validity of AI time horizons---a statistical look at the METR plot](https://arxiv.org/abs/2610.12466) - Drew T. Nguyen, William Fithian (2026). arXiv:2610.12466
- [OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537) - Mengqi Yuan et al. (2026). arXiv:2606.29537
- [Pairing Matters: Performance, Failures, and Efficiency in Lightweight Coding Agents](https://arxiv.org/abs/2610.32131) - Lu Zhao, Christopher M. Poskitt, David Lo (2026). arXiv:2610.32131
- [RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents](https://arxiv.org/abs/2609.04898) - Aziz Ben Amor et al. (2026). arXiv:2609.04898
- [Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents](https://arxiv.org/abs/2601.15322) - Raffi Khatchadourian (2026). arXiv:2601.15322
- [Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?](https://arxiv.org/abs/2608.04828) - Jinyi Han et al. (2026). arXiv:2608.04828
- [SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory](https://arxiv.org/abs/2611.22017) - Gengyue Dong et al. (2026). arXiv:2611.22017
- [Termination Lag: Coding Agents Solve Early but Stop Late](https://arxiv.org/abs/2611.14960) - Musa Cim, Burak Topcu, Mahmut Taylan Kandemir (2026). arXiv:2611.14960
- [The Double Measurement Confound in Agent Benchmarks: De-Scaffolding, Ground-Truth Scoring, and Reliability Beyond the Mean](https://arxiv.org/abs/2609.09218) - Yonghong Zhang et al. (2026). arXiv:2609.09218
- [ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets](https://arxiv.org/abs/2610.21098) - Zichuan Xu et al. (2026). arXiv:2610.21098
- [Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://arxiv.org/abs/2605.22505) - Kai Tzu-iunn Ong et al. (2026). arXiv:2605.22505
- [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285) - Zhiyong Cao et al. (2026). arXiv:2610.32285
- [VeRO: A Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.22480) - Varun Ursekar et al. (2026). arXiv:2602.22480
- [VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342) - Ruotian Peng et al. (2026). arXiv:2610.26342
- [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516) - Jason Wei et al. (2025). arXiv:2504.12516
- [Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems](https://arxiv.org/abs/2506.17208) - Matias Martinez, Xavier Franch (2025). arXiv:2506.17208
- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) - Yuxuan Zhu et al. (2025). arXiv:2507.02825
- [GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks](https://arxiv.org/abs/2510.04374) - Tejal Patwardhan et al. (2025). arXiv:2510.04374
- [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977) - Sayash Kapoor et al. (2025). arXiv:2510.11977
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270) - Ziqian Zhong, Aditi Raghunathan, Nicholas Carlini (2025). arXiv:2510.20270
- [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) - Chunqiu Steven Xia et al. (2025). arXiv:2511.13646
- [MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive MCP Use](https://arxiv.org/abs/2509.24002) - Zijian Wu et al. (2025). arXiv:2509.24002
- [Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving](https://arxiv.org/abs/2504.02605) - Daoguang Zan et al. (2025). arXiv:2504.02605
- [Remote Labor Index: Measuring AI Automation of Remote Work](https://arxiv.org/abs/2510.26787) - Mantas Mazeika et al. (2025). arXiv:2510.26787
- [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints](https://arxiv.org/abs/2509.09853) - Zhiyu Fan et al. (2025). arXiv:2509.09853
- [SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](https://arxiv.org/abs/2502.12115) - Samuel Miserendino et al. (2025). arXiv:2502.12115
- [The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason](https://arxiv.org/abs/2506.12286) - Shanchao Liang, Spandan Garg, Roshanak Zilouchian Moghaddam (2025). arXiv:2506.12286
- [Your Harness is Not Secure: Benchmarking Real-world Threat of Command Line Interface Agent](https://arxiv.org/abs/2510.06607) - Weidi Luo et al. (2025). arXiv:2510.06607
- [Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations](https://arxiv.org/abs/2411.00640) - Evan Miller (2024). arXiv:2411.00640
- [AI Agents That Matter](https://arxiv.org/abs/2407.01502) - Sayash Kapoor et al. (2024). arXiv:2407.01502
- [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) - Harsh Trivedi et al. (2024). arXiv:2407.18901
- [CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark](https://arxiv.org/abs/2409.11363) - Zachary S. Siegel et al. (2024). arXiv:2409.11363
- [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](https://arxiv.org/abs/2408.08926) - Andy K. Zhang et al. (2024). arXiv:2408.08926
- [RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts](https://arxiv.org/abs/2411.15114) - Hjalmar Wijk et al. (2024). arXiv:2411.15114
- [SWE-Bench+: Enhanced Coding Benchmark for LLMs](https://arxiv.org/abs/2410.06992) - Reem Aleithan et al. (2024). arXiv:2410.06992
- [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) - Grégoire Mialon et al. (2023). arXiv:2311.12983

### Repositories: evaluation harnesses and benchmarks

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | 46.5k | Apache-2.0 | 2026-11-19 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 27.5k | MIT | 2026-11-19 | Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple declarative configs with command line and CI/CD integration.  Used by OpenAI and Anthropic. |
| [openai/evals](https://github.com/openai/evals) | 19.8k | NOASSERTION | 2026-04-14 | Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks. |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 19.6k | Apache-2.0 | 2026-11-19 | The LLM Evaluation Framework |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | 16.4k | Apache-2.0 | 2026-11-14 | Supercharge Your LLM Application Evaluations 🚀 |
| [ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla) | 13.1k | Apache-2.0 | 2026-10-17 | Gorilla: Training and Evaluating LLMs for Function Calls (Tool Calls) |
| [harbor-framework/harbor](https://github.com/harbor-framework/harbor) | 7.3k | Apache-2.0 | 2026-11-19 | Framework for evaluating and improving agents |
| [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.2k | MIT | 2026-09-18 | SWE-bench: Can Language Models Resolve Real-world Github Issues? |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | 6.0k | Apache-2.0 | 2026-11-19 | 🐢 Open-Source Evaluation & Testing library for LLM Agents |
| [openai/simple-evals](https://github.com/openai/simple-evals) | 4.7k | MIT | 2026-04-22 |  |
| [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | 4.0k | Apache-2.0 | 2026-11-19 | Multi-tier framework for evaluating AI agent skills and plugins with quality gates, security scanning, harness compatibility checks, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior. Ships reusable CI templates that bring every check to any repository. |
| [THUDM/AgentBench](https://github.com/THUDM/AgentBench) | 3.8k | Apache-2.0 | 2026-02-08 | A Comprehensive Benchmark to Evaluate LLMs as Agents (ICLR'24) |
| [truera/trulens](https://github.com/truera/trulens) | 3.7k | MIT | 2026-11-18 | Evaluation and Tracking for LLM Experiments and AI Agents |
| [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | 3.4k | MIT | 2026-10-08 | LLM-as-a-Verifier is a general-purpose framework that provides fine-grained feedback for any agent without requiring additional training. It achieves SOTA performance across coding, robotics, and medical agentic benchmarks. |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.3k | MIT | 2026-11-19 | Inspect: A framework for large language model evaluations |
| [xlang-ai/OSWorld](https://github.com/xlang-ai/OSWorld) | 3.3k | Apache-2.0 | 2026-11-14 | \[NeurIPS 2024\] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments |
| [harbor-framework/terminal-bench-1](https://github.com/harbor-framework/terminal-bench-1) | 2.6k | Apache-2.0 | 2026-07-11 | A benchmark for LLMs on complicated tasks in the terminal |
| [sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench) | 2.5k | MIT | 2026-11-10 | τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains |
| [openai/mle-bench](https://github.com/openai/mle-bench) | 1.8k | NOASSERTION | 2026-04-24 | MLE-bench is a benchmark for measuring how well AI agents perform at machine learning engineering |
| [web-arena-x/webarena](https://github.com/web-arena-x/webarena) | 1.6k | Apache-2.0 | 2025-11-26 | Code repo for "WebArena: A Realistic Web Environment for Building Autonomous Agents" |
| [sierra-research/tau-bench](https://github.com/sierra-research/tau-bench) | 1.5k | MIT | 2026-03-18 | Code and Data for Tau-Bench |
| [ServiceNow/BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | NOASSERTION | 2026-11-18 | BrowserGym, a Gym environment for web task automation |
| [openai/frontier-evals](https://github.com/openai/frontier-evals) | 1.3k | MIT | 2026-10-12 | OpenAI Frontier Evals |
| [harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench) | 1.1k | Apache-2.0 | 2026-11-19 | Measuring and evolving with the frontier of agent work |
| [google-research/android_world](https://github.com/google-research/android_world) | 1.0k | Apache-2.0 | 2026-11-10 | AndroidWorld is an environment and benchmark for autonomous agents |
| [microsoft/WindowsAgentArena](https://github.com/microsoft/WindowsAgentArena) | 917 | MIT | 2026-10-26 | Windows Agent Arena (WAA) 🪟 is a scalable OS platform for testing and benchmarking of multi-modal AI agents. |
| [SWE-bench/SWE-smith](https://github.com/SWE-bench/SWE-smith) | 836 | MIT | 2026-11-16 | \[NeurIPS 2025 D&B Spotlight\] Scaling Data for SWE-agents |
| [TheAgentCompany/TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) | 822 | MIT | 2025-11-17 | An agent benchmark with tasks in a simulated software company. |
| [UKGovernmentBEIS/inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) | 750 | MIT | 2026-11-19 | Collection of evals for Inspect AI |
| [scaleapi/SWE-bench_Pro-os](https://github.com/scaleapi/SWE-bench_Pro-os) | 569 | MIT | 2026-09-22 | SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? |
| [harbor-framework/terminal-bench-2](https://github.com/harbor-framework/terminal-bench-2) | 450 | Apache-2.0 | 2026-04-30 |  |

## Security

### Papers and resources

- ["Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild](https://arxiv.org/abs/2602.06547) - Yi Liu et al. (2026). arXiv:2602.06547
- [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](https://arxiv.org/abs/2609.03884) - Pengxun Li et al. (2026). arXiv:2609.03884
- [Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems](https://arxiv.org/abs/2607.28147) - Yu Cui et al. (2026). arXiv:2607.28147
- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) - Yi Liu et al. (2026). arXiv:2601.10338
- [Agents of Chaos](https://arxiv.org/abs/2602.20021) - Natalie Shapira et al. (2026). arXiv:2602.20021
- [Approval Laundering: Systematizing Approval--Execution Binding Failures in AI Coding-Agent Harnesses](https://arxiv.org/abs/2609.38983) - Yang Wang (2026). arXiv:2609.38983
- [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069) - Xing Wang, Xiaoyi Zhang, Jie Shao (2026). arXiv:2609.00069
- [Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents](https://arxiv.org/abs/2609.08371) - Dimitrios Stamatios Bouras, Yihan Dai, Sergey Mechtaev (2026). arXiv:2609.08371
- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923) - Hanna Foerster et al. (2026). arXiv:2601.09923
- [Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](https://arxiv.org/abs/2610.31376) - Chao Gu, Quanyan Zhu (2026). arXiv:2610.31376
- [Comparing Human Oversight Strategies for Computer-Use Agents](https://arxiv.org/abs/2604.04918) - Chaoran Chen et al. (2026). arXiv:2604.04918
- [Compositional Safety Failures in Harness Evolution: Identification and Runtime Monitoring](https://arxiv.org/abs/2609.33123) - Zhixiang Zhang et al. (2026). arXiv:2609.33123
- [Control OSWorld: An AI Control Environment for GUI Computer Use Agents](https://arxiv.org/abs/2610.03818) - Maria Sanchez del Rio, Mikhail Terekhov (2026). arXiv:2610.03818
- [Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors](https://arxiv.org/abs/2611.22583) - Yujun Wang et al. (2026). arXiv:2611.22583
- [EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents](https://arxiv.org/abs/2609.05903) - Nanxi Li et al. (2026). arXiv:2609.05903
- [FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents](https://arxiv.org/abs/2605.27333) - Haoxuan Jia et al. (2026). arXiv:2605.27333
- [From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents](https://arxiv.org/abs/2610.22987) - Xianglin Yang et al. (2026). arXiv:2610.22987
- [From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](https://arxiv.org/abs/2611.13960) - Simon Hegelich et al. (2026). arXiv:2611.13960
- [From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors](https://arxiv.org/abs/2605.31042) - Jiejun Tan et al. (2026). arXiv:2605.31042
- [HARDE: Optimizing Agent Harnesses for Runtime Risk Detection and Execution Control](https://arxiv.org/abs/2609.38291) - Zhuo Liu et al. (2026). arXiv:2609.38291
- [Harness Matters: Measuring and Dissecting Security Resilience in Web Agents](https://arxiv.org/abs/2611.11971) - Xinyi Wu et al. (2026). arXiv:2611.11971
- [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639) - Zhengyang Zhu et al. (2026). arXiv:2610.07639
- [HASTE: Evolving Agent Harnesses Against Emerging Attacks Using Sparse Evidence](https://arxiv.org/abs/2610.02920) - Xiqiao Xiong et al. (2026). arXiv:2610.02920
- [Let the Agent Do It? How Software Practitioners Understand and Make Permission Decisions in Agentic AI Assistants](https://arxiv.org/abs/2610.06047) - Larissa Salerno et al. (2026). arXiv:2610.06047
- [OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents](https://arxiv.org/abs/2610.01508) - Taolin Zhang et al. (2026). arXiv:2610.01508
- [Quantifying Frontier LLM Capabilities for Container Sandbox Escape](https://arxiv.org/abs/2603.02277) - Rahul Marchand et al. (2026). arXiv:2603.02277
- [Rethinking Access Control for AI Agents: Recent Advances and Open Challenges](https://arxiv.org/abs/2611.06764) - Chijin Zhou, Quan Zhang (2026). arXiv:2611.06764
- [SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time](https://arxiv.org/abs/2609.36580) - Yu Cheng et al. (2026). arXiv:2609.36580
- [Same-Origin Policy for Agentic Browsers](https://arxiv.org/abs/2606.14027) - Xilong Wang et al. (2026). arXiv:2606.14027
- [Scanning the Harness: Configuration Exposures in AI Coding-Agent Supply Chains](https://arxiv.org/abs/2609.07360) - Benjamin Kapner et al. (2026). arXiv:2609.07360
- [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](https://arxiv.org/abs/2608.16393) - Zonghao Ying et al. (2026). arXiv:2608.16393
- [Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations](https://arxiv.org/abs/2606.15008) - Saeid Jamshidi et al. (2026). arXiv:2606.15008
- [Self-Healing Harness for Runtime Oversight of Agent Self-Modification](https://arxiv.org/abs/2609.24130) - Sina Tayebati et al. (2026). arXiv:2609.24130
- [SI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative) - National Institute of Standards and Technology (2026).
- [Singapore Launches New Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai) - Infocomm Media Development Authority (2026).
- [The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems](https://arxiv.org/abs/2602.17753) - Leon Staufer et al. (2026). arXiv:2602.17753
- [Towards Agentic AI Governance: A Preliminary Assessment](https://arxiv.org/abs/2607.07612) - Mubarak Raji, Masooda Bashir (2026). arXiv:2607.07612
- [Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models](https://arxiv.org/abs/2611.11571) - Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar (2026). arXiv:2611.11571
- [What Survives Self-Evolution: Provenance Marks in Copied Agent Harnesses](https://arxiv.org/abs/2610.21458) - Jieyu Li et al. (2026). arXiv:2610.21458
- [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222) - Zichuan Li et al. (2026). arXiv:2609.01222
- [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) - Xingbang He et al. (2026). arXiv:2608.27299
- [When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents](https://arxiv.org/abs/2609.13889) - Shuhuai Huang, Jingfeng Zhang, Hong Jia (2026). arXiv:2609.13889
- [Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities](https://arxiv.org/abs/2610.29379) - Gadi Evron (2026). arXiv:2610.29379
- [Who Is Behind the Harness? Verifying Model Identity in Coding Agents through Behavioral Fingerprinting](https://arxiv.org/abs/2609.28559) - Chuyi Wang et al. (2026). arXiv:2609.28559
- ["Your AI, My Shell": Demystifying Prompt Injection Attacks on Agentic AI Coding Editors](https://arxiv.org/abs/2509.22040) - Yue Liu et al. (2025). arXiv:2509.22040
- [Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061) - Qiusi Zhan et al. (2025). arXiv:2503.00061
- [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - OWASP Agentic Security Initiative (2025).
- [Agents Rule of Two: A Practical Approach to AI Agent Security](https://ai.meta.com/blog/practical-ai-agent-security/) - Meta AI (2025).
- [AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents](https://arxiv.org/abs/2503.18666) - Haoyu Wang, Christopher M. Poskitt, Jun Sun (2025). arXiv:2503.18666
- [Authenticated Delegation and Authorized AI Agents](https://arxiv.org/abs/2501.09674) - Tobin South et al. (2025). arXiv:2501.09674
- [Ctrl-Z: Controlling AI Agents via Resampling](https://arxiv.org/abs/2504.10374) - Aryan Bhatt et al. (2025). arXiv:2504.10374
- [Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) - Edoardo Debenedetti et al. (2025). arXiv:2503.18813
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) - Luca Beurer-Kellner et al. (2025). arXiv:2506.08837
- [DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](https://arxiv.org/abs/2506.12104) - Hao Li et al. (2025). arXiv:2506.12104
- [Firewalls to Secure Dynamic LLM Agentic Networks](https://arxiv.org/abs/2502.01822) - Sahar Abdelnabi et al. (2025). arXiv:2502.01822
- [LlamaFirewall: An open source guardrail system for building secure AI agents](https://arxiv.org/abs/2505.03574) - Sahana Chennabasappa et al. (2025). arXiv:2505.03574
- [MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits](https://arxiv.org/abs/2504.03767) - Brandon Radosevich, John Halloran (2025). arXiv:2504.03767
- [MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers](https://arxiv.org/abs/2508.14925) - Zhiqiang Wang et al. (2025). arXiv:2508.14925
- [MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents](https://arxiv.org/abs/2502.05174) - Kaijie Zhu et al. (2025). arXiv:2502.05174
- [Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://arxiv.org/abs/2503.03704) - Shen Dong et al. (2025). arXiv:2503.03704
- [Meta-SecAlign: Training LLMs against Prompt Injection for Robust Agents](https://arxiv.org/abs/2507.02735) - Sizhe Chen et al. (2025). arXiv:2507.02735
- [Multi-Agent Systems Execute Arbitrary Malicious Code](https://arxiv.org/abs/2503.12188) - Harold Triedman, Rishi Jha, Vitaly Shmatikov (2025). arXiv:2503.12188
- [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866) - Thomas Kuntz et al. (2025). arXiv:2506.14866
- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - OWASP Gen AI Security Project (2025).
- [Progent: Securing AI Agents with Privilege Control](https://arxiv.org/abs/2504.11703) - Tianneng Shi et al. (2025). arXiv:2504.11703
- [Prompt Injection Attack to Tool Selection in LLM Agents](https://arxiv.org/abs/2504.19793) - Jiawen Shi et al. (2025). arXiv:2504.19793
- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://arxiv.org/abs/2505.21936) - Zeyi Liao et al. (2025). arXiv:2505.21936
- [RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage](https://arxiv.org/abs/2502.08966) - Peter Yong Zhong et al. (2025). arXiv:2502.08966
- [Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643) - Manuel Costa et al. (2025). arXiv:2505.23643
- [Security Best Practices - Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) - Model Context Protocol project (2025).
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://arxiv.org/abs/2503.22738) - Zhaorun Chen, Mintong Kang, Bo Li (2025). arXiv:2503.22738
- [Systems Security Foundations for Agentic Computing](https://arxiv.org/abs/2512.01295) - Mihai Christodorescu et al. (2025). arXiv:2512.01295
- [The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections](https://arxiv.org/abs/2510.09023) - Milad Nasr et al. (2025). arXiv:2510.09023
- [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) - Simon Willison (2025).
- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575) - Ivan Evtimov et al. (2025). arXiv:2504.18575
- [Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast](https://arxiv.org/abs/2402.08567) - Xiangming Gu et al. (2024). arXiv:2402.08567
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) - Edoardo Debenedetti et al. (2024). arXiv:2406.13352
- [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) - Maksym Andriushchenko et al. (2024). arXiv:2410.09024
- [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784) - Zhaorun Chen et al. (2024). arXiv:2407.12784
- [Artificial intelligence risk management framework: generative artificial intelligence profile](https://doi.org/10.6028/NIST.AI.600-1) - National Institute of Standards and Technology (US) (2024). doi:10.6028/NIST.AI.600-1
- [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) - Yanzhe Zhang, Tao Yu, Diyi Yang (2024). arXiv:2411.02391
- [Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720) - Keegan Hines et al. (2024). arXiv:2403.14720
- [GoEX: Perspectives and Designs Towards a Runtime for Autonomous LLM Applications](https://arxiv.org/abs/2404.06921) - Shishir G. Patil et al. (2024). arXiv:2404.06921
- [GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2406.09187) - Zhen Xiang et al. (2024). arXiv:2406.09187
- [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691) - Qiusi Zhan et al. (2024). arXiv:2403.02691
- [Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283) - Donghyun Lee, Mo Tiwari (2024). arXiv:2410.07283
- [StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/abs/2402.06363) - Sizhe Chen et al. (2024). arXiv:2402.06363
- [System-Level Defense against Indirect Prompt Injection Attacks: An Information Flow Control Perspective](https://arxiv.org/abs/2409.19091) - Fangzhou Wu, Ethan Cecchetti, Chaowei Xiao (2024). arXiv:2409.19091
- [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682) - Feiran Jia et al. (2024). arXiv:2412.16682
- [Visibility into AI Agents](https://arxiv.org/abs/2401.13138) - Alan Chan et al. (2024). arXiv:2401.13138
- [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942) - Ryan Greenblatt et al. (2023). arXiv:2312.06942
- [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) - Hakan Inan et al. (2023). arXiv:2312.06674
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) - Kai Greshake et al. (2023). arXiv:2302.12173
- [The Dual LLM pattern for building AI assistants that can resist prompt injection](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) - Simon Willison (2023).

### Repositories: safety, guardrails and red-teaming

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [usestrix/strix](https://github.com/usestrix/strix) | 76.6k | Apache-2.0 | 2026-11-19 | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | 52.1k | AGPL-3.0 | 2026-11-19 | Shannon is an AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production. |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 26.9k | Apache-2.0 | 2026-11-19 | Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them. |
| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | 16.5k | MIT | 2026-07-14 | Automated Penetration Testing Agentic Framework Powered by Large Language Models |
| [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio) | 12.0k | MIT | 2026-11-19 | An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines. |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | 10.1k | Apache-2.0 | 2026-11-18 | the LLM vulnerability scanner |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | 7.6k | Apache-2.0 | 2026-11-18 | Adding guardrails to large language models. |
| [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | 7.6k | Apache-2.0 | 2026-11-19 | A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation. |
| [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.5k | NOASSERTION | 2026-11-19 | NeMo Guardrails is an open-source library for applying programmable safety and security controls to LLM and agentic applications. |
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 7.1k | AGPL-3.0 | 2026-09-08 | autonomous red teaming platform; multi-agent offensive-security meta-harness |
| [superagent-ai/superagent](https://github.com/superagent-ai/superagent) | 6.9k | MIT | 2026-08-25 | Superagent protects your AI applications against prompt injections, data leaks, and harmful outputs. Embed safety directly into your app and prove compliance to your customers. |
| [BitterSecurity/Decepticon](https://github.com/BitterSecurity/Decepticon) | 6.6k | Apache-2.0 | 2026-11-18 | Autonomous Hacking Agent for Red Team |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 6.6k | MIT | 2026-11-18 | AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10. |
| [microsoft/PyRIT](https://github.com/microsoft/PyRIT) | 5.0k | MIT | 2026-11-19 | Open-source AI red teaming toolkit from Microsoft. Test generative AI systems with automated scans, adaptive multi-turn attacks, and a web UI. |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | 4.5k | NOASSERTION | 2026-11-13 | Set of tools to assess and improve LLM security. |
| [snyk/agent-scan](https://github.com/snyk/agent-scan) | 3.3k | Apache-2.0 | 2026-11-19 | Security scanner for AI agents, MCP servers and agent skills. |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | 3.1k | Apache-2.0 | 2026-10-23 | DeepTeam is a framework to red team LLMs and AI agents. |
| [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) | 2.7k | NOASSERTION | 2026-11-16 | Security Scanner for Agent Skills |
| [safety-research/bloom](https://github.com/safety-research/bloom) | 1.4k | MIT | 2026-05-07 | bloom - evaluate any behavior immediately  🌸🌱 |
| [meridianlabs-ai/inspect_petri](https://github.com/meridianlabs-ai/inspect_petri) | 1.4k | MIT | 2026-11-18 | An alignment auditing agent capable of quickly exploring alignment hypothesis |
| [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) | 1.1k | Apache-2.0 | 2026-11-19 | Scan MCP servers for potential threats & security findings. |
| [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) | 1.1k | MIT | 2026-06-02 | A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. |
| [invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant) | 477 | Apache-2.0 | 2026-01-12 | Guardrails for secure and robust agent development |
| [google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection) | 423 | Apache-2.0 | 2025-06-20 | Code for the paper "Defeating Prompt Injections by Design" |
| [UKGovernmentBEIS/control-arena](https://github.com/UKGovernmentBEIS/control-arena) | 270 | MIT | 2026-11-16 | ControlArena is a collection of settings, model organisms and protocols - for running control experiments. |
| [openai/openai-guardrails-python](https://github.com/openai/openai-guardrails-python) | 268 | MIT | 2026-11-18 | OpenAI Guardrails - Python |
| [thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) | 168 | MIT | 2025-08-11 |  |

## Courses and learning

### Papers and resources

- [Advanced Large Language Model Agents MOOC, Spring 2025](https://agenticai-learning.org/sp25) - Dawn Song, Xinyun Chen, Kaiyu Yang (2025).

### Repositories: educational and minimal harnesses

| Repository | Stars | License | Last push | Description |
|---|---:|---|---|---|
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 87.4k | NOASSERTION | 2026-11-13 | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 80.6k | MIT | 2026-11-15 | Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1 |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 80.5k | MIT | 2026-11-17 | 18 Lessons to Get Started Building AI Agents |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77.2k | MIT | 2026-11-17 | Examples and guides for using the OpenAI API |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 58.8k | Apache-2.0 | 2026-10-08 | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 54.9k | MIT | 2026-11-17 | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 50.2k | MIT | 2026-11-19 | Your lightweight open-source personal agent. |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | 47.4k | MIT | 2026-11-14 | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | 35.2k | Apache-2.0 | 2026-11-17 | This repository contains the Hugging Face Agents Course. |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | 33.5k | Apache-2.0 | 2026-11-19 | Fast, small, and fully autonomous AI personal assistant infrastructure, any OS, any platform — deploy anywhere, swap anything 🦀 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 31.1k | MIT | 2026-11-19 | Your own always-on AI assistant: self-hosted, open source, lightweight. Each agent runs in its own container on your machine, on the harness you choose (Claude Code, Codex, Cursor, OpenCode). Talk to it from Slack, WhatsApp, Telegram, Discord and more. |
| [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | 25.5k | MIT | 2026-11-15 | Harness engineering beginner tutorial, from 0 to 1 |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 25.1k | NOASSERTION | 2026-11-02 | 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems. |
| [yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) | 22.4k | none | 2026-01-31 |  |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | 21.9k | NOASSERTION | 2026-11-15 | End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment. |
| [The-Pocket/PocketFlow](https://github.com/The-Pocket/PocketFlow) | 11.3k | MIT | 2026-07-26 | Pocket Flow: 100-line LLM framework. Let Agents build Agents! |
| [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | 9.8k | MIT | 2026-11-16 | The 100 line AI agent that solves GitHub issues or helps you in your command line. Radically simple, no huge configs, no giant monorepo—but scores >74% on SWE-bench verified! |
| [ed-donner/agents](https://github.com/ed-donner/agents) | 6.6k | MIT | 2026-11-16 | Repo for the Complete Agentic AI Engineering Course |
| [ghuntley/how-to-build-a-coding-agent](https://github.com/ghuntley/how-to-build-a-coding-agent) | 5.9k | none | 2026-11-18 | A workshop that teaches you how to build your own coding agent. Similar to Roo code, Cline, Amp, Cursor, Windsurf or OpenCode. |
| [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | 4.9k | MIT | 2026-07-24 | Demystify AI agents by building them yourself. Local LLMs, no black boxes, real understanding of function calling, memory, and ReAct patterns. |
| [shareAI-lab/claw0](https://github.com/shareAI-lab/claw0) | 3.4k | none | 2026-06-30 | 0 - 1 learn OpenClaw: sections to build an claw-AI agent from scratch |
| [wquguru/harness-books](https://github.com/wquguru/harness-books) | 3.3k | none | 2026-04-19 | Harness engineering in two books: constraints, query loops, context governance and multi-agent verification in Claude Code and Codex. harness-books.agentway.dev |
| [1rgs/nanocode](https://github.com/1rgs/nanocode) | 2.8k | none | 2026-01-14 | Minimal Claude Code alternative. Single Python file, zero dependencies, ~250 lines. |
| [itayinbarr/little-coder](https://github.com/itayinbarr/little-coder) | 2.7k | Apache-2.0 | 2026-09-18 | A harness optimized to smaller LLMs |
| [czl9707/build-your-own-openclaw](https://github.com/czl9707/build-your-own-openclaw) | 1.9k | MIT | 2026-11-17 | A step-by-step guide to build your own AI agent. |
| [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | 1.2k | Apache-2.0 | 2026-10-24 | Learn harness engineering by building Claude Code from scratch. Free, open-source course: 8 articles, 6 videos, 1 codebase. |

## License

[CC0 1.0](LICENSE). Repository descriptions are quoted from GitHub.
