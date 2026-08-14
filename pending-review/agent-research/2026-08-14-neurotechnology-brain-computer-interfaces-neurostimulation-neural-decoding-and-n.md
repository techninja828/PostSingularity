# Neurotechnology Evidence Review: Bidirectional Interfaces, Neural Decoding, Neurostimulation, and Neuro-Rights
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-08-14
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The audited evidence supports a mixed, conservative conclusion for 2026-08-07 through 2026-08-14. Portable closed-loop EEG–stimulation hardware, improved constrained brain-to-audio reconstruction, and a planned recording-and-stimulation implant trial show concrete technical and translational progress. However, speech-imagery replication failures, decoder robustness limits, declining long-term electrode performance, adverse-event history, narrow clinical cohorts, and unresolved privacy, security, liability, and regulatory gaps substantially constrain claims of rich, durable, general-purpose neural communication. The evidence strengthens the case for early assistive and controlled-feedback applications and for governance debate, but does not demonstrate reliable naturalistic decoding or control of affect, reward, mood, immersive experience, or subjective sensory content. Recommended canon treatment is to qualify Neural Links and add constrained safety and maintenance functions, debate governance tensions in The Bliss Divergence, and leave AI Trust, off-world settlement, and analog-social assumptions unchanged pending direct evidence.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-08-07 through 2026-08-14
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### Portable EEG–tES hardware demonstrates compact closed-loop neuromodulation

- Event date: 2026-08-07
- Sources: `S1`
- Observed fact: A preprint posted on August 7, 2026 describes a wearable platform combining 8-channel EEG acquisition with 2-channel transcranial electrical stimulation in a single microcontroller-based system. The platform supports sampling up to 8 kHz per EEG channel, programmable tDCS, tACS, and temporal-interference stimulation waveforms, EEG correlation of up to 99% under controlled conditions and 93.5% on a gelatin head phantom, and stimulation-current errors below 1%.
- Significance: This is a concrete engineering step toward portable, adaptive, closed-loop neurostimulation rather than a purely laboratory-bound system. It is relevant to the prediction that AI-mediated mental-state or therapeutic control could become more practical, while the measured results primarily establish signal and stimulation fidelity—not clinical efficacy or reliable control of mood, reward, or immersive experience.

### Retrieval-guided generation improves the faithfulness of brain-to-audio reconstruction

- Event date: 2026-08-10
- Sources: `S2`
- Observed fact: A preprint posted on August 10, 2026 introduces RAG-Audio, which decodes fMRI into a semantic audio embedding, retrieves a matching real-audio exemplar, and uses that exemplar to initialize a frozen generative audio model. On the Brain2Music dataset, the method improved ten-way stimulus identification from 0.14–0.18 for direct generation to 0.40–0.43, compared with a 0.10 chance level, and reduced Fréchet Audio Distance from 13.49 to 1.25 for AudioLDM.
- Significance: The result is a measurable improvement in neural decoding fidelity for reconstructed auditory content. It supports the narrower claim that AI can make decoded neural representations more usable and less dominated by generative-model priors, but it remains far from rich, private, two-way communication of thoughts, emotions, or sensory experience.

### A proposed safety mechanism addresses single-fault risks in implantable neural recording electronics

- Event date: 2026-08-11
- Sources: `S3`
- Observed fact: A preprint posted on August 11, 2026 identifies a safety hazard in DC-coupled neural-recording front ends: failure of an input transistor could create a direct DC path from the power supply into cortical tissue. The proposed detector monitors DC imbalance and disables the amplifier. In a 65-nanometer design, it detects a worst-case 6.4-nA fault across process and operating corners within 0.81 milliseconds, with the authors comparing the result to an ISO 14708-3 electrode-current limit.
- Significance: This is a material counter-signal to narratives focused only on bandwidth and capability. Safe long-term neural interfaces require fault detection, tissue-protection mechanisms, and standards-compatible engineering. The work directly bears on the safety tradeoff in high-bandwidth implants and on whether bidirectional neural systems can scale beyond tightly controlled clinical research.

### The 2026 NIH BRAIN Initiative Conference foregrounds tools, human neuroscience, precision therapies, and NeuroAI

- Event date: 2026-08-11 through 2026-08-13
- Sources: `S4`
- Observed fact: The NIH BRAIN Initiative Conference took place in Rockville, Maryland, from August 11 through August 13, 2026. The official program description lists sessions on brain tools and technologies, connectivity across scales, precision molecular circuit therapies, accelerating human neuroscience, and BRAIN NeuroAI, alongside poster sessions and scholar spotlights.
- Significance: The event is an authoritative signal of research priorities: neural recording and modulation, computational neuroscience, human translation, and NeuroAI are being treated as connected parts of the same technology agenda. It indicates institutional momentum, but the event itself is not evidence that any specific capability has reached clinical deployment or broad social adoption.

### A five-participant implantable recording-and-stimulation trial begins its planned August 2026 start

- Event date: August 2026; the registry specifies the month but not an exact day
- Sources: `S5`
- Observed fact: ClinicalTrials.gov record NCT07521930, titled Interfacing With NeuroTechnology to Expand Neural Throughput, lists a recruiting Johns Hopkins University study with an August 2026 start date. The trial plans to enroll five participants and evaluates an implantable device that records and stimulates different brain areas so adults with disabling paralysis can control and receive feedback from assistive devices. Collaborators include Blackrock Neurotech, the Johns Hopkins Applied Physics Laboratory, and Kennedy Krieger Institute.
- Significance: This is a concrete translational signal for bidirectional implanted interfaces: the protocol explicitly combines neural recording, stimulation, assistive-device control, and feedback. It is more relevant to the high-bandwidth-interface prediction than a marketing announcement, but it remains an early-stage safety and preliminary-efficacy study rather than evidence of durable, general-purpose neural communication.

### Speech-imagery BCI results did not reproduce reliably across datasets and pipelines

- Event date: 2026-05-06 deposit date; study reported as 2026 and in press during the priority window
- Sources: `S6`
- Observed fact: A 2026 study attempting to reproduce published speech-imagery decoding pipelines found that all evaluated studies contained missing methodological details, some lacked cross-validation procedures, and reproduced accuracies were consistently lower than originally reported, with discrepancies ranging from 2% to 39%. Across three public speech-imagery datasets and a newly collected dataset, only 36% of participants exceeded statistical-significance thresholds, compared with 91% in motor-imagery datasets. The authors concluded that the feasibility of speech imagery as a practical BCI paradigm may have been overestimated.
- Significance: This is direct counterevidence against assuming that neural decoding advances transfer cleanly from controlled demonstrations to dependable communication. It particularly weakens optimistic claims about decoding private speech, imagined language, affect, or other internal content, because the underlying signal patterns and evaluation procedures were not stable enough to reproduce across datasets.

### Neural-decoder leaderboards can conceal robustness, efficiency, and cross-recording failures

- Event date: 2026-07-21; assessed during August 7–14, 2026
- Sources: `S7`
- Observed fact: The BEND-BCI benchmark evaluated 23 neural-decoding methods across motor, visual, speech, and spatial tasks using 16 real or synthetic neural recordings. It found that adding held-out accuracy alone did not reliably identify the most robust, computationally efficient, or cross-recording-consistent models. Decoder rankings changed when robustness to input perturbations, computational cost, and latent consistency were included, and simpler baselines were competitive with or outperformed more heavily parameterized deep-learning models.
- Significance: This narrows claims that higher benchmark accuracy automatically represents durable neural-interface progress. Real deployment requires performance under noise, distribution shift, limited hardware, and repeated use. The benchmark suggests that models selected by accuracy leaderboards may be poorly suited to safety-critical, low-power, or long-term BCI operation.

### Cognitive-state decoding faces harder problems than motor and language control

- Event date: 2026-07-17; assessed during August 7–14, 2026
- Sources: `S8`
- Observed fact: A review published in Trends in Cognitive Sciences states that BCIs have achieved important results in restoring movement and communication, but decoding or restoring cognitive functions such as attention and memory poses fundamentally new challenges. Cognitive processes are described as distributed and dynamic rather than relying on the more localized and stable representations used in motor and language control.
- Significance: This is expert evidence against extrapolating from successful motor or speech prostheses to reliable control of mood, reward, memory, attention, emotion, or immersive experience. It implies that the neural representations relevant to the governance prediction may be less stable, less localized, and more context-dependent than optimistic narratives assume.

### Long-term intracortical stimulation showed gradual loss of functional electrodes despite favorable safety results

- Event date: 2026-07-15; assessed during August 7–14, 2026
- Sources: `S9`
- Observed fact: A 2026 early-feasibility clinical trial followed five participants receiving intracortical microstimulation over implant durations of two to ten years. Across 27 combined implant-years, the study reported more than 168 million stimulation pulses without serious adverse events or direct negative effects on electrode health. However, stimulation detection thresholds increased by approximately 3.5 microamperes per year, and only 64% ± 13% of electrodes remained reliably capable of evoking tactile sensations, representing an approximately 21% decrease in functional electrodes; one participant retained 60% after ten years.
- Significance: The findings provide unusually long-duration human evidence that stimulation can remain useful, but they also show gradual performance degradation and a limited evidence base. This weakens claims that implantable bidirectional interfaces will simply scale in channel count and remain stable indefinitely. Long-term function may depend on accepting declining electrode yield, recalibration, or eventual revision and replacement.

### Implantable BCI clinical evidence remains small, selective, investigational, and operationally demanding

- Event date: 2026-04 through 2029 projected trial timeline; registry status assessed during August 7–14, 2026
- Sources: `S10`, `S11`
- Observed fact: The ClinicalTrials.gov record for Synchron’s INTENT endovascular BCI describes a recruiting early-feasibility study for people with bilateral upper-limb motor impairment, with an estimated enrollment of 10 participants, an estimated study start in April 2026, primary completion in June 2027, and study completion in December 2029. Other implantable BCI studies similarly impose narrow eligibility requirements, including stable paralysis, sufficient cortical motor structures, the ability to participate in long-term training, proximity to the clinical site, and exclusion of other implanted stimulators or serious conditions.
- Significance: The deployment evidence remains centered on small, carefully selected clinical cohorts rather than broad use. Long follow-up timelines, surgical eligibility constraints, training demands, and dependence on specialized centers make it premature to treat current implant demonstrations as scalable consumer or general-purpose neural interfaces.

### U.S. oversight analysis identifies unresolved privacy, security, safety, and legal gaps for neural implants

- Event date: 2026-04-02; policy implications remained relevant during August 7–14, 2026
- Sources: `S12`
- Observed fact: The U.S. Government Accountability Office reported that neural implants are currently available only to people with certain medical needs, while future augmentation uses could include brain-to-brain communication, hands-free computer control, and accelerated learning. GAO identified device safety, malfunctions, data privacy, device security, radio interference, evaluation of capability claims, and insufficient oversight tools as implications requiring policy attention. It also reported that existing privacy law may not protect neural-implant data collected outside clinical contexts, that HIPAA does not cover all nonclinical data, and that comprehensive federal privacy legislation was absent as of the report’s analysis.
- Significance: This directly supports the neuro-rights concern while also challenging the assumption that technical capability will automatically translate into safe or legitimate deployment. The governance problem is not only future misuse of decoded mental states; it includes present uncertainty over who controls neural data, how claims are evaluated, how malfunction liability is assigned, and which regulator has authority over augmentative systems.

### Current BCI safety evidence does not eliminate adverse-event and fault-management concerns

- Event date: Safety data through 2021; FDA guidance issued 2021; assessed during August 7–14, 2026
- Sources: `S13`, `S14`
- Observed fact: A BrainGate feasibility-study safety report covering clinical trials through December 31, 2021 documented 68 device-related adverse events, including six serious adverse events. The most notable safety events included postoperative seizures in two participants. Separately, FDA guidance for neurological devices emphasizes premarket testing, clinical considerations, and postmarket safety monitoring for implanted BCI and neurostimulation systems.
- Significance: Even relatively encouraging implant safety records include nontrivial adverse events and require formal investigational-device oversight. This weighs against treating a successful demonstration or a favorable small cohort as proof of safe long-term deployment. It also reinforces that electrical-fault detection is only one layer of a broader safety case involving surgery, seizures, infection, device failure, and postmarket monitoring.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S5`, `S6`, `S7`, `S9`, `S10`, `S11`, `S12`, `S13`, `S14`
- Evidence: Evidence shows concrete progress toward bidirectional neural interfaces: an implantable recording-and-stimulation trial is planned, portable closed-loop EEG–stimulation hardware has demonstrated controlled signal and stimulation fidelity, and neural decoding quality has improved for constrained auditory reconstruction. Counterevidence remains substantial: speech-imagery results reproduced poorly, decoder robustness does not track headline accuracy, long-term stimulation shows declining functional-electrode yield, and current implant studies remain small, selective, investigational, and operationally demanding. No evidence demonstrates safe, rich, durable two-way communication of sensory or emotional information between people and AI.
- Real-world implication: Bidirectional clinical neurotechnology is advancing, but current evidence supports narrow assistive and experimental applications rather than general-purpose high-bandwidth communication. Safety engineering, long-term degradation, privacy, surgical risk, and reproducibility remain major barriers to broader deployment.
- PostSingularity implication: A storyworld can plausibly include early bidirectional neural links, especially for assistive devices and controlled feedback, but treating rich emotional or sensory exchange as routine would require additional advances in decoding stability, implant longevity, safety, and governance.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S1`, `S3`, `S8`, `S9`, `S12`, `S13`, `S14`
- Evidence: The evidence strengthens the governance premise even though reliable control of mood, reward, or immersive experience has not been demonstrated. A portable closed-loop EEG–stimulation platform shows engineering progress toward adaptive neuromodulation, while the GAO identifies unresolved neural-data privacy, security, safety, capability-evaluation, liability, and oversight gaps. Expert review also indicates that cognitive and affective processes are more distributed and dynamic than relatively mature motor or communication targets. No direct evidence shows broad clinical or commercial mental-state control.
- Real-world implication: Governance concerns are already warranted at the level of neural data, stimulation safety, consent, and claims about capability, but the strongest claims about dependency or meaning remain prospective. Policy development is likely to precede reliable consumer-scale mood or experience control.
- PostSingularity implication: The assumption supports treating engineered mental states as a central institutional and ethical fault line in the storyworld. However, reliable affective control should be portrayed as an emerging or constrained capability unless later evidence establishes durable naturalistic control.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: `S12`, `S14`
- Evidence: The supplied evidence supports stronger oversight in general: the GAO identifies gaps in evaluating neural-device capability claims, privacy, security, and regulation, and FDA materials describe formal testing and monitoring requirements. However, the packet contains no direct evidence of AI transparency standards, content-provenance adoption, model-audit uptake, verification rituals, or graduated disclosure rules specifically increasing in response to AI influence.
- Real-world implication: There is evidence for unresolved oversight needs, but not enough to conclude that societies are responding through the specific provenance and audit systems described by the assumption. Adoption, enforcement, and public legitimacy remain unmeasured here.
- PostSingularity implication: A provenance-centered trust infrastructure remains a plausible storyworld development, but it should not be treated as empirically established by this evidence. The ledger should await direct regulatory, institutional, or deployment signals.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: None of the supplied developments directly addresses launch cost, propulsion, orbital settlement, closed-loop life support, in-space manufacturing, human-health limits, or autonomous off-world communities. The neural-technology evidence does not provide a basis for assessing sustained off-world settlement.
- Real-world implication: The current evidence produces no directional update on whether AI and abundant energy will make durable orbital or off-world communities practical.
- PostSingularity implication: Off-world settlement remains available as a long-horizon storyworld premise, but this packet does not justify changing its forecast probability or technical assumptions.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied evidence contains no measured information about device-free spaces, right-to-disconnect policies, analog-media growth, low-technology communities, intergenerational cultural practices, or resistance to neural integration. The quality notes explicitly state that no evidence was located showing analog practices disappearing or cultural resistance being negligible.
- Real-world implication: There is no basis in this search for a directional update on the persistence or revival of analog practices. Both continued resistance and gradual displacement remain possible.
- PostSingularity implication: Analog countercultures remain a plausible storyworld response to pervasive AI and neural technology, but their prevalence, durability, and political significance should remain uncommitted until social evidence is available.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S3`, `S5`, `S6`, `S7`, `S9`, `S10`, `S11`, `S12`, `S13`, `S14`
- Why this location: The evidence supports concrete progress toward bidirectional recording and stimulation, but it does not support treating rich, durable, emotional, or sensory exchange as routine. Replication failures, robustness limits, long-term electrode degradation, surgical risks, and unresolved privacy and oversight issues materially qualify the current broad capability claims.
- Proposed change: Add a qualification to the Summary stating that neural links are grounded in established or emerging assistive and controlled-feedback applications, while high-bandwidth two-way sensory or emotional exchange remains constrained by decoding reliability, implant longevity, fault management, clinical validation, consent, and neural-data governance. Preserve the existing claims about shared realities and available functions as post-singularity canon, but distinguish routine capability from advanced or exceptional use.
- Implementation steps:
  1. Insert the qualification within the Summary after the opening description of direct nervous-system communication, before the existing capability list or immediately after it.
  2. Cross-reference Trust Fabrics and Privacy Drift for transparency, consent, access control, and neural-data governance concerns.
  3. Retain the existing emotional-regulation and user-override language, but review it against the new safety qualification so that override-by-choice does not imply absence of surgical, electrical, or long-term device risks.
  4. Review the Story Use examples after this edit to ensure malfunction, resistance, and advanced shared-reality scenes reflect constrained rather than universally reliable technology.
- Dependencies or conflicts:
  - The existing Summary calls neural links safe and deeply personalized; this must be reconciled with S3, S9, S13, and S14, which identify electrical, long-term, surgical, seizure, and monitoring risks.
  - S5 and S10 describe separate implant studies and must not be merged; NCT07521930 and NCT07543367 should remain distinct if referenced.
  - S2 concerns fMRI-based auditory reconstruction, while S6 concerns speech-imagery reproducibility; neither establishes general neural-link communication or rich thought exchange.
  - The proposed qualification may narrow the apparent universality of the existing Story Use examples without removing the post-singularity premise.

### `worldbible/technologies/neural-links.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S3`, `S5`, `S6`, `S7`, `S9`, `S10`, `S11`, `S13`, `S14`
- Why this location: The audited evidence adds implementation constraints that are absent from the current function list: closed-loop stimulation is technically plausible, but practical systems require fault detection, calibration, robustness testing, long-term maintenance, and narrowly defined clinical or assistive use cases.
- Proposed change: Add a Function subsection or bullet group describing closed-loop sensing and stimulation as an emerging technical layer, including signal-quality monitoring, stimulation-fault shutdown, recalibration as electrode performance changes, and deployment limits imposed by clinical eligibility, training, and specialized care. State that controlled auditory reconstruction and assistive feedback are narrower demonstrated targets than spontaneous thought, emotion, or immersive-experience exchange.
- Implementation steps:
  1. Place the new material at the end of the existing Function section, using Function as the insertion anchor.
  2. Describe S1’s portable EEG–tES result as controlled engineering evidence rather than clinical proof, and describe S3’s detector as one fault-management mechanism rather than a complete safety system.
  3. Add explicit operational requirements for robustness, cross-recording validation, latency, calibration, and long-term electrode monitoring based on S6, S7, and S9.
  4. Cross-reference AI Agents and Communication Channels only where their existing consent and thoughtstream concepts remain compatible with the more limited demonstrated real-world capabilities.
  5. Have a canon reviewer check whether the existing claims about identity shifts, emotional streaming, and sensory input are intended as mature Cycle 3 technology or as rare, higher-tier capabilities.
- Dependencies or conflicts:
  - The current Function section says neural links can temporarily shift identity, memory weight, or sensory input; S8 and the excluded claims caution against presenting cognitive or affective control as currently reliable in real-world use.
  - S9’s declining functional-electrode fraction introduces maintenance, recalibration, revision, or replacement consequences that may affect character continuity and access inequality.
  - S11’s eligibility and participation constraints conflict with any implication that implantable links are universally available, especially to healthy users.
  - FDA oversight and historical adverse events in S13–S14 should not be reduced to a single electronic fault detector.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **debate**
- Evidence relationship: **supports**
- Assumptions: `PS-NEURO-002`
- Sources: `S1`, `S3`, `S8`, `S9`, `S12`, `S13`, `S14`
- Why this location: The evidence strengthens the premise that engineered mental states create governance and ethical fault lines, particularly around neural-data control, stimulation safety, capability claims, consent, liability, and oversight. It does not establish reliable consumer-scale mood or immersive-experience control, so the philosophical claims should remain prospective or institutionally contested rather than presented as settled technical reality.
- Proposed change: Add a debate to Philosophical Tensions distinguishing the availability of regulated bliss states in canon from the uncertain real-world reliability and safety of the systems that produce them. The added text should identify neural-data ownership, false or inflated capability claims, consent under stimulation, fault liability, unequal access to maintenance, and the legitimacy of oversight as disputes that intensify before affective control becomes dependable.
- Implementation steps:
  1. Insert the new debate after the existing questions about effort, pain, and civilization, using Philosophical Tensions as the anchor.
  2. Connect the debate to Trust Fabrics for verification and oversight, and to Privacy Drift for exposure, consent, and control of neural data.
  3. Preserve the existing three-way social split over permanent exit, periodic bliss, and refusal; add institutional disputes over safety evidence and accountability rather than replacing that cultural division.
  4. Review whether Emotional Integrity Contracts need an explicit distinction between behavioral regulation, informed consent, and verified control of neural stimulation.
  5. Keep the language prospective or constrained where it refers to mood, reward, or immersive-experience control, because the audited evidence does not demonstrate those capabilities in naturalistic human use.
- Dependencies or conflicts:
  - The current Function section presents bliss exits as safe and regulated; S3, S9, S13, and S14 support adding safety layers without treating them as proof of risk-free operation.
  - S8 indicates that distributed and dynamic cognitive processes are harder to decode or control than motor and communication targets, which limits direct extrapolation to bliss or affective engineering.
  - S12’s governance findings are U.S.-specific and identify gaps rather than documenting enacted neuro-rights protections; the storyworld may generalize them only as inspiration, not as direct historical fact.
  - The added debate should not imply that the 2026 evidence proves the social consequences of perpetual bliss or that current trials provide direct evidence for bliss technology.

### `philosophy/ai-trust.md` -> Function

- Priority: **watch**
- Recommendation: **no-change**
- Evidence relationship: **no-material-effect**
- Assumptions: `PS-AI-003`
- Sources: `S12`, `S14`
- Why this location: The evidence confirms unresolved neural-device oversight and formal regulatory requirements, but it does not assess AI transparency standards, provenance adoption, model-audit uptake, verification rituals, or graduated disclosure. It therefore cannot justify changing the existing account of AI trust practices.
- Proposed change: Make no repository edit to AI Trust. Do not add neural-device governance evidence as proof that public AI action logs, Trust Fabric protocols, or open-thread review practices have been adopted. Reopen this file only if direct evidence of AI provenance, audit, enforcement, or institutional legitimacy becomes available.
- Implementation steps:
  1. Leave the Function section unchanged for this evidence cycle.
  2. Record S12 and S14 as watch sources for future evidence about capability evaluation, privacy, security, and regulatory oversight that could eventually affect AI trust practices.
  3. If later evidence is found, evaluate AI Trust before Trust Fabrics, then reconcile any resulting terminology or cross-reference changes in both files.
  4. Keep the current cross-reference to Trust Fabrics intact because the audited packet neither challenges nor validates that fictional governance system.
- Dependencies or conflicts:
  - S12 concerns neural-implant policy gaps rather than AI decision transparency, so importing its conclusions would overstate the evidence.
  - S14 describes FDA processes for neurological devices and does not establish a general AI-audit or provenance regime.
  - The existing Trust Fabrics claims about transparency protocols, provenance trails, and Third-Mind Panels remain declared canon but are not empirically supported by this audit.

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

- The strongest neural-interface results are largely preprints, small feasibility studies, registry entries, reviews, or controlled demonstrations rather than large, independently replicated clinical trials.
- The evidence spans different modalities and tasks—EEG, fMRI, intracortical stimulation, endovascular implants, motor control, speech imagery, and auditory reconstruction—and cannot be combined into a single general measure of neural-interface capability.
- No direct evidence establishes reliable naturalistic decoding or control of affect, reward, mood, immersive experience, or subjective sensory content.
- Long-term implant safety and performance remain uncertain because the available studies involve small cohorts, investigational systems, and incomplete evidence on infection, mechanical degradation, corrosion, wireless security, revision, and explantation.
- The GAO governance findings are U.S.-specific and identify gaps rather than documenting enacted, harmonized neuro-rights protections.
- No direct evidence was supplied for provenance adoption, AI audit systems, off-world settlement, or analog-practice trends.
- The two packets contain different INTENT registry records and should not be merged: NCT07521930 is a Johns Hopkins University study planning five participants with an August 2026 start month, whereas NCT07543367 is a Synchron early-feasibility study estimating 10 participants and an April 2026 start. The shared INTENT terminology does not establish that they are the same trial.
- The first packet reports exact-window engineering and decoding improvements, while the second packet reports adjacent-period replication, robustness, cognitive-decoding, and long-term-degradation constraints. These are not direct factual contradictions, but they conflict with any broader inference that laboratory performance establishes reliable deployment.
- The first packet characterizes the EEG–tES platform as a concrete step toward portable closed-loop neuromodulation; its own evidence is controlled testing and a gelatin head phantom, while the counterevidence packet emphasizes that deployment requires robustness, efficiency, long-term stability, and clinical validation.
- The RAG-Audio benchmark improvement and the speech-imagery reproducibility findings concern different modalities and tasks. They cannot be treated as contradictory measurements of one system or as evidence that neural decoding generally succeeds or fails.
- A claim that the portable EEG–tES platform demonstrates human safety, clinical effectiveness, reliable control of mood, reward, or immersive experience, or reliable decoding of complex mental states is excluded.
- A claim that RAG-Audio demonstrates spontaneous thought decoding, private two-way communication, or unconstrained audio generation from neural signals alone is excluded.
- A claim that the proposed fault detector constitutes regulatory approval, clinical validation, or a complete implant-safety solution is excluded.
- A claim that the NIH BRAIN Initiative Conference demonstrates clinical deployment, broad social adoption, high-bandwidth bidirectional communication, affect decoding, reliable mental-state control, or a direct neuro-rights policy outcome is excluded.
- A claim that the NCT07521930 study had definitely begun on a specific day between August 7 and August 14, 2026 is excluded; the registry specifies only an August start month.
- A claim that speech-imagery decoding is impossible is excluded. The retained evidence supports methodological and replication concerns, not impossibility.
- A claim that BEND-BCI establishes clinical failure of a particular decoder or that leaderboard accuracy is irrelevant is excluded; it establishes that accuracy alone is insufficient for deployment assessment.
- A claim that cognitive BCIs cannot eventually work is excluded; the review identifies distributed, dynamic, and context-dependent challenges rather than impossibility.
- A claim that long-term intracortical stimulation is permanently stable or risk-free, or that the five-participant study generalizes to emotional-state control, general cognition, or healthy-user augmentation is excluded.
- A claim that current implantable BCI demonstrations constitute scalable consumer or general-purpose neural interfaces is excluded.
- A claim that brain-to-brain communication, accelerated learning, emotion decoding, or other future augmentation scenarios identified by GAO are currently available is excluded.
- A claim that the GAO report documents a specific neural-data breach, implant malfunction, enacted neuro-rights law, or comprehensive legal conclusion applicable outside the United States is excluded.
- A claim that historical BrainGate safety results establish safety for all current or future implantable BCI and neurostimulation systems is excluded.
- A claim that the FDA page documents an August 2026 clearance, approval, warning, recall, or enforcement action is excluded.
- Claims that direct neuro-rights policy developments occurred during August 7–14, 2026 are excluded because no verified law, regulation, court ruling, standards publication, or government policy release dated within the window was located.
- Claims that any finding establishes rich two-way communication between nervous systems and AI or reliable naturalistic decoding or control of affect, subjective experience, reward, mood, or immersive experience are excluded.
- PS-SPACE-001 was assessed as insufficient-evidence with no directional update. None of the supplied sources addresses launch economics, propulsion, life support, in-space manufacturing, human-health limits, or autonomous off-world communities, so no edit is warranted in worldbible/technologies/aerospace-systems.md or worldbible/timeline.md.
- PS-SOCIAL-002 was assessed as insufficient-evidence with no directional update. The packet contains no measured evidence about device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, or resistance to neural integration, so no edit is warranted in worldbible/timeline.md.
- The mixed PS-NEURO-001 assessment is covered by the qualification and function plans in worldbible/technologies/neural-links.md; the plans preserve the post-singularity premise while separating narrow assistive progress from routine rich neural exchange.
- The strengthened PS-NEURO-002 assessment is covered by the debate plan in philosophy/bliss-divergence.md; the evidence supports governance tension but does not establish reliable naturalistic mood, reward, or immersive-experience control.
- PS-AI-003 remains insufficient-evidence despite relevant governance sources. The no-change/watch item records the assessment and prevents unsupported transfer of neural-device oversight findings into claims about AI provenance or audit adoption.
- The two INTENT registry records, NCT07521930 and NCT07543367, should remain separate in any future implementation. The supplied evidence does not justify adding either record to canon now.
- No source establishes rich two-way communication, reliable affect or subjective-experience decoding, permanent implant stability, broad consumer deployment, harmonized neuro-rights law, off-world settlement, or analog-practice trends; these claims should remain unedited unless later evidence directly addresses them.

## Watchlist

- Independent replication of bidirectional neural recording-and-stimulation results across larger and more diverse cohorts.
- Long-term implant outcomes, including electrode survival, recalibration burden, revision and explantation rates, infection, seizure, mechanical, and wireless-security risks.
- Demonstrations that decode or control affect, reward, mood, or immersive experience reliably in naturalistic human settings.
- Clinical-trial results from NCT07521930 and NCT07543367, while keeping the two registry records separate.
- Standardized BCI benchmarks combining accuracy with robustness, privacy leakage, latency, energy use, calibration burden, long-term degradation, and clinical benefit.
- AI provenance and audit requirements, adoption rates, enforcement actions, and evidence that these systems gain public or institutional legitimacy.
- Launch economics, closed-loop life-support performance, autonomous mission operations, and human-health outcomes for sustained off-world habitation.
- Device-free-space usage, right-to-disconnect legislation, analog-media and low-tech-community trends, and evidence of cultural resistance to neural integration.

## Sources

- `S1` [Design and Validation of a Portable EEG-tES Platform Supporting High-Rate EEG Recording and Temporal Interference Stimulation](https://arxiv.org/abs/2608.06783) — arXiv; 2026-08-07; primary-research; URL supplied in structured research output. Provides the exact hardware architecture, sampling specifications, fidelity measurements, and stimulation-error results for a portable closed-loop neuromodulation platform.
- `S2` [RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction](https://arxiv.org/abs/2608.09331) — arXiv; 2026-08-10; primary-research; URL supplied in structured research output. Reports the neural-decoding method, benchmark results, chance-level comparison, and quantitative improvement in audio reconstruction fidelity.
- `S3` [Neural implants and human safety: single-fault detection for DC-coupled recording front ends](https://arxiv.org/abs/2608.10361) — arXiv; 2026-08-11; primary-research; URL supplied in structured research output. Documents a specific implant-safety failure mode and provides quantitative detection latency, fault-current, circuit-technology, and standards-limit details.
- `S4` [2026 BRAIN Initiative Conference](https://www.nih.gov/brain/events/2026-brain-initiative-conference) — National Institutes of Health; 2026-07-30; official-release; URL supplied in structured research output. Officially documents the August 11–13 conference dates and its technology, human-neuroscience, precision-therapy, and NeuroAI agenda.
- `S5` [Interfacing With NeuroTechnology to Expand Neural Throughput (INTENT), NCT07521930](https://clinicaltrials.gov/study/NCT07521930) — ClinicalTrials.gov; unknown; regulatory; URL supplied in structured research output. Provides the registered study status, planned enrollment, August 2026 start month, sponsors, collaborators, and recording-plus-stimulation objectives.
- `S6` [Decoding Speech Imagery or Just Noise?: A Symptom of the Replicability Crisis](https://repository.essex.ac.uk/43210/) — University of Essex Research Repository; 2026-05-06; primary-research; URL supplied in structured research output. Reports an independent reproduction and replication analysis showing lower reproduced accuracies, missing methodological details, inconsistent time-frequency patterns, and low participant-level statistical reliability.
- `S7` [Benchmarking Neural Decoders for Brain-Computer Interfaces and Neural Population Analysis](https://www.biorxiv.org/content/10.64898/2026.07.21.739953v1) — bioRxiv; 2026-07-21; primary-research; URL supplied in structured research output. Provides a multi-axis benchmark showing that accuracy rankings change when robustness, computational cost, and cross-recording consistency are considered.
- `S8` [The emerging field of cognitive brain-computer interfaces](https://pubmed.ncbi.nlm.nih.gov/42469083/) — Trends in Cognitive Sciences / PubMed; 2026-07-17; reputable-secondary; URL supplied in structured research output. Provides an expert synthesis distinguishing the relatively mature motor and communication BCI results from the more difficult problem of decoding distributed, dynamic cognitive processes.
- `S9` [Long-term safety and efficacy of intracortical microstimulation in humans](https://pubmed.ncbi.nlm.nih.gov/42455900/) — Science Translational Medicine / PubMed; 2026-07-15; primary-research; URL supplied in structured research output. Reports the longest-duration human intracortical microstimulation evidence located in the search, including implant duration, pulse count, adverse events, rising thresholds, and declining functional-electrode fraction.
- `S10` [INdependence Through Endovascular Neuroprosthetic Technology (INTENT): an Early Feasibility Study, NCT07543367](https://clinicaltrials.gov/study/NCT07543367) — ClinicalTrials.gov; 2026-05-11; regulatory; URL supplied in structured research output. Documents the recruiting status, early-feasibility design, estimated enrollment of 10, narrow target population, and multi-year completion schedule for an implanted BCI study.
- `S11` [An Early Feasibility Study of the ReHAB System, NCT03898804](https://clinicaltrials.gov/study/NCT03898804) — ClinicalTrials.gov; unknown; regulatory; URL supplied in structured research output. Shows operational and eligibility constraints for implantable BCI research, including stable paralysis, long-term task participation, geographic proximity, and exclusion criteria involving other implanted devices.
- `S12` [On the Horizon: Three Science and Technology Trends That Could Affect Society](https://www.gao.gov/products/gao-26-108079) — U.S. Government Accountability Office; 2026-04-02; regulatory; URL supplied in structured research output. Provides an authoritative assessment of neural-implant safety, privacy, security, regulatory, and capability-evaluation gaps.
- `S13` [Interim Safety Profile From the Feasibility Study of the BrainGate Neural Interface System](https://pmc.ncbi.nlm.nih.gov/articles/PMC10074470/) — Neurology / PMC; 2023-03-01; primary-research; URL supplied in structured research output. Reports device-related adverse events and serious adverse events from implanted BCI feasibility studies, including postoperative seizures.
- `S14` [Neurological Devices](https://www.fda.gov/medical-devices/products-and-medical-procedures/neurological-devices) — U.S. Food and Drug Administration; unknown; regulatory; URL supplied in structured research output. Documents FDA’s regulatory framework for neurological devices and its specific implanted BCI guidance covering nonclinical testing and clinical considerations.

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
  "id": "research_2026-08-14_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology Evidence Review: Bidirectional Interfaces, Neural Decoding, Neurostimulation, and Neuro-Rights",
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
