# Neurotechnology Evidence Review: Incremental Progress, Persistent Deployment Constraints, and Emerging Neuro-Rights Risks
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-07-29
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The audited evidence from 2026-07-22 through 2026-07-29 shows incremental progress in neural recording, task-specific decoding, wireless neuromodulation, minimally invasive implantation methods, portability, and clinically oriented BCI research. It does not establish chronic high-bandwidth human neural communication, generalized real-time speech or affect decoding, reliable AI-mediated mood or reward control, routine home-use implantation, or broad adoption of AI provenance systems. Neuro-rights concerns are becoming technically specific: current reviews identify unresolved issues involving raw recordings, decoded inferences, decoder parameters, closed-loop signals, timing metadata, consent, ownership, secondary use, misuse, and monetization. The evidence therefore qualifies PS-NEURO-001, strengthens the governance premise of PS-NEURO-002 while limiting its technological premise, leaves PS-AI-003 insufficiently evidenced at the broad societal level, and provides no basis to assess PS-SPACE-001 or PS-SOCIAL-002. Canon implications are conservative review recommendations only; no assumption registry or canon file has been updated.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-07-22 through 2026-07-29
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### First-in-human testing begins for Ability Neurotech’s novel BCI platform

- Event date: 2026-07-22
- Sources: `S1`
- Observed fact: Ability Neurotech announced on July 22, 2026 that its first-in-human procedure had been conducted at the Technical University of Munich’s University Hospital Rechts der Isar. The study is planned to involve up to five people undergoing brain-tumor surgery, with approximately 20–30 minutes of intraoperative neural recording per patient. Initial procedures focused on end-to-end signal-acquisition validation under general anesthesia; later stages are intended to examine neural decoding during speech and motor tasks in conscious patients.
- Significance: This is a translational milestone from prototype development toward human neural-signal acquisition. If subsequent stages produce usable speech or motor decoding, the study could provide evidence for less established BCI architectures and expand the competitive field beyond the best-known implant developers. Limitations: The available source is a reputable specialist-news report describing a company announcement, not a peer-reviewed clinical publication or regulatory record. The reported procedure is an intraoperative feasibility study, not evidence of chronic implantation, long-term safety, useful bandwidth, or independent everyday use. No quantitative decoding results, participant outcomes, adverse-event data, or regulatory authorization details were available in the searched material.

### Hybrid EEG/EMG group BCI demonstrates online control of UAV swarms

- Event date: 2026-07-22
- Sources: `S2`
- Observed fact: A Frontiers in Neurorobotics study published July 22, 2026 described a group brain-computer-interface system combining hand-movement signals, visual evoked potentials, EEG, and EMG with shared-control algorithms for UAV-swarm operation. In eight participants, the system achieved reported offline accuracy of 88.91 ± 5.06% and online accuracy of 88.89 ± 1.96%.
- Significance: The result extends neural decoding from single-user assistive control toward multi-person, shared-control robotic systems. It is relevant to the high-bandwidth-interface signal because it demonstrates multimodal decoding and AI-mediated action selection, although it remains far from rich two-way communication or sensory/emotional exchange. Limitations: The experiment involved only eight participants and used noninvasive signals combined with hand movement and visual-evoked paradigms. The reported accuracies are task-specific and do not establish robust control of complex UAV missions, safety in uncontrolled environments, or generalization across users and settings. The abstract does not establish long-duration use, clinical utility, or bandwidth comparable to natural speech or continuous motor control.

### Ultralight infrared-controlled wireless tDCS and DBS systems enable stimulation in freely moving mice

- Event date: 2026-07-24
- Sources: `S3`
- Observed fact: A Microsystems & Nanoengineering study published July 24, 2026 reported wireless infrared-controlled neuromodulation devices for freely behaving mice. The transcranial direct-current-stimulation device weighed less than 1.5 grams and the deep-brain-stimulation device less than 0.5 grams. Wavelength-selective phototransistors independently controlled stimulation channels at 810 and 950 nanometers. In mouse experiments targeting the secondary motor cortex, stimulation produced direction-specific circling behavior, while open-field testing found no detectable locomotor effect from device attachment or infrared illumination alone.
- Significance: The work advances the hardware needed for closed-loop and behavior-linked neuromodulation experiments by reducing tethering, device weight, and control complexity. It supports the possibility of more naturalistic stimulation studies, but does not yet demonstrate reliable therapeutic mood control or human use. Limitations: The devices were tested in mice, not humans. The system used external infrared illumination and did not demonstrate autonomous closed-loop stimulation based on recorded neural or behavioral signals. The behavioral validation was limited, including small animal samples and motor-circuit stimulation; effects on cognition, affect, dependency, or long-term tissue health were not established. The study demonstrates stimulation delivery, not high-fidelity decoding or bidirectional human communication.

### Clinical iBCI data protections are identified as inadequate for decoded neural information

- Event date: 2026-07-27
- Sources: `S4`
- Observed fact: A Communications Medicine review published July 27, 2026 argued that implantable BCI data remain insufficiently protected despite existing health-privacy frameworks such as HIPAA and GDPR. It identified five gaps: overreliance on conventional de-identification, limited individual control and rights, conflated consent practices, limited safeguards against misuse, and underspecified ownership. The review recommends stronger rights over neural data, separate consent for different data uses, limits on harmful secondary uses, and monetization guardrails.
- Significance: This is a direct neuro-rights signal. The governance issue is no longer limited to speculative consumer mind-reading: the review frames clinical iBCI systems as producing longitudinal raw recordings, decoded inferences, and personalized model parameters that may reveal intended actions, linguistic content, and other cognitive processes. Limitations: This is a review and policy analysis, not evidence that a specific breach, misuse event, or court decision occurred during the window. The authors describe the governance risks as anticipatory because large-scale clinical iBCI datasets are only beginning to emerge. The article proposes protections but does not establish adoption, enforcement, or consensus among regulators or device developers.

### Subcellular-diameter carbon-fiber electrode motes receive a minimally invasive rat-cortex implantation method

- Event date: 2026-07-28
- Sources: `S5`
- Observed fact: A Frontiers in Neuroscience study published July 28, 2026 described a method for implanting individual wireless neural-interface motes with penetrating subcellular-diameter carbon-fiber electrodes into rat cortex. The paper positions distributed one- to two-channel wireless motes, or neural dust, as a route to removing wired connections through the scalp and potentially increasing implant biocompatibility. The method addresses the problem that batch implantation of such devices can damage or displace large numbers of neurons.
- Significance: This is a hardware-pathway signal for scalable, distributed neural interfaces. If the approach can be combined with reliable wireless power, telemetry, and long-term tissue compatibility, it could increase channel distribution while reducing per-electrode invasiveness. It is relevant to channel-count and long-term-implant-safety questions, but remains preclinical. Limitations: The reported work used rats and non-functional motes; it did not demonstrate neural recording, stimulation, decoding, or wireless clinical operation. The study does not establish chronic implantation stability, immune response, signal quality, power delivery, data bandwidth, or safety in humans. Individual one- to two-channel motes would require large numbers of implants and a scalable external communication and power architecture.

### IEEE EMBC 2026 programming reflects a shift toward home-use and clinically oriented EEG BCI systems

- Event date: 2026-07-28
- Sources: `S6`, `S7`
- Observed fact: The IEEE EMBC 2026 program on July 28, 2026 included a BCI/BMI session featuring a presentation titled “Toward an Implantable Brain–Computer Interface for Home Use: Development of a Lightweight Portable WIMAGINE System,” alongside work on EEG-based visual-evoked and motor-imagery interfaces, personalized stimulation, and LLM-based P300 spellers. A related IEEE mini-symposium focused on EEG BCIs for cognitive assessment, stroke rehabilitation, and personalized neurological care.
- Significance: The program is not itself a measured product milestone, but it is a useful field signal: research attention is concentrating on portability, home operation, rehabilitation, clinical assessment, and language-model-assisted decoding. Those are the practical bottlenecks separating laboratory demonstrations from durable real-world use. Limitations: Conference-program entries are announcements of presentations, not peer-reviewed evidence of the underlying systems’ performance. The searched program pages did not provide complete abstracts, datasets, safety results, or independent validation for all listed presentations. This finding should not be treated as evidence that home-use implantable BCIs are clinically available.

### Closed-loop BCI rehabilitation evidence remains methodologically weak and difficult to generalize

- Event date: 2026-06-24
- Sources: `S8`
- Observed fact: A 2026 Frontiers in Neurology review identified persistent limitations in closed-loop BCI studies for stroke rehabilitation, including small sample sizes, possible mismatch between feedback and users’ endogenous intentions, difficulty ruling out placebo effects, and unresolved problems with individual-model generalization and system stability. The review also summarized reported invasive-BCI safety events, including skin irritation and low but nonzero rates of infection or death in the cited evidence base.
- Significance: This weakens claims that promising laboratory decoding or stimulation results already demonstrate robust, general-purpose clinical systems. Small samples, limited controls, and user-specific calibration make it difficult to infer population-level efficacy, durable benefit, or reliable operation outside supervised research settings. It directly challenges PS-NEURO-001 and narrows PS-NEURO-002 by showing that closed-loop control remains technically and clinically constrained. Limitations: The source is a review rather than a new randomized clinical trial or failed replication. The safety rates are summarized from cited studies and may combine heterogeneous devices, populations, and definitions of adverse events. The review concerns stroke rehabilitation and should not automatically be generalized to every BCI application.

### Implantable BCI deployment still carries unresolved surgical, device, and postmarket-surveillance risks

- Event date: 2026-07-29
- Sources: `S9`, `S10`
- Observed fact: The FDA’s neurological-device regulatory overview continues to identify implantation and stimulation-related adverse effects, imaging and electromagnetic-interference risks, and usability risks for active implantable neurological devices. The FDA also describes the need for robust registries and postmarket surveillance to support future neurological-device applications. The agency’s dedicated implanted-BCI guidance remains a framework for non-clinical testing and clinical considerations rather than evidence that high-bandwidth implantable BCIs are broadly approved for routine use.
- Significance: The regulatory pathway itself is evidence of deployment friction. A device can produce technically impressive signals while still requiring extensive evidence on surgical risk, interference, usability, long-term safety, and postmarket performance. This constrains forecasts of near-term mass adoption and directly bears on the falsifiers of intractable tissue response, unacceptable safety tradeoffs, and insufficient chronic evidence in PS-NEURO-001. Limitations: The FDA page is a general regulatory overview and does not report a new rejection, suspension, or adverse incident during the priority window. Regulatory requirements do not prove that a specific BCI device will fail to satisfy them. The page covers neurological devices broadly, so some listed risks are not unique to BCIs.

### Current iBCI data standards do not adequately represent real-time decoders and closed-loop control

- Event date: 2026-07-27
- Sources: `S4`
- Observed fact: A Communications Medicine review published July 27, 2026 reported that existing general neurodata standards were designed primarily for retrospective research datasets and do not adequately specify decoder architectures and parameters, closed-loop or effector-control signals, or device-specific timing and synchronization metadata for operational implantable BCIs. The review separately identified gaps involving de-identification, individual control, consent, misuse safeguards, and ownership.
- Significance: This is both a privacy and deployment constraint. High-bandwidth neural interfaces require data portability, auditability, security, and reproducibility across recording devices, decoders, cloud processors, and effectors. Missing standards make independent validation and safe transfer of a user’s decoder more difficult, while weak rights over derived inferences create governance risks before any speculative emotional or immersive interface becomes technically mature. This strongly challenges PS-NEURO-001 and supports the governance premise of PS-NEURO-002. Limitations: The article is a review and policy analysis rather than a documented breach or misuse case. The identified standards gap does not establish that every current iBCI system is noncompliant or unsafe. The proposed safeguards have not yet been shown to be widely adopted or enforced.

### Neural-dust implantation research remains non-functional and preclinical despite claims of scalable distributed interfaces

- Event date: 2026-07-28
- Sources: `S5`
- Observed fact: A Frontiers in Neuroscience study published July 28, 2026 described an implantation method for individual wireless motes with subcellular-diameter carbon-fiber electrodes in rat cortex. The implanted motes were non-functional. The paper addresses insertion efficiency and tissue-displacement problems but does not demonstrate neural recording, stimulation, decoding, wireless power, telemetry, chronic stability, or human operation.
- Significance: The result narrows optimistic interpretations of distributed high-channel-count neural interfaces. Miniaturizing electrodes and improving implantation are necessary engineering steps, but they do not establish a functioning scalable system. Large numbers of one- or two-channel motes would still require reliable power, addressing, synchronization, telemetry, explantation or maintenance strategies, and long-term tissue compatibility. This directly bears on the channel-count and long-term-safety falsifiers in PS-NEURO-001. Limitations: The study is an animal implantation-method paper, not a functional neural-interface demonstration. The motes were explicitly non-functional in the reported work. The study does not quantify chronic immune response, signal degradation, wireless bandwidth, power efficiency, or human surgical risk.

### Speech-decoding progress still depends on condition-specific datasets and does not establish generalized real-time mind reading

- Event date: 2026-07-27
- Sources: `S11`
- Observed fact: A Frontiers in Psychology paper published July 27, 2026 described construction of a Chinese-speech EEG dataset across multiple neural conditions, together with interpretability-driven spatial optimization. The publication centers on dataset construction and model-development methods rather than an independent demonstration of unrestricted, real-time, cross-user speech decoding in natural environments.
- Significance: This is a benchmark and generalization constraint. Dataset construction and improved spatial optimization can raise reported decoding performance without solving distribution shift, user calibration, linguistic variability, movement artifacts, or real-world continuous operation. It narrows claims that neural decoding is approaching general-purpose linguistic or affective access and indicates that PS-NEURO-001 should distinguish task-specific classification from durable high-bandwidth communication. Limitations: The source may contain technical results beyond the abstract-level information retrieved here. The finding does not show that the method fails; it shows that the reported publication does not establish unrestricted real-world decoding. EEG speech decoding and intracortical speech decoding have different signal-quality and deployment constraints.

### Home-use implantable BCI remains a conference-stage objective rather than demonstrated routine deployment

- Event date: 2026-07-28
- Sources: `S6`, `S7`
- Observed fact: The IEEE EMBC 2026 program on July 28, 2026 listed a presentation titled “Toward an Implantable Brain–Computer Interface for Home Use: Development of a Lightweight Portable WIMAGINE System.” The same program and related mini-symposium described EEG BCIs in the context of cognitive assessment, stroke rehabilitation, neurological monitoring, and personalized care. The program provides evidence of research direction, not evidence that home-use implantable systems have completed broad clinical validation or entered routine care.
- Significance: The wording “toward” and the conference format are important counterevidence against treating home operation as an established capability. Portability, unsupervised use, maintenance, caregiver burden, cybersecurity, calibration drift, reimbursement, and emergency handling remain separate deployment problems. This weakens optimistic interpretations of current demonstrations and supports the missing-deployment-evidence concern for PS-NEURO-001. Limitations: Conference listings are not peer-reviewed outcome reports. The program pages do not provide complete performance data, safety data, sample sizes, or independent validation for every presentation. A conference presentation could describe a mature prototype, but the listing alone cannot establish clinical availability.

### Focused-ultrasound neuromodulation evidence remains concentrated in pilot, preclinical, and translational research settings

- Event date: 2026-07-22 through 2026-07-24
- Sources: `S12`, `S13`
- Observed fact: The Focused Ultrasound Neuromodulation Conference held July 22–24, 2026 presented transcranial ultrasound stimulation as a research area focused on translation from bench to clinic. Its listed program included pilot human diffusion-MRI work, animal studies involving sleep and hypothalamic targets, guinea-pig work, and discussions of cellular and molecular effects. The program did not establish reliable human control of mood, reward, dependency, or immersive affective states.
- Significance: This is counterevidence to strong interpretations of engineered mental-state control. Targeting a circuit or changing a behavioral measure in an animal or pilot study is not equivalent to safe, reproducible, consent-preserving control of subjective mood or reward in humans. The evidence supports the narrower claim that neurostimulation may influence specific physiological or behavioral variables while leaving the governance scenarios in PS-NEURO-002 technologically unproven. Limitations: A conference program is not a systematic review or definitive assessment of the full field. The absence of a listed demonstration is not proof that no other group has achieved a related result. Some presentations may have contained unpublished data unavailable on the public program page.

### Neuro-rights concerns are becoming technically specific before enforceable protections are established

- Event date: 2026-07-27
- Sources: `S4`
- Observed fact: The July 27, 2026 Communications Medicine review states that existing privacy frameworks remain inadequate for implantable BCI data and identifies unresolved issues involving de-identification, individual control, consent, misuse, and ownership. It also notes that iBCI data may include raw recordings, processed features, decoded inferences, and personalized model parameters, with external processors involved because of limited on-device power and computational resources.
- Significance: The governance challenge is not limited to speculative consumer mind reading. Operational iBCI systems may distribute sensitive neural data across implants, external processors, clinical systems, model-training pipelines, and effectors. Until rights over derived inferences, decoder parameters, secondary uses, and monetization are clarified, expanded neural interfaces can increase dependency and institutional asymmetry even when used for legitimate clinical purposes. This supports PS-NEURO-002 while also constraining PS-AI-003: provenance and audit systems may be necessary, but the field has not yet shown that they are adopted or enforceable. Limitations: The source is a review and does not document a specific neural-data breach or coercive deployment during the priority window. The governance proposals are normative and do not establish enacted law. Some risks depend on future scale and the degree of neural information that particular devices can actually decode.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S4`, `S5`, `S6`, `S7`, `S8`, `S9`, `S10`, `S11`
- Evidence: Evidence shows incremental progress toward neural interfaces: first-in-human intraoperative recording, task-specific multimodal EEG/EMG control, research toward portable home-use systems, improved implantation methods, and condition-specific speech-decoding datasets (S1, S2, S5, S6, S7, S11). However, the supplied evidence does not demonstrate chronic implantation, long-term safety, durable high bandwidth, generalized real-time communication, sensory or emotional exchange, or routine home deployment. Reviews identify unresolved generalization, stability, surgical, interference, privacy, metadata, and postmarket-surveillance problems (S4, S8, S9, S10).
- Real-world implication: The field is advancing through narrow translational and task-specific milestones, but current evidence does not support claims of safe, general-purpose, high-bandwidth two-way neural communication. Clinical deployment remains constrained by chronic safety, calibration, data governance, regulatory, and reliability requirements.
- PostSingularity implication: A post-singularity setting could plausibly overcome bandwidth, safety, and decoder-generalization bottlenecks, but the current evidence supports treating rich human-AI neural communication as a capability requiring major intervening breakthroughs rather than an established trajectory. Any future deployment would need durable consent, decoder portability, auditability, privacy, and reversible control.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S3`, `S4`, `S8`, `S12`, `S13`
- Evidence: The Communications Medicine review identifies concrete governance gaps involving de-identification, individual control, consent, misuse safeguards, ownership, decoded inferences, model parameters, closed-loop signals, and operational timing metadata (S4). This directly supports the claim that neural interfaces can create consent, dependency, asymmetry, and control questions. At the same time, focused-ultrasound and mouse-neuromodulation evidence remains pilot, preclinical, or translational and does not establish reliable human control of mood, reward, dependency, or immersive experience (S3, S12, S13).
- Real-world implication: Neuro-governance concerns are already relevant for clinical and emerging operational iBCI systems, especially around data rights, secondary use, consent, and institutional control. The evidence does not yet show reliable broad mental-state engineering, so immediate policy concerns should focus on actual neural data and device-mediated interventions rather than speculative consumer mind control.
- PostSingularity implication: If reliable AI-mediated mental-state control becomes possible, the documented present-day gaps indicate that consent architecture, ownership, reversibility, anti-dependency safeguards, and limits on coercive or monetized use would become foundational governance problems. The technological premise remains unproven, but the governance direction is supported.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: `S4`
- Evidence: The supplied evidence documents governance and auditability needs for implantable BCI data, including missing decoder, closed-loop, timing, consent, ownership, and misuse provisions (S4). It does not provide direct evidence of broad AI transparency standards, content-provenance adoption, model-audit requirements, or graduated oversight responding to AI influence across society. The neuro-rights review proposes safeguards but does not establish adoption, enforcement, or regulatory consensus.
- Real-world implication: There is evidence for a narrower need for provenance and audit systems in operational neural-interface ecosystems, but not enough supplied evidence to assess the broader prediction that increasing AI influence is producing stronger societal provenance and audit systems.
- PostSingularity implication: A post-singularity society may require comprehensive provenance, verification, and audit rituals, particularly where AI systems mediate neural data or consequential decisions. The current record does not establish whether such systems will be widely adopted, effective, or politically durable.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: No supplied source addresses launch cost, orbital or off-world station duration, closed-loop life support, in-space manufacturing, propulsion, autonomous mission operations, or sustained human settlement. The evidence packet is concentrated on neural interfaces and neuromodulation, so it provides no basis for a directional verdict.
- Real-world implication: The supplied evidence does not change the assessment of sustained orbital or off-world settlement. Its practicality remains unresolved on the listed engineering, biological, and economic dimensions.
- PostSingularity implication: The assumption remains a plausible post-singularity scenario, but no conclusion about its likelihood or timing can be drawn from the audited evidence provided.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied quality notes explicitly state that evidence for analog practices, device-free spaces, right-to-disconnect responses, or low-technology communities specific to neurotechnology users was not located in the priority window. None of the cited sources measures analog-media growth, low-tech community formation, or cultural resistance to pervasive integration.
- Real-world implication: The evidence packet cannot establish whether analog and private practices are persisting, expanding, or disappearing as a response to AI and neural technology. The assumption remains unassessed rather than weakened or strengthened.
- PostSingularity implication: Analog or low-technology practices remain a plausible agency-preserving response in a post-singularity society, but the supplied evidence offers no empirical basis for forecasting their prevalence, social role, or durability.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S4`, `S5`, `S6`, `S7`, `S8`, `S9`, `S10`, `S11`
- Why this location: The evidence supports incremental progress in neural recording, task-specific decoding, portability, and implantation methods, but challenges the file’s unqualified presentation of neural links as safe, deeply personalized shared realities. No supplied source demonstrates chronic human operation, generalized high-bandwidth communication, sensory or emotional exchange, or routine home deployment.
- Proposed change: Retain the existing capabilities list, but add a qualification that current real-world precursors remain task-specific and development-stage: first-in-human work is intraoperative feasibility testing; noninvasive control results are small-sample demonstrations; neural-dust work is non-functional and preclinical; and home-use systems remain conference-stage research. State that chronic safety, signal stability, decoder generalization, regulatory approval, privacy, and postmarket surveillance remain unresolved before treating these capabilities as routine deployment evidence.
- Implementation steps:
  1. Insert a subsection immediately after the existing Function content, using the nearest available anchor heading “Function,” titled for example “### Development Constraints.”
  2. Distinguish established in-world canon capabilities from the audited real-world evidence rather than replacing the existing post-singularity premise.
  3. Cross-reference [Trust Fabrics](./trust-fabrics.md) for neural-data provenance, consent, and audit requirements, and [Privacy Drift](./privacy-drift.md) for access boundaries and derived neural information.
  4. Review terminology against the existing claims “direct nervous system communication,” “shared realities,” and “emotional regulation systems” so the added qualification does not imply that current evidence validates those post-singularity capabilities.
  5. After this file is reviewed, check any timeline placement for Neural Link Age references before adding a real-world milestone to canon chronology; no timeline edit is warranted from these sources alone.
- Dependencies or conflicts:
  - The Summary currently states that neural links are safe and enable identity, memory, sensory, and emotional-state shifts; the proposed qualification must not silently convert those fictional capabilities into present-day technical claims.
  - S8 is contextual review evidence dated June 24, 2026, outside the July 22–29 priority window, and should be labeled as supporting context rather than a window development.
  - S5 concerns non-functional rat motes and must not be described as demonstrated recording, stimulation, decoding, wireless power, telemetry, or human deployment.
  - S6 and S7 document conference programming and research direction, not clinical availability or validated home-use implantation.
  - S9 and S10 establish regulatory friction and classification requirements, not approval failure or a specific adverse event.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **supports**
- Assumptions: `PS-NEURO-002`
- Sources: `S3`, `S4`, `S8`, `S12`, `S13`
- Why this location: The evidence strengthens the governance premise by identifying concrete rights, consent, ownership, misuse, and operational-data gaps for implantable BCIs. It also limits the technological premise: mouse stimulation and focused-ultrasound programs remain preclinical, pilot, or translational and do not establish reliable human control of mood, reward, dependency, or immersive experience.
- Proposed change: Add a paragraph to the philosophical tensions discussion separating present neural-data governance from speculative affective engineering. Specify that raw recordings, decoded inferences, decoder parameters, closed-loop signals, timing metadata, secondary uses, ownership, and monetization require explicit consent and control, while reliable human mood or reward manipulation remains unestablished. Reframe the social danger of bliss as a future extrapolation grounded in current governance gaps, not as a capability already demonstrated by contemporary neuromodulation.
- Implementation steps:
  1. Append the new paragraph at the end of the existing “Philosophical Tensions” section, preserving the existing questions about effort, pain, and social cohesion.
  2. Use the terms “decoded inferences,” “decoder parameters,” and “closed-loop control signals” consistently with S4 and distinguish them from the file’s fictional “Memory Threads” and “Emotional Integrity Contracts.”
  3. Cross-reference [Neural Links](../worldbible/technologies/neural-links.md) for interface capabilities and [Trust Fabrics](../worldbible/technologies/trust-fabrics.md) for accountability and audit mechanisms.
  4. Keep the existing cultural split between permanent exits, periodic bliss, and refusal, but mark its underlying reliable human mental-state control as a post-singularity premise rather than evidence-supported present-day deployment.
  5. Review the revised passage against S3, S12, and S13 to ensure animal motor effects and pilot human studies are not represented as affective or immersive-state control.
- Dependencies or conflicts:
  - The file currently describes bliss exits as safe, regulated, and reviewable through Emotional Integrity Contracts; adding present-day governance gaps may create tension unless the contracts are explicitly treated as post-singularity safeguards.
  - S3 demonstrates stimulation delivery and motor behavior in mice, not mood control, dependency control, or human use.
  - S12 and S13 list translational, pilot, and preclinical focused-ultrasound work and do not establish reproducible human affective-state control.
  - S8 supports caution about closed-loop reliability and safety but concerns stroke rehabilitation and heterogeneous cited evidence rather than a new failed replication.
  - The proposed change should not imply that S4 documents an actual breach, coercive deployment, enacted neuro-rights law, or binding regulatory standard.

### `worldbible/technologies/trust-fabrics.md` -> Summary

- Priority: **watch**
- Recommendation: **monitor**
- Evidence relationship: **qualifies**
- Assumptions: `PS-AI-003`
- Sources: `S4`
- Why this location: S4 provides evidence for a narrower need for provenance, consent, ownership, and auditability in operational neural-interface ecosystems, but it does not establish broad societal adoption of AI transparency standards, model-audit mandates, or graduated oversight. The broader assumption therefore remains insufficiently evidenced.
- Proposed change: Leave the broad Summary claims unchanged rather than asserting that the audited evidence proves societal provenance or audit-system adoption. Add, only if maintainers want a narrowly scoped clarification, a sentence stating that emerging implantable neural-data systems expose unresolved requirements for decoder provenance, closed-loop signal logging, consent, ownership, and secondary-use controls; do not present these requirements as adopted or enforceable Trust Fabric practice.
- Implementation steps:
  1. Prefer no content edit unless the repository intends Trust Fabrics to cover neural-interface governance explicitly; record S4 as a monitored extension of the existing Summary.
  2. If the clarification is approved, place it at the end of “Summary” and label the requirements as emerging or unresolved rather than established canon institutions.
  3. Cross-reference [Neural Links](./neural-links.md) and [AI Trust](../../philosophy/ai-trust.md) only after confirming that the relative links match repository conventions.
  4. Do not add a new timeline event, technology-index entry, or claim of regulatory adoption from this review.
  5. Reassess after evidence appears showing enacted standards, enforcement, or broad operational adoption of AI provenance and model-audit systems.
- Dependencies or conflicts:
  - The existing Trust Fabrics file already presents Transparency Protocols, Provenance Trails, Emotive Integrity Tags, Third-Mind Panels, and Resonance Drift Alerts as established in-world systems; S4 does not validate those fictional institutions in present-day practice.
  - Adding neural-data requirements could overlap with Privacy Drift’s Gradient Privacy Fields and contextual consent claims; terminology and ownership boundaries should be reconciled before editing.
  - S4 is a review and policy analysis, not evidence of a breach, enacted law, binding standard, enforcement action, or consensus among regulators and developers.

### Nearby Canon Used for Context

- [`worldbible/technologies/neural-links.md`](../../worldbible/technologies/neural-links.md) — declared canon source for PS-NEURO-001
- [`philosophy/bliss-divergence.md`](../../philosophy/bliss-divergence.md) — declared canon source for PS-NEURO-002
- [`worldbible/technologies/trust-fabrics.md`](../../worldbible/technologies/trust-fabrics.md) — declared canon source for PS-AI-003
- [`philosophy/ai-trust.md`](../../philosophy/ai-trust.md) — declared canon source for PS-AI-003
- [`worldbible/technologies/aerospace-systems.md`](../../worldbible/technologies/aerospace-systems.md) — declared canon source for PS-SPACE-001
- [`worldbible/timeline.md`](../../worldbible/timeline.md) — declared canon source for PS-SOCIAL-002
- [`worldbible/technologies/ai-agents.md`](../../worldbible/technologies/ai-agents.md) — content: and, interfaces, neural; neurotechnology directory preference
- [`worldbible/technologies/communication-channels.md`](../../worldbible/technologies/communication-channels.md) — content: and, neural, sensory; neurotechnology directory preference
- [`worldbible/technologies/index.md`](../../worldbible/technologies/index.md) — content: and, emotion, neural; neurotechnology directory preference
- [`philosophy/index.md`](../../philosophy/index.md) — content: and, neural; neurotechnology directory preference
- [`worldbible/technologies/privacy-drift.md`](../../worldbible/technologies/privacy-drift.md) — content: and, neural; neurotechnology directory preference
- [`worldbible/technologies/robotics.md`](../../worldbible/technologies/robotics.md) — content: and, interfaces; neurotechnology directory preference

## Uncertainties

- The Ability Neurotech evidence is a company announcement reported by specialist news and provides no peer-reviewed decoding results, chronic outcomes, adverse-event data, or regulatory authorization details.
- The UAV result is an eight-participant, noninvasive, task-specific demonstration; its approximately 88.9% accuracy does not establish naturalistic high-bandwidth communication or cross-user generalization.
- The neural-dust study used non-functional motes in rats and did not demonstrate recording, stimulation, decoding, wireless power, telemetry, chronic stability, or human operation.
- Conference programs document research direction and presentations, not complete datasets, independent validation, safety outcomes, or clinical availability.
- The neuro-rights evidence is anticipatory policy analysis and does not document a breach, coercive deployment, enacted law, binding standard, enforcement action, or court ruling.
- The focused-ultrasound and wireless-neuromodulation evidence does not establish reliable, reproducible, consent-preserving control of human mood, reward, dependency, or immersive subjective experience.
- The FDA sources describe regulatory requirements and classifications but do not establish approval, rejection, suspension, or failure of a specific implantable BCI.
- The Frontiers in Neurology review is contextual evidence from June 2026 and summarizes heterogeneous prior safety and efficacy studies rather than reporting a new randomized trial.
- No supplied evidence addresses off-world settlement or the persistence of analog social practices.
- The Ability Neurotech finding reports first-in-human testing, but the evidence is a company announcement reported by specialist news rather than a peer-reviewed clinical outcome or regulatory record; no contradiction exists between the procedure occurring and the absence of demonstrated chronic deployment.
- The hybrid EEG/EMG UAV study reports approximately 88.9% task-specific accuracy, while the counterevidence shows that such benchmark performance does not establish generalization, long-duration operation, clinical utility, or naturalistic high-bandwidth communication.
- The Communications Medicine review is used in both packets for privacy and governance gaps; the findings are substantively consistent, with one packet emphasizing five protection gaps and the other adding decoder, closed-loop, timing, and synchronization metadata deficiencies.
- The neural-dust finding is presented as a hardware-pathway signal in one packet and as counterevidence to scalable distributed interfaces in the other. These are complementary interpretations: the study demonstrates an implantation method for non-functional rat motes, not a functional chronic neural-interface system.
- The IEEE EMBC program is characterized as a field signal toward home-use and clinically oriented systems, while the counterevidence characterizes home-use implantation as a conference-stage objective. These claims are compatible because the program documents research direction rather than routine clinical deployment.
- The FDA material identifies regulatory requirements and risks but does not document a new rejection, suspension, approval, or adverse incident during the window; it therefore constrains deployment claims without independently proving device failure.
- The stroke-rehabilitation review is dated 2026-06-24, outside the stated 2026-07-22 through 2026-07-29 focus window. It is retained as contextual counterevidence, not as a development occurring during the priority window.
- PS-SPACE-001 is insufficiently evidenced and has no supplied source IDs addressing launch cost, orbital duration, life support, in-space manufacturing, propulsion, autonomous operations, or sustained settlement. No repository edit is warranted in worldbible/technologies/aerospace-systems.md or worldbible/timeline.md.
- PS-SOCIAL-002 is insufficiently evidenced and has no supplied source IDs addressing analog practices, device-free spaces, right-to-disconnect policies, low-technology communities, or resistance to neural integration. No edit is warranted in worldbible/timeline.md or any supplied social or technology file.
- PS-AI-003 remains insufficiently evidenced at the broad societal level. The Trust Fabrics item records a watch-only, no-acceptance option for the narrower neural-data governance implication; no claim of broad provenance-system adoption should be added.
- No source supports editing philosophy/index.md or worldbible/technologies/index.md: the audited material does not establish a new stable canon concept, chronology entry, or repository-wide category requiring index changes.
- No source supports adding a new dated event to worldbible/timeline.md. The audited developments are real-world research and policy signals, not established post-singularity chronology.
- The supplied quality notes state that sources were deduplicated by URL and substantive identity. The Communications Medicine review is represented once as S4, the rat-cortex mote study once as S5, and each IEEE EMBC program page once as S6 and S7.
- Primary research was preferred where available. Company-only information about Ability Neurotech remains identified as company-announcement evidence through the reputable-secondary source S1.
- The Ability Neurotech result is first-in-human intraoperative feasibility evidence, not chronic implantation, long-term safety, quantitative decoding, independent everyday use, or regulatory authorization.
- The UAV result is an eight-participant, noninvasive, multimodal, task-specific demonstration. Its offline and online accuracy values should not be treated as general-purpose neural decoding or deployment evidence.
- The mouse neuromodulation result demonstrates wireless infrared-controlled stimulation delivery and behavior-linked motor effects in freely moving mice, not human therapeutic use, autonomous closed-loop operation, mood control, or bidirectional communication.
- The rat neural-dust work used non-functional motes and therefore does not establish recording, stimulation, decoding, wireless power, telemetry, chronic stability, or human operation.
- Conference programs S6, S7, S12, and S13 document presentations and research direction, not complete datasets, peer-reviewed outcomes, safety results, independent validation, or clinical availability.
- The Frontiers in Neurology review is a review rather than a new randomized trial or failed replication, and its summarized safety evidence combines heterogeneous cited studies.
- The FDA sources are regulatory and classification materials. Regulatory requirements and device classifications should not be interpreted as evidence that a named BCI device has failed or succeeded in approval.
- The EEG speech-decoding source documents dataset construction and model-development methods but does not establish unrestricted, real-time, cross-user speech decoding in natural environments.
- The neuro-rights evidence is anticipatory review and policy analysis. It identifies governance gaps but does not document a specific breach, misuse event, enacted statute, binding standard, enforcement action, or court ruling during the window.
- No authoritative regulatory record was found during the window showing a new FDA, EU, or other national approval for an implantable BCI, chronic neural decoder, or closed-loop neurostimulation therapy.
- No primary clinical-trial results were found during the window demonstrating long-term human bidirectional BCI operation, sensory restoration at scale, decoded affect, or reliable AI-mediated mood or reward control.
- No independently verified failed replication specific to a named 2026 BCI or neurostimulation result was located during the July 22–29 priority window.
- No source established safe, reproducible, AI-mediated control of mood, reward, dependency, or immersive subjective experience in humans.
- No public cost-of-goods, implantation-cost, explantation-cost, maintenance-cost, or reimbursement analysis was found for next-generation high-channel-count implantable BCIs.
- No source demonstrated chronic operation of a large distributed neural-dust or mote network with validated wireless power, telemetry, synchronization, and tissue-response data.
- Evidence for analog practices, device-free spaces, or right-to-disconnect responses specific to neurotechnology users was not located in the priority window, so PS-SOCIAL-002 remains unassessed.
- Claims that Ability Neurotech’s first-in-human procedure demonstrated chronic implantation, long-term safety, useful bandwidth, quantitative speech or motor decoding, participant outcomes, or independent everyday use are excluded.
- Claims that the hybrid EEG/EMG UAV-swarm study demonstrates robust control of complex UAV missions, safety in uncontrolled environments, cross-user generalization, natural speech bandwidth, continuous motor control, rich two-way communication, or sensory/emotional exchange are excluded.
- Claims that the wireless mouse tDCS and DBS devices demonstrated human use, reliable therapeutic mood control, cognitive or affective control, autonomous closed-loop stimulation, long-term tissue safety, or bidirectional human communication are excluded.
- Claims that the rat neural-dust mote study demonstrated functional neural recording, stimulation, decoding, wireless power, telemetry, chronic stability, scalable high-channel-count operation, or human clinical deployment are excluded.
- Claims that IEEE EMBC conference listings demonstrate clinically available home-use implantable BCIs, broad clinical validation, routine care, safety, performance, or independent validation are excluded.
- Claims that focused-ultrasound conference programs demonstrate reliable human control of mood, reward, dependency, or immersive affective states are excluded.
- Claims that the Communications Medicine review documents an actual neural-data breach, coercive deployment, court decision, enacted neuro-rights law, binding standard, regulatory adoption, or enforcement action are excluded.
- Claims that the FDA regulatory overview or sub-scalp implanted EEG classification establishes a new approval, rejection, suspension, adverse incident, or outcome for a specific implantable BCI are excluded.
- Claims that the Frontiers in Neurology review constitutes a new failed replication or proves that every BCI application has the summarized safety profile are excluded.
- Claims that the Chinese-speech EEG paper demonstrates unrestricted, real-time, cross-user speech decoding, generalized mind reading, or affective access in natural environments are excluded.
- Claims of durable high channel count, chronic wireless operation, acceptable long-term tissue response, general-purpose linguistic or emotional decoding, safe AI-mediated mood or reward control, or broad routine deployment are excluded because no source in the supplied packets established them.
- Claims concerning analog practices, device-free spaces, or right-to-disconnect responses specific to neurotechnology users are excluded because evidence for these claims was not located in the priority window.

## Watchlist

- Chronic human BCI studies reporting retention, adverse events, explantation rates, signal degradation, and usable channel bandwidth.
- Independent quantitative results from the Ability Neurotech first-in-human study, including conscious speech or motor decoding and participant outcomes.
- Functional demonstrations of distributed neural motes with wireless power, telemetry, synchronization, chronic tissue-response measurements, and human deployment.
- Regulatory clearances or approvals for implantable BCIs intended for home use, general communication, sensory exchange, or closed-loop neuromodulation.
- Evidence of generalized, real-time, cross-user speech, affect, or sensory decoding outside tightly controlled task-specific datasets.
- Adoption and enforcement of neural-data rights covering raw recordings, decoded inferences, decoder parameters, secondary uses, ownership, and monetization.
- Independent evidence of reliable human mood, reward, dependency, or immersive-state modulation with explicit consent and long-term safety data.
- Concrete AI provenance, model-audit, disclosure, and verification mandates, together with evidence of adoption and enforcement.
- Launch-cost trends, closed-loop life-support demonstrations, in-space manufacturing, autonomous mission operations, and long-duration human habitation results.
- Measures of device-free spaces, right-to-disconnect policy, analog-media use, low-technology communities, and intergenerational cultural resistance to integration.

## Sources

- `S1` [Ability Neurotech announces first-in-human testing of novel BCI technology](https://neuronewsinternational.com/ability-neurotech-announces-first-in-human-testing-of-novel-bci-technology/) — NeuroNews International; 2026-07-22; reputable-secondary; URL supplied in structured research output. Reports the first-in-human procedure, planned sample size, intraoperative recording duration, study site, and intended next-stage decoding tasks.
- `S2` [A Group Brain-Controlled Method for UAVs Using a Hybrid Paradigm of Hand movement and Visual Evoked](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2026.1858496/abstract) — Frontiers in Neurorobotics; 2026-07-22; primary-research; URL supplied in structured research output. Provides the study design, multimodal neural-decoding method, participant count, and offline and online accuracy measurements.
- `S3` [Ultralight infrared-controlled wireless neuromodulation systems for freely behaving mice](https://www.nature.com/articles/s41378-026-01389-9) — Microsystems & Nanoengineering; 2026-07-24; primary-research; URL supplied in structured research output. Reports device mass, optical-control wavelengths, stimulation modalities, behavioral validation, and motor-circuit effects in freely moving mice.
- `S4` [Advancing data protections for implantable brain-computer interfaces](https://www.nature.com/articles/s43856-026-01797-y) — Communications Medicine; 2026-07-27; primary-research; URL supplied in structured research output. Provides the dated review, its five identified protection gaps, and proposed safeguards for clinical implantable BCI data. It also documents missing metadata and governance provisions for operational iBCI systems, including decoder parameters, closed-loop control signals, timing, consent, ownership, and misuse safeguards.
- `S5` [A method for efficient, rapid, and minimally invasive implantation of individual non-functional motes with penetrating subcellular-diameter carbon fiber electrodes into rat cortex](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1848862/full) — Frontiers in Neuroscience; 2026-07-28; primary-research; URL supplied in structured research output. Reports the implantation method, neural-dust rationale, electrode scale, animal model, and the tissue-damage problem the technique is intended to address. It provides direct evidence that the reported advance concerns implantation of non-functional rat-cortex motes rather than demonstrated chronic recording, stimulation, decoding, or human deployment.
- `S6` [IEEE EMBC 2026: Brain-Computer Interface and Brain-Machine Interface I](https://cmsworkshops.com/EMBC2026/view_session.php?SessionID=1058) — IEEE EMBC 2026 program; 2026-07-28; official-release; URL supplied in structured research output. Documents the July 28 BCI/BMI session and its specific presentation on a lightweight portable WIMAGINE system for home use. The presentation is explicitly framed as development toward an implantable BCI for home use.
- `S7` [EEG-Based Brain–Computer Interfaces: IEEE EMBC 2026 Mini Symposium](https://www.gtec.at/event/embc-2026-mini-symposium-eeg-based-bci-for-cognitive-assessment-and-neurorehab/) — g.tec medical engineering / IEEE EMBC 2026; 2026-07-28; official-release; URL supplied in structured research output. Documents the clinically oriented EEG-BCI mini-symposium covering cognitive assessment, neurorehabilitation, cortical excitability, and BCI-TMS integration. It shows that clinical EEG-BCI work remains organized around assessment, rehabilitation, monitoring, and personalized care rather than broad consumer or general-purpose deployment.
- `S8` [Advancing stroke rehabilitation: the potential and challenges of closed-loop brain-computer interface technology](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2026.1861673/full) — Frontiers in Neurology; 2026-06-24; primary-research; URL supplied in structured research output. Identifies small samples, placebo concerns, individual-model generalization problems, system-stability limitations, and summarized safety evidence for closed-loop BCI rehabilitation.
- `S9` [Regulatory Overview for Neurological Devices](https://www.fda.gov/medical-devices/neurological-devices/regulatory-overview-neurological-devices) — U.S. Food and Drug Administration; unknown; regulatory; URL supplied in structured research output. States the FDA’s implanted-BCI guidance framework and identifies implantation, stimulation, interference, usability, and postmarket-surveillance requirements relevant to deployment.
- `S10` [Product Classification: Sub-scalp implanted EEG system for remote patient monitoring](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/classification.cfm?id=4173) — U.S. Food and Drug Administration; 2026-06-22; regulatory; URL supplied in structured research output. Illustrates that even a sub-scalp implanted EEG monitoring system is treated as a prescription neurological device requiring formal regulatory classification.
- `S11` [Decoding Chinese speech across multiple neural conditions via EEG: dataset construction and interpretability driven spatial optimization](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1833448/full) — Frontiers in Psychology; 2026-07-27; primary-research; URL supplied in structured research output. Documents a condition-specific EEG speech-decoding dataset and optimization approach, while leaving open the generalization and deployment gap between benchmark decoding and unrestricted real-time communication.
- `S12` [FUN 2026 - Focused Ultrasound Neuromodulation Conference 2026](https://www.ibmt.fraunhofer.de/en/ibmt-events-fairs/fun-2026.html) — Fraunhofer Institute for Biomedical Engineering; unknown; official-release; URL supplied in structured research output. Documents the July 22–24 conference and explicitly frames focused-ultrasound neuromodulation around translation from bench to clinic.
- `S13` [Program - FUN26 - Focused Ultrasound Neuromodulation Conference Paris 2026](https://www.itrusst.com/fun26-program) — ITRUSST; unknown; official-release; URL supplied in structured research output. Lists pilot human, mouse, guinea-pig, and cellular or molecular neuromodulation studies, illustrating the preclinical and early-translational status of the field.

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
  "id": "research_2026-07-29_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology Evidence Review: Incremental Progress, Persistent Deployment Constraints, and Emerging Neuro-Rights Risks",
  "tags": [
    "research",
    "pending-review",
    "neurotechnology"
  ],
  "introduced_in_cycle": 0,
  "related_characters": [],
  "impact": [
    "assumption tracking",
    "canon review"
  ],
  "tracked_assumptions": [
    "PS-NEURO-001",
    "PS-NEURO-002",
    "PS-AI-003",
    "PS-SPACE-001",
    "PS-SOCIAL-002"
  ],
  "generated_by": "postsingularity-research",
  "mock": false
}
```
