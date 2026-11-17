# Robotics 2026-11-10 to 2026-11-17: Deployment Expansion Without Proven General-Purpose Dexterity
Tags: [research], [pending-review], [robotics]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-11-17
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

general-purpose robotics, dexterity, robot learning, and autonomous logistics

## Executive Summary

The audited window strengthens the case that embodied AI is expanding as a task-specific capacity layer in autonomous delivery, warehouse trials, factory coordination, security, and human-machine emergency response. DoorDash reports hundreds of thousands of aggregate autonomous deliveries; GXO and Apptronik describe conditional future humanoid trials; Toyota describes large planned robotics investment; and Ring reports autonomous indoor navigation products. Research also reports faster simulation and optimization, contact-rich humanoid reaching, and improved targeted learning. However, the evidence does not establish broad general-purpose automation or current large-scale labor substitution. Persistent grasp failures, benchmark distribution gaps, unfamiliar-partner brittleness, humanoid safety hazards, utilization and workflow requirements, supply-chain constraints, and missing independent cost-per-productive-hour data remain decisive constraints. Recommended canon action is limited revision of robotics and drone-logistics descriptions to qualify deployment, learning, safety, and economics claims; no registry or unrelated canon updates are warranted.

## Research Scope

- Lane: `robotics`
- Research window: 2026-11-10 through 2026-11-17
- Tracked assumptions: `PS-ROBOTICS-001`, `PS-SPACE-001`, `PS-AI-003`, `PS-NEURO-001`, `PS-AI-001`

## Observed Developments

### DoorDash reports hundreds of thousands of autonomous deliveries across its robot and drone network

- Event date: 2026-11-12
- Sources: `S1`
- Observed fact: DoorDash Labs reported that it had completed hundreds of thousands of lifetime autonomous deliveries across its Dot delivery robots and other robot and drone partners. Dot uses eight cameras, lidar, radar, cloud-based simulation, and logged intervention data; software changes are tested against millions of simulated driving scenarios before real-world validation. Dot is designed to operate in bike lanes at speeds of up to 25 mph. The broader Autonomous Delivery Platform matches orders among human Dashers, ground robots, and drones using variables including order size, distance, traffic, and merchant preparation.
- Significance: This is one of the clearest deployment signals in the window for autonomous logistics. It indicates that robot delivery is being integrated as a capacity-management layer alongside human labor rather than treated as a standalone replacement. The learning loop—real-world logs, simulation, software updates, and field confirmation—is materially relevant to robot-learning transfer and cost-per-productive-hour, although the source does not provide per-robot utilization, intervention rates, delivery cost, or profitability.

### GXO and Apptronik establish a path toward scaled Apollo humanoid deployment

- Event date: 2026-11-12
- Sources: `S2`
- Observed fact: GXO Logistics and Apptronik announced an expanded partnership covering live operational trials of Apollo humanoid robots and a planned Robotics-as-a-Service framework. The companies said they had already conducted data collection and live autonomous evaluations on more than 50 logistics tasks at Apptronik’s Robot Park. Planned trials beginning in 2027 will cover goods-to-person and person-to-goods picking, case and tote movement, packing, and sortation. Subject to productivity, safety, and operational performance, the companies intend to work toward a global rollout of up to 1,000 Apollo robots over four years, with initial North American deployment expected in late 2027.
- Significance: The material development is not current mass deployment but the shift from demonstrations toward KPI-gated commercial trials across multiple warehouse workflows. The use of a Robotics-as-a-Service model could lower adoption barriers and make robot capability measurable as an operating expense. The breadth of the task list is relevant to the prediction that embodied AI will automate material coordination beyond one narrow warehouse motion.

### Toyota outlines a factory-robotics program linking production, logistics, and skilled-worker data

- Event date: 2026-11-11
- Sources: `S3`
- Observed fact: Toyota described a three-stage automation strategy progressing from conventional repetitive-task robots, to synchronized end-to-end production and logistics, to people-and-robot collaboration. Toyota said it and its suppliers expect to invest approximately JPY 1 trillion, or about $6.3 billion, annually from 2028 onward to renew aging production equipment. The company estimated that this investment could support approximately 150,000 robots across Toyota and Toyota Group companies and 250,000 robots at suppliers. Toyota also described an integrated Factory Control Platform connecting equipment, logistics, and the supply chain, with physical AI systems learning from approximately 18,000 highly skilled Takumi workers worldwide.
- Significance: This is a significant industrial-scale signal for embodied AI because it connects robot deployment to manufacturing process data, skilled human demonstrations, and logistics coordination rather than isolated robot cells. If executed, the planned installed base would provide a large environment for transfer learning and validation of collaborative robotics. However, the figures are future investment and deployment targets, not current robot counts or demonstrated general-purpose capability.

### Amazon’s Ring Robotics launches autonomous indoor security robots

- Event date: 2026-11-10
- Sources: `S4`
- Observed fact: Ring announced two autonomous mobile products: Ring Drone Cam, an indoor flying security camera, and Ring Rover Cam, a wheeled business-security robot. The company said both use its AI Pilot system to map spaces, suggest patrol points, navigate around obstacles, and perform patrol or investigation tasks automatically. Ring Rover Cam is described as autonomously patrolling business premises, investigating disturbances, and streaming video at up to 4K resolution.
- Significance: The launch is evidence of general-purpose mobile autonomy moving into a consumer and commercial service category, with robots expected to navigate changing indoor environments rather than repeat a fixed industrial motion. It is relevant to embodied-AI adoption, but it is a weaker signal for general-purpose manipulation because the products are primarily perception, navigation, and surveillance systems.

### RoboKit reports large simulation and optimization speedups for robot learning

- Event date: 2026-11-15
- Sources: `S5`
- Observed fact: RoboKit, a proposed general-purpose toolkit for differentiable robot optimization, reported 2–60× speedups over task-specific baselines across seven tasks. The authors reported optimizing 4,096 grasps in 2.97 seconds, distilled policies running 9–240× faster at comparable accuracy, and reinforcement learning reaching a GPU baseline’s scores up to 2.1× sooner on the same simulator. The toolkit combines parallel GPU optimization, collision and rendering representations, physics, policy distillation, and reinforcement learning.
- Significance: This is a meaningful infrastructure signal for robot learning because faster differentiable optimization can reduce the compute and iteration cost of training manipulation policies and generating grasp solutions. It may improve the economics of simulation-heavy learning and make it easier to test many robot morphologies or task variants. The result is more relevant to the enabling layer of general-purpose robotics than to demonstrated field deployment.

### A real-time contact-rich humanoid reaching controller demonstrates sim-to-real transfer

- Event date: 2026-11-14
- Sources: `S6`
- Observed fact: A study on a Unitree H1-2 humanoid used local sensing, fiducial markers, and sampling-based whole-body model-predictive control to brace against a surface and reach objects beyond the robot’s normal standing workspace. The controller ran at 34 Hz on a laptop, extended reach by approximately 50 cm, sustained a loaded posture for more than four minutes before pose-estimation drift, reached commanded targets in 89% of trials, and completed the full reach-and-recovery cycle in 81% of 54 trials across six targets and three table heights.
- Significance: The result is a concrete dexterity and whole-body-manipulation signal: contact with the environment is used as a resource for expanding workspace rather than treated only as a failure mode. The real-time laptop implementation and sim-to-real transfer are relevant to practical deployment of mobile manipulators and humanoids in cluttered environments. It also illustrates that progress is currently coming from tightly engineered controllers and sensing assumptions, not yet from unconstrained general-purpose autonomy.

### DARPA’s Triage Challenge reports human-machine teams operating in complex disaster scenarios

- Event date: 2026-11-16
- Sources: `S7`
- Observed fact: DARPA reported that its Triage Challenge finals concluded on November 13, with RoboScout winning the systems competition and Disruptors winning the data competition. Competitors used autonomous systems and human-machine teams to navigate simulated catastrophic environments involving a tornado scenario, smoke, darkness, complex obstacles, victim identification, triage, and evacuation. DARPA stated that human-machine teams outperformed the other evaluated approaches in the challenge environment.
- Significance: The event provides a field-relevant test of autonomous navigation, perception, coordination, and physical assistance under degraded conditions. It is relevant to the wider claim that autonomous robots can coordinate maintenance, emergency response, and care-like work. The strongest measured takeaway is not fully autonomous replacement of people but the apparent advantage of human-machine teaming in difficult environments.

### Recent robot-learning work still treats persistent grasp failures as an unresolved deployment bottleneck

- Event date: 2026-11-13
- Sources: `S8`
- Observed fact: A November 13, 2026 study reports that reinforcement learning improved average point-cloud grasping performance on unseen objects, but left a subset of specific grasps persistently unsolved. In simulation, success improved from 55% with Contact-GraspNet to 83% with reinforcement learning, while the hard cases that reinforcement learning continued to fail on improved from 24% to 45% after adding 58 targeted human demonstrations in virtual reality.
- Significance: This directly narrows claims that more data or generic reinforcement learning is sufficient for robust dexterity. The need to identify recurring failure cases and inject targeted human corrections suggests that long-tail grasp failures remain a central barrier to general-purpose manipulation, especially in warehouses, homes, and farms where objects and contact conditions vary.

### Humanoid safety research identifies emergency stops and loss of balance as deployment-specific hazards

- Event date: 2026-11-11
- Sources: `S9`
- Observed fact: A November 11, 2026 paper on full-size humanoid deployment analyzes cases in which robots lose balance and require emergency stopping. It argues that abruptly stopping a humanoid can itself create hazards because the robot may retain momentum, fall, or exert uncontrolled forces, and proposes graduated force authority rather than relying only on conventional emergency-stop behavior.
- Significance: This challenges the assumption that existing industrial-robot safety practices can be transferred directly to bipedal humanoids working near people. A safety architecture that must manage falls, momentum, force authority, and partial shutdown states could increase validation requirements, complicate certification, and reduce practical autonomy in shared logistics or manufacturing environments.

### Agility’s regulatory filing identifies technical reliability, safety, supply-chain, and profitability risks for humanoid scale-up

- Event date: 2026-11-16
- Sources: `S10`
- Observed fact: Agility Robotics’ November 16, 2026 SEC filing states that commercial deployment of Digit and future products may be delayed by bipedal locomotion, software reliability, regulatory requirements, supply-chain constraints, and unforeseen obstacles. The filing also identifies risks from falls, collisions, unintended movements, latent defects, component shortages involving actuators, sensors, batteries, and computing hardware, and the need to increase utilization across multiple shifts and broaden the range of workflows before larger-scale adoption becomes commercially viable.
- Significance: This is unusually direct counterevidence from a leading humanoid vendor: the company’s own risk disclosure treats safe operation, component availability, manufacturing, utilization, and workflow breadth as unresolved conditions rather than solved capabilities. It weakens near-term claims that humanoids will rapidly replace labor across varied logistics tasks, even where pilots have demonstrated useful motions.

### Robot-learning benchmarks continue to expose large gaps between in-distribution competence and robust physical generalization

- Event date: 2026-10-08
- Sources: `S11`
- Observed fact: A real-robot benchmark study reports that five vision-language-action policies achieved approximately 67.5%–73.3% success on in-distribution spatial configurations, but only about 40.7%–52.0% on out-of-distribution configurations. Directly specified instructions improved success by 28.3–40.0 percentage points, indicating sensitivity to wording and spatial arrangement even when the relevant objects, concepts, and actions were represented during training.
- Significance: Although published before the priority window, this is a strong falsifier for interpreting high aggregate manipulation scores as general-purpose dexterity. Performance is materially affected by spatial distribution and instruction formulation, which are precisely the kinds of variations encountered in ordinary warehouses, homes, hospitals, and shared human workspaces.

### New benchmark work argues that common manipulation scores can overstate general capability

- Event date: 2026-06-02
- Sources: `S12`
- Observed fact: A benchmark audit identifies shortcut solvability, insufficient statistical significance, benchmark overfitting, and dependence on data sources as failure modes in manipulation evaluation. The audit reports that a small probe model without a language encoder reached performance near published state-of-the-art on LIBERO, that many reported gains were not statistically established, and that randomizing block poses within the training range reduced performance for every tested policy on CALVIN.
- Significance: This undermines optimistic comparisons based on leaderboard gains, especially when those gains are used to infer general-purpose dexterity or transfer. If benchmark scores can be matched by smaller probes or collapse under modest distribution changes, apparent progress may reflect task-specific shortcuts rather than durable embodied competence.

### Full-scale deployment remains gated by utilization and workflow breadth, not only by successful demonstrations

- Event date: 2026-11-16
- Sources: `S13`
- Observed fact: Agility’s regulatory materials state that customer deployments repeatedly reinforced four requirements for broader adoption: safe operation alongside people, utilization across multiple shifts, heavier payload capacity, and the ability to perform a broader range of workflows within a facility. The same materials describe Digit 5 availability as beginning in the first half of 2027, with expansion over the following six to nine months, rather than immediate broad deployment.
- Significance: The evidence suggests that successful pilots and isolated task completion are insufficient indicators of automation at scale. A robot may perform a task in a live customer environment yet remain economically unattractive if it cannot run for multiple shifts, handle varied payloads, recover from failures, or serve enough workflows to justify integration and support costs.

### Import and national-security measures create a nontechnical barrier to robotics scaling

- Event date: 2026-11-02
- Sources: `S14`, `S15`
- Observed fact: A U.S. presidential proclamation published in the Federal Register identifies imported robotics, industrial machinery, and components as a national-security concern and directs action concerning imports. The document explicitly includes autonomous robots, humanoid robots, quadruped robots, and autonomous ground vehicles among advanced robotic systems with strategic significance. Separate FCC materials state that certain foreign-produced advanced robotic devices were added to the Covered List unless conditionally approved.
- Significance: These measures create potential friction for scaling autonomous logistics and humanoid fleets through component availability, supplier qualification, import authorization, and compliance costs. Even if robot capability improves, geopolitical controls and manufacturing concentration could limit deployment speed, raise unit costs, or force redesigns and domestic-sourcing programs.

### Self-play and simulation can produce brittle coordination that fails with unfamiliar partners

- Event date: 2026-11-13
- Sources: `S16`
- Observed fact: A November 13, 2026 study of humanoid parcel handovers reports that a receiver trained through alternating PPO self-play achieved 90%–95% success with its learned partner but only 31% with scripted partners it had never encountered. Delaying the partner’s offer by one second reduced success as low as 6% in one seed. Hidden start-delay randomization improved unseen-partner performance to 80%, showing both the severity of the brittleness and the need for deliberately adversarial variation during training.
- Significance: This is a direct challenge to claims that multi-agent robot learning naturally transfers from simulated or self-play partners to human coworkers, other robots, or changing logistics systems. Small timing changes caused catastrophic degradation, implying that coordination policies can memorize interaction conventions rather than learn robust intent inference and recovery.

## Assumption Assessments

### PS-ROBOTICS-001: Embodied AI automates material coordination

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S7`, `S8`, `S9`, `S10`, `S11`, `S12`, `S13`, `S14`, `S15`, `S16`
- Evidence: Evidence strengthens the narrower claim that embodied AI is expanding in autonomous delivery, warehouse trials, factory coordination, security patrols, and staged emergency-response settings. DoorDash reports hundreds of thousands of autonomous deliveries across its robot and drone network; GXO and Apptronik describe conditional future trials across more than 50 evaluated logistics tasks; Toyota describes large planned robotics investment and integrated factory-control systems; and Ring reports autonomous indoor navigation products. Robot-learning and real-hardware studies also show progress in optimization, manipulation, and sim-to-real control. However, the evidence does not establish broad general-purpose automation or current large-scale substitution across construction, care, maintenance, and unconstrained material coordination. Persistent grasp failures, benchmark distribution gaps, unfamiliar-partner brittleness, humanoid safety hazards, utilization requirements, supply-chain constraints, and absent independent cost-per-productive-hour data materially limit the claim.
- Real-world implication: Embodied AI is becoming a meaningful capacity layer in delivery, warehouse, manufacturing, security, and human-machine response workflows, but adoption is likely to remain task-specific and KPI-gated. Near-term growth should not be interpreted as proof that robots can broadly replace human labor across varied physical environments. Reliability, recovery labor, safety certification, workflow breadth, utilization, supply chains, and fully loaded economics remain decisive constraints.
- PostSingularity implication: If a post-singularity capability discontinuity occurs, the current deployment evidence provides plausible infrastructure and learning pathways for rapid expansion of autonomous material coordination, especially where fleets, simulation, and logistics data already exist. It does not by itself establish that post-singularity systems will solve long-tail dexterity, embodied safety, human coordination, or deployment economics; those would remain explicit transition conditions rather than assumed outcomes.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied audited evidence concerns terrestrial robotics, autonomous logistics, robot learning, humanoid safety, and robotics regulation. It contains no direct evidence on launch cost, orbital station duration, closed-loop life support, in-space manufacturing, autonomous space missions, or human health limits in long-duration off-world environments.
- Real-world implication: No directional update is justified on whether autonomous systems, improved propulsion, and closed-loop life support will make sustained orbital or off-world communities practical. The assumption remains unassessed from this evidence set.
- PostSingularity implication: The evidence does not establish whether a post-singularity system could overcome propulsion, life-support closure, radiation, maintenance, and human-health constraints. Off-world settlement should remain a separate conditional branch rather than being inferred from terrestrial robotics progress.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied audited evidence contains no direct evidence on AI transparency standards, content provenance adoption, model audits, regulatory disclosure rules, verification rituals, or social responses to opaque high-impact AI. Robotics safety and regulatory materials address physical deployment risks, not provenance or audit systems for influential AI.
- Real-world implication: No directional update is justified on whether AI influence is producing stronger provenance, verification, audit-trail, or graduated-oversight institutions. Adoption and effectiveness of such systems remain unassessed here.
- PostSingularity implication: The evidence does not indicate whether post-singularity societies would rely on inspectable provenance and audit rituals, or whether those mechanisms would remain technically and institutionally effective against more capable systems. The storyworld assumption should not be strengthened from the robotics evidence.

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied audited evidence contains no direct evidence on brain-computer-interface channel count, bidirectional neural implants, long-term implant safety, decoded speech, decoded affect, sensory exchange, or emotional communication between people and AI.
- Real-world implication: No directional update is justified on the feasibility or safety of high-bandwidth two-way neural interfaces. The assumption remains unassessed against the supplied sources.
- PostSingularity implication: The evidence provides no basis for deciding whether post-singularity systems could enable rich neural communication or overcome tissue response, bandwidth, privacy, and safety constraints. Neural-interface capabilities should remain explicitly uncertain rather than treated as a consequence of general AI progress.

### PS-AI-001: Recursive AI progress can create a societal discontinuity

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied audited evidence includes progress in robot learning, simulation, physical control, and autonomous deployment, but no direct measurements of AI research automation, recursive self-improvement, frontier capability growth, or the relative speed of institutional adaptation. Robotics progress does not establish a societal discontinuity caused by recursive AI improvement.
- Real-world implication: No directional update is justified on whether recursive or tightly coupled AI development will advance rapidly enough to make existing institutions and expectations lose relevance. The key signals and falsifiers for this assumption were not measured by the supplied evidence.
- PostSingularity implication: The evidence does not establish the existence, timing, or magnitude of a singularity-scale discontinuity. Any post-singularity implications remain conditional on a separate finding that AI systems can materially automate AI research and outpace institutional adaptation.

## Canon Implementation Plan

### `worldbible/technologies/robotics.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S7`, `S8`, `S9`, `S10`, `S11`, `S12`, `S13`, `S14`, `S15`, `S16`
- Why this location: The evidence supports expanding embodied AI in delivery, warehouse trials, factory coordination, security, and human-machine emergency response, but challenges any implication that adaptive robotics already provides broad general-purpose automation. Long-tail grasp failures, distribution-sensitive benchmarks, unfamiliar-partner brittleness, humanoid safety hazards, utilization requirements, supply-chain constraints, and missing independent economic data materially narrow the claim.
- Proposed change: Retain the existing description of adaptive robots and human-centered coordination, but add a qualification stating that current real-world adoption is task-specific and KPI-gated. Identify autonomous delivery, warehouse trials, factory logistics, security patrols, and staged emergency response as demonstrated or emerging domains, while explicitly stating that broad replacement of human labor across construction, care, maintenance, and unconstrained material coordination is not established. Add that deployment remains conditional on reliability, recovery labor, safety, workflow breadth, utilization, supply chains, and fully loaded operating economics.
- Implementation steps:
  1. Insert the qualification immediately after the existing Summary paragraph under the exact “Summary” heading.
  2. Preserve the existing links to Drone Logistics and Trust Fabrics; add cross-references to Drone Logistics for delivery integration and Trust Fabrics only if the new text discusses human oversight or accountability.
  3. Use cautious terminology such as “reported,” “planned,” “pilot-stage,” and “task-specific” for company announcements, future targets, staged challenges, and preprints.
  4. Review this change against the Function and Philosophical Tensions sections so that the summary does not imply capabilities or autonomy levels contradicted by the detailed limitations.
- Dependencies or conflicts:
  - The current Summary says robots reshape bodies and roles on the fly; this must not be read as unconstrained physical generalization.
  - S1 aggregates multiple robot and drone partners and does not provide Dot-specific utilization, intervention, uptime, or cost data.
  - S2 and S3 describe conditional or future deployment plans rather than current general-purpose scale.
  - S8, S11, S12, and S16 limit claims about transfer, dexterity, benchmark generalization, and coordination with unfamiliar partners.
  - S9, S10, S13, S14, and S15 introduce safety, utilization, supply-chain, import, and regulatory constraints that may affect future story chronology.

### `worldbible/technologies/robotics.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S5`, `S6`, `S7`, `S8`, `S9`, `S11`, `S12`, `S16`
- Why this location: The existing functions describe adaptive hardware, swarm coordination, and emotional telemetry but do not represent the audited learning and control pipeline. The evidence adds simulation-heavy training, real-world logging, targeted human correction, contact-rich whole-body control, deliberate coordination randomization, and safety controls, while showing that these mechanisms remain bounded by task and environment assumptions.
- Proposed change: Add a subsection under Function describing the operational learning loop: real-world logs and intervention data feed simulation and policy updates; differentiable optimization and policy distillation reduce iteration cost; targeted human demonstrations address persistent grasp failures; contact-aware model-predictive control can extend manipulation reach; and training with timing variation improves unfamiliar-partner handovers. Qualify these capabilities by stating that they do not guarantee robust performance on unseen objects, changing layouts, degraded sensors, long-horizon workflows, or unanticipated human partners. Add that humanoid operation requires graduated force authority and recovery-aware safety behavior rather than relying only on abrupt emergency stops.
- Implementation steps:
  1. Append the new material under the existing “Function” heading after the current bullets, without deleting the existing modular-joint, swarm-mesh, or emotional-telemetry claims.
  2. Separate enabling methods from demonstrated deployment: identify S5, S6, S8, and S16 as research or controlled evaluations and S1 and S7 as operational or staged examples.
  3. State the human-intervention and safety limitations in the same subsection so the function description does not imply that simulation speedups or successful demonstrations establish general-purpose autonomy.
  4. Cross-check terminology against Trust Fabrics if “human collaborators” is expanded into governance or oversight; keep this edit focused on physical operation and learning rather than AI provenance.
- Dependencies or conflicts:
  - S5 reports simulator and optimization speedups, not equivalent gains on deployed physical robots.
  - S6 relies on fiducial markers, limited trials, and a specific reach-and-recovery behavior.
  - S8 shows that targeted demonstrations improve hard grasp cases but do not solve long-tail manipulation.
  - S9 indicates that emergency stopping can itself create falling or force hazards for full-size humanoids.
  - S11, S12, and S16 show that benchmark and self-play performance can collapse under distribution, wording, timing, or partner changes.

### `worldbible/technologies/robotics.md` -> Cultural Effects

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S7`, `S10`, `S13`, `S14`, `S15`
- Why this location: The evidence supports cultural and institutional effects from robots becoming capacity layers in delivery, logistics, manufacturing, security, and emergency response. It also shows that adoption is constrained by safety alongside people, multi-shift utilization, payload and workflow breadth, component availability, import controls, and the economics of recovery and supervision.
- Proposed change: Add cultural effects describing robots as complementary capacity layers working alongside human labor rather than automatic labor replacements. Include the emergence of Robotics-as-a-Service and KPI-gated trials, the social value of human-machine teams in difficult environments, and the possibility that import restrictions and component controls make robot access uneven across regions. Add a qualification that announced delivery volumes, investment plans, and rollout targets should not be treated as proof of independent fleet scale, broad labor substitution, or equal access.
- Implementation steps:
  1. Insert the material under “Cultural Effects” after any existing cultural-effects content, using a short bullet list consistent with the file’s current format.
  2. Link to Drone Logistics for autonomous delivery and fleet coordination; do not add links to unsupplied files.
  3. Distinguish current reported activity from future plans by labeling GXO-Apptronik and Toyota developments as trials, targets, or planned investment.
  4. Review the resulting cultural claims against the timeline so any cycle placement is supported before adding a specific introduced cycle or historical milestone.
- Dependencies or conflicts:
  - S1 is first-party and aggregates Dot with other robot and drone partners; it lacks independent audit, intervention, uptime, and cost data.
  - S2 is a conditional future deployment path, not a binding 1,000-robot order or current 1,000-robot fleet.
  - S3’s projected robot totals do not identify the proportion that is general-purpose, learning-enabled, humanoid, collaborative, or fixed automation.
  - S7 supports human-machine teaming more directly than fully autonomous replacement.
  - S10 and S13 describe unresolved utilization, workflow breadth, safety, supply, and profitability conditions.
  - S14 and S15 create possible regional and supply-chain disparities, but their effects on prices and schedules are not quantified.

### `worldbible/technologies/drone-logistics.md` -> Function

- Priority: **low**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S4`, `S7`
- Why this location: The existing Function section presents autonomous drone networks as mature, harmonious, and rapidly adjustable. The audited evidence supports networked autonomous delivery and navigation, but also frames autonomy as an integrated capacity-management layer involving human Dashers, robots, drones, safety operators, and staged human-machine teams rather than a fully independent replacement system.
- Proposed change: Add a qualification under Function stating that delivery assignment can dynamically combine human couriers, ground robots, and drones according to order size, distance, traffic, and preparation time. Clarify that autonomous delivery systems may retain intervention, supervision, recovery, and validation requirements, and that reported aggregate delivery volume does not establish per-robot utilization, autonomy rate, or cost per delivery. Keep the existing energy, routing, oversight, and cargo-pod bullets unchanged unless a later chronology review requires reconciliation.
- Implementation steps:
  1. Append the qualification after the existing Function bullets under the exact “Function” heading.
  2. Cross-reference Robotics using the existing relative link only if the repository convention permits; otherwise describe the relationship in prose without introducing a new path.
  3. Avoid changing “near-instant” or “equitable distribution” in Summary unless a separate review establishes whether those are intended as settled canon rather than aspirational cultural framing.
  4. Review this file after the Robotics Summary edit so both documents use consistent terms for human-robot teaming, intervention, and fleet-level evidence.
- Dependencies or conflicts:
  - The current Summary states that fleets replaced most manual shipping; the new qualification should not silently convert that settled worldbuilding claim into a real-world forecast.
  - S1 reports aggregate DoorDash network volume and does not provide a clean Dot-specific deployment count or economics.
  - S4 concerns indoor security navigation rather than delivery or dexterous material handling and should not be used to expand drone logistics into manipulation.
  - S7’s strongest result is human-machine teaming in staged or simulated disaster environments, not routine autonomous logistics.

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

- The robotics evidence is heavily weighted toward company-reported announcements, planned deployments, vendor facilities, staged challenges, preprints, and simulator-based evaluations rather than independent fleet audits.
- No independent audit was found for the reported hundreds of thousands of autonomous deliveries, including intervention rates, remote-supervision hours, uptime, incidents, human labor inputs, or fully loaded cost per delivery.
- Future GXO-Apptronik and Toyota deployment targets are conditional or planned and do not establish current general-purpose robot scale.
- Evidence is materially thinner for construction, care, maintenance, off-road transport, and unconstrained household work than for delivery, warehouses, factories, security, and staged emergency-response settings.
- Robot-learning results do not yet establish broad physical generalization across unseen objects, long-horizon workflows, changing layouts, maintenance states, degraded sensors, or unfamiliar human partners.
- No supplied evidence addresses off-world settlement, provenance and audit institutions, neural interfaces, recursive AI research automation, or institutional adaptation speed.
- No independent cost-per-productive-hour comparison was supplied for humanoids, conventional automation, and human labor performing the same workflows.
- The implications of robotics supply-chain and import controls for deployment cost and schedule are identified qualitatively but not quantified.
- DoorDash reports hundreds of thousands of lifetime autonomous deliveries across Dot and other robot and drone partners, while the counterevidence search found no independent audit of the figure, intervention rate, human labor input, uptime, incidents, or fully loaded cost per delivery. The claims are therefore compatible but not independently reconciled at the fleet or economics level.
- GXO and Apptronik describe live autonomous evaluations on more than 50 logistics tasks and a possible rollout of up to 1,000 Apollo robots, while the evidence also states that the trials and rollout are future-oriented, conditional, and without production throughput, uptime, intervention, safety, or cost results. This is a demonstration and planned-deployment signal, not evidence of current scaled deployment.
- Toyota describes planned investment and a possible installed base of approximately 400,000 robots from 2028 onward, while the source does not specify how many would be general-purpose, learning-enabled, humanoid, or conventional fixed automation. The scale forecast should not be treated as present general-purpose capability.
- RoboKit reports large simulation and optimization speedups, while the grasping, benchmark, and handover evidence shows that faster simulation or training does not establish robust physical generalization, long-tail grasp reliability, or unfamiliar-partner coordination.
- The Unitree H1-2 study demonstrates a specific real-hardware contact-rich reaching behavior with sim-to-real transfer, while the study’s fiducial-marker assumptions, limited trial count, and fixed task do not support claims of broad unconstrained dexterity.
- DARPA reports that human-machine teams outperformed other evaluated approaches in a staged or simulated challenge environment. This supports human-machine teaming more directly than fully autonomous general-purpose operation.
- Agility’s regulatory materials describe active commercial deployments and future product plans but also identify safe operation, multi-shift utilization, payload, workflow breadth, component supply, and profitability as unresolved scale conditions. These statements are not proof of commercial failure, but they contradict interpretations that useful pilots alone demonstrate near-term broad deployment.
- The hundreds-of-thousands figure aggregates Dot with other robot and drone delivery partners, so it is not a clean Dot deployment count.
- The article is an AWS-hosted first-party case study and does not provide independent operational verification.
- Dot still uses safety operators during testing, and the source does not state the residual remote-assistance rate in production.
- The source reports technical architecture and delivery volume but not fully loaded cost per delivery or cost per productive hour.
- The announcement is a letter of intent and does not constitute a binding 1,000-robot order or deployment.
- The cited 50-task evaluations occurred in a vendor training facility, not necessarily in customer warehouses under production conditions.
- The release provides no throughput, uptime, intervention, injury, or cost-per-hour results.
- Initial scaled deployment is planned for 2027, so the evidence is forward-looking rather than proof of current scale.
- The announced investment and robot totals are plans beginning in 2028, not current deployments.
- The release does not specify how many of the projected robots will be general-purpose, learning-enabled, humanoid, or conventional fixed automation.
- No measured productivity, safety, uptime, or cost-per-hour results are provided.
- The claims come from Toyota’s own showcase and are not independently audited.
- The announcement does not report deployment counts, autonomy uptime, intervention frequency, or false-alarm rates.
- The systems appear focused on navigation and sensing; no dexterous manipulation or physical material handling is described.
- The claims are first-party product claims without independent testing.
- Commercial availability, geographic coverage, and actual customer adoption are not quantified in the source.
- The reported comparisons are primarily simulator- and benchmark-based; the abstract does not establish equivalent gains on physical robots.
- Speedups depend on the selected baselines, hardware, task formulation, and simulator implementation.
- The source does not provide evidence of long-horizon household or warehouse deployment.
- The work is a preprint and should not be treated as independently replicated performance.
- The evaluation involved only 54 trials and six targets across three table heights.
- Fiducial markers were used, limiting claims about uninstrumented environments.
- Pose-estimation drift eventually ended the sustained-posture test.
- The system performs a specific reaching-and-recovery behavior and does not demonstrate broad task generalization or autonomous task planning.
- The results come from a challenge scenario rather than routine operational deployment.
- The environments and tasks were simulated or staged, so performance may not transfer directly to real disasters.
- The release does not provide detailed task-level scores, intervention rates, latency, or cost metrics.
- The result supports human-machine teaming more directly than fully autonomous general-purpose robotics.
- The reported results are primarily simulation-based rather than evidence of sustained production deployment.
- The study concerns grasping rather than complete long-horizon manipulation or logistics workflows.
- The hard-case improvement remains below reliable industrial performance levels.
- The paper is a preprint and the result has not been independently replicated in the cited source.
- The source is a technical preprint and does not provide a large statistical incident database.
- The described deployment lessons may not generalize across all humanoid platforms or facility layouts.
- The proposal is a safety framework rather than evidence that a deployed system has met a validated injury-risk threshold.
- The source does not quantify the economic cost of the proposed safety controls.
- SEC risk disclosures are legally cautious and do not establish that every listed risk has materialized.
- The filing is company-reported and may emphasize downside risks for disclosure purposes.
- The source does not provide independent measurements of incident rates, uptime, or cost per productive hour.
- Agility also reports active commercial deployments and future orders, so the filing is evidence of constraints rather than proof of commercial failure.
- The benchmark uses the SO-101 robot arm and tabletop tasks rather than full mobile manipulation or humanoid logistics.
- The study evaluates three policies fully in the main comparison, limiting breadth.
- The result is a benchmark finding, not a direct measure of commercial deployment economics.
- The event predates the November 10–17 priority window and is included as relevant counterevidence rather than a new in-window deployment event.
- The audit predates the priority window and concerns selected benchmarks rather than all current evaluations.
- It does not measure the latest commercial systems directly.
- The conclusions depend on the audit protocols and selected probe models.
- Benchmark weaknesses do not imply that no underlying capability improvement has occurred.
- The requirements are reported by the vendor and are not accompanied by independently audited utilization or productivity data.
- The filing describes intended product improvements, not verified performance of Digit 5.
- The evidence is concentrated on one humanoid vendor and may not represent all logistics robots.
- No full cost-per-productive-hour or labor-substitution calculation is provided.
- The proclamation and FCC notice do not quantify effects on commercial logistics-robot prices or delivery schedules.
- The relevant actions began before the November 10–17 window and are included as an active constraint affecting that period.
- Not every commercial robot or component is necessarily covered by the measures.
- The documents describe policy and regulatory exposure, not a demonstrated deployment failure.
- The experiment concerns parcel handover rather than complete warehouse coordination.
- Results are reported in simulation and may not capture hardware latency, sensing noise, or human behavior.
- The paper studies a limited number of seeds and partner conditions, although it includes held-out conditions.
- The improved method still requires carefully designed training randomization rather than demonstrating unconstrained generalization.
- No independently audited deployment count or cost-per-productive-hour data was found for humanoid robots in logistics during November 10–17, 2026.
- The GXO-Apptronik announcement provides future targets and trial plans but no production throughput, uptime, intervention, safety, or labor-substitution measurements.
- The strongest autonomous-delivery volume figure aggregates multiple DoorDash robot and drone partners, preventing a clean estimate of Dot-specific scale or economics.
- No primary-source result in the window demonstrated broad, unconstrained dexterous manipulation across many unseen household or industrial tasks in ordinary environments.
- Robot-learning papers found in the window were largely preprints or simulation-heavy studies; independent replication and large-scale physical validation remain limited.
- No standards, regulatory records, or certification changes specifically affecting general-purpose or humanoid logistics robots were identified in the priority window.
- Evidence for care, construction, maintenance, and off-road material transport was thinner than evidence for warehouse, delivery, security, and staged emergency-response applications.
- No independent audit was found for the November 2026 claims of hundreds of thousands of autonomous deliveries, including intervention rates, human labor inputs, uptime, incidents, or fully loaded cost per delivery.
- No public dataset was found that reports safety incidents, near misses, falls, or emergency-stop activations across deployed humanoid logistics fleets during the priority window.
- No independently replicated physical benchmark was found demonstrating broad dexterous manipulation across many unseen objects, long-horizon tasks, and changing human partners in ordinary warehouse or household environments.
- Evidence remains sparse on how robot-learning policies perform after maintenance, sensor replacement, battery degradation, software updates, or changes in floor layout and inventory mix.
- No reliable fleet-level data was found on remote supervision hours, teleoperation frequency, recovery labor, or the ratio of autonomous actions to human interventions.
- No independent cost-per-productive-hour comparison was found between humanoid robots, conventional automation, and human labor for the same logistics workflows.
- The search found regulatory and supply-chain constraints but no complete cross-jurisdiction survey of certification, workplace-safety, liability, privacy, or insurance requirements for general-purpose robots.
- Evidence for construction, care, maintenance, and off-road material coordination remains materially thinner than evidence for structured warehouse, delivery, security, and staged research settings.
- PS-SPACE-001 was assessed as insufficient-evidence. No edit is warranted in worldbible/technologies/aerospace-systems.md or locations/orbital-sanctuary.md because the audited sources contain no direct evidence on launch cost, orbital duration, closed-loop life support, in-space manufacturing, autonomous space missions, radiation, or long-duration human health.
- PS-AI-003 was assessed as insufficient-evidence. No edit is warranted in worldbible/technologies/trust-fabrics.md or philosophy/ai-trust.md because the evidence addresses physical robotics safety and regulation, not AI transparency standards, provenance adoption, model audits, disclosure rules, or social responses to opaque high-impact AI.
- PS-NEURO-001 was assessed as insufficient-evidence. No edit is warranted in worldbible/technologies/neural-links.md because none of the audited sources addresses neural-interface bandwidth, bidirectional implants, decoded speech or affect, long-term implant safety, sensory exchange, or neural privacy.
- PS-AI-001 was assessed as insufficient-evidence. No edit is warranted in worldbible/singularity-event.md or worldbible/timeline.md because robotics deployment and learning results do not measure recursive AI research automation, frontier capability growth, institutional adaptation speed, or a singularity-scale discontinuity.
- The technology index does not require a change from this evidence set. Robotics and Drone Logistics are already represented in worldbible/technologies/index.md, and the audited material does not establish a new technology category, chronology entry, or metadata value that should be added without a broader repository consistency review.
- No source supports a new canon claim for construction, care, maintenance, agriculture, off-road transport, or unconstrained household robotics. Those domains should remain on the watchlist rather than being added to the affected files as established capability.
- No independent fleet-level audit or cost-per-productive-hour comparison was supplied. The proposed revisions therefore qualify deployment and economics claims without replacing them with quantitative canon figures.
- Excluded claim: DoorDash’s hundreds of thousands of autonomous deliveries are not a clean Dot-specific deployment count.
- Excluded claim: DoorDash’s delivery volume does not establish per-robot utilization, intervention rates, delivery cost, profitability, or cost per productive hour.
- Excluded claim: GXO and Apptronik have not established a binding order for 1,000 Apollo robots or a current 1,000-robot deployment.
- Excluded claim: More than 50 evaluated logistics tasks at Apptronik’s Robot Park do not constitute production deployment in customer warehouses.
- Excluded claim: The planned GXO-Apptronik 2027 trials do not establish current commercial scale.
- Excluded claim: Toyota’s projected 2028 investment and robot totals are not current deployments and do not demonstrate general-purpose, learning-enabled, or humanoid capability.
- Excluded claim: Ring’s launch does not demonstrate dexterous manipulation, physical material handling, quantified customer adoption, or production autonomy performance.
- Excluded claim: RoboKit’s simulator speedups do not establish equivalent gains on physical robots, long-horizon deployment, or independently replicated general-purpose capability.
- Excluded claim: The Unitree H1-2 reaching study does not demonstrate broad task generalization, unconstrained general-purpose autonomy, or uninstrumented-environment dexterity.
- Excluded claim: The DARPA Triage Challenge does not demonstrate routine real-disaster deployment or fully autonomous replacement of human responders.
- Excluded claim: Reinforcement learning or additional data has not solved persistent long-tail grasp failures.
- Excluded claim: The graduated-force-authority proposal does not establish a validated injury-risk threshold or proven deployment safety.
- Excluded claim: Agility’s SEC risk disclosures do not prove commercial failure or establish independently measured incident rates, uptime, or cost per productive hour.
- Excluded claim: Benchmark scores from SO-101, LIBERO, CALVIN, or related studies do not establish broad general-purpose dexterity in warehouses, homes, hospitals, or shared workspaces.
- Excluded claim: Agility’s described customer requirements do not establish verified Digit 5 performance or a full cost-per-productive-hour or labor-substitution result.
- Excluded claim: The proclamation or FCC notice does not demonstrate a commercial robotics deployment failure or quantify specific price or schedule effects.
- Excluded claim: Self-play handover success with a learned partner does not transfer to unfamiliar human or robot partners without deliberately designed variation and recovery testing.
- Excluded claim: Any company-reported future forecast, product announcement, pilot, staged challenge, simulation result, or preprint alone does not establish large-scale deployed general-purpose robotics.

## Watchlist

- Independent fleet-level audits of autonomous delivery and warehouse robots, including autonomy rates, intervention and teleoperation hours, uptime, incidents, recovery labor, and fully loaded cost per productive hour.
- Production results from the planned GXO-Apptronik trials: throughput, safety, multi-shift utilization, payload range, workflow breadth, intervention rates, and customer economics.
- Toyota’s realized robot counts and the proportion that are general-purpose, learning-enabled, collaborative, or conventional fixed automation.
- Physical evaluations of dexterous manipulation under unseen objects, changing layouts, sensor degradation, maintenance, battery aging, and long-horizon workflows.
- Human-robot coordination tests with unfamiliar partners, timing variation, interruptions, recovery behavior, and real warehouse conditions.
- Validated safety and certification results for full-size humanoids, including falls, emergency stops, graduated force authority, near misses, and injury rates.
- Evidence of deployment in care, construction, maintenance, agriculture, and off-road material transport rather than only structured logistics and staged environments.
- Launch-cost trends, closed-loop life-support performance, long-duration human-health data, in-space manufacturing, and autonomous mission operations for PS-SPACE-001.
- AI transparency standards, provenance adoption, independent model audits, and regulatory disclosure requirements for PS-AI-003.
- BCI channel count, bidirectional implant demonstrations, long-term safety, decoded speech or affect, and privacy outcomes for PS-NEURO-001.
- AI research automation, frontier capability-evaluation trends, and measured institutional adaptation speed for PS-AI-001

## Sources

- `S1` [How DoorDash uses AWS to build a self-driving delivery robot](https://www.aboutamazon.com/stories/doordash-aws-autonomous-delivery-robot) — Amazon Web Services / Amazon; 2026-11-12; official-release; URL supplied in structured research output. First-party operational account of DoorDash’s autonomous delivery robot, learning pipeline, simulation regime, hardware, and cumulative delivery volume.
- `S2` [GXO and Apptronik Expand Partnership to Scale Humanoid Deployment](https://investors.gxo.com/news-releases/news-release-details/gxo-and-apptronik-expand-partnership-scale-humanoid-deployment) — GXO Logistics; 2026-11-12; official-release; URL supplied in structured research output. Primary corporate announcement describing Apollo trials, evaluated logistics tasks, planned workflows, RaaS structure, and conditional deployment targets.
- `S3` [Toyota Powers What’s Next in Mobility and Manufacturing](https://pressroom.toyota.com/toyota-powers-whats-next-in-mobility-and-manufacturing/) — Toyota USA Newsroom; 2026-11-11; official-release; URL supplied in structured research output. First-party description of Toyota’s physical-AI, robotics, factory-control, worker-data, and future deployment strategy.
- `S4` [Ring announces Ring Robotics, ushering in a new era of security](https://www.aboutamazon.com/news/devices/ring-drone-cam-rover-cam-security-robot) — Amazon / Ring; 2026-11-10; official-release; URL supplied in structured research output. Primary product announcement documenting the launch of autonomous indoor aerial and ground robots and the AI navigation system behind them.
- `S5` [RoboKit: Accelerating Parallel Differentiable Optimization for Robot Learning](https://arxiv.org/abs/2611.20185) — arXiv; 2026-11-15; primary-research; URL supplied in structured research output. Primary research source reporting quantitative speedups for differentiable optimization, grasp planning, policy distillation, and reinforcement-learning workflows.
- `S6` [Leaning Over to Reach Far-Away Objects](https://arxiv.org/abs/2611.19100) — arXiv; 2026-11-14; primary-research; URL supplied in structured research output. Primary study with real-hardware measurements for contact-rich humanoid manipulation, real-time control, reach extension, and sim-to-real transfer.
- `S7` [DARPA Triage Challenge completes Finals event](https://www.darpa.mil/news/2026/triage-finals-winners) — DARPA; 2026-11-16; official-release; URL supplied in structured research output. Official challenge result describing autonomous systems and human-machine teams operating in smoke, darkness, obstacles, victim-identification, triage, and evacuation scenarios.
- `S8` [Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality](https://arxiv.org/abs/2611.18919) — arXiv; 2026-11-13; primary-research; URL supplied in structured research output. Primary study quantifying persistent grasp failures and the need for targeted human intervention to improve hard cases.
- `S9` [Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority](https://arxiv.org/abs/2611.15928) — arXiv; 2026-11-11; primary-research; URL supplied in structured research output. Primary source focused on failure modes, emergency-stop hazards, falls, and safety control requirements for full-size humanoids.
- `S10` [Agility Robotics Form S-1/A filing archived by the SEC](https://www.sec.gov/Archives/edgar/data/2074973/000121390026120842/ea0312344-s1a1_agility.htm) — U.S. Securities and Exchange Commission; 2026-11-16; regulatory; URL supplied in structured research output. Primary regulatory copy of the company’s risk disclosures and customer-economics constraints, including technical, safety, manufacturing, supply-chain, regulatory, and profitability barriers to humanoid deployment.
- `S11` [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696) — arXiv; 2026-10-08; primary-research; URL supplied in structured research output. Primary real-robot benchmark showing substantial in-distribution to out-of-distribution performance degradation and instruction sensitivity.
- `S12` [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) — arXiv; 2026-06-02; primary-research; URL supplied in structured research output. Primary audit of manipulation benchmarks identifying overfitting, shortcut solutions, statistical weakness, and distribution-sensitivity problems.
- `S13` [Agility Robotics Form S-1/A filing archived by the SEC](https://www.sec.gov/Archives/edgar/data/2074973/000121390026120832/ea0312345-s1a1_agility.htm) — U.S. Securities and Exchange Commission; 2026-11-16; regulatory; URL supplied in structured research output. Primary filing describing customer-identified requirements for safe operation, multi-shift utilization, payload, workflow breadth, and future availability timelines.
- `S14` [Proclamation 11077: Adjusting Imports of Robotics, Industrial Machinery, and Their Parts and Components Into the United States](https://www.govinfo.gov/content/pkg/FR-2026-11-02/html/2026-22385.htm) — U.S. Government Publishing Office / Federal Register; 2026-11-02; regulatory; URL supplied in structured research output. Official U.S. proclamation identifying robotics and related components as a national-security-sensitive import category.
- `S15` [Public Notice on Foreign-Produced Advanced Robotic Devices](https://docs.fcc.gov/public/attachments/DA-26-996A1.pdf) — Federal Communications Commission; 2026-07-28; regulatory; URL supplied in structured research output. Official notice describing Covered List treatment and conditional approval requirements for certain advanced robotic devices.
- `S16` [When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners](https://arxiv.org/abs/2611.18435) — arXiv; 2026-11-13; primary-research; URL supplied in structured research output. Primary study quantifying severe self-play overfitting and failure under unfamiliar partner timing in humanoid handover.

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
  "id": "research_2026-11-17_general-purpose-robotics-dexterity-robot-learnin",
  "type": "research_brief",
  "name": "Robotics 2026-11-10 to 2026-11-17: Deployment Expansion Without Proven General-Purpose Dexterity",
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
