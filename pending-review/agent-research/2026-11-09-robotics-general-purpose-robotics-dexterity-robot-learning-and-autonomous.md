# Robotics Evidence Review: Dexterity Progress, General-Purpose Limits, and Autonomous Logistics Readiness
Tags: [research], [pending-review], [robotics]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-11-09
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

general-purpose robotics, dexterity, robot learning, and autonomous logistics

## Executive Summary

The November 2–9, 2026 evidence shows meaningful progress in dexterous manipulation, tactile feedback, simulation, robot-learning transfer, fleet infrastructure, and early logistics pilots. It does not establish reliable open-world, long-horizon physical autonomy. Positive results from DexHOT, T-Rex, NVIDIA, and related studies coexist with a 73% failure rate in ArmnetBench, severe long-horizon degradation in LADDER, low task scores and false-success reports in RoboARCade, reset and scene-drift failures in CRONOS, and only 20.70% success for a simulated recursive-improvement approach. The decision-relevant conclusion is mixed: narrow, structured, monitored deployments are expanding, while broad substitution of human coordination across transport, maintenance, construction, and care remains unsupported. Canon review should qualify robotics and drone-logistics claims, preserve other canon files unchanged, and continue monitoring fleet-level reliability, intervention, safety, economics, and open-world recovery.

## Research Scope

- Lane: `robotics`
- Research window: 2026-11-02 through 2026-11-09
- Tracked assumptions: `PS-ROBOTICS-001`, `PS-SPACE-001`, `PS-AI-003`, `PS-NEURO-001`, `PS-AI-001`

## Observed Developments

### DexArena introduces a standardized test for long-horizon bimanual dexterity

- Event date: 2026-11-02
- Sources: `S1`
- Observed fact: A research team released DexArena, a benchmark covering 10 long-horizon tasks and 30 stage-level tasks across household and industrial scenarios. The benchmark includes explicit stage-level success conditions, standardized simulation configurations, scene randomization, trajectory replay, and human-teleoperated demonstrations. The authors report substantial remaining difficulty in precise manipulation, generalization to scene variation, and composing skills across task stages.
- Significance: This is material because it shifts evaluation away from isolated grasps toward multi-stage behavior, where general-purpose robot learning is most likely to fail. It provides a more relevant measurement layer for whether a robot can coordinate perception, bimanual control, object handling, and skill transitions rather than merely demonstrate individual motions.

### DexHOT reports cross-object hand-and-object configuration transfer

- Event date: 2026-11-03
- Sources: `S2`
- Observed fact: DexHOT frames dexterous manipulation as transfer between feasible hand-object configurations rather than object-pose control alone. On a benchmark containing 120 objects, one policy achieved 80.5% transfer success on seen objects and 69.4% on unseen objects. On a real dexterous hand, it achieved 61.5% success over 200 transfers and 90% task success across six demonstration-guided tasks.
- Significance: The result is relevant to robot-learning transfer because it makes hand posture and contact configuration explicit, potentially improving composition of long-horizon skills. The unseen-object result is a concrete, though limited, signal that dexterity policies may generalize beyond memorized object instances.

### Human-object motion priors are used to improve dexterous learning and cross-embodiment transfer

- Event date: 2026-11-04
- Sources: `S3`, `S4`
- Observed fact: A study published during the window uses human-object interaction datasets to predict future hand-object states and convert those predictions into a general-purpose reinforcement-learning reward. The method was evaluated in simulation and on real robots across three manipulation tasks, and the authors report improved success and generalization on novel objects, including deployment across different robot hands.
- Significance: This is a notable robot-learning signal because it targets one of the main bottlenecks in dexterity: the expense of collecting task-specific robot demonstrations and engineering rewards. Human data are used as a source of object-centric motion priors rather than copied directly, which could help transfer skills across robot embodiments.

### T-Rex combines vision-language action generation with high-rate tactile correction

- Event date: 2026-11-05
- Sources: `S5`, `S6`
- Observed fact: Panasonic and academic and industry collaborators announced Tactile-Reactive Dexterous Manipulation (T-Rex), which combines approximately 5 Hz vision-language action generation with approximately 20 Hz fingertip-tactile action correction. Across 12 real-world contact-rich tasks, the system achieved a 65% average success rate versus 35% for the reported best baseline; removing tactile information reduced the average to 42%.
- Significance: This is one of the clearest recent measurements that tactile feedback can materially improve contact-rich manipulation beyond vision-language control alone. The task set includes page turning, egg transfer, applying toothpaste, unlocking with a key, card removal, and light-bulb screwing, which are closer to fragile or force-sensitive handling than simple pick-and-place.

### NVIDIA reports a broader simulation-and-foundation-model stack for dexterous robot learning

- Event date: 2026-11-09
- Sources: `S7`, `S8`
- Observed fact: At CoRL, NVIDIA described GR00T 2, Isaac Lab 3.0, Newton physics integration, Isaac Lab-Arena, and new benchmarks and agentic workflows. NVIDIA reports that GR00T 2 completed at least one attempt on 40 of 50 evaluated tasks without task-specific demonstrations, achieved 71% average success with one demonstration per task and 95% with five, and transferred skills between robot bodies without robot demonstrations. NVIDIA also reports up to 2.5x training throughput with Isaac Lab 3.0 and Newton on a vision-based dexterous benchmark, and a single policy achieving more than 98% training success across 20 NIST Assembly Task Board tasks using roughly 39x less GPU time than separate per-task policies.
- Significance: The development matters because it targets the scaling problem underlying general-purpose robotics: producing data, training policies, evaluating failures, and transferring skills across tasks and bodies. The reported results suggest progress in reducing simulation and training costs, while the open evaluation infrastructure could make claims easier to compare.

### Serve Robotics opens fleet-scale connectivity, data curation, and physical-AI infrastructure to other robot companies

- Event date: 2026-11-05
- Sources: `S9`
- Observed fact: Serve Robotics launched Physical AI Services on November 5. The offering includes technology for connecting robots to off-board intelligence, identifying valuable training data at fleet scale, and supplying real-world foundation-model data. Serve reported more than 2,000 deployed robots operating in over 40 cities and 27 hospitals, and said the platform already supports thousands of vehicles across construction, mining, autonomous trucking, and delivery applications.
- Significance: This is a material autonomous-logistics signal because it indicates that operational infrastructure around robot fleets—connectivity, data selection, monitoring, and learning loops—is becoming a product category separate from robot hardware. That infrastructure may be necessary for scaling autonomous systems beyond controlled pilots and could support transfer of operational lessons across different robot types.

### ID Logistics and Terra Robotics prepare a real-world humanoid sorting pilot in Germany

- Event date: 2026-11-01
- Sources: `S10`
- Observed fact: ID Logistics and Terra Robotics entered a strategic partnership effective November 1, 2026. The companies report that two Unitree G1 EDU6 humanoid robots learned the same sorting process in parallel. The robots can distinguish cartons from mailer bags and sort them into shipping boxes using five-fingered hands with tactile sensors. The partners plan to select a task from four or five candidate scenarios and begin a pilot under real operating conditions at an ID Logistics site in Germany within six months.
- Significance: This is a concrete logistics deployment signal, but still at the pilot stage. It shows that humanoid platforms with tactile hands are being evaluated for contract-logistics processes rather than only demonstrated in laboratories, and that the intended test is under real operating conditions rather than solely in simulation or a staged demonstration.

### Real-robot evaluation found a 73% failure rate across seven manipulation policies

- Event date: 2026-11-02
- Sources: `S11`, `S12`
- Observed fact: ArmnetBench released 3,118 autonomous rollouts from seven imitation-learning and vision-language-action policies across 12 tabletop tasks on low-cost SO-101 robot cells. Human operators labelled 73% of the autonomous rollouts as failures, with every policy evaluated on the same demonstrations, robot cell, and task set.
- Significance: This is direct counterevidence against treating broad robot-learning claims as evidence of reliable physical competence. The result shows that even when policies are evaluated on a standardized real-robot setup with shared demonstrations, most attempts can still fail. It also provides failure data that optimistic benchmark summaries often omit.

### Agentic robot control remains below dependable general-purpose performance and often misjudges its own success

- Event date: 2026-11-05
- Sources: `S13`
- Observed fact: RoboARCade evaluated agentic robot-control systems on long-horizon manipulation tasks across three robot embodiments with widened initial-condition variation. GPT-6 Astra achieved 49.8% and Claude Fable 5.1 achieved 43.6%. The benchmark reports that failures usually arose from selecting poor manipulation strategies or executing a suitable strategy imprecisely, while agents incorrectly claimed success on 24% to 39% of attempted subtasks.
- Significance: The findings challenge the assumption that stronger multimodal reasoning automatically produces reliable physical autonomy. The relatively low task scores, execution errors, and false-positive success reports point to a monitoring problem: an autonomous logistics system may not only fail, but also fail to recognize that it has failed.

### Naive continual robot learning collapses when scene resets become infrequent

- Event date: 2026-11-03
- Sources: `S14`
- Observed fact: CRONOS tested reinforcement-learning fine-tuning of pretrained vision-language-action policies under non-episodic scene resets, a setting intended to resemble continued real-world operation. Direct fine-tuning failed as reset intervals increased: OpenVLA success fell from 65% to 37% and then 0%, while SpatialVLA fell from 65% to 25% and then 2%. Objects progressively drifted out of reachable workspace, creating unrecoverable scenes that required human intervention. A heuristic reset strategy raised SpatialVLA success from 14% to 64% in one setting.
- Significance: This is a direct deployment barrier for claims that robots can learn continuously while working. Real facilities cannot assume clean episodic resets after every task. The study indicates that continual operation introduces state drift, unrecoverable configurations, and reset labor that can erase the expected economic advantage of autonomous learning.

### Failure localization and catastrophic forgetting remain obstacles to recursive robot improvement

- Event date: 2026-11-04
- Sources: `S15`
- Observed fact: A technical report on Compounding Physical RSI identifies three barriers to recursive improvement in generalist robot policies: terminal feedback rarely identifies which stage caused a failure, failed trajectories often lack corrective actions, and updating shared policy parameters can degrade previously learned skills. On the 42-task RoboDojo-Sim benchmark, the proposed system achieved a three-seed mean success rate of only 20.70%, despite ranking first among the evaluated entries.
- Significance: The result narrows optimistic interpretations of recursive AI progress in robotics. Even a method explicitly designed to convert failures into inherited capability remained at roughly one-fifth task success on its benchmark. The need for stage attribution, validated corrective data, and retention testing suggests that robot self-improvement is not an automatic consequence of collecting more execution traces.

### Benchmark design itself can overstate general manipulation capability

- Event date: 2026-11-02
- Sources: `S16`, `S17`
- Observed fact: A benchmark audit identified shortcut solvability, insufficient statistical significance, benchmark overfitting, and dependence on data sources as failure modes that weaken manipulation benchmarks as proxies for general capability. The audit reported that a 0.09-billion-parameter probe without a language encoder reached performance near reported state of the art on LIBERO, that many reported gains were not statistically established, and that randomizing block poses within the training range reduced performance for every tested policy on CALVIN.
- Significance: This challenges the evidentiary foundation behind optimistic robot-learning claims. High benchmark scores may reflect task shortcuts, fixed layouts, or evaluation artifacts rather than transferable dexterity. If benchmark gains do not survive small variations or stronger diagnostics, they should not be treated as evidence that robots can coordinate diverse logistics, maintenance, construction, or care work.

### Regulatory review blocked SoftBank’s acquisition of ABB’s robotics business in China

- Event date: 2026-11-06
- Sources: `S18`
- Observed fact: SoftBank reported on November 6 that China’s Office of the Working Mechanism for Foreign Investment Security Review had prohibited SoftBank’s acquisition of ABB’s robotics business in China. The transaction remained subject to regulatory approvals and other closing conditions.
- Significance: This is counterevidence against assuming that robotics capacity, supply chains, and consolidation can scale frictionlessly across markets. Foreign-investment screening can block ownership transfers involving robotics assets, creating geopolitical, regulatory, and operational fragmentation for companies attempting to build globally integrated robotics platforms.

### Long-horizon manipulation success collapses even when short-horizon policies look strong

- Event date: 2026-11-02
- Sources: `S19`, `S20`
- Observed fact: The LADDER benchmark reported that low-level policies achieving 85.4% success on single-subgoal simulated tasks fell to 5.2%–15.8% on two-to-ten-subgoal tasks and to 0.5% on eight-to-ten-subgoal tasks. In real-robot tests, corresponding success was 1.2% on WidowX and 5.6% on Franka. Tool-calling orchestration improved performance, but GPT-Policy reached about 62% overall while incurring approximately $4.02 in API cost per episode and $8,134 for one full evaluation.
- Significance: This is a strong falsifier for extrapolating isolated skill demonstrations into general-purpose logistics competence. Chaining otherwise competent subtasks creates multiplicative reliability losses, and using frontier-model orchestration introduces latency and inference costs that may be incompatible with high-throughput operations.

## Assumption Assessments

### PS-ROBOTICS-001: Embodied AI automates material coordination

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S5`, `S7`, `S9`, `S10`, `S11`, `S13`, `S14`, `S15`, `S18`, `S19`
- Evidence: Evidence shows meaningful progress in dexterous manipulation, tactile feedback, simulation, fleet infrastructure, and early logistics pilots. However, real-robot and long-horizon evaluations report substantial failure: ArmnetBench found a 73% failure rate, LADDER found success collapsing to 0.5% on eight-to-ten-subgoal tasks, and RoboARCade found low task scores and frequent false success reports. Deployment counts exist for delivery robots, but audited cost per productive hour, intervention rates, uptime, safety, and labor-substitution economics are absent. The evidence supports growth in narrow or structured automation, but not yet reliable general-purpose coordination across transport, maintenance, construction, and care.
- Real-world implication: Robot deployment and supporting data infrastructure are expanding, especially in delivery and structured logistics, while general-purpose embodied autonomy remains unreliable outside constrained tasks. Near-term adoption is more likely to favor narrow, monitored applications than broad substitution of human coordination across diverse physical work.
- PostSingularity implication: A post-singularity setting can plausibly contain extensive embodied automation, but reliable material coordination should not be treated as automatic. The storyworld would need to account for intervention, reset, maintenance, supply-chain, regulatory, and failure-management systems unless substantially stronger evidence of robust open-world autonomy emerges.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied evidence concerns terrestrial robotics, manipulation benchmarks, logistics pilots, and robotics-sector regulatory friction. It contains no audited evidence on launch cost, orbital station duration, closed-loop life support, in-space manufacturing, autonomous space missions, or human health limits in long-duration off-world habitats.
- Real-world implication: No directional update to the practicality of sustained orbital or off-world settlement is warranted from the supplied evidence. The claim remains dependent on unassessed aerospace, life-support, health, and economic developments.
- PostSingularity implication: The assumption may remain available as a storyworld possibility, but the supplied record does not justify treating abundant energy or autonomous systems as sufficient conditions for settlement. Habitat reliability, human biology, logistics, and governance would still require explicit support.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied evidence includes benchmark audits and discussion of robot-policy failure reporting, but it provides no direct evidence on AI transparency standards, content provenance adoption, model-audit regimes, regulatory disclosure rules, or broader social demand for inspectable AI provenance and graduated oversight.
- Real-world implication: No directional conclusion about the strengthening or weakening of provenance and audit systems is supported. Robotics benchmark evidence shows that evaluation quality matters, but it does not establish broader institutional adoption of AI provenance systems.
- PostSingularity implication: A post-singularity society could plausibly use provenance rituals and audit trails, but the supplied evidence does not establish that such systems become socially required, widely adopted, or effective against high-impact opaque systems.

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: No supplied source reports neural-interface channel count, bidirectional implants, long-term implant safety, decoded speech or affect, sensory communication, emotional communication, or durable neural bandwidth improvements.
- Real-world implication: There is no evidence in the supplied record to update the feasibility or timing of safe, high-bandwidth neural interfaces. Tissue response, privacy, safety, and long-term usability remain unresolved within this evidence set.
- PostSingularity implication: Rich two-way communication between nervous systems and AI remains an unsupported storyworld capability here. If included, it should be treated as a separate technological development requiring evidence for durable interfaces, safety, privacy, and meaningful sensory or affective bandwidth.

### PS-AI-001: Recursive AI progress can create a societal discontinuity

- Proposed verdict: **insufficient-evidence**
- Confidence: **medium**
- Sources: `S7`, `S8`, `S13`, `S14`, `S15`
- Evidence: The supplied robotics evidence shows progress in simulation, tactile manipulation, policy transfer, and fleet data systems, but it also documents weak long-horizon reliability, catastrophic forgetting, failure-localization problems, and only 20.70% success for a simulated system explicitly aimed at compounding physical improvement. These results provide no direct measurement of recursive AI research automation, general capability acceleration, or institutional adaptation speed, and no evidence establishes a societal discontinuity.
- Real-world implication: The record supports neither a claim that recursive improvement is producing a near-term institutional discontinuity nor a claim that such a discontinuity is impossible. In robotics, self-improvement remains technically constrained rather than visibly self-sustaining; broader AI research automation and governance response are unmeasured here.
- PostSingularity implication: The supplied evidence does not justify assuming that existing institutions become irrelevant through recursive AI progress. A post-singularity transition remains a scenario possibility, but it requires separate evidence for rapid general capability gains, feedback loops in AI research, and failure of institutions to adapt.

## Canon Implementation Plan

### `worldbible/technologies/robotics.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S2`, `S3`, `S5`, `S7`, `S10`, `S11`, `S13`, `S14`, `S15`, `S19`
- Why this location: The evidence supports meaningful advances in dexterous manipulation, tactile correction, transfer learning, simulation, and early logistics pilots, but it also shows that general-purpose reliability remains unestablished. ArmnetBench reported a 73% autonomous-rollout failure rate, LADDER reported severe long-horizon degradation, and RoboARCade found both low task scores and frequent false-success reports.
- Proposed change: Add a qualification to the Summary stating that adaptive robots can perform increasingly capable structured manipulation and logistics tasks, but dependable open-world coordination remains limited by long-horizon error accumulation, scene drift, failure recognition, recovery, and human intervention. Preserve the existing claims about adaptive bodies, emotional context, swarm coordination, and human intention while narrowing any implication that these capabilities are universally reliable.
- Implementation steps:
  1. Insert the qualification at the end of the existing Summary, after the current description of adaptive robots, swarm coordination, and human intention.
  2. Name long-horizon composition, infrequent-reset operation, false success reporting, and recovery from unrecoverable states as the specific unresolved limitations rather than describing robots as broadly dependable.
  3. Add source-facing terminology for structured tasks, pilots, and monitored operation so the canon distinguishes laboratory or benchmark capability from sustained open-world deployment.
  4. Review the Function and Story Use sections after this change to ensure examples of autonomous repair and rogue-swarm behavior do not imply unattended reliability that the revised Summary explicitly limits.
- Dependencies or conflicts:
  - The existing Summary presents emotional telemetry and Trust Fabrics as mechanisms that keep human intention central; the new qualification should not imply that oversight mechanisms eliminate mechanical failure or deployment constraints.
  - The existing robotics metadata states an introduced cycle of 3 and impacts of adaptive labor and human-robot symbiosis; the proposed change does not require chronology changes but may require a later metadata note if the setting distinguishes demonstration capability from mature deployment.
  - Results from S5 and S7 are company-reported or first-party, while S11, S13, S14, S15, and S19 use different embodiments, horizons, and success definitions; the text must avoid treating their percentages as directly comparable.

### `worldbible/technologies/robotics.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S9`, `S10`, `S11`, `S13`, `S14`, `S15`, `S18`, `S19`
- Why this location: The reviewed evidence adds material tensions absent from the supplied robotics excerpt: deployment requires monitoring and reset labor, autonomous systems may misjudge their own success, recursive improvement can cause forgetting, and robotics supply chains face regulatory ownership friction. These issues directly deepen the file’s treatment of autonomy and human control.
- Proposed change: Add a subsection under Philosophical Tensions covering the obligations created by failure-aware deployment: who performs resets and recovery, who is accountable when a robot incorrectly reports success, whether corrective learning can damage existing skills, and how regulatory or ownership barriers fragment supposedly global robotic infrastructure.
- Implementation steps:
  1. Insert the new subsection under Philosophical Tensions, using the closest existing heading as the anchor and retaining the file’s existing philosophical framing.
  2. Describe human intervention, reset labor, auditability of success claims, catastrophic forgetting, and supply-chain or ownership restrictions as unresolved social questions rather than settled technical defects.
  3. Cross-reference Trust Fabrics only for oversight and provenance concepts; do not imply that trust protocols solve physical recovery, uptime, or regulatory problems.
  4. Review Story Use for opportunities to represent intervention, maintenance, failed handoffs, or contested accountability without changing the existing Arin and rogue-swarm examples.
- Dependencies or conflicts:
  - Trust Fabrics and AI Trust describe transparency, verification, and communal oversight, but the cited robotics evidence does not establish that such systems provide reliable physical recovery or accurate self-reporting.
  - The SoftBank disclosure in S18 concerns an acquisition prohibition in China, not a general deployment ban; the wording must preserve this distinction and avoid turning one transaction into universal geopolitical canon.
  - The 20.70% result in S15 is simulated and the CRONOS evidence in S14 is primarily simulation-based; both should be framed as warnings about failure modes, not direct predictions of physical fleet performance.

### `worldbible/technologies/drone-logistics.md` -> Cultural Effects

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S9`, `S10`, `S11`, `S13`, `S14`, `S18`, `S19`
- Why this location: The file currently describes drone logistics as globally coordinated, near-instant, and largely replacing manual shipping. The evidence supports expansion of fleet infrastructure and structured logistics, especially through Serve’s reported deployment, but does not support generalized reliability, unattended operation, or equivalent performance across humanoid and dexterous systems.
- Proposed change: Qualify the Cultural Effects section by distinguishing mature, monitored delivery networks from experimental or pilot-stage general-purpose robotics. Add that communities experience both expanded access and new dependence on intervention crews, recovery procedures, data infrastructure, regulatory permissions, and uneven service reliability.
- Implementation steps:
  1. Insert the qualification after the existing Cultural Effects bullets, preserving the current claims about remote access, drone corridors, piloting competitions, and rejection of drones.
  2. State that the strongest evidence concerns delivery or structured logistics infrastructure, while humanoid sorting and dexterous manipulation remain pilot or benchmark-stage capabilities.
  3. Add a cross-reference to Robotics for the distinction between narrow fleet deployment and broad adaptive physical autonomy.
  4. Review the Summary and Function sections for any wording that implies all fleets operate with uniform autonomy, instant response, or uninterrupted equitable distribution.
- Dependencies or conflicts:
  - S9 reports more than 2,000 deployed robots and platform support, but the figures are company-reported and do not establish uptime, intervention frequency, safety, or cost per productive hour.
  - S10 describes a planned German pilot rather than a completed deployment; the file should not present it as established logistics capability.
  - The existing statement that fleets replaced most manual shipping and enabled equitable distribution is broader than the supplied evidence. A human canon review should decide whether that claim is intentional post-singularity background or should be narrowed to avoid conflating fictional maturity with current evidence.
  - S18 establishes ownership and regulatory friction in one transaction, not a comprehensive global logistics constraint; any added cultural effect should remain geographically and causally bounded.

### Nearby Canon Used for Context

- [`worldbible/technologies/robotics.md`](../../worldbible/technologies/robotics.md) — declared canon source for PS-ROBOTICS-001
- [`worldbible/technologies/drone-logistics.md`](../../worldbible/technologies/drone-logistics.md) — declared canon source for PS-ROBOTICS-001
- [`worldbible/technologies/aerospace-systems.md`](../../worldbible/technologies/aerospace-systems.md) — declared canon source for PS-SPACE-001
- [`worldbible/technologies/trust-fabrics.md`](../../worldbible/technologies/trust-fabrics.md) — declared canon source for PS-AI-003
- [`philosophy/ai-trust.md`](../../philosophy/ai-trust.md) — declared canon source for PS-AI-003
- [`worldbible/technologies/neural-links.md`](../../worldbible/technologies/neural-links.md) — declared canon source for PS-NEURO-001
- [`worldbible/singularity-event.md`](../../worldbible/singularity-event.md) — declared canon source for PS-AI-001
- [`worldbible/timeline.md`](../../worldbible/timeline.md) — declared canon source for PS-AI-001
- [`worldbible/technologies/index.md`](../../worldbible/technologies/index.md) — content: and, drone, logistics, robotics; robotics directory preference
- [`locations/analog-haven.md`](../../locations/analog-haven.md) — content: and, embodied; robotics directory preference
- [`locations/orbital-sanctuary.md`](../../locations/orbital-sanctuary.md) — content: and, logistics; robotics directory preference
- [`worldbible/technologies/ai-agents.md`](../../worldbible/technologies/ai-agents.md) — content: and, learning; robotics directory preference

## Uncertainties

- Positive benchmark and laboratory results report substantial dexterity, transfer, tactile-feedback, and simulation-training improvements, while ArmnetBench reports a 73% failure rate across real-robot rollouts and LADDER reports severe long-horizon success collapse. These results are not directly numerically comparable because they use different robots, tasks, success definitions, and environments.
- NVIDIA reports 71% average success with one demonstration and 95% with five on its evaluated tasks, whereas RoboARCade reports 43.6% and 49.8% for evaluated agentic systems and LADDER reports 0.5% on eight-to-ten-subgoal tasks. The difference may reflect task horizon, embodiment, benchmark design, and whether results are simulation or physical-robot measurements; it does not establish that any claim is false.
- DexHOT reports 61.5% success over 200 real-robot transfers and T-Rex reports 65% average success across 12 real-world tasks, but neither result demonstrates sustained unattended operation, throughput, intervention rate, or deployment economics.
- Serve Robotics reports more than 2,000 deployed robots and platform support for thousands of vehicles, while the ID Logistics and Terra Robotics announcement concerns a planned pilot that had not yet begun. These are different deployment stages and should not be combined as evidence of general-purpose humanoid deployment.
- Benchmark audits and counterbenchmarks identify shortcut solvability, weak statistical significance, overfitting, scene-reset failures, and long-horizon degradation. Consequently, headline benchmark scores from DexArena, NVIDIA, or other sources should not be interpreted as equivalent evidence of general capability.
- The November 6 SoftBank disclosure documents regulatory prohibition of an acquisition in China, but it does not contradict evidence of robot operation or technical capability; it demonstrates regulatory and ownership friction rather than deployment failure.
- Source identifiers were deduplicated and renumbered from S1 through S20. Every development references only valid source IDs.
- The strongest evidence is primary research, but several sources are company or platform announcements and therefore company-reported rather than independently audited.
- The Panasonic T-Rex result is company-reported in the release; the associated research paper is older than the priority window and provides technical context rather than an in-window independent audit.
- The NVIDIA figures are first-party reports and include simulation, benchmark, and training-efficiency results. They do not establish sustained physical deployment, safety, intervention rates, cycle time, or total operating cost.
- Serve Robotics deployment counts and platform capabilities are company-reported, with no independent uptime, intervention-rate, safety, or unit-economics data in the release.
- The ID Logistics and Terra Robotics announcement concerns a planned pilot. The real operating pilot had not yet begun at the time of the announcement and is planned for the following six months.
- ArmnetBench provides direct real-robot counterevidence, but it uses low-cost SO-101 arms and tabletop tasks rather than humanoids, mobile manipulators, or warehouse-scale logistics.
- RoboARCade and CRONOS are primarily simulation-based and do not establish warehouse-scale or long-duration physical performance.
- Compounding Physical RSI is a technical preprint and its benchmark is simulated rather than a sustained physical deployment.
- The benchmark audit was published before the priority window, although it remained directly relevant to benchmark interpretation during the window.
- LADDER was published before the priority window; its evidence remains relevant but is not an in-window publication.
- MekaWire is a secondary account of LADDER and is retained as supporting context, not as a replacement for the primary paper.
- No authoritative source found in the priority window reported audited cost per productive hour, total cost of ownership, or labor-substitution economics for humanoid or dexterous logistics robots.
- No regulatory filing or independent safety evaluation was found for the announced humanoid logistics pilots or the new dexterous manipulation systems.
- Deployment counts were available from Serve Robotics, but comparable fleet counts, uptime, intervention rates, and task-level productivity were not available for the other companies reviewed.
- The strongest dexterity results in the window remain benchmark, laboratory, or company-reported demonstrations; evidence for sustained open-world operation outside structured environments remains thin.
- No large-scale independent comparison was found between humanoid robots, conventional fixed automation, autonomous mobile robots, and human labor using the same task mix, throughput definition, uptime window, and safety accounting.
- No authoritative incident database was found that reports robot-caused worker injuries, near misses, or hazardous failures for the newest humanoid and dexterous-robot pilots in the priority window.
- The search found evidence of regulatory friction affecting robotics corporate ownership, but not a comprehensive map of export controls, certification requirements, insurance barriers, or labor-law constraints governing general-purpose robot deployment.
- Safety and security findings involving malicious prompts, backdoored planners, or unsafe robot instructions were found mainly outside the November 2–9 window; a dated in-window primary safety evaluation would strengthen the counterevidence packet.
- Benchmark failures do not by themselves establish that commercial fixed-automation systems are uneconomic; the main unresolved question is whether narrow, highly structured deployments can remain profitable while general-purpose claims continue to underperform.
- The benchmark and laboratory results do not support the claim that general-purpose robots have achieved reliable open-world physical competence.
- The DexArena benchmark does not establish reliable physical-robot performance, production-ready policies, or cost per productive hour.
- DexHOT’s transfer results do not establish robustness across many robot morphologies, cluttered logistics settings, deformable goods, or prolonged operation.
- The human-object motion-prior study does not establish reliable general transfer across substantially different morphologies or broad warehouse deployment.
- T-Rex’s 65% average success rate does not establish unattended reliability, long-duration operation, maintenance requirements, throughput, or economic viability.
- NVIDIA’s ‘completed at least one attempt’ result is not evidence of dependable reliability. Simulation-throughput gains and training success do not establish sustained physical deployment.
- Serve Robotics’ reported fleet count does not show that one general-purpose robot can perform many logistics tasks or that the service improves cost per productive hour.
- The ID Logistics and Terra Robotics announcement does not establish a completed deployment, throughput, error rate, intervention rate, uptime, safety performance, labor comparison, or cost per productive hour.
- The ArmnetBench 73% failure rate should not be generalized to every policy, robot morphology, or warehouse environment.
- RoboARCade’s false-success rates should not be treated as quantitative predictions of industrial failure rates.
- CRONOS does not prove that physical-world resets can be performed cheaply or safely, and its simulation results do not establish a complete commercial fleet-management system.
- The Compounding Physical RSI ranking and 20.70% success rate do not establish broad real-world generalization or automatic recursive improvement from execution traces.
- The benchmark audit does not prove that the underlying robot policies lack capability outside the audited settings.
- The SoftBank regulatory decision does not establish a general ban on robot deployment or robot exports, and a single transaction cannot establish the future frequency of similar interventions.
- LADDER’s benchmark and cost results do not establish production pricing, caching arrangements, or performance across pushing, sliding, articulated objects, and logistics-specific interactions.
- No claim that autonomous systems coordinate a growing share of maintenance, construction, or care work at scale with independently verified economic results is supported by the supplied evidence.
- No claim of audited cost per productive hour, total cost of ownership, labor substitution, maintenance burden, or profitability for general-purpose humanoid or dexterous logistics robots is supported by the supplied evidence.
- PS-SPACE-001 is assessed as insufficient-evidence with no directional update. The supplied sources address terrestrial robotics, manipulation, logistics, and one ownership transaction, not launch economics, orbital settlement, closed-loop life support, in-space manufacturing, autonomous space missions, or long-duration human health. No edit is warranted in worldbible/technologies/aerospace-systems.md or locations/orbital-sanctuary.md from this evidence set.
- PS-AI-003 is assessed as insufficient-evidence. Benchmark and robot-policy audit findings establish that evaluation quality matters, but they do not demonstrate adoption of AI provenance standards, transparency regulation, model-audit regimes, or socially required oversight. No change is warranted in worldbible/technologies/trust-fabrics.md or philosophy/ai-trust.md.
- PS-NEURO-001 is assessed as insufficient-evidence. No supplied source addresses neural-interface bandwidth, bidirectional implants, decoded affect, sensory communication, long-term implant safety, privacy, or durability. No change is warranted in worldbible/technologies/neural-links.md.
- PS-AI-001 is assessed as insufficient-evidence rather than directional. S7, S8, S13, S14, and S15 provide robotics learning and failure evidence, but none measures recursive AI research automation, general capability acceleration, or institutional discontinuity. No change is warranted in worldbible/singularity-event.md or worldbible/timeline.md.
- The technology index does not require an edit: the reviewed evidence does not introduce a new technology file or invalidate the existing Robotics and Drone Logistics links. Any index change should wait for an approved terminology or taxonomy decision.
- No supplied evidence establishes audited cost per productive hour, total cost of ownership, labor substitution, maintenance burden, safety performance, or profitability for general-purpose robots. These claims should remain unadded until the watchlist evidence is available.
- The evidence mixes simulation, laboratory demonstrations, company-reported results, tabletop real-robot benchmarks, and early pilots; these measures are not directly comparable.
- No audited cost per productive hour, total cost of ownership, uptime, intervention rate, maintenance burden, or labor-substitution result is supplied for general-purpose robots.
- The extent to which benchmark performance transfers to open-world transport, maintenance, construction, or care work remains unresolved.
- The supplied sources do not cover aerospace settlement, neural interfaces, AI provenance institutions, or broad recursive AI capability trends.
- Several positive robotics results are first-party or company-reported, while the strongest counterevidence comes from independent benchmark studies with different task definitions and embodiments.
- Regulatory and ownership friction is evidenced by one robotics transaction but is not a comprehensive account of export controls, certification, insurance, labor law, or deployment constraints.

## Watchlist

- Independent fleet-level measurements of robot uptime, intervention frequency, safety incidents, throughput, maintenance, and cost per productive hour.
- Long-horizon, open-world physical evaluations across varied environments and embodiments, including recovery from unrecoverable states and infrequent-reset operation.
- Completed real-world logistics pilots reporting error rates, human intervention, cycle time, safety performance, and comparison with conventional automation and human labor.
- Evidence of autonomous AI research automation, sustained capability acceleration, and whether institutional adaptation keeps pace.
- Adoption and enforcement of AI provenance, model-audit, disclosure, and verification standards for high-impact systems.
- Launch economics, closed-loop life-support duration, human health outcomes, in-space manufacturing, and autonomous mission operations.
- Neural-interface channel bandwidth, bidirectional sensory or affective decoding, long-term implant safety, privacy outcomes, and durability.

## Sources

- `S1` [DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation](https://arxiv.org/abs/2611.02629) — arXiv; 2026-11-02; primary-research; URL supplied in structured research output. Primary research source introducing the benchmark, its task structure, evaluation protocol, and baseline findings.
- `S2` [DexHOT: Learning Hand–Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119) — arXiv; 2026-11-03; primary-research; URL supplied in structured research output. Primary paper reporting quantitative seen-object, unseen-object, and real-robot transfer results.
- `S3` [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979) — arXiv; 2026-11-04; primary-research; URL supplied in structured research output. Primary research source describing the human-data-to-reward pipeline, real-world experiments, novel-object generalization, and cross-embodiment tests.
- `S4` [AAAI Proceedings record for Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://ojs.aaai.org/index.php/AAAI/article/view/38892) — AAAI; 2026-01-01; primary-research; URL supplied in structured research output. Author-linked proceedings record confirming the paper’s formal publication venue and oral-paper status.
- `S5` [Panasonic HD Co-Develops a Robot Manipulation AI That Performs Dexterous Bimanual Tasks by Reacting Instantly to Fingertip Touch](https://news.panasonic.com/global/press/en261105-2) — Panasonic Holdings Corporation; 2026-11-05; official-release; URL supplied in structured research output. First-party release containing the architecture, update rates, task list, baseline comparison, and tactile-ablation result.
- `S6` [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055) — arXiv; 2026-06-22; primary-research; URL supplied in structured research output. Associated research paper providing the technical basis for the announced tactile-reactive system.
- `S7` [Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/) — NVIDIA; 2026-11-09; official-release; URL supplied in structured research output. First-party technical announcement with quantitative GR00T 2, simulation-throughput, policy-training, benchmark, and industrial-partner claims.
- `S8` [NVIDIA Advances Isaac Platform for General-Purpose Robotics With New Reference Humanoid, Frameworks, Simulation Pipelines and Data](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Advances-Isaac-Platform-for-General-Purpose-Robotics-With-New-Reference-Humanoid-Frameworks-Simulation-Pipelines-and-Data/default.aspx) — NVIDIA; 2026-10-21; official-release; URL supplied in structured research output. First-party platform release detailing Isaac Lab 3.0, the reference humanoid, robot-learning workflows, datasets, and safety-related integration; included as supporting context for the November 9 CoRL announcements.
- `S9` [Serve Robotics Launches Physical AI Services, Opening Technology Behind Its Robot Fleets to Leading Physical AI Companies](https://serverobotics.gcs-web.com/node/10031/pdf) — Serve Robotics; 2026-11-05; official-release; URL supplied in structured research output. First-party release reporting deployment counts, operating geographies, hospital operations, platform functions, and external launch customers.
- `S10` [ID Logistics and Terra Robotics Pave the Way for Humanoid Robotics in Contract Logistics](https://www.id-logistics.com/media/2026/11/PR-ID-Logistics-Humanoid-Robots-Germany.pdf) — ID Logistics and Terra Robotics; 2026-11-01; official-release; URL supplied in structured research output. Primary company release documenting the partnership date, two-robot setup, tactile sorting capability, candidate applications, and planned real-world pilot.
- `S11` [Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks](https://arxiv.org/abs/2611.03168) — arXiv; 2026-11-02; primary-research; URL supplied in structured research output. Primary release of the real-robot rollout corpus, including the 3,118 autonomous episodes, seven evaluated policies, 12 tasks, and 73% failure rate.
- `S12` [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](https://arxiv.org/abs/2607.24481) — arXiv; 2026-07-30; primary-research; URL supplied in structured research output. Underlying benchmark paper describing the shared demonstrations, multi-cell evaluation design, policy comparison, and three-way episode labels.
- `S13` [RoboARCade: Benchmarking Agentic Robot Control](https://arxiv.org/abs/2611.08209) — arXiv; 2026-11-05; primary-research; URL supplied in structured research output. Primary benchmark paper reporting task scores, failure causes, widened initial conditions, and agent success-claim errors.
- `S14` [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080) — arXiv; 2026-11-03; primary-research; URL supplied in structured research output. Primary study quantifying performance decay under infrequent scene resets, unrecoverable states, human intervention requirements, and recovery from targeted reset strategies.
- `S15` [Compounding Physical RSI: Turning Execution Failure into Inherited Capability](https://arxiv.org/abs/2611.06654) — arXiv; 2026-11-04; primary-research; URL supplied in structured research output. Primary technical report documenting failure-localization, corrective-data, and skill-retention barriers, together with the reported 20.70% success rate.
- `S16` [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) — arXiv; 2026-06-02; primary-research; URL supplied in structured research output. Primary audit of manipulation benchmarks, reporting shortcut solutions, weak statistical evidence, overfitting, and sensitivity to modest scene variation.
- `S17` [Robot Manipulation Benchmark Audit Artifacts](https://ripl.github.io/manipulation_benchmark_audit/) — University of Illinois Robotics and Intelligent Perception Lab; unknown; primary-research; URL supplied in structured research output. Repository containing the diagnostics and artifacts used to test whether benchmark scores support claims of general manipulation capability.
- `S18` [Update on Acquisition of ABB Ltd’s Robotics Business](https://group.softbank/media/Project/sbg/sbg/news/press/2026/20261106/pdf/20261106_en.pdf) — SoftBank Group Corp.; 2026-11-06; official-release; URL supplied in structured research output. Official disclosure confirming the Chinese regulatory prohibition and the continuing approval conditions affecting the robotics transaction.
- `S19` [LADDER: A Long-Horizon Robot Manipulation Benchmark](https://arxiv.org/abs/2610.18053) — arXiv; 2026-10-22; primary-research; URL supplied in structured research output. Primary benchmark reporting the collapse from short-horizon to long-horizon success, real-robot results, orchestration limits, and inference-cost measurements.
- `S20` [LADDER benchmark analysis and full paper reproduction](https://mekawire.com/papers/ladder-a-long-horizon-robot-manipulation-benchmark-2610-18053) — MekaWire; unknown; reputable-secondary; URL supplied in structured research output. Secondary account reproducing the benchmark’s task-horizon results, cost figures, real-robot limitations, and failure analysis.

## Human Review Checklist

- [ ] Open every source and verify the cited claim and date.
- [ ] Confirm demonstrations are not described as deployments.
- [ ] Check for contradictory evidence and missing primary sources.
- [ ] Accept, revise, or reject each proposed assumption verdict.
- [ ] Verify every target file and heading still exists.
- [ ] Accept, revise, or reject each proposed repository edit.
- [ ] Move accepted changes through the normal contribution workflow.

```json
{
  "id": "research_2026-11-09_general-purpose-robotics-dexterity-robot-learnin",
  "type": "research_brief",
  "name": "Robotics Evidence Review: Dexterity Progress, General-Purpose Limits, and Autonomous Logistics Readiness",
  "tags": [
    "research",
    "pending-review",
    "robotics"
  ],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": [
    "assumption tracking",
    "canon review"
  ],
  "tracked_assumptions": [
    "PS-ROBOTICS-001",
    "PS-SPACE-001",
    "PS-AI-003",
    "PS-NEURO-001",
    "PS-AI-001"
  ],
  "generated_by": "postsingularity-research",
  "mock": false
}
```
