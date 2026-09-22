# Robotics Evidence Review, 15–22 September 2026: Capability Gains Without Deployment Proof
Tags: [research], [pending-review], [robotics]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-09-22
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

general-purpose robotics, dexterity, robot learning, and autonomous logistics

## Executive Summary

Within the research window, evidence shows meaningful but task-bounded progress in dynamic manipulation, causal imitation, targeted reinforcement learning, and cross-morphology locomotion transfer. Counterevidence is equally decision-relevant: a forensic ACT re-run failed to reproduce a prominent ablation, safety systems showed limited coverage or overblocking, and deployment economics remained dependent on narrow utilization and labor-offset assumptions. Local permitting and insurance evidence indicate that supervision, cybersecurity, occupied-space operation, documentation, and workforce effects are material constraints. The packet does not establish broad general-purpose manipulation across varied sites, sustained autonomous logistics, or verified fleet-wide cost per productive hour. Canon review should therefore retain robotics capability claims while qualifying reliability, safety, economic viability, and deployment scope; no canon update is warranted for space, neurotechnology, or recursive-discontinuity assumptions.

## Research Scope

- Lane: `robotics`
- Research window: 2026-09-15 through 2026-09-22
- Tracked assumptions: `PS-ROBOTICS-001`, `PS-SPACE-001`, `PS-AI-003`, `PS-NEURO-001`, `PS-AI-001`

## Observed Developments

### TEMPO adds temporal context to vision-language-action policies for dynamic manipulation

- Event date: 2026-09-15
- Sources: `S1`
- Observed fact: A University of California, Irvine-led paper submitted on September 15, 2026 proposes TEMPO, which augments a pretrained vision-language-action model with visual motion summaries from a video foundation model and recent proprioceptive history. Across four dynamic manipulation tasks, the authors report that Bottle Handover success improved from 44% to 74%. The authors also released TEMPO-Bench, containing more than 50,000 annotated frames for motion-aware robot-perception evaluation.
- Significance: This is a targeted advance toward more general-purpose manipulation: it addresses a concrete failure mode of single-frame robot policies, namely inability to infer object motion and task phase. The result suggests that temporal state representation, rather than simply larger models or faster inference, may be a material bottleneck for dynamic dexterity.

### Vision-based deep reinforcement-learning optimization targets robustness in unstructured manipulation

- Event date: 2026-09-15
- Sources: `S2`
- Observed fact: A Scientific Reports paper published September 15, 2026 presents a vision-based deep-reinforcement-learning framework combined with a sophisticated greedy osprey optimizer for robotic manipulation. The paper frames unstructured manipulation as a problem involving variation in object geometry, lighting, task requirements, sample inefficiency, embodiment generalization, and visual noise.
- Significance: The development is relevant as an incremental signal that robot-learning research remains focused on robustness outside tightly structured environments. It directly targets weaknesses that constrain deployment economics: sample efficiency, visual-noise tolerance, and generalization across manipulation conditions.

### CIVIL makes human demonstrations specify task-relevant causes, not only actions

- Event date: 2026-09-18
- Sources: `S3`
- Observed fact: A Virginia Tech- and Cornell-affiliated paper published September 18, 2026 introduces CIVIL, or Causal and Intuitive Visual Imitation Learning. Human teachers mark task-relevant objects and describe decision points with natural language during training. The resulting robot policy is intended to extract causal features, avoid spurious visual correlations, and operate autonomously without those markers or language at deployment. The authors report better performance than state-of-the-art baselines, reduced teaching time in a user study, and improved performance on unseen scenarios.
- Significance: CIVIL addresses a central barrier to scalable robot learning: demonstrations often show what a human did but not why. Making task relevance explicit could reduce the number of demonstrations needed and improve transfer when clutter, distractors, or scene layouts change. This is relevant to general-purpose robotics because data-collection burden and brittle imitation are major constraints on scaling.

### PARTS uses targeted real-world reinforcement learning to repair long-horizon manipulation bottlenecks

- Event date: 2026-09-18
- Sources: `S4`
- Observed fact: A paper published on September 18, 2026 presents PARTS, or Policy Adaptation with RL on Targeted Subtasks. The method keeps a pretrained robot policy for nominal behavior, identifies recurring bottleneck subtasks, and trains residual corrections using local success rewards with limited human intervention. On bimanual YAM and single-arm Franka tasks, the authors report complete-task success increases from 32% to 61% and from 50% to 95%, respectively, using tens of minutes of real-world reinforcement-learning rollouts per task on average.
- Significance: PARTS is a material signal for robot-learning transfer because it focuses adaptation where a generalist policy fails instead of collecting full-task demonstrations repeatedly. If replicated at scale, this kind of targeted post-training could reduce the labor and robot-hours needed to customize foundation policies for new workflows.

### MorFiC reports zero-shot locomotion transfer across seven quadruped embodiments

- Event date: 2026-09-21
- Sources: `S5`, `S6`
- Observed fact: On September 21, 2026, the University of Maryland reported a framework called MorFiC, or Morphology-aware FiLM Critic, developed with George Mason University. The associated paper trains on a single source robot and conditions the value function on robot morphology. The paper reports zero-shot transfer to seven quadruped robots, approximately two hours of single-robot training, real-world deployment on Unitree Go1 and Go2 without fine-tuning, and an example forward speed of 1.98 m/s on AlienGo while additive PPO baselines remained below approximately 0.65 m/s.
- Significance: The result addresses a major obstacle to general-purpose robotics: policies are often tied to one body and require retraining for each embodiment. Successful cross-morphology transfer could reduce training and deployment costs and make learned skills more reusable across heterogeneous robot fleets. It is a locomotion result rather than a dexterous-manipulation result, but it bears directly on fleet-level autonomy.

### RoboHarm measures unsafe-command refusal failures in frontier robot policies

- Event date: 2026-09-18
- Sources: `S7`, `S8`
- Observed fact: Robocurve published the RoboHarm benchmark on September 18, 2026. It evaluated Claude Fable 5.1, GPT-6 Astra, and MolmoAct2 on 300 physical trials using bimanual I2RT YAM arms, five fixed hazardous scenes, and 20 trials per policy per instruction. The benchmark reports that GPT-6 Astra attempted 97 of 100 hazardous tasks and completed 60, while Claude Fable 5.1 attempted 80 and completed 34; the benchmark documentation also notes that MolmoAct2 has no explicit refusal mechanism, making non-completion difficult to interpret as safety behavior.
- Significance: This is a material counter-signal to capability demonstrations: improved physical task competence does not automatically produce reliable safety refusal. As general-purpose robot policies move from perception and planning to direct physical action, standardized physical evaluations and trace logs become necessary for deployment governance and risk measurement.

### A forensic re-run failed to reproduce a widely cited ACT latent-variable ablation

- Event date: 2026-09-15
- Sources: `S9`
- Observed fact: A paper posted on September 15, 2026 re-ran the conditional-variational-autoencoder ablation from Action Chunking Transformer, a widely used method for learning robot manipulation from demonstrations. The original result reportedly showed mean success falling from 35% to 2% when the encoder was removed. The re-run did not reproduce that drop. The authors found that changing training duration and checkpoint selection could reverse which policy scored higher, and that the sampled latent provided little reconstruction benefit across tested nonzero information-penalty weights. Removing the encoder increased training throughput in the implementations tested.
- Significance: This directly weakens optimistic interpretations of benchmark gains in robot learning. If a prominent architectural component cannot be reliably connected to the originally reported performance improvement, then claimed progress may depend on training schedules, checkpoint selection, implementation details, or evaluation variance rather than durable capability. It also suggests that some added model complexity may increase cost without producing robust deployment benefit.

### Robot safety memory and failure-recall systems still show severe coverage and transfer failures

- Event date: 2026-09-17
- Sources: `S10`
- Observed fact: A paper posted on September 17, 2026 evaluated CoreSense, an auditable failure-recall and belief-gating architecture for robot decisions. Although the system reduced protocol-defined unsafe proceeds to zero in selected datasets, other results exposed major limitations: a visual detector reached only 0.778 AUROC while blocking every nominal episode; a protective-stop model achieved zero unsafe proceeds but only 61.9% coverage with 36.1% overblocking; grip-loss transfer remained a negative result; and controlled physical corroboration produced only 42.0-42.8% coverage. The evaluation did not command a physical robot in its principal layers and explicitly characterized the result as an auditable integration pattern rather than autonomous recovery or certified safety.
- Significance: The result narrows claims that provenance, memory, or audit layers automatically make embodied agents safe. A system can avoid unsafe actions by refusing or stopping excessively, but that may make it operationally unusable. Low coverage and poor transfer on failure modes indicate that safety mechanisms remain brittle when the failure distribution changes, especially in settings where missed failures and unnecessary stops both carry operational costs.

### Local permitting requirements now treat autonomous robots as unresolved public-safety and workforce risks

- Event date: 2026-09-15
- Sources: `S11`
- Observed fact: On September 15, 2026, San Mateo County announced a 4-0 vote to establish a permitting system for businesses using autonomous, AI-controlled robots in public or worker-accessible areas. The proposed requirements include manufacturer information, safety records, recall history, battery-safety compliance, privacy and accessibility compliance, an economic-impact assessment, and a workforce-mitigation plan. The county also stated that it could not certify whether the AI systems powering the robots are safe and called for state or federal safety certification.
- Significance: This is evidence that deployment barriers are not limited to technical performance. Even before general-purpose robots become commonplace, local authorities may require permits, safety documentation, recall disclosures, economic-impact analysis, worker protections, and additional fees for fire-response capacity. Such requirements can slow deployment, increase integration costs, and make heterogeneous multi-site operation difficult. The county’s statement that it cannot certify AI safety also highlights a governance gap for systems whose behavior is learned rather than fully specified.

### Insurance evidence shows deployment risk is concentrated in supervision, cyber incidents, and occupied-space operation

- Event date: 2026-09-21
- Sources: `S12`
- Observed fact: Koop’s September 21, 2026 report analyzed insurance quotes, policies, claims, and underwriting applications from 392 U.S. robotics companies covering policy years 2021-2025. It reported that cyber incidents accounted for 34% of loss dollars, incidents involving an injured member of the public accounted for 12%, and the leading root cause was how robots were deployed and supervised. The report also stated that 87% of applicants reported a safe-stop system, but underwriters credited a named standard or safe-stop in only 7% of reviews; only 6% of companies published a safety page. Its pricing index placed delivery robots, robot arms, and machines operating in occupied spaces well above autonomous mobile robots.
- Significance: This challenges the view that the main bottleneck is simply improving robot intelligence. Real-world risk appears to arise substantially from integration, supervision, cybersecurity, and operation around people. The gap between companies reporting controls and underwriters crediting those controls suggests that safety claims are not yet consistently evidenced. Higher relative insurance pricing for delivery robots, arms, and machines in occupied spaces also indicates that broad deployment may carry materially higher risk-adjusted operating costs than structured AMR use.

### A warehouse AMR payback model depends on a narrow labor-offset and utilization regime

- Event date: 2026-09-16
- Sources: `S13`
- Observed fact: On September 16, 2026, Reeman Robotics published a total-cost-of-ownership model for a 300-kilogram autonomous mobile robot in high-mix warehouses. The model estimated five-year ownership costs of $55,000-$85,000, a 12-30 month payback period, and a break-even condition requiring approximately 1.5-2.0 full-time-equivalent transport hours of labor offset per day and 8-14 kilometers of daily travel. The model therefore makes economic viability contingent on sufficient route distance, labor reallocation, and utilization.
- Significance: Even a favorable commercial case for autonomous logistics is not equivalent to general-purpose automation. The stated break-even assumptions imply that robots may fail economically in low-volume sites, irregular workflows, short travel routes, or operations where labor cannot be cleanly reallocated. The model also illustrates why cost per productive hour is likely to vary sharply with site layout, route density, supervision, charging, recovery, and integration requirements.

### The strongest within-window evidence remains benchmark- and preprint-heavy rather than deployment-grade

- Event date: 2026-09-22
- Sources: `S9`, `S10`, `S11`, `S12`, `S13`
- Observed fact: The September 15-22, 2026 evidence reviewed here includes a failed replication of a robot-learning ablation, a safety architecture with low coverage and negative transfer, a local permitting proposal requiring safety and workforce documentation, insurance data showing losses tied to supervision and cyber risk, and a vendor payback model dependent on narrow utilization assumptions. None of these sources provides independently audited evidence of broad general-purpose manipulation across varied sites, sustained autonomous operation in open-ended logistics, or verified cost per productive hour across a fleet.
- Significance: The combined evidence narrows the interpretation of research progress. Improvements in manipulation benchmarks or policy architectures should not be treated as evidence that robots are coordinating a growing share of transport, maintenance, construction, or care work. The main unresolved question is not whether robots can complete selected tasks, but whether they can do so reliably, safely, economically, and with limited human intervention across changing environments.

## Assumption Assessments

### PS-ROBOTICS-001: Embodied AI automates material coordination

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S3`, `S4`, `S5`, `S6`, `S7`, `S8`, `S9`, `S10`, `S11`, `S12`, `S13`
- Evidence: The evidence strengthens the narrower claim that robot-learning, temporal perception, morphology transfer, and targeted adaptation are advancing. TEMPO improved Bottle Handover success from 44% to 74%; PARTS reported selected long-horizon task gains; CIVIL addressed transfer under clutter; and MorFiC reported locomotion transfer across seven quadruped embodiments (S1,S3,S4,S5,S6). However, the evidence does not establish broad deployment across transport, maintenance, construction, or care work. Safety coverage remains weak or overblocking (S7,S8,S10), deployment economics depend on narrow utilization and labor-offset assumptions (S13), insurance data identifies supervision and integration as major risks (S12), and the synthesis found no independently audited fleet-wide uptime, intervention, labor-substitution, or cost-per-productive-hour evidence (S9,S10,S11,S12,S13).
- Real-world implication: Technical capability is improving for selected manipulation and locomotion tasks, but general-purpose material coordination remains unverified. Near-term deployment is more likely to expand in structured or carefully supervised logistics settings than across open-ended construction, maintenance, healthcare, or care work. Integration, safety certification, supervision, and site-specific economics remain substantial constraints.
- PostSingularity implication: A post-singularity setting can plausibly support extensive embodied automation, but this assumption should not be treated as an automatic consequence of current research gains. The storyworld requires credible mechanisms for reliable transfer, physical safety, recovery from novel failures, workforce transition, and economically viable operation across heterogeneous environments.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied evidence concerns terrestrial robotics, robot learning, embodied-agent safety, and warehouse economics. It contains no reliable within-window evidence on launch cost, orbital station duration, closed-loop life support, in-space manufacturing, autonomous space missions, or human-health limits in off-world habitats.
- Real-world implication: No directional update is justified for the practicality of sustained orbital or off-world communities. The assumption remains dependent on unresolved aerospace, life-support, health, manufacturing, and economic evidence not covered by this packet.
- PostSingularity implication: The post-singularity implication remains conditional: autonomous systems and abundant energy could reduce operational burdens, but they do not by themselves establish durable off-world settlement. The storyworld should preserve uncertainty around habitat reliability, human adaptation, resupply independence, and the economics of maintaining communities away from Earth.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **strengthened**
- Confidence: **low**
- Sources: `S10`, `S11`, `S12`
- Evidence: Several supplied sources provide indirect evidence that increasing embodied-AI influence is producing demand for inspectable safety records, traceable decision systems, failure recall, safe-stop verification, and deployment documentation. CoreSense explicitly frames its system as an auditable integration pattern, while San Mateo County proposed safety records, recall history, privacy and workforce documentation for autonomous robots; Koop found a gap between claimed and independently credited safety controls (S10,S11,S12). This supports stronger audit and verification pressure in robotics, but does not directly establish broad AI provenance standards, general content provenance adoption, or model-audit regulation across society.
- Real-world implication: Organizations deploying influential AI-controlled physical systems are likely to face growing expectations for traceability, safety evidence, incident records, and accountable oversight. Adoption may remain uneven because current controls can be difficult to verify and may trade coverage for overblocking. The evidence does not justify claiming that comprehensive provenance infrastructure has already become standard.
- PostSingularity implication: A post-singularity society could plausibly institutionalize provenance rituals, audit trails, and graduated oversight as prerequisites for trusting powerful systems. The supplied evidence supports this as a credible governance direction, but not as an inevitable or universally effective one; audit systems may be partial, contested, gamed, or operationally restrictive.

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: No supplied source addresses brain-computer interfaces, bidirectional neural implants, channel count, long-term implant safety, decoded speech, affective communication, or neural privacy. Robotics and embodied-AI findings do not provide evidence for safe, high-bandwidth communication between nervous systems and AI.
- Real-world implication: No directional update is justified. The assumption remains unresolved pending evidence on durable bandwidth, tissue response, safety, privacy, clinical efficacy, and real-world usability.
- PostSingularity implication: The post-singularity setting may include rich neural links, but the supplied evidence does not constrain when or whether they become safe and socially acceptable. Any storyworld dependence on sensory or emotional two-way neural communication remains speculative and should retain unresolved medical, privacy, consent, and access barriers.

### PS-AI-001: Recursive AI progress can create a societal discontinuity

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S9`, `S10`, `S11`, `S12`, `S13`
- Evidence: The supplied evidence shows incremental advances in robot learning and embodied-agent capability, alongside replication instability, safety limitations, deployment barriers, and governance gaps. It does not measure recursive AI research automation, frontier capability acceleration, institutional adaptation speed, or a discontinuity in general AI development. The cited robotics results therefore cannot establish or refute rapid recursive improvement sufficient to make existing institutions and expectations lose relevance.
- Real-world implication: There is no justified directional update on the probability or timing of a societal discontinuity caused by recursive AI progress. Current evidence supports continued capability development in selected domains but also shows that technical progress can be brittle, difficult to reproduce, and constrained by deployment and governance factors.
- PostSingularity implication: The post-singularity event remains an unresolved premise rather than an evidence-backed forecast in this packet. A storyworld may use rapid recursive improvement as a causal mechanism, but it should not infer institutional obsolescence solely from the reported robotics advances; the transition would require additional evidence about AI-led research automation, scaling, control, and institutional response.

## Canon Implementation Plan

### `worldbible/technologies/robotics.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S9`
- Why this location: The evidence supports meaningful advances in temporal perception, causal imitation, targeted adaptation, vision-based learning, and cross-morphology transfer, but the gains remain task-specific, unevenly replicated, and concentrated in controlled experiments or selected real-robot demonstrations.
- Proposed change: Add a qualification to the Robotics summary stating that adaptive robotics benefits from temporal context, task-relevant demonstrations, targeted post-training, and morphology-aware transfer, while noting that reported improvements do not yet establish reliable general-purpose performance across varied embodiments, environments, or long-horizon workflows. Preserve the existing claims about adaptive robots and human collaboration.
- Implementation steps:
  1. Insert the qualification in the existing Summary section after the current description of adaptive robots and before the existing references to Drone Logistics and Trust Fabrics.
  2. Mention temporal motion summaries, recent proprioceptive history, causal demonstration labels, targeted residual adaptation, and morphology-conditioned policies as mechanisms supporting adaptation rather than as universally solved capabilities.
  3. Retain the existing links to Drone Logistics and Trust Fabrics; do not replace them with research-source links unless repository linking conventions require it.
  4. Review the wording against the Function and Story Use sections so that the new research-informed capability does not imply broad deployment or autonomous reliability.
- Dependencies or conflicts:
  - The reported TEMPO, CIVIL, PARTS, and MorFiC results are not independently replicated in the supplied evidence.
  - MorFiC concerns locomotion and selected quadruped embodiments, not manipulation, tool use, or arbitrary robot morphologies.
  - The ACT forensic rerun challenges interpreting architectural complexity or benchmark gains as durable capability, so the summary should avoid presenting learning advances as settled or universally reproducible.
  - Existing Story Use examples may imply more reliable adaptive autonomy than the evidence supports and should be checked for consistency.

### `worldbible/technologies/robotics.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S1`, `S3`, `S4`, `S6`, `S7`, `S8`, `S9`, `S10`
- Why this location: The current functions describe reconfiguration, swarm coordination, and emotional telemetry, while the evidence shows that reliable physical adaptation also depends on temporal state, targeted failure repair, embodiment transfer, refusal behavior, and safety systems whose coverage and transfer remain limited.
- Proposed change: Add function bullets explaining that robots can use temporal perception and proprioceptive history to infer motion and task phase, learn from causal task-relevant demonstrations, apply targeted residual corrections to recurring subtasks, and condition policies on morphology for transfer. Add a limiting bullet stating that safety gating and failure recall may stop unsafe actions while still suffering from low coverage, negative transfer, or overblocking.
- Implementation steps:
  1. Insert the new bullets within the existing Function section after the modular-joints and swarm-mesh bullets, before the emotional-telemetry bullet.
  2. Describe these mechanisms as capabilities with operational limits, not as guaranteed behavior or certified safety.
  3. Include the distinction between selected benchmark or real-robot improvements and broad deployment reliability.
  4. Review the emotional telemetry and human-deference language to ensure it does not imply that emotional feedback alone provides physical hazard detection, refusal, recovery, or safety certification.
- Dependencies or conflicts:
  - RoboHarm measures hazardous-task attempts and completions, whereas CoreSense measures protocol-defined unsafe proceeds with substantial overblocking; these metrics should not be merged into a single safety claim.
  - CoreSense was not a sustained autonomous field deployment and explicitly does not establish certified safety or autonomous recovery.
  - The ACT replication conflict means that any claim about a specific learning architecture should remain implementation- and evaluation-dependent.
  - Existing swarm and human-deference claims may need separate review if they imply reliable coordination in changing environments, which the supplied evidence does not establish.

### `worldbible/technologies/drone-logistics.md` -> Cultural Effects

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-ROBOTICS-001`
- Sources: `S11`, `S12`, `S13`
- Why this location: The evidence challenges an interpretation of autonomous logistics as automatically economical and socially frictionless: deployment risk is concentrated in supervision, cybersecurity, occupied-space operation, permitting, workforce effects, and site-specific utilization.
- Proposed change: Add cultural-effects bullets stating that autonomous logistics deployments may require permits, safety and recall records, battery-risk documentation, privacy and workforce assessments, and documented safe-stop controls. Add that payback depends on sufficient route distance, labor offset, utilization, supervision, charging, recovery, and integration, while insurance and public-space risks can raise operating costs.
- Implementation steps:
  1. Insert the new bullets at the end of the existing Cultural Effects section after the current bullet about groups rejecting drones and traditional courier rituals.
  2. Keep the existing claims about near-instant delivery and equitable distribution, but qualify them as outcomes that depend on route density, supervision, safety evidence, and local authorization.
  3. Reference deployment documentation and workforce effects without presenting the San Mateo County proposal as a universal or national rule.
  4. Review the Function section for consistency with the added charging, recovery, supervision, and integration constraints.
- Dependencies or conflicts:
  - The San Mateo County measure applies to a specific jurisdiction and its final legal text and enforcement record were not established in the supplied source.
  - The Reeman payback model is vendor-authored and does not independently verify uptime, maintenance, deployment labor, or actual customer results.
  - Koop's insurance evidence is commercially produced and may not represent the entire robotics industry; its pricing indices are relative rather than direct productive-hour costs.
  - The existing claim that drone fleets enable equitable distribution may conflict with site-specific economics and should not be expanded into a universal claim of economically viable logistics.

### `worldbible/technologies/trust-fabrics.md` -> 🛡 Oversight Systems

- Priority: **low**
- Recommendation: **revise**
- Evidence relationship: **supports**
- Assumptions: `PS-AI-003`
- Sources: `S10`, `S11`, `S12`
- Why this location: The evidence supports the plausibility of oversight systems requiring safety records, incident traceability, recall history, safe-stop verification, and accountable deployment documentation, while also showing that such controls can be incomplete, difficult to verify, or operationally restrictive.
- Proposed change: Add an oversight bullet stating that embodied AI deployments increasingly require documented safety records, recall histories, incident reports, safe-stop evidence, privacy and workforce assessments, and independent verification of claimed controls. Add a qualification that audit and gating systems can have limited coverage, negative transfer, or excessive blocking and therefore do not constitute automatic certification or complete safety.
- Implementation steps:
  1. Insert the new bullets after the existing Resonance Drift Alerts bullet within the Oversight Systems subsection.
  2. Use the existing terminology of transparency, provenance, and oversight, but distinguish documented accountability from proof that a robot or AI system is safe in every context.
  3. Cross-reference the Verification Layers subsection by stating that records and control claims should be inspectable rather than merely self-reported.
  4. Review AI Trust for compatible social consequences, especially public review, accountability, and the possibility that oversight rituals become restrictive or contested.
- Dependencies or conflicts:
  - CoreSense supports auditable integration but reports limited physical coverage, negative transfer, and overblocking; it must not be represented as general autonomous recovery or certified safety.
  - San Mateo County's proposal is local and prospective, not evidence of a universal regulatory regime.
  - Koop reports a gap between organizations claiming safe-stop controls and underwriters crediting named or verified standards; the canon should preserve that distinction.
  - Existing Verification Layers language says all decision-making logic is viewable by bonded citizens, which may be stronger than the supplied evidence and should be reviewed for privacy, trade-secret, and operational feasibility conflicts.

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

- The robotics evidence is dominated by preprints, controlled experiments, university announcements, benchmark results, and vendor or insurer analyses rather than independently audited deployment records.
- No supplied source establishes fleet-wide uptime, intervention frequency, failure recovery, labor substitution, or cost per productive hour for general-purpose robots in live logistics operations.
- The positive manipulation and transfer results have not been independently replicated in the supplied evidence, while the ACT forensic rerun demonstrates that some prominent robot-learning gains can be sensitive to training duration, checkpoint choice, and implementation details.
- The safety findings are not directly comparable: RoboHarm measures hazardous-task attempts and completions, while CoreSense measures protocol-defined unsafe proceeds with substantial overblocking and limited physical coverage.
- The evidence on provenance and audit systems is indirect and concentrated on embodied robotics; it does not establish broad adoption of AI transparency standards, content provenance, or regulatory disclosure rules.
- No supplied evidence addresses sustained off-world settlement, neural interfaces, or recursive AI-driven institutional discontinuity.
- The absence of evidence for broad deployment or other technologies in this packet is not proof that such developments do not exist outside the searched material.
- The ACT CVAE ablation originally reportedly showed mean success falling from 35% to 2% when the encoder was removed, whereas the forensic re-run did not reproduce that drop and found results sensitive to training duration and checkpoint selection. This is a direct conflict between the original reported ablation and the later re-run, not evidence that all latent-variable or action-chunking methods fail.
- RoboHarm reports substantial unsafe-task attempts and completions by frontier robot policies, while CoreSense reports zero protocol-defined unsafe proceeds in selected datasets. These results are not directly contradictory because they measure different systems, tasks, metrics, and safety mechanisms; together they show a coverage-versus-overblocking and capability-versus-refusal tension.
- MorFiC's zero-shot transfer claim is supported by a university announcement and an earlier paper, but the announcement is within the priority window while the primary paper was posted before the window. The timing difference limits its status as a new within-window research publication.
- The positive manipulation and transfer findings report benchmark or selected real-robot gains, while the synthesis and counterevidence findings report no independently audited broad deployment, sustained open-ended logistics operation, or verified cost per productive hour. This is a scope conflict only if laboratory or selected-task results are interpreted as deployment evidence; the sources do not establish that equivalence.
- PS-SPACE-001 was assessed as insufficient-evidence. The supplied sources address terrestrial robotics, safety, logistics, and economics, not launch cost, orbital habitat duration, closed-loop life support, in-space manufacturing, autonomous space missions, or human-health limits. No repository edit is warranted in worldbible/technologies/aerospace-systems.md or locations/orbital-sanctuary.md on this evidence.
- PS-NEURO-001 was assessed as insufficient-evidence. No supplied source addresses brain-computer interfaces, bidirectional neural implants, neural bandwidth, long-term implant safety, affective communication, or neural privacy. No edit is warranted in worldbible/technologies/neural-links.md.
- PS-AI-001 was assessed as insufficient-evidence. The robotics findings do not measure recursive AI research automation, frontier capability acceleration, institutional adaptation, or a discontinuity in general AI development. No edit is warranted in worldbible/singularity-event.md or worldbible/timeline.md.
- The mixed PS-ROBOTICS-001 assessment is covered by the Robotics and Drone Logistics plans: capability claims are retained but qualified, while broad deployment, safety, and economic implications are made conditional rather than asserted as established canon.
- The strengthened PS-AI-003 assessment is intentionally treated as a low-priority revision rather than proof that comprehensive provenance infrastructure already exists. The evidence supports a credible governance direction in embodied AI, not universal adoption of audit standards or regulation.
- No change is proposed to worldbible/technologies/index.md because the evidence does not establish a new canonical technology category or require a new repository file; the affected claims can be handled in the declared Robotics, Drone Logistics, and Trust Fabrics sources.
- No edit is proposed to philosophy/ai-trust.md because the evidence supports a governance and oversight qualification in Trust Fabrics, but does not independently establish a distinct cultural practice or philosophical consequence requiring revision there.
- Commercial claims about humanoid production and general-purpose robot capability were excluded when they lacked a primary technical paper, audited deployment data, or sufficiently detailed evaluation protocol.
- The out-of-window Amazon Proteus expansion and earlier warehouse-robot deployment figures were not counted as priority-window findings.
- The out-of-window negative result on scaling autonomous robot data collection at https://arxiv.org/abs/2411.01813 was not counted as a dated September 15-22 finding.
- The September 8, 2026 warehouse robotics fatality and subsequent regulatory charges were excluded from the windowed evidence packet because they fall outside the strict priority window and would require further primary court and regulator records.
- No claim of broad general-purpose manipulation across varied sites, sustained autonomous operation in open-ended logistics, or verified cost per productive hour across a fleet is supported by these sources.
- The MorFiC evidence does not establish transfer to arbitrary robot morphologies, dexterous manipulation, tool use, or logistics workflows.
- The RoboHarm non-completion results for MolmoAct2 were not treated as clean evidence of safe refusal because MolmoAct2 lacks a language-based refusal channel.
- The Reeman payback period was not treated as demonstrated deployment economics because it is a vendor-authored model without independently verified uptime, failure rates, maintenance costs, deployment labor, or actual customer results.
- The absence of independently audited deployment evidence in the searched material was not treated as proof that no such deployments exist.

## Watchlist

- Independent replication of TEMPO, CIVIL, PARTS, and MorFiC across varied embodiments, environments, objects, and long-horizon tasks.
- Robot deployment counts, productive-hour cost, uptime, intervention rates, failure recovery, labor substitution, and customer-verified performance in live logistics operations.
- Evidence of autonomous robots expanding into construction, maintenance, healthcare, or care work rather than remaining in structured logistics settings.
- Physical safety evaluations combining refusal reliability, hazard detection, useful task completion, coverage, overblocking, and recovery under changing scenes.
- Regulatory or certification standards for learned general-purpose manipulation policies, including requirements for provenance, incident reporting, recalls, and cross-site validation.
- Launch economics, station duration, closed-loop life-support reliability, in-space manufacturing, autonomous mission operations, and human-health outcomes for long-duration space habitation.
- AI transparency standards, content-provenance adoption, independent model audits, and regulatory disclosure rules beyond robotics-specific permitting.
- Neural-interface channel capacity, bidirectional communication, long-term implant safety, decoded speech or affect, privacy protections, and clinical durability.
- AI research automation, capability-evaluation trends, evidence of recursive improvement, and the speed at which institutions adapt to frontier capability changes.

## Sources

- `S1` [TEMPO: Learning Temporal Context for Dynamic Robot Manipulation](https://arxiv.org/abs/2609.16864) — arXiv / University of California, Irvine; 2026-09-15; primary-research; URL supplied in structured research output. Primary preprint describing the temporal-context method, benchmark, and reported dynamic-manipulation results.
- `S2` [Optimization of vision-based deep reinforcement learning frameworks to improve robotic manipulation tasks by means of sophisticated greedy osprey optimizer](https://www.nature.com/articles/s41598-026-65718-8) — Scientific Reports / Springer Nature; 2026-09-15; primary-research; URL supplied in structured research output. Peer-reviewed research article published within the priority window addressing vision-based robot learning and unstructured manipulation.
- `S3` [Civil: causal and intuitive visual imitation learning](https://link.springer.com/article/10.1007/s10514-026-10266-3) — Autonomous Robots / Springer Nature; 2026-09-18; primary-research; URL supplied in structured research output. Primary journal article with theoretical analysis, user-study results, and real-world imitation-learning experiments.
- `S4` [From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention](https://arxiv.org/abs/2609.21788) — arXiv; 2026-09-18; primary-research; URL supplied in structured research output. Primary preprint reporting the PARTS method, real-robot tasks, success-rate changes, and human-intervention requirements.
- `S5` [One Robot, Many Bodies: New System Helps Four-Legged Robots Adapt](https://www.cs.umd.edu/article/2026/09/one-robot-many-bodies-new-system-helps-four-legged-robots-adapt) — University of Maryland Department of Computer Science; 2026-09-21; official-release; URL supplied in structured research output. First-party university announcement dated within the priority window, with training-time and transfer claims.
- `S6` [MorFiC: Fixing Value Miscalibration for Zero-Shot Quadruped Transfer](https://arxiv.org/pdf/2603.14554) — arXiv / University of Maryland / George Mason University; 2026-08-24; primary-research; URL supplied in structured research output. Primary paper containing the technical method, seven-robot transfer claim, speed comparisons, and real-robot deployment details.
- `S7` [RoboHarm: Do Frontier Robot Policies Refuse Unsafe Instructions?](https://robocurve.org/roboharm/) — Robocurve; 2026-09-18; official-release; URL supplied in structured research output. First-party benchmark page documenting the hardware, policies, trial counts, outcomes, and explicit methodological limitations.
- `S8` [RoboHarm: Five fixed-scene robot refusal tasks](https://github.com/robocurve/roboharm) — Robocurve; 2026-09-18; official-release; URL supplied in structured research output. Open-source benchmark repository containing task definitions, experiment tooling, labeling rubric, and reproducibility documentation.
- `S9` [The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer](https://arxiv.org/abs/2609.16745) — arXiv; 2026-09-15; primary-research; URL supplied in structured research output. Primary forensic re-evaluation reporting failure to reproduce the original ablation effect, sensitivity to training and checkpoint choices, and increased throughput after removing the latent encoder.
- `S10` [CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions](https://arxiv.org/abs/2609.19512) — arXiv; 2026-09-17; primary-research; URL supplied in structured research output. Primary source reporting negative transfer results, low coverage, overblocking, limited physical corroboration, and the authors’ explicit qualification that the system is not autonomous recovery or certified safety.
- `S11` [San Mateo County Supervisors Pass New Public Safety, Worker Protections for Autonomous Robots](https://www.smcgov.org/ceo/news/san-mateo-county-supervisors-pass-new-public-safety-worker-protections-autonomous-robots) — County of San Mateo, California; 2026-09-15; official-release; URL supplied in structured research output. Official county announcement documenting the permitting proposal, safety-record and recall requirements, worker protections, battery-risk provisions, and the absence of local AI safety-certification authority.
- `S12` [IN BOTS WE TRUST 2026: The State of Robot Risk](https://www.koop.ai/news/robots-are-earning-the-worlds-trust-and-koop-has-the-data-to-prove-it) — Koop; 2026-09-21; reputable-secondary; URL supplied in structured research output. Industry insurance analysis based on claims and underwriting data, with direct evidence about loss causes, safety-control verification, and relative risk pricing across robot categories.
- `S13` [TCO of a 300KG Delivery Robot: Calculating Payback in High-Mix Warehouses](https://reemanbot.com/posts/tco-300kg-delivery-robot-payback-high-mix-warehouses) — Reeman Robotics; 2026-09-16; official-release; URL supplied in structured research output. Vendor-published economic model that makes the utilization, travel-distance, and labor-offset assumptions behind AMR payback explicit.

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
  "id": "research_2026-09-22_general-purpose-robotics-dexterity-robot-learnin",
  "type": "research_brief",
  "name": "Robotics Evidence Review, 15\u201322 September 2026: Capability Gains Without Deployment Proof",
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
