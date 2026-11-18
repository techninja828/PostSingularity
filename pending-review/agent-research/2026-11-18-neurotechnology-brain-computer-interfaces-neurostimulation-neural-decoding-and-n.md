# Neurotechnology Evidence Review: Narrow BCI Progress, Persistent Deployment Limits, and Fragmented Neuro-Rights
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-11-18
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The audited evidence materially strengthens the case for continued clinical translation of narrow brain-computer interfaces: implanted silent-speech control, configurable recording-and-stimulation platforms, rehabilitation experiments, and a new early-feasibility trial all show concrete progress. It does not validate unrestricted speech decoding, rich two-way sensory or emotional communication, maintenance-free adaptive neurostimulation, reliable AI-mediated mood or reward control, or broad clinical deployment. Counterevidence includes benchmark-to-clinic performance gaps, limited real-time decoding value, signal drift, recalibration, power and thermal constraints, battery replacement and infection risks, weak stimulation specificity, and unresolved agency and dependency risks. Neural-data governance is becoming more concrete through Delaware’s enacted protections and related state measures, but remains fragmented and primarily privacy-focused rather than a comprehensive neuro-rights regime. The repository mapper recommends qualifying Neural Links and Bliss Divergence while preserving their post-singularity premises; no canon change is warranted for the insufficient-evidence assessments concerning broader AI provenance, space settlement, or analog social persistence.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-11-11 through 2026-11-18
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### Implanted ECoG BCI decodes self-paced silent speech for smart-home control

- Event date: 2026-11-11
- Sources: `S1`
- Observed fact: A peer-reviewed Communications Biology study reported that one participant with amyotrophic lateral sclerosis used a chronically implanted electrocorticographic BCI to control smart-home devices through silently mimed speech, without visual or auditory timing cues. Across 18 experimental sessions, the system achieved a median decoding accuracy of 97.1% against a 7.14% chance level and a median of 11.86 correct decodes per minute.
- Significance: This is a concrete advance toward private, autonomous communication and environmental control for people with paralysis. It directly supports the neural-decoding component of PS-NEURO-001, while demonstrating useful bandwidth through a relatively small command vocabulary rather than unrestricted natural conversation.

### An open translational platform combines a 32-channel implant with adaptive stimulation and BCI2000

- Event date: 2026-11-12
- Sources: `S2`, `S3`
- Observed fact: A technical publication described and characterized the CorTec Brain Interchange–BCI2000 ecosystem as an open platform for implantable BCI and adaptive neuromodulation research. The Brain Interchange system is described as supporting simultaneous neural acquisition from up to 32 channels at 1 kHz, stimulation through selectable channels, wireless transmission, and integration with BCI2000 for real-time signal processing and closed-loop control. Reported testing included recording noise, transfer function, latency, impedance measurement, and closed-loop stimulation experiments.
- Significance: The development addresses a major bottleneck for PS-NEURO-001 and PS-NEURO-002: moving from isolated demonstrations toward repeatable, configurable, multi-modal research infrastructure. Standardized hardware-software interfaces and reproducible workflows could accelerate work on bidirectional interfaces and adaptive stimulation, although they do not themselves demonstrate clinical efficacy.

### Neuralink opened a new early-feasibility trial for robotic implantation across three disabling conditions

- Event date: 2026-11-12
- Sources: `S4`
- Observed fact: The PRIME2 study record was updated on November 12, 2026. It is a recruiting, single-group early-feasibility study of Neuralink’s fully implanted N1 BCI and R1 robotic inserter in adults with severe upper-limb impairment caused by spinal-cord injury, ALS, or chronic ischemic stroke. The registry lists an estimated enrollment of up to 10 participants, computer-cursor or virtual-keyboard control as the intended function, serious adverse device effects as the primary outcome, and follow-up of approximately two years, with optional extended follow-up.
- Significance: This is a meaningful clinical-translation signal: the trial expands the target population beyond a single diagnosis and explicitly foregrounds adverse-device monitoring and longitudinal follow-up. It provides evidence of continued movement toward implanted BCI deployment, but remains a feasibility study rather than proof of safety, durability, or high-bandwidth communication.

### EEG neurofeedback paired with robotic gait training improved sensorimotor measures in people with chronic complete spinal-cord injury

- Event date: 2026-11-12
- Sources: `S5`
- Observed fact: An ahead-of-print IEEE study published November 12 reported a two-stage intervention involving 12 EEG neurofeedback sessions using a robotic gait-training system. The protocol trained participants to self-modulate mu rhythms at 8–12 Hz and beta rhythms at 15–20 Hz, first with a single-channel setup and then with a multi-channel BCI. The authors reported improvements in rhythm modulation, inter-region connectivity, and clinical measures including motor function, neurogenic bladder management, and functional independence.
- Significance: The study is relevant to neurostimulation and closed-loop rehabilitation because it combines neural decoding, feedback, and robotic assistance rather than treating BCI as a purely communicative interface. It offers a possible path toward therapeutic neurotechnology, but the findings remain preliminary and do not demonstrate direct restoration of severed spinal pathways.

### Clinical motor-imagery decoding remains substantially weaker than benchmark performance

- Event date: 2026-11-13
- Sources: `S10`
- Observed fact: A November 13, 2026 Journal of Neural Engineering study reported 85.13 ± 10.53% accuracy on the public BCI Competition IV 2a dataset, but only 71.9 ± 8.9% accuracy on a custom dataset involving 20 stroke patients. The authors identified suboptimal patient engagement and limited EEG feature-decoding capacity as existing challenges. The augmented-reality paradigm improved performance over a traditional two-dimensional paradigm, but the clinical result remained materially below the benchmark result.
- Significance: The benchmark-to-clinic gap is direct counterevidence against treating high offline or public-dataset accuracy as evidence of deployment readiness. It narrows optimistic interpretations of neural decoding by showing that patient heterogeneity, engagement, and clinical context remain significant sources of performance loss. This challenges PS-NEURO-001’s implied trajectory from decoding demonstrations toward broad, reliable interfaces.

### A beta oscillation preceding movement cancellation showed a neural correlate but limited real-time decoding value

- Event date: 2026-11-14
- Sources: `S6`
- Observed fact: A Communications Biology study published November 14 recorded 32-electrode cortex-wide EEG and treadmill velocity in head-fixed rats performing movement stops. It reported a single beta oscillation cycle in left motor cortex approximately 200 milliseconds before movement cancellation, with beta power carrying information about future velocity during stop planning. However, machine-learning analyses found limited utility for real-time action decoding.
- Significance: The finding is a useful counter-signal to claims that identifying a neural correlate automatically yields a reliable control channel. It supports more cautious assessment of neural decoding: precise timing and reproducibility matter, and biologically meaningful signals may still be unsuitable for real-time BCI control.

### Deep-brain stimulation requires recurring generator replacement and carries cumulative procedural risk

- Event date: 2026-11-14
- Sources: `S13`
- Observed fact: A systematic review published November 14, 2026 analyzed 30 human studies comprising 4,101 observations of non-rechargeable deep-brain-stimulation implantable pulse generators. Reported device longevity ranged from approximately 2 to more than 6 years. Higher stimulation-energy demand was associated with shorter longevity. The review reported major infection after 30 replacements, corresponding to 2.3%, and found that each previous replacement increased infection odds with an odds ratio of 1.6. Two deaths were associated with depletion-related parkinsonism-hyperpyrexia syndrome. Sixty percent of the included studies were judged to have a high risk of bias.
- Significance: The findings provide concrete counterevidence to visions of continuously operating adaptive neurostimulation without substantial maintenance or safety tradeoffs. Battery depletion, repeated surgery, infection risk, energy demand, and evidence-quality problems all constrain scaling. This is relevant to PS-NEURO-002 because engineered mood or reward control would require reliable long-duration stimulation, while the current implant ecosystem still imposes recurrent hardware interventions and clinically consequential failure modes.

### Non-invasive attention decoding was close to chance when overt gaze cues were removed

- Event date: 2026-11-15
- Sources: `S11`
- Observed fact: A November 15, 2026 NeuroImage study decoded attended spatial location from whole-head high-density fNIRS in an overt attention task, with a reported mean decoding latency of 2.4 seconds. However, decoding fell close to chance in a covert auditory condition in which participants maintained central fixation while attending to the same talkers. Control experiments indicated that overt-condition decoding was influenced by sustained eye position or gaze direction rather than attention alone.
- Significance: This is a strong constraint on claims that non-invasive neural decoding can privately infer attention or mental content in realistic settings. The result suggests that apparent decoding success may depend on observable behavioral correlates and may not survive when those correlates are removed. It weakens extrapolations from controlled demonstrations toward covert, continuous mind-reading or affective inference under PS-NEURO-001 and PS-NEURO-002.

### Delaware’s privacy framework places neural data inside sensitive-data protections beginning January 1, 2027

- Event date: 2026-11-16
- Sources: `S7`, `S8`, `S9`
- Observed fact: During the priority window, Delaware legislative records and policy analysis surfaced the state’s HB 380, signed September 2, 2026. The law defines sensitive data to include neural data generated by measuring an individual’s central nervous system and states that the amendment becomes effective January 1, 2027. The framework includes consent requirements, proportionality requirements for processing sensitive data, a revocation mechanism, and data-protection-assessment obligations.
- Significance: This is a concrete neuro-rights and neural-privacy signal: protection is being implemented through ordinary consumer-privacy law rather than a standalone constitutional neuro-right. It matters for PS-NEURO-002 because it creates governance constraints around neural sensing, derived features, consent, sale, and downstream processing, even though it does not regulate mood control or therapeutic stimulation directly.

### Long-term neural decoding remains constrained by signal drift, recalibration, power, heat, and maintenance requirements

- Event date: 2026-11-18
- Sources: `S12`
- Observed fact: A 2026 review of generalizable neural decoding for clinically scalable BCIs identifies instability of neural signals and their relationship to intended behavior as a fundamental barrier to long-term performance. It describes biological responses around implanted electrodes, mechanical micromotion, changes in electrode impedance and unit identity, decoder drift, user fatigue, behavioral adaptation, and disease progression. It further reports that implantable systems face strict limits on power consumption, telemetry bandwidth, memory, latency, and thermal dissipation, while high-capacity models may be difficult to run within milliwatt-scale implantable power budgets. The review states that prospective home-use evaluation and validated update, fallback, audit, and rollback protocols remain necessary.
- Significance: This directly challenges the assumption that improved decoding algorithms or larger channel counts automatically produce durable, scalable BCIs. The limiting problem is an interacting system of tissue response, changing behavior, embedded computation, thermal safety, calibration burden, caregiver support, cybersecurity, and maintenance. These constraints are especially damaging to the strongest form of PS-NEURO-001, which assumes sustained high-bandwidth two-way operation rather than short laboratory sessions.

### Closed-loop stimulation creates agency, dependency, and unintended-output risks that remain unresolved

- Event date: 2026-11-18
- Sources: `S14`
- Observed fact: The IEEE Neuroethics Framework for Medical Applications, Fall 2026 version 1, states that stimulation technologies face risks including pain, tissue damage, undesirable neuroplastic effects, habituation, infection, biotoxicity, and inflammation. It identifies possible effects on identity, agency, and emotional wellbeing, and notes that closed-loop systems are more difficult to model because real-time decoding errors can produce unintended device or interface outputs. The framework also raises dependence on neurotechnology for basic activities and emphasizes efficiency, safety, and traceability as central requirements.
- Significance: This is expert and standards-oriented counterevidence against assuming that reliable mood or experience engineering would be merely an engineering extension of current BCIs. The framework treats agency, dependence, emotional wellbeing, and erroneous control as unresolved safety and governance problems. It supports PS-NEURO-002 as a governance concern, but simultaneously narrows the claim by showing that the required reliability and traceability conditions are not yet settled.

### Current neuro-rights protections are fragmented privacy provisions rather than comprehensive safeguards against cognitive manipulation

- Event date: 2026-11-18
- Sources: `S15`, `S16`
- Observed fact: A November 18, 2026 analysis of neurorights legislation reported that four U.S. states—Colorado, California, Montana, and Connecticut—had enacted rules bringing neural activity within protected personal data. The same analysis states that these measures generally place neural data inside existing sensitive-data regimes rather than creating standalone neurorights. It also described the Cantabrian Digital Health Act as still being a bill in parliamentary passage rather than enacted law. The legal approach therefore remains a patchwork of state privacy rules and proposals rather than a uniform framework covering mental privacy, cognitive liberty, compelled neural disclosure, or manipulation through stimulation.
- Significance: This narrows optimistic interpretations of PS-NEURO-002 and PS-AI-003. Neural-data protection is becoming more visible, but the observed legal instruments primarily regulate collection and processing. They do not yet provide comprehensive protection against closed-loop behavioral influence, dependency, involuntary stimulation, or misuse of inferred mental states. Governance development is therefore real but incomplete and jurisdictionally fragmented.

### Available stimulation systems still lack selective access to specific neuronal types and many deep circuits

- Event date: 2026-11-18
- Sources: `S17`
- Observed fact: A 2026 RAND Europe report on governing augmentative BCIs states that no clinically or commercially available technology can selectively target specific neuronal types or isolated circuits. It reports that non-invasive methods and cortical implants have limited access to subcortical structures relevant to memory, emotion, and motivation, while focused ultrasound still faces resolution and hardware constraints. The report also identifies power-transfer efficiency, heat dissipation, telemetry bandwidth, miniaturization, and the limited availability of trained neurosurgeons as deployment constraints.
- Significance: These are physical and operational barriers to the strongest versions of PS-NEURO-001 and PS-NEURO-002. Rich sensory or emotional two-way communication would require more precise recording and stimulation than currently available systems provide. Likewise, reliable mood or reward engineering is constrained by broad circuit-level modulation, limited access to relevant deep structures, power and heat limits, and specialized surgical capacity.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S4`, `S10`, `S11`, `S12`, `S13`, `S17`
- Evidence: Evidence strengthens the neural-decoding and bidirectional-platform components of the claim: an implanted ECoG system achieved 97.1% median accuracy for a limited silent-speech command set in one participant, and a 32-channel platform demonstrated simultaneous recording, stimulation, wireless transmission, and closed-loop experimentation. A recruiting early-feasibility trial provides additional clinical-translation evidence. However, the supplied evidence does not establish rich two-way communication, sensory or emotional exchange, unrestricted speech decoding, durable long-term safety, broad generalization, or scalable deployment. Clinical benchmark-to-patient performance gaps, signal drift, recalibration, power, heat, maintenance, surgical, and stimulation-specificity constraints materially limit the stronger version of the assumption.
- Real-world implication: Neural interfaces are progressing from demonstrations toward early clinical translation, particularly for constrained communication, device control, rehabilitation, and adaptive stimulation. Near-term systems should be treated as narrow, supervised, and maintenance-intensive rather than as general-purpose high-bandwidth links. Long-term safety, reliability, privacy, and population-level performance remain unresolved.
- PostSingularity implication: A post-singularity setting could plausibly support rich two-way nervous-system-to-AI communication only if it resolves the current bottlenecks in stable bandwidth, precise stimulation, tissue compatibility, power, thermal management, calibration, and agency protections. The supplied evidence supports this as a conditional trajectory, not as an established capability; any storyworld deployment should distinguish narrow command channels from genuinely sensory or emotional exchange.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S7`, `S8`, `S9`, `S13`, `S14`, `S15`, `S16`, `S17`
- Evidence: The governance component is strengthened by evidence that closed-loop stimulation raises unresolved questions about agency, dependency, emotional wellbeing, unintended outputs, traceability, and consent. Delaware has enacted neural-data protections effective January 1, 2027, and other jurisdictions have adopted or considered related privacy measures. However, no supplied source demonstrates reliable AI-mediated control of human mood, reward, immersive experience, or emotional state. Current systems remain limited by stimulation specificity, access to deep circuits, power, safety, maintenance, and clinical evidence.
- Real-world implication: Neurotechnology is already generating governance requirements around neural-data collection, consent, derived features, safety, and accountability, even before reliable mental-state engineering exists. Regulation is likely to remain fragmented and focused initially on privacy and medical safety rather than comprehensive protection against cognitive manipulation or dependency.
- PostSingularity implication: If future systems make engineered mental states reliable and scalable, consent, autonomy, dependency, participation, and meaning would become major governance problems rather than merely technical design issues. The current evidence supports preparing for that problem and establishing traceability and agency safeguards, but does not justify treating advanced mood or reward control as an observed capability.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: `S14`, `S16`
- Evidence: The supplied evidence contains substantial discussion of neural-data privacy, clinical traceability, safety monitoring, and audit or rollback needs for implanted systems, but it does not provide direct evidence about AI transparency standards, general AI provenance adoption, model-audit uptake, verification rituals, or regulatory disclosure rules. The materials therefore do not establish a directional change for the broader claim that AI influence is driving stronger provenance and audit systems.
- Real-world implication: There is insufficient basis in this evidence packet to conclude that broader AI provenance and audit systems are strengthening or gaining adoption. Neural-technology governance may provide adjacent examples of consent, traceability, and data-protection requirements, but those should not be generalized to the overall AI governance environment.
- PostSingularity implication: A post-singularity society could require extensive provenance, verification, and graduated oversight for influential AI systems, but the supplied evidence does not show whether those institutions emerge, succeed, or become enforceable. The assumption should remain open pending direct evidence from AI governance, provenance infrastructure, and audit practice.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: No supplied source addresses launch economics, propulsion, orbital or off-world settlement, closed-loop life support, in-space manufacturing, human health in long-duration habitation, or autonomous mission operations. The evidence packet is focused on neural interfaces and neurotechnology governance, so it provides no directional support or contradiction for sustained off-world settlement.
- Real-world implication: No assessment of the practicality or timing of sustained orbital or off-world communities can be made from the supplied evidence. The key engineering, medical, economic, and operational indicators remain unobserved in this packet.
- PostSingularity implication: The assumption remains a possible post-singularity pathway, but its plausibility depends on evidence outside the current packet concerning energy abundance, autonomous construction and maintenance, life-support closure, radiation protection, propulsion, and human adaptation. No storyworld conclusion should be drawn from the supplied developments alone.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: No supplied source addresses device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, or cultural resistance to pervasive AI and neural integration. The neuro-rights material establishes privacy and agency concerns but does not measure the persistence or revival of analog practices.
- Real-world implication: The packet does not show whether tactile, private, or low-technology practices are expanding, persisting, or disappearing. Privacy and agency concerns may create conditions for such practices, but that inference is not sufficient evidence of the claimed social trend.
- PostSingularity implication: Analog countercultures remain a plausible social response to pervasive integration, especially where people value unmediated agency and private meaning. Their scale, durability, and intergenerational transmission remain unknown and should not be treated as established by the current evidence.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S10`, `S11`, `S12`, `S13`, `S17`
- Why this location: The evidence supports progress toward implanted neural control, but it does not support treating current or near-term systems as unrestricted, durable, high-bandwidth communication. The existing summary presents neural links as broadly capable of thought, emotion, identity, memory, and sensory exchange without recording the substantial limits identified by the audited evidence.
- Proposed change: Add a qualification to the Summary stating that precursor systems provide narrow, task-specific neural control and communication, while richer two-way sensory or emotional exchange depends on unresolved advances in signal stability, stimulation precision, calibration, power, thermal management, maintenance, surgical scalability, privacy, and agency protection. Preserve the post-singularity capability as a conditional worldbuilding development rather than implying that contemporary demonstrations already establish it.
- Implementation steps:
  1. Insert the qualification immediately after the existing Summary description of neural-link capabilities, using the Summary heading as the edit anchor.
  2. Distinguish limited command decoding, device control, rehabilitation, and closed-loop experimentation from unrestricted speech, continuous affective inference, or rich sensory exchange.
  3. Cross-reference the Function section for operational constraints and retain the existing Cultural Effects and Story Use material unless later review identifies a direct continuity conflict.
  4. Review terminology against the Bliss Divergence file so that neural immersion and emotional-state engineering are not presented as equally established capabilities without an in-world technological explanation.
- Dependencies or conflicts:
  - The existing claims that neural links are safe, deeply personalized, and capable of shifting identity, memory weight, and sensory input may conflict with the evidence’s unresolved safety, agency, stimulation-specificity, and maintenance concerns.
  - The single-participant silent-speech result in S1 supports only a limited command vocabulary and should not be used to justify unrestricted natural speech or rich two-way communication.
  - The technical capabilities described in S2 and S3 are platform demonstrations, not evidence of durable clinical deployment or broad human efficacy.
  - The post-singularity setting may intentionally resolve present-day limitations; any such resolution should be stated as an in-world development rather than inferred directly from the audited evidence.

### `worldbible/technologies/neural-links.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **challenges**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S4`, `S5`, `S6`, `S10`, `S11`, `S12`, `S13`, `S17`
- Why this location: The current Function claims imply reliable and wide-ranging neural exchange, while the evidence shows benchmark-to-clinic performance loss, limited real-time decoding value, signal drift, recalibration, power and heat constraints, recurring implant risks, and limited access to precise or deep stimulation targets.
- Proposed change: Add a concrete limitations subsection under Function that states neural-link performance varies by task, modality, user, and clinical context; that systems require calibration and maintenance; that implants face battery, infection, replacement, power, and thermal constraints; and that current stimulation cannot selectively address all neuronal types or deep circuits relevant to emotion, memory, or motivation. State that closed-loop operation requires monitoring, fallback, audit, and rollback safeguards.
- Implementation steps:
  1. Add the limitations subsection directly under the existing Function heading, before Cultural Effects.
  2. Include narrow silent-speech and device-control interfaces, rehabilitation systems, and recording-and-stimulation platforms as examples of demonstrated or emerging functions without presenting them as general-purpose links.
  3. Add operational requirements for recalibration, longitudinal follow-up, adverse-event monitoring, cybersecurity, and explicit user consent during closed-loop operation.
  4. Review Story Use examples involving link malfunction or immersive simulation so that failures can reflect calibration, drift, bandwidth, stimulation, or consent problems rather than only generic malfunction.
  5. Check the PS Technology Index entry after editing to ensure the file remains accurately categorized without adding unsupported capability labels.
- Dependencies or conflicts:
  - S5 reports rehabilitation gains from a combined EEG, neurofeedback, and robotic-gait intervention; the file should not attribute those gains solely to neural links.
  - S6 is preclinical and reports limited real-time decoding utility, so it should inform caution rather than be treated as human deployment evidence.
  - S12, S13, and S17 constrain claims of continuous, maintenance-free operation and precise mood or reward control.
  - The existing Function language about emotional regulation systems preventing psychological threshold violations should be reconciled with S14’s unresolved risks from closed-loop decoding errors, dependency, agency effects, and unintended outputs.

### `philosophy/bliss-divergence.md` -> Summary

- Priority: **medium**
- Recommendation: **debate**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-002`
- Sources: `S7`, `S8`, `S9`, `S13`, `S14`, `S15`, `S16`, `S17`
- Why this location: The evidence strengthens the governance relevance of neural data, consent, traceability, dependency, and agency, but provides no evidence that reliable AI-mediated control of human mood, reward, or perpetual immersive joy currently exists. The existing Summary treats safe neural immersion as an established technical option without distinguishing the storyworld’s mature capability from present-day evidence.
- Proposed change: Add a qualification to the Summary explaining that the technical basis for bliss immersion is a post-singularity achievement whose safety and legitimacy remain contested, not a capability established by current neurotechnology. Explicitly frame the central conflict as involving consent, dependency, agency, traceability, and the possibility of erroneous or unintended closed-loop effects, alongside the existing question of whether remaining in reality has meaning.
- Implementation steps:
  1. Insert the qualification after the existing Summary description of perpetual AI-mediated joy, using Summary as the exact edit anchor.
  2. Preserve the established Bliss Divergence premise while marking reliable mood or reward engineering as an in-world technological condition rather than a conclusion supported by current evidence.
  3. Add a cross-reference to Trust Fabrics or AI Trust only if the human reviewer decides that bliss authorization and traceability use those broader institutions; do not infer that the supplied evidence establishes such adoption.
  4. Review the Function and Philosophical Tensions sections together so that claims of safety, community review, and voluntary entry or exit are consistent with the unresolved risks described in S14 and the fragmented legal protections in S7–S9 and S15–S16.
- Dependencies or conflicts:
  - The existing phrase 'safe neural immersion' may conflict with S13’s maintenance and procedural risks, S14’s stimulation and agency risks, and S17’s limits on precise access to relevant circuits.
  - The existing claim that citizens may enter or leave bliss states under community review implies governance mechanisms that are not demonstrated by the supplied real-world evidence; it should remain clearly in-world canon.
  - The evidence concerns privacy and medical-safety governance more directly than mood engineering, so the file should not imply that Delaware HB 380 or other privacy provisions regulate bliss states comprehensively.
  - The storyworld’s perpetual bliss premise may intentionally exceed current technology; the proposed qualification should narrow evidentiary interpretation without removing that fictional capability.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **debate**
- Evidence relationship: **extends**
- Assumptions: `PS-NEURO-002`
- Sources: `S13`, `S14`, `S15`, `S16`, `S17`
- Why this location: The audited evidence adds governance tensions that are not fully represented by the existing questions about effort, pain, and social cohesion. It introduces dependency, cognitive liberty, unintended outputs, traceability, unequal access, jurisdictional fragmentation, and the risk that participation becomes socially or functionally necessary.
- Proposed change: Extend Philosophical Tensions with explicit questions about whether bliss participation can remain voluntary when people depend on neurotechnology for basic activities, how users can revoke or contest a closed-loop system’s influence, who is accountable for erroneous stimulation or inferred mental states, and whether fragmented neural-data protections can meaningfully protect autonomy.
- Implementation steps:
  1. Add the new questions at the end of the existing Philosophical Tensions section.
  2. Tie the questions to the existing Emotional Integrity Contracts and Memory Threads without asserting that current law already supplies equivalent protections.
  3. Add a narrative distinction between data governance, which may regulate collection and processing, and cognitive-liberty or anti-manipulation protections, which remain incomplete in the audited evidence.
  4. Review Story Use for plots involving withdrawal, dependency, consent revocation, audit trails, or disputed emotional authenticity so the new tensions produce concrete consequences.
- Dependencies or conflicts:
  - S15 and S16 describe fragmented privacy protections and recommendations rather than a uniform binding regime; the fictional governance system should not be presented as a direct real-world legal extrapolation.
  - S14 identifies closed-loop decoding errors and unintended outputs as unresolved risks, which may challenge any absolute claim that Emotional Integrity Contracts guarantee safe outcomes.
  - S17 reports limited access to deep circuits and broad circuit-level modulation, creating a technical dependency for any canon explanation of precise reward or mood engineering.

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

- The silent-speech result concerns one participant and a limited command vocabulary; it does not establish unrestricted speech, emotional decoding, rich sensory exchange, or broad population generalization.
- The CorTec platform demonstrates technical capabilities and closed-loop experiments, not approved therapeutic use, durable human benefit, or routine clinical deployment.
- The PRIME2 record describes a recruiting early-feasibility study and planned monitoring, not completed implantation, safety outcomes, efficacy, durability, or deployment scale.
- Long-term implant performance remains uncertain because of signal drift, tissue response, recalibration, power, heat, battery replacement, infection, maintenance, and user adaptation.
- No supplied source provides independent evidence of reliable AI-mediated control of human mood, reward, emotional state, immersive experience, or other engineered mental states.
- Neural-data protections are emerging but fragmented; their implementation outcomes and effects on commercial collection or secondary use are not yet observable in the supplied window.
- No evidence was supplied concerning AI provenance and audit adoption, off-world settlement, or persistence of analog practices.
- The evidence does not establish whether current governance frameworks will remain voluntary and fragmented or become binding, interoperable, and enforceable.
- The implanted silent-speech study reported a median decoding accuracy of 97.1% in one participant and a limited command set, whereas the motor-imagery study reported 85.13 ± 10.53% on a public benchmark but 71.9 ± 8.9% in 20 stroke patients. These findings are not directly inconsistent because they use different modalities, tasks, datasets, and populations, but they conflict if generalized into a universal claim that high benchmark or laboratory accuracy predicts clinical deployment readiness.
- The Delaware evidence describes one enacted state framework effective January 1, 2027, while the November 18 neurorights analysis describes a broader but fragmented set of state protections. These are compatible: Delaware is an additional concrete example, not evidence of a comprehensive or uniform neurorights regime.
- The CorTec materials describe simultaneous acquisition, stimulation, wireless transmission, and closed-loop experimentation, while the counterevidence identifies unresolved long-term drift, power, thermal, maintenance, and safety barriers. The technical platform capability does not contradict the deployment barriers because platform characterization is not clinical deployment evidence.
- The silent-speech study and the rat movement-stopping study differ in practical decoding value. The rat study’s limited real-time utility does not refute the human silent-speech result; it limits generalization from a neural correlate in a preclinical task to a reliable control channel across systems.
- Forecasts or implications about future rich two-way communication, mood engineering, reward control, large-scale deployment, or durable clinical benefit are not supported as observed developments.
- Reliable AI-mediated control of mood, reward, emotional state, immersive experience, or other engineered mental states in humans during the priority window is excluded from the evidence-supported claims.
- Rich two-way nervous-system-to-AI communication established by the supplied BCI performance evidence is excluded.
- Unrestricted natural speech decoding, emotional decoding, or rich two-way communication established by the implanted silent-speech study is excluded.
- Routine clinical deployment, long-term implant safety, generalization across users, or clinical efficacy established by the single-participant silent-speech study is excluded.
- Clinical efficacy or approved therapeutic use established by the CorTec Brain Interchange–BCI2000 technical characterization and closed-loop demonstrations is excluded.
- Completed implantation, enrollment milestones, safety outcomes, efficacy, durability, or routine deployment established by the recruiting PRIME2 registry record is excluded.
- Direct restoration of severed spinal pathways established by the EEG neurofeedback and robotic gait-training study is excluded.
- A neural correlate automatically yielding a reliable real-time control channel, based on the rat movement-stopping study, is excluded.
- Private, continuous mind-reading or reliable affective inference established by non-invasive attention-decoding demonstrations is excluded.
- Continuous, maintenance-free adaptive neurostimulation without battery, infection, replacement, power, heat, and safety tradeoffs is excluded.
- Comprehensive protection against mental privacy violations, cognitive manipulation, compelled neural disclosure, involuntary stimulation, or dependency established by the identified privacy laws and policy instruments is excluded.
- A universal or uniform neuro-rights regime established by Delaware HB 380 or the identified state privacy provisions is excluded.
- Selective access to specific neuronal types or isolated deep circuits established by currently available clinical or commercial stimulation systems is excluded.
- A new binding international instrument specific to cognitive liberty, mental privacy, compelled neural disclosure, or neural manipulation during the priority window is excluded.
- PS-AI-003 was assessed as insufficient-evidence with low confidence. No repository edit is warranted because S14 and S16 concern neurotechnology safety, traceability, privacy, and recommendations rather than direct evidence of broader AI provenance systems, model-audit adoption, verification rituals, or disclosure rules. Continue monitoring the declared Trust Fabrics and AI Trust files for direct AI-governance evidence.
- PS-SPACE-001 was assessed as insufficient-evidence with low confidence and has no supplied source IDs. No repository edit is warranted because the packet contains no evidence about launch economics, propulsion, life support, orbital settlement, in-space manufacturing, radiation protection, or autonomous mission operations. Do not infer a timeline or capability change for Aerospace Systems.
- PS-SOCIAL-002 was assessed as insufficient-evidence with low confidence and has no supplied source IDs. No repository edit is warranted because the packet does not establish growth or decline in analog practices, device-free spaces, right-to-disconnect policies, low-technology communities, or intergenerational cultural persistence. The neural-privacy and agency concerns may motivate such practices in fiction, but they do not justify changing the PS Timeline.
- The mixed PS-NEURO-001 assessment is covered by both a qualifying edit to the Neural Links Summary and a constraints-focused edit under Function. Together they preserve supported narrow-interface progress while preventing current demonstrations from being generalized into unrestricted or maintenance-free two-way communication.
- The mixed PS-NEURO-002 assessment is covered by qualifying the Bliss Divergence Summary and extending its Philosophical Tensions. These edits preserve the established post-singularity premise while making governance, agency, dependency, and technical uncertainty explicit.
- No timeline edit is proposed for the dated developments because the supplied evidence does not establish a new post-singularity cycle milestone, and the existing timeline’s Cycle 3 Neural Link Age and Cycle 5 Bliss Divergence references are not directly contradicted by the audited packet.

## Watchlist

- Results from the PRIME2 and other implanted BCI early-feasibility studies, including enrollment, serious adverse events, explantations, device longevity, performance across diagnoses, and patient-reported autonomy.
- Multi-participant and multi-year validation of implanted silent-speech or speech-decoding systems, including unrestricted vocabulary, sensory feedback, emotional information, home use, recalibration burden, and cybersecurity.
- Evidence of stable bidirectional stimulation and recording with precise access to sensory, emotional, reward, or deep-brain circuits without unacceptable tissue, agency, dependency, infection, power, or thermal risks.
- Implementation and enforcement outcomes for Delaware HB 380 and other neural-data privacy laws, including consent withdrawal, derived-feature processing, commercial secondary use, and enforcement actions.
- Binding national or international neurotechnology rules addressing mental privacy, cognitive liberty, compelled neural disclosure, involuntary stimulation, manipulation, or dependency.
- Direct evidence of AI provenance standards, model audits, disclosure requirements, verification infrastructure, and adoption in high-impact deployments.
- Launch-cost trends, closed-loop life-support demonstrations, long-duration human habitation results, in-space manufacturing, autonomous mission operations, and off-world construction milestones.
- Device-free spaces, right-to-disconnect rules, analog-media consumption, low-tech communities, and evidence of intergenerational persistence or revival of analog practices.

## Sources

- `S1` [Self-paced silent speech brain-computer interface for device control](https://www.nature.com/articles/s42003-026-10477-5) — Communications Biology / Nature Portfolio; 2026-11-11; primary-research; URL supplied in structured research output. Primary human study reporting measured accuracy and command throughput for self-paced silent-speech decoding with an implanted ECoG BCI. The DOI record was deduplicated because it identifies the same study.
- `S2` [A translational platform for brain-computer interfaces and adaptive neuromodulation: Technical characterization, long-term validation, and implementation of the CorTec Brain Interchange–BCI2000 ecosystem](https://visualize.jove.com/43019594-a-translational-platform-for-brain-computer-interfaces-and-adaptive-neuromodulation-technical-characterization-long-term-validation-and-implementation-of-the-cortec-brain-interchange-bci2000-ecosystem) — Journal of Visualized Experiments / JoVE; 2026-11-12; primary-research; URL supplied in structured research output. Technical publication describing the implantable recording-and-stimulation platform, software integration, validation methods, and closed-loop capabilities.
- `S3` [CorTec publications listing for the Brain Interchange platform](https://cortec-neuro.com/bci/publications) — CorTec; 2026-11-10; official-release; URL supplied in structured research output. First-party publication listing documenting the platform’s release and related closed-loop neuromodulation work. It is retained as company-originated corroboration, not independent evidence.
- `S4` [NCT07929792: An Early Feasibility Study of a Robotically Implanted Brain-Computer Interface for Neural Control of External Devices](https://clinicaltrials.gov/study/NCT07929792) — ClinicalTrials.gov; 2026-11-12; regulatory; URL supplied in structured research output. Official clinical-trial record for the recruiting PRIME2 study, including population, intervention, enrollment, outcomes, and follow-up plan. The Syfrah record was deduplicated because it imports ClinicalTrials.gov data.
- `S5` [Robotic Gait Multi-channel Mu Beta Neurofeedback Training in Paraplegics Enhanced Inter-regional Connectivity and Sensorimotor Functions](https://pubmed.ncbi.nlm.nih.gov/43019280/) — PubMed / IEEE Transactions on Neural Systems and Rehabilitation Engineering; 2026-11-12; primary-research; URL supplied in structured research output. Primary indexed record for a BCI-enabled EEG neurofeedback and robotic gait-training study in people with complete spinal-cord injury. The DOI record was deduplicated because it identifies the same study.
- `S6` [Volitional stopping is preceded by a transient motor cortex EEG beta oscillation](https://www.nature.com/articles/s42003-026-11331-4) — Communications Biology / Nature Portfolio; 2026-11-14; primary-research; URL supplied in structured research output. Primary experimental study measuring the timing, information content, and practical decoding limits of a motor-cortex EEG signal. The DOI record was deduplicated because it identifies the same study.
- `S7` [House Bill 380 legislative document](https://legis.delaware.gov/json/BillDetail/GenerateHtmlDocument?docTypeId=2&legislationId=143105&legislationName=HB380&legislationTypeId=1) — Delaware General Assembly; 2026-09-02; regulatory; URL supplied in structured research output. Official legislative text defining neural data as sensitive data and specifying the January 1, 2027 effective date.
- `S8` [HB 380 bill detail](https://legis.delaware.gov/BillDetail/143105) — Delaware General Assembly; 2026-09-02; regulatory; URL supplied in structured research output. Official status record confirming that HB 380 was signed on September 2, 2026. It is retained because it supports enactment status, while S7 supports statutory text.
- `S9` [Neural Data Becomes Sensitive Data in Delaware on January 1](https://risktemplate.com/blog/2026-11-16-neural-data-sensitive-data-delaware-signal-test-vendor-evidence/) — RiskTemplates; 2026-11-16; reputable-secondary; URL supplied in structured research output. Policy analysis surfaced during the priority window that explains operational implications for neural-data vendors and derived neural features.
- `S10` [Augmented reality paradigm and EA-DGCNN decoding algorithm for motor imagery in stroke patients](https://pubmed.ncbi.nlm.nih.gov/42981608/) — PubMed / Journal of Neural Engineering; 2026-11-13; primary-research; URL supplied in structured research output. Primary human study reporting both public-benchmark performance and performance on a 20-patient clinical dataset, exposing a benchmark-to-clinic gap. The DOI record was deduplicated because it identifies the same study.
- `S11` [Decoding spatial attention in the cocktail party problem using whole-head high-density fNIRS](https://www.sciencedirect.com/science/article/pii/S1053811926006075) — Elsevier / NeuroImage; 2026-11-15; primary-research; URL supplied in structured research output. Primary study explicitly comparing overt and covert attention decoding and reporting latency and gaze-related confounding. The PubMed record was deduplicated because it identifies the same study.
- `S12` [Generalizable neural decoding for clinically scalable brain-computer interfaces](https://www.nature.com/articles/s44385-026-00119-0) — Nature Portfolio; unknown; reputable-secondary; URL supplied in structured research output. Comprehensive review identifying instability, hardware, power, thermal, recalibration, home-use, and maintenance barriers to clinical BCI deployment.
- `S13` [Longevity of Non-Rechargeable Implantable Pulse Generators in Deep Brain Stimulation: A Systematic Review](https://pubmed.ncbi.nlm.nih.gov/43033155/) — PubMed / Stereotactic and Functional Neurosurgery; 2026-11-14; primary-research; URL supplied in structured research output. Systematic review reporting generator longevity, replacement complications, infection odds, depletion-related deaths, and risk-of-bias assessment. The DOI record was deduplicated because it identifies the same study.
- `S14` [IEEE Neuroethics Framework Medical Application, Fall 2026 v.1](https://brain.ieee.org/wp-content/uploads/2026/11/IEEE-Neuroethics-Framework-Medical-Application.pdf) — IEEE Brain; unknown; standard; URL supplied in structured research output. Framework explicitly addressing stimulation risks, agency, dependency, closed-loop decoding errors, unintended outputs, and traceability.
- `S15` [Neurorights: which countries and states already protect brain data](https://www.santiagoramonycajal.org/en/2026/11/18/where-mental-privacy-is-already-law/) — Santiago Ramón y Cajal Foundation; 2026-11-18; reputable-secondary; URL supplied in structured research output. Contemporary legal analysis distinguishing enacted neural-data privacy provisions from standalone neurorights and noting the status of the Cantabrian bill.
- `S16` [Recommendation on the Ethics of Neurotechnology](https://unesdoc.unesco.org/ark:/48223/pf0000394866) — UNESCO; unknown; official-release; URL supplied in structured research output. International normative source showing that global neurotechnology governance remains framed as recommendations and policy guidance rather than uniformly binding legal protection.
- `S17` [Governing Augmentative Brain–Computer Interfaces](https://cfg.eu/wp-content/uploads/CFG_RAND-Europe-2026-governing-augmentative-brain-computer-interfaces.pdf) — RAND Europe / CFG; unknown; reputable-secondary; URL supplied in structured research output. Technology and governance assessment documenting limits in stimulation specificity, deep-brain access, power, bandwidth, miniaturization, and surgical scalability.

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
  "id": "research_2026-11-18_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology Evidence Review: Narrow BCI Progress, Persistent Deployment Limits, and Fragmented Neuro-Rights",
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
