# Neurotechnology 2026 Window Review: Decoding Progress, Deployment Limits, and Neuro-Rights Gaps
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-10-01
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The audited evidence shows meaningful progress in neural decoding, including imagined-speech and semantic representations, improved motor-cortex modeling, and broader clinical neural-signal interpretation. It does not establish scalable, fully implanted, wireless, bidirectional neural-AI communication, durable sensory feedback, or reliable AI-mediated control of mood, reward, or immersive affective states. Long-term deployment remains constrained by single-participant evidence, invasive and specialized infrastructure, caregiver dependence, external-validation failure, neural variability, adaptive-decoder effects, and hardware risks. Governance pressure is strengthened around neural privacy, consent, provenance, auditability, secondary use, and institutional accountability, but no binding neuro-rights regime was identified in the specified window. The assumption registry and canon remain unchanged; the canon implications below are conservative review recommendations for human consideration.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-09-24 through 2026-10-01
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### A decoding method addresses nonidentifiability in motor-cortex models

- Event date: 2026-09-25
- Sources: `S1`
- Observed fact: A Nature Communications study published on September 25, 2026 developed a method to reduce nonidentifiability when inferring motor-cortex inputs. Using neural recordings, the authors reported similar encoding of initial and corrective movements after applying the method, addressing a technical problem that can make different latent neural explanations appear equally plausible.
- Significance: This is relevant to neural decoding reliability: more identifiable models could improve decoder interpretation, robustness, and transfer across movement contexts. It supports incremental progress toward higher-confidence BCI control, but does not itself demonstrate a clinical BCI or increased communication bandwidth.

### Randomized pilot study reports exploratory benefits from at-home microtesla magnetic therapy for long COVID cognitive impairment

- Event date: 2026-09-28
- Sources: `S2`, `S3`
- Observed fact: A Brain Communications research article published on September 28, 2026 evaluated at-home Microtesla Magnetic Therapy in 30 adults with cognitive impairment associated with long COVID. The study reported that the intervention was feasible, safe, and well tolerated; exploratory outcomes favored active treatment over sham for working memory, verbal learning, processing speed, and emotional well-being, with the largest differences at follow-up.
- Significance: The study is a concrete example of non-invasive neurostimulation moving toward home use and targeting cognition and affect rather than only motor symptoms. If replicated, this type of intervention could make neurostimulation more accessible while also raising questions about monitoring, consent, and the governance of AI- or device-mediated mood and cognitive modulation.

### High-density electrocorticography decodes imagined speech with performance near overt speech

- Event date: 2026-09-29
- Sources: `S4`
- Observed fact: A Nature Neuroscience study published on September 29, 2026 used high-density electrocorticography from nine participants undergoing awake brain surgery. The authors reported robust articulatory-kinematic encoding across imagined and overt speech, shared frontoparietal planning signals, modality-specific sensorimotor populations, and a generalized decoder with median prediction accuracy of 80.4% for speech imagery versus 78.3% for speech articulation, against a reported chance level of 16.7%.
- Significance: This is a material neural-decoding result because it measures internally generated speech-related activity rather than only overt movement. It strengthens the technical basis for communication BCIs that could operate without audible articulation and is directly relevant to the possibility of richer neural communication with AI systems.

### Human hippocampal populations encode semantic information in context-sensitive distributed patterns

- Event date: 2026-09-30
- Sources: `S5`
- Observed fact: A Nature Neuroscience study published on September 30, 2026 recorded hippocampal neuronal responses while people listened to narrative speech. The study reported robust semantic encoding after controlling for phonemics and grammar; neural population distances correlated with semantic distances, and the neural patterns showed alignment with GPT-2 embeddings and LLM-derived measures of polysemy.
- Significance: The result expands the measurable neural content available for decoding beyond simple motor commands or phonetic features. It is relevant to future semantic BCIs and brain-AI interfaces because it suggests that distributed neural activity contains context-sensitive information about word meaning. It also increases the importance of mental privacy and limits on secondary use of neural data.

### FDA clears Ceribell software for longitudinal EEG trending and amplitude-integrated EEG analysis

- Event date: 2026-09-30
- Sources: `S6`
- Observed fact: Ceribell announced on September 30, 2026 that the FDA had cleared new software for its EEG platform through a 510(k) pathway. The cleared functions include Alpha-Delta Ratio and Relative Alpha trending, burst-suppression monitoring, and amplitude-integrated EEG. The company stated that the features are intended to support bedside interpretation across neonatal and adult care settings and are expected to be delivered through an automatic software update in the first half of 2027.
- Significance: This is a regulatory and deployment signal for algorithm-assisted neural monitoring rather than a breakthrough BCI. It shows neural-signal interpretation moving into broader clinical workflows, where automated summaries can influence sedation, seizure, cerebral-perfusion, and neonatal-care decisions. That increases the importance of auditability, validation across populations, and clear separation between measured EEG trends and clinical inference.

### A leading long-term BCI demonstration remains a single-participant, research-grade system with substantial setup and infrastructure requirements

- Event date: 2026-06-15
- Sources: `S7`
- Observed fact: A Nature Medicine study published June 15, 2026 reported nearly two years of home use by one man with ALS, totaling more than 3,800 hours and more than 183,000 decoded sentences. However, the system used four implanted 64-electrode arrays connected through percutaneous wired connections; care partners still performed daily setup and initialization; the home installation consisted of networked research computers mounted on a mobile cart; and the system relied on eye gaze in addition to neural decoding for interface control.
- Significance: This is important counterevidence to claims that high-bandwidth implanted BCIs are already broadly deployable. The result demonstrates unusually strong performance for one participant, but the implementation still depends on invasive hardware, trained caregivers, specialized equipment, and a tightly supported clinical-research context. It does not establish scalable deployment across patients, autonomous operation without caregivers, wireless portability, or durable performance across diverse neurological conditions.

### Neural-decoding performance remains vulnerable to recording variability and external-validation failure

- Event date: 2026
- Sources: `S8`, `S9`
- Observed fact: A 2026 Nature Methods perspective stated that poor generalizability continues to hinder the mapping of brain activity to behavior and that predictive models often fail external validation when tested on independent datasets. It identified dataset shift, inadequate statistical power, data leakage, and training-data manipulation as threats to replicability. Earlier primary BCI research likewise found that conventional decoders trained on stale data could fail completely or become unusable on some test days: one decoder failed in 4 of 6 sessions for one monkey and 6 of 6 sessions for another.
- Significance: These findings challenge optimistic interpretations of high within-dataset or within-session decoding accuracy. A decoder that performs well under controlled training conditions may not generalize across people, recording sessions, electrode states, laboratories, or long-term physiological changes. This directly narrows claims about durable, high-bandwidth neural communication and raises the evidentiary bar for independent replication and cross-subject deployment.

### Adaptive assistance can alter the neural representations it is supposed to decode

- Event date: 2026-09-15
- Sources: `S10`
- Observed fact: A Nature Communications study published September 15, 2026 analyzed monkeys practicing a motor BCI with adaptive decoders. Over time, task-relevant information became concentrated in fewer neurons and in a small number of neural modes. The authors concluded that assistive decoders can manipulate error information used for long-term learning and may directly contribute to forming altered neural representations.
- Significance: This is a counterexample to the assumption that AI assistance simply improves BCI performance without changing the underlying biological signal. Closed-loop systems may create feedback effects in which the decoder changes what the user’s brain learns to represent, potentially reducing transferability, complicating calibration, and creating new safety and interpretability problems. It is especially relevant to two-way brain-AI systems in which the algorithm is both reading and shaping neural behavior.

### Neurostimulation hardware failures can produce serious injury, loss of therapy, and explant or replacement procedures

- Event date: 2026-06-17
- Sources: `S11`, `S12`
- Observed fact: The U.S. FDA reported in 2026 that Boston Scientific’s Infinion CX spinal-cord-stimulator lead could experience mechanical stress, high impedance, lead fracture, inadequate stimulation, and possible explant or replacement. As of May 27, 2026, the manufacturer had reported 1,081 serious injuries and no deaths associated with the issue. A separate FDA Class 2 recall for Vercise deep-brain-stimulation systems stated that wire breaks in rechargeable implantable pulse generators could prevent successful stimulation, cause undesired sensations, produce loss of therapy or return of symptoms, and require device removal or replacement.
- Significance: These incidents are not BCI-specific, but they are directly relevant to the broader assumption that chronic neural interfaces can be made safe and durable at scale. They show that implanted stimulation systems remain vulnerable to mechanical and electrical failure even in established therapeutic markets. For future bidirectional BCIs, similar failures could affect not only loss of function but also unintended stimulation, data integrity, neural privacy, and emergency explant decisions.

### A within-window temporal-interference stimulation result was validated in a human cadaver, not in a living person

- Event date: 2026-09-26
- Sources: `S13`
- Observed fact: A study listed on September 26, 2026 investigated focal and steerable temporal-interference stimulation of the left posterior insula using intracranial recordings in a human cadaver. The study described the insula as a difficult deep target for conventional non-invasive stimulation and presented the work as a proof-of-concept validation.
- Significance: This illustrates a recurring translational gap in neurostimulation: anatomical targeting and electric-field feasibility do not establish efficacy, tolerability, or safety in living humans. Cadaver validation cannot measure induced perceptual changes, seizures, heating, unintended network effects, behavioral outcomes, or repeated-use risks. It therefore does not support claims of reliable control over mood, reward, interoception, or immersive affective states.

### A September 26, 2026 DBS programming study found mixed outcomes and explicitly called for larger, longer, multicenter validation

- Event date: 2026-09-26
- Sources: `S14`
- Observed fact: A prospective study published September 26, 2026 evaluated image-guided programming in 30 Parkinson’s disease patients with chronic subthalamic DBS. Of the 20 patients with configuration mismatches between conventional and image-guided programming, 11 improved, 4 showed no change, and 3 worsened after one month. The authors stated that the study had a relatively small, highly selected, single-center cohort and that longer follow-up and larger multicenter prospective studies were needed.
- Significance: This is counterevidence to broad claims that increasingly precise software-controlled stimulation reliably produces better outcomes. Even in an established therapeutic indication, the intervention helped some patients, did not help others, and worsened outcomes in a minority. The short follow-up and selection constraints leave open questions about durability, adverse effects, reproducibility, and whether improved motor control generalizes to mood, cognition, reward, or other engineered mental states.

### Ethical and data-governance frameworks remain behind the technical capabilities of implantable BCIs

- Event date: 2026-09-07
- Sources: `S15`, `S16`
- Observed fact: A Nature Neuroscience commentary published September 7, 2026 argued that ethical clarity must keep pace with expanding human BCI implantation and called for a distinction between research participation and patient care, long-term support for study participants, protection against disproportionate research burdens, and meaningful clinical purpose. A separate Communications Medicine review published July 27, 2026 argued that existing privacy protections such as HIPAA and GDPR are insufficient for clinical implantable BCI data and that common neurodata standards were designed for retrospective research datasets rather than real-time systems containing decoder parameters, closed-loop control signals, and device timing metadata.
- Significance: The evidence narrows the claim that neuro-rights can be handled by ordinary medical privacy law or conventional research ethics. As neural interfaces become more capable of inferring speech, semantic content, or behavioral intent, unresolved issues include data portability, secondary use, long-term participant support, ownership of decoder-generated inferences, cybersecurity, and consent for adaptive closed-loop systems. The governance problem is therefore not hypothetical, but neither is it solved by existing general-purpose frameworks.

### The evidence base does not support reliable AI-mediated control of mood, reward, or immersive affective experience

- Event date: 2026-09-24 through 2026-10-01
- Sources: `S13`, `S14`
- Observed fact: The searched evidence included motor decoding, imagined or overt speech decoding, semantic representation studies, Parkinson’s motor stimulation, and exploratory non-invasive stimulation, but no authoritative within-window human study demonstrating reliable, repeatable, AI-mediated control of mood, reward, emotional experience, or immersive affective states. The strongest within-window stimulation evidence involved motor outcomes, a small pilot, or cadaver-level proof of concept.
- Significance: This is a direct constraint on the prediction that engineered mental states will soon become a large-scale governance problem through reliable closed-loop control. Neuro-rights concerns remain important because neural data and stimulation capabilities are advancing, but the current evidence does not yet establish the technical reliability, specificity, or generality required for broad affective-state manipulation. The near-term governance problem may therefore center more on inference, privacy, consent, and institutional power than on precise emotional engineering.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S4`, `S5`, `S7`, `S8`, `S9`, `S10`, `S11`, `S12`
- Evidence: Evidence strengthens the decoding side of the claim: high-density ECoG decoded imagined speech near overt-speech performance, hippocampal recordings showed context-sensitive semantic information, and improved modeling addressed a motor-decoding identifiability problem (S1, S4, S5). However, long-term deployment remains a single-participant, research-grade demonstration dependent on percutaneous wired hardware, caregiver setup, specialized infrastructure, and eye gaze (S7). External-validation failures, neural variability, adaptive-decoder effects, and implant or stimulation hardware failures continue to constrain reliability, durability, safety, and scalability (S8, S9, S10, S11, S12). No authoritative evidence in the supplied record establishes a chronic, fully implanted, wireless, bidirectional human interface with durable sensory or emotional feedback.
- Real-world implication: Neural interfaces are making measurable progress toward speech and semantic communication, but current evidence supports incremental clinical and research applications rather than safe, scalable, rich two-way communication with AI. Validation across users, sessions, hardware, and long-term conditions remains the main bottleneck, alongside privacy, maintenance, caregiver, and hardware-safety requirements.
- PostSingularity implication: A post-singularity setting can plausibly treat high-bandwidth neural-AI communication as an achieved capability, but it should preserve deployment constraints as meaningful sources of inequality, dependence, failure, privacy risk, and institutional control. Sensory or emotional exchange requires additional evidence beyond present speech and semantic decoding results.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **mixed**
- Confidence: **medium**
- Sources: `S2`, `S3`, `S4`, `S5`, `S13`, `S14`, `S15`, `S16`
- Evidence: The supplied evidence supports an emerging governance problem around neural inference, consent, privacy, adaptive feedback, and institutional power. Imagined-speech and semantic-decoding results expand the content that may become inferable, while ethical and data-governance analyses identify gaps in current protections for real-time implantable BCI data (S4, S5, S15, S16). A home-use magnetic-stimulation pilot and a mixed-outcome DBS programming study show movement toward accessible or software-guided modulation, but the evidence remains preliminary (S2, S3, S14). Direct evidence for reliable AI-mediated control of mood, reward, emotional valence, or immersive affective experience is absent; cadaver-level stimulation evidence does not establish living-human control (S13).
- Real-world implication: Governance concerns are already justified for neural data, consent, secondary use, closed-loop adaptation, and long-term participant support, even though precise emotional-state engineering is not demonstrated. Near-term policy is more likely to address inference, privacy, device accountability, and clinical boundaries than widespread reliable mood or reward control.
- PostSingularity implication: In a post-singularity world, engineered mental states could become a major governance issue if technical reliability improves, but the supplied evidence does not warrant treating that outcome as established. The storyworld should distinguish reliable affective control from the earlier and better-supported problems of neural privacy, dependency, consent, and algorithmic influence.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S6`, `S8`, `S9`, `S10`, `S15`, `S16`
- Evidence: The evidence shows neural-signal interpretation entering clinical workflows through FDA-cleared EEG-trending software, while also emphasizing the need for auditability, validation across populations, and separation of measured signals from clinical inference (S6). Broader evidence of external-validation failure, dataset shift, decoder instability, adaptive systems changing the signals they interpret, and unresolved implantable-BCI data protections further supports demand for provenance and oversight (S8, S9, S10, S15, S16). However, the supplied record does not establish broad public adoption of provenance systems, binding AI transparency rules, or completed audit regimes.
- Real-world implication: As AI-mediated interpretation affects clinical and other high-impact decisions, pressure for traceable inputs, model validation, audit trails, disclosure, and graduated oversight is increasing. The immediate evidence supports a governance need and deployment direction, not a completed societal consensus or universal provenance infrastructure.
- PostSingularity implication: A post-singularity society would plausibly make provenance and inspectability central rituals for deciding whether an AI-generated claim, action, or neural inference is trusted. These systems should be treated as contested institutions with failure modes and power asymmetries, not as automatic guarantees of truth.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: The supplied evidence is concentrated on neural decoding, neurostimulation, implant safety, and AI governance. It contains no authoritative evidence on launch economics, propulsion, closed-loop life support, in-space manufacturing, station duration, autonomous mission operations, or sustained human off-world communities.
- Real-world implication: No directional update can be made from this evidence packet about whether AI and abundant energy will enable sustained off-world settlement. The assumption remains dependent on aerospace and life-support evidence not present here.
- PostSingularity implication: The post-singularity implication remains open. Off-world settlement should not be inferred from the demonstrated neural and AI developments in this packet; it requires separate evidence concerning transportation, habitat reliability, human health, energy availability, and autonomous industrial support.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: `S15`, `S16`
- Evidence: The supplied evidence does not report device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, intergenerational cultural behavior, or measurable resistance to pervasive AI and neural integration. Ethical and privacy concerns around BCIs (S15, S16) indicate potential reasons for resistance, but they do not establish persistence or revival of analog practices.
- Real-world implication: The claim cannot be directionally assessed from the audited evidence. Privacy and consent concerns may create conditions for low-tech or private practices, but no supplied source demonstrates that such practices are growing or persisting across generations.
- PostSingularity implication: A post-singularity setting may include analog practices as a counterweight to integration, but that is currently a worldbuilding extrapolation rather than an evidence-backed update. Their prevalence, social status, and relation to agency remain unresolved.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S4`, `S5`, `S7`, `S8`, `S9`, `S10`, `S11`, `S12`
- Why this location: The evidence supports stronger neural decoding for imagined speech, semantic information, and motor modeling, but it does not support treating rich two-way neural-AI communication as universally reliable or broadly deployable. Long-term use remains invasive, caregiver-dependent, infrastructure-heavy, and vulnerable to validation, adaptation, and hardware failures.
- Proposed change: Retain the existing claims that neural links enable direct nervous-system communication and shared realities, but add an explicit qualification that high-bandwidth communication depends on user-specific calibration, stable recordings, validated models, and functioning hardware. State that performance may vary across users, sessions, devices, and physiological changes; that current analogues remain dependent on invasive or specialized infrastructure; and that durable sensory or emotional exchange requires capabilities beyond demonstrated speech and semantic decoding.
- Implementation steps:
  1. Insert the qualification immediately after the existing Summary description of direct nervous-system communication, using this heading as the anchor.
  2. Distinguish demonstrated or plausible decoded speech and semantic exchange from the stronger claim of continuous, private-thought, sensory, or emotional communication.
  3. Cross-reference the existing Function section for consent and interface behavior, and the Philosophical Tensions section for privacy, dependency, unequal access, and failure consequences.
  4. Review terminology against PS-NEURO-002 so that neural links do not imply reliable mood, reward, or immersive-affect control without separate canon support.
- Dependencies or conflicts:
  - The existing Summary calls neural links safe and deeply personalized; this should be reconciled with documented implant, stimulation, and decoder failure risks without eliminating the storyworld capability.
  - The existing Function claim that links can shift identity, memory weight, or sensory input is stronger than the supplied evidence for real-world technology and should be framed as post-singularity canon or a distinct advanced capability rather than as an evidence-backed near-term extrapolation.
  - The existing Story Use material presents malfunction as a plot device; the new reliability constraints should make malfunction, recalibration, caregiver dependence, and unequal access internally consistent rather than exceptional anomalies.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **debate**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-002`
- Sources: `S2`, `S3`, `S4`, `S5`, `S13`, `S14`, `S15`, `S16`
- Why this location: The evidence strengthens concerns about neural inference, consent, secondary use, adaptive feedback, and institutional power. It does not establish reliable human control of mood, reward, emotional valence, or immersive affective states; the cadaver study and preliminary stimulation results are insufficient for that claim.
- Proposed change: Add a distinction to the philosophical debate: near-term governance concerns arise from the ability to infer speech, semantic content, and behavioral or clinical signals, and from systems that adapt to or shape neural representations. Separately label precise AI-mediated control of bliss, mood, reward, or immersive affect as contested, unproven, and dependent on future validation, consent safeguards, and long-term safety evidence.
- Implementation steps:
  1. Place the distinction at the end of the existing Philosophical Tensions section, after the questions about effort, pain, and social cohesion.
  2. Add a debate point contrasting established or emerging neural-data risks with the unverified premise that emotional states can be reliably engineered at scale.
  3. Cross-reference neural-links.md for communication and sensory-interface constraints, and trust-fabrics.md for provenance, oversight, and audit requirements.
  4. Review the Summary and Function sections afterward so that Emotional Integrity Contracts and Memory Threads govern both voluntary bliss participation and the handling of inferred or algorithmically influenced mental states.
- Dependencies or conflicts:
  - The existing Summary describes perpetual AI-mediated joy as an available option; the new distinction must clarify whether that is established post-singularity canon, a future capability, or a deliberately contested social belief.
  - The existing Function states that bliss exits are regulated and recorded; this may conflict with the privacy and consent concerns in S15 and S16 unless the record specifies who can access Memory Threads, how inferred states are handled, and whether consent covers adaptive systems.
  - The storyworld should avoid implying that the supplied evidence establishes reliable affective control; emotional engineering can remain a major fictional development, but it should be marked as a later or disputed capability.

### `worldbible/technologies/trust-fabrics.md` -> 🛡 Oversight Systems

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **supports**
- Assumptions: `PS-AI-003`
- Sources: `S6`, `S8`, `S9`, `S10`, `S15`, `S16`
- Why this location: FDA-cleared EEG-trending software and broader evidence on validation failure, neural variability, adaptive decoder effects, and implantable-BCI data gaps strengthen the canon premise that influential AI systems require inspectability and oversight. The evidence supports the need for these systems, but not the claim that existing audits guarantee truth or universal safety.
- Proposed change: Expand the Oversight Systems subsection with a requirement that high-impact neural and clinical AI systems disclose validation scope, dataset or population limitations, model and decoder version history, adaptive changes, uncertainty, and separation between measured neural trends and clinical or behavioral inference. Add that Third-Mind Panels review failures, drift, and deployment context rather than merely refining emotional clarity.
- Implementation steps:
  1. Add the new oversight requirements directly beneath the existing Third-Mind Panels, Shadow Protocols, and Resonance Drift Alerts bullets.
  2. Extend Resonance Drift Alerts to include dataset shift, cross-session performance loss, unvalidated population transfer, and changes caused by closed-loop assistance.
  3. Cross-reference the existing Verification Layers subsection so provenance trails include decoder parameters, device timing, model updates, and the distinction between raw signals, derived inferences, and decisions.
  4. Review AI Trust after this edit to ensure its public rituals describe contested review and calibrated confidence rather than automatic validation.
- Dependencies or conflicts:
  - The existing Summary says trust fabrics ensure actions align with cultural resonance and human meaning; the new language should avoid implying that transparency alone ensures correctness.
  - The existing Verification Layers claim that all decision-making logic is viewable may conflict with practical limits around proprietary models, real-time implant data, and privacy-sensitive neural records; the canon should define what is inspectable, by whom, and under what consent conditions.
  - The existing Resonance Drift Alerts currently imply that an AI can re-align after behavioral deviation; adaptive decoders may change the neural representations they interpret, so oversight must monitor the human-system feedback loop as well as the AI output.
  - The Ceribell evidence concerns clinical monitoring software rather than a general AI governance regime; it should be used as the rationale for stricter provenance and validation practices, not as proof that the storyworld’s oversight institutions already exist everywhere.

### `philosophy/ai-trust.md` -> Function

- Priority: **low**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-AI-003`
- Sources: `S6`, `S8`, `S9`, `S10`, `S15`, `S16`
- Why this location: AI Trust already establishes cross-checks, public logs, and community review. The audited evidence extends that framework by showing that neural and clinical systems require evidence about generalization, uncertainty, adaptation, and data governance in addition to visible decision records.
- Proposed change: Add a sentence or short paragraph stating that trust logs record the evidence boundary of an AI claim: training and validation populations, independent-validation status, model or decoder version, adaptive changes, uncertainty, and whether an output is a measurement, an inference, or a recommendation. State that public review can expose limitations but cannot convert a poorly generalizing system into a reliable one.
- Implementation steps:
  1. Insert the addition after the existing Function description of open-thread review and comparison with Trust Fabric protocols.
  2. Link the new language to Trust Fabrics for implementation details and to neural-links.md for neural-interface-specific consequences.
  3. Preserve the existing cultural practices while adding a norm that users may challenge unsupported transfer from one population, session, or device to another.
  4. Have the reviewer reconcile this terminology with the Verification Layers and Oversight Systems headings before approving related edits.
- Dependencies or conflicts:
  - The existing Cultural Effects section says families teach children to read trust logs; the new evidence-boundary concept may require deciding whether ordinary citizens can inspect technical validation records or rely on specialized Third-Mind Panels.
  - The existing claim that agents publicly log emotional cues raises neural-privacy questions under S15 and S16; the canon should distinguish consented emotional metadata from raw neural data and decoder-generated inferences.
  - This file describes cultural reasons for trusting AI, while Trust Fabrics describes operational controls; terminology for logs, provenance, validation, and review should remain consistent across both files.

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

- The evidence window and publication dates are future-dated relative to ordinary current-world verification, so the assessment relies on the supplied audited record rather than independent source checking.
- No authoritative within-window evidence establishes a chronic, fully implanted, wireless, bidirectional human BCI with durable sensory feedback at scale.
- The strongest imagined-speech and semantic-decoding results lack independent multi-site replication and long-term everyday-use validation in the supplied record.
- The long-term home-use BCI result is from one participant and remains dependent on invasive wired hardware, caregiver support, specialized infrastructure, and eye-gaze control.
- The supplied evidence does not establish population-level rates for implant maintenance, infection, explant, hardware failure, or caregiver burden.
- The microtesla therapy study was a small pilot in a specific long-COVID population, and its exploratory outcomes do not establish general cognitive enhancement or reliable affective control.
- No authoritative human evidence in the packet demonstrates reliable AI-mediated control of mood, reward, emotional valence, or immersive affective experience.
- The Ceribell source establishes FDA clearance but not independent validation, clinical outcome benefit, reimbursement, adoption, or long-term effectiveness.
- No binding federal neuro-rights law or comprehensive international neuro-rights regime was identified in the specified window.
- No evidence was supplied for aerospace economics, closed-loop habitats, propulsion, off-world manufacturing, or analog cultural practices.
- No direct source-to-source factual contradiction was identified. The evidence instead contains tensions between high-performance demonstrations and deployment constraints: the imagined-speech and semantic studies report strong laboratory decoding, while the long-term BCI, external-validation, and decoder-variability evidence limits generalization to independent users, sessions, and settings.
- The Ceribell announcement reports FDA 510(k) clearance and planned software delivery, whereas the available evidence does not establish real-world adoption, reimbursement, prospective clinical outcomes, or independent validation of the newly cleared features.
- The long-term home-use BCI demonstrates sustained performance in one participant, but its percutaneous wired hardware, caregiver setup, research infrastructure, and eye-gaze component conflict with any broader claim that comparable systems are already scalable, autonomous, wireless, or generally deployable.
- The imagined-speech and semantic studies provide human neural-recording evidence, but they do not contradict the counterevidence that no independent multi-site replication or durable chronic-device deployment evidence was found within the window.
- The microtesla magnetic-therapy pilot reported exploratory benefits, while the counterevidence emphasizes that small, selected, short-duration studies do not establish general cognitive enhancement or reliable affective control.
- The DBS programming study found improvement in some patients, no change in others, and worsening in a minority; this conflicts with any claim that increasingly precise software-controlled stimulation reliably improves outcomes for all patients.
- The cadaver temporal-interference study demonstrates anatomical and biophysical proof of concept only; it does not conflict with, and cannot be used to establish, living-human efficacy or safety.
- The first packet concerns September 24 through October 1, 2026; several counterevidence sources fall outside that window and are retained because they directly qualify claims made about deployment, reliability, hardware durability, and governance.
- The Nature Communications motor-cortex study concerns motor-cortex modeling rather than a deployed human BCI.
- The result addresses inference ambiguity, not implant longevity, channel count, or end-user performance.
- The source record does not establish whether the method generalizes across patients, recording technologies, or long-term use.
- The sample size was small: 30 adults.
- The study was a pilot, so efficacy estimates are preliminary.
- The reported outcomes were exploratory and require larger, independently replicated trials.
- The evidence concerns a specific long-COVID population and does not establish general cognitive enhancement or reliable mood control.
- The recordings were temporary intraoperative ECoG recordings, not chronic implants.
- Participants were neurosurgical patients undergoing awake language mapping, not people using an assistive BCI in daily life.
- The task involved syllable imagery and articulatory trajectories rather than unrestricted inner speech or continuous conversation.
- The study does not demonstrate long-term stability, privacy protection, or reliable decoding of spontaneous thoughts.
- The study measured semantic representations during language listening rather than decoding a person's private, self-generated thoughts.
- The findings do not show that a practical device can reconstruct arbitrary meaning in real time.
- The comparison with GPT-2 embeddings is an analytical correspondence, not evidence that brains and language models implement the same mechanism.
- The source record does not establish performance in unconstrained communication or across individuals.
- The source is a company announcement about FDA clearance, not an independent clinical-outcomes study.
- The clearance concerns monitoring and interpretation software, not neural stimulation or communication control.
- The announcement does not provide detailed sensitivity, specificity, calibration, subgroup, or prospective outcome data for the newly cleared features.
- The company stated that deployment through an automatic software update was planned for the first half of 2027, so real-world adoption had not yet been demonstrated in the announcement.
- The study is a major positive result rather than a failed trial, so its constraints should not be interpreted as evidence that the technology cannot work.
- The participant achieved sustained use and high prompted-word accuracy, which narrows rather than eliminates the deployment objection.
- The source does not provide a population-level estimate of installation cost, maintenance burden, or failure rate.
- The study used a percutaneous wired interface rather than a fully implanted wireless system.
- The Nature Methods article is a perspective about neuroimaging predictive models broadly, not a new randomized BCI trial.
- The older BCI experiment used monkeys and an earlier generation of decoders, so its exact failure rates may not apply to current human systems.
- Some modern adaptive decoders may substantially reduce the instability described in earlier work.
- The sources do not provide a standardized current benchmark covering all major invasive and non-invasive BCI platforms.
- The experiment used monkeys rather than human patients.
- The study examined motor BCI learning, not speech, affect, sensory feedback, or clinical neurostimulation.
- The observed representational changes may sometimes be beneficial rather than harmful.
- The study does not establish that adaptive assistance causes clinically significant degradation in deployed systems.
- The Infinion CX device is a spinal-cord stimulator rather than a cortical BCI.
- The Vercise recall concerned a component and labeling issue in a deep-brain-stimulation system, not evidence that all DBS systems fail at the same rate.
- The FDA figures are manufacturer-reported serious injuries and do not establish a population-wide incidence rate.
- These recalls do not prove that newer BCI hardware will have equivalent failure modes.
- The source is a visual research listing rather than a full peer-reviewed article page with complete methods and outcome data.
- Cadaver experiments can provide useful anatomical and biophysical evidence, but they cannot evaluate clinical efficacy or living-brain responses.
- The finding concerns one stimulation technique and one target, not all forms of non-invasive neurostimulation.
- The publication date and indexing details should be independently checked against the final journal record.
- The study concerns Parkinson’s motor symptoms, not affective or cognitive state control.
- The sample was small and came from one center.
- Only 18 patients were included in the outcome analysis after the configuration-mismatch selection process.
- The study compared programming strategies rather than testing a new neural interface architecture.
- The one-month follow-up cannot establish long-term benefit or safety.
- The Nature Neuroscience source is a commentary rather than empirical outcome research.
- The Communications Medicine source is a review and policy analysis, not a binding legal determination.
- The sources identify governance deficiencies but do not establish that widespread commercial misuse has already occurred.
- The cited frameworks and laws differ across jurisdictions, so the conclusions are not uniform globally.
- Absence of evidence in the searched window is not evidence that no unindexed or proprietary work exists.
- Some therapeutic DBS and psychiatric neuromodulation studies may address mood or affect but were not sufficient here to establish reliable AI-mediated control.
- The search was constrained to the specified priority window and publicly accessible authoritative sources.
- Future closed-loop systems could improve rapidly through proprietary trials or unpublished engineering work.
- No authoritative source found within the priority window documenting a new FDA authorization or peer-reviewed human result for a chronic, bidirectional implanted BCI with durable sensory feedback.
- No verified primary evidence found within the window for a major increase in implant channel count, long-term implant safety, or independent at-home use comparable to thousands of hours.
- No authoritative neuro-rights law, regulation, standard, or binding policy action published between September 24 and October 1, 2026 was identified. The search did find relevant neuro-AI governance activity dated September 8, 2026, outside the specified window.
- No strong within-window evidence was found for reliable AI-mediated control of mood, reward, or immersive affective states in humans.
- The search did not verify the reported September 29, 2026 first-in-human Paradromics wireless BCI implantation through a primary institutional, regulatory, or company source; it was therefore excluded from the findings.
- Several developments in the search results were announcements, conference events, or secondary reports rather than measured clinical or engineering results and were excluded or treated cautiously.
- No authoritative within-window evidence was found for a chronic, fully implanted, wireless, bidirectional human BCI delivering durable sensory feedback at scale.
- No independent multi-site replication was found within the window for the strongest high-bandwidth speech, semantic, or imagined-speech decoding results.
- No public evidence was found for population-level cost, maintenance, explant, infection, or caregiver burdens across current invasive BCI trials.
- No verified within-window dataset was found comparing decoder performance across independent patients, hospitals, implant manufacturers, and recording modalities under common benchmarks.
- No authoritative within-window human evidence was found for reliable AI-mediated control of mood, reward, emotional valence, or immersive affective experience.
- No binding federal neuro-rights law or comprehensive international neuro-rights regime was identified within September 24 through October 1, 2026. The available sources mainly describe policy gaps, ethical recommendations, or jurisdiction-specific protections.
- No strong within-window evidence was found for a failed human replication of the September 29 imagined-speech or September 30 semantic-decoding studies; the main counterevidence remains methodological, translational, and deployment-oriented.
- No authoritative evidence was found establishing real-world adoption, reimbursement, or long-term clinical outcomes for newly cleared neural-signal interpretation software announced during the window.
- The search did not independently verify several company or secondary reports concerning new first-in-human implantations, wireless BCI milestones, or defense deployments; those claims were excluded from the evidence findings unless supported by primary institutional, regulatory, or peer-reviewed sources.
- The reported September 29, 2026 first-in-human Paradromics wireless BCI implantation was excluded because it was not independently verified through a primary institutional, regulatory, or company source.
- Claims that a chronic, bidirectional implanted BCI with durable sensory feedback was newly authorized or demonstrated at scale within the priority window were excluded.
- Claims of a major increase in implant channel count, long-term implant safety, or independent at-home use comparable to thousands of hours were excluded because no verified primary evidence was found within the window.
- Claims that a new neuro-rights law, regulation, standard, or binding policy action was published between September 24 and October 1, 2026 were excluded because no authoritative within-window source was identified.
- Claims of reliable AI-mediated control of mood, reward, emotional valence, or immersive affective states in humans were excluded.
- Claims that the cadaver temporal-interference study demonstrated living-human efficacy, tolerability, safety, mood control, reward control, interoceptive control, or immersive affective-state control were excluded.
- Claims that the imagined-speech study demonstrated unrestricted inner-speech decoding, continuous conversation, spontaneous-thought decoding, long-term stability, or privacy protection were excluded.
- Claims that the hippocampal semantic study demonstrated reconstruction of arbitrary private thoughts, practical real-time semantic decoding, unconstrained communication, or a shared brain-LLM mechanism were excluded.
- Claims that the microtesla magnetic-therapy pilot established general cognitive enhancement, reliable mood control, or efficacy outside the specific long-COVID population were excluded.
- Claims that FDA clearance of the Ceribell software established independent clinical-outcome benefit, real-world adoption, reimbursement, or long-term clinical effectiveness were excluded.
- Claims that the FDA recalls establish equivalent failure rates or equivalent failure modes for all newer BCI hardware were excluded.
- Claims that adaptive assistance necessarily causes clinically significant degradation in deployed systems were excluded.
- Claims that image-guided DBS programming reliably improves outcomes for all patients or establishes control of mood, cognition, reward, or other engineered mental states were excluded.
- Conference events, announcements, secondary reports, and company or defense claims lacking measured clinical or engineering evidence were excluded or treated cautiously.
- PS-SPACE-001 was assessed as insufficient-evidence with high confidence. No supplied source addresses launch economics, propulsion, life-support closure, in-space manufacturing, autonomous mission operations, or sustained off-world communities, so no repository edit is warranted in aerospace-systems.md or timeline.md from this packet.
- PS-SOCIAL-002 was assessed as insufficient-evidence with high confidence. Sources S15 and S16 identify privacy, consent, and governance gaps but do not establish device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, or intergenerational resistance. No change is proposed to timeline.md or the available cultural or technology files.
- The mixed assessment for PS-NEURO-001 is covered by a qualification rather than a replacement of the Neural Links canon: the evidence supports progress in decoding while challenging assumptions of universal reliability, scalability, durability, and emotional exchange.
- The mixed assessment for PS-NEURO-002 is covered by a targeted debate expansion in The Bliss Divergence: governance risks around inference and consent are actionable, while reliable affective-state control remains unsubstantiated and should not be presented as an evidence-backed update.
- The strengthened assessment for PS-AI-003 is covered by additions to Trust Fabrics and AI Trust. These plans do not claim that public provenance, audit, or transparency systems are already universally adopted; they translate the evidence into contested post-singularity institutions and review practices.

## Watchlist

- Independent replication and cross-subject validation of imagined-speech and semantic neural decoding.
- Chronic fully implanted and wireless BCI demonstrations with durable bidirectional sensory feedback.
- Long-term implant safety, infection, mechanical failure, explant, maintenance, and caregiver-burden data.
- Closed-loop systems that decode and deliberately shape neural representations, including evidence of beneficial or harmful adaptation.
- Human trials of precise affective, reward, or immersive-state modulation with long-term follow-up and meaningful consent safeguards.
- Adoption and independent clinical-outcome data for FDA-cleared neural-signal interpretation software.
- Binding neurodata, neuro-rights, provenance, audit, and disclosure standards for adaptive AI and implantable systems.
- Launch-cost trends, autonomous mission operations, life-support closure, in-space manufacturing, and long-duration human habitat results.
- Device-free spaces, right-to-disconnect rules, analog-media use, and low-technology communities across generations.

## Sources

- `S1` [Combatting nonidentifiability to infer motor cortex inputs yields similar encoding of initial and corrective movements](https://www.nature.com/articles/s41467-026-77911-4) — Nature Communications; 2026-09-25; primary-research; URL supplied in structured research output. Primary research on a methodological bottleneck in neural decoding and motor-cortex modeling.
- `S2` [Microtesla magnetic therapy for cognitive impairment in long COVID: a randomized pilot study](https://academic.oup.com/braincomms/article/8/5/fcag364/) — Brain Communications / Oxford Academic; 2026-09-28; primary-research; URL supplied in structured research output. Primary randomized pilot study of non-invasive magnetic neurostimulation with cognitive and emotional outcomes.
- `S3` [Advance articles listing for Microtesla magnetic therapy study](https://academic.oup.com/BRAINCOMMS/advance-articles) — Brain Communications / Oxford Academic; 2026-09-28; primary-research; URL supplied in structured research output. Official journal listing confirming the publication date, study type, population, and reported findings.
- `S4` [A neural architecture for imagined and overt speech motor dynamics](https://www.nature.com/articles/s41593-026-02456-0) — Nature Neuroscience; 2026-09-29; primary-research; URL supplied in structured research output. Primary human ECoG study reporting quantitative decoding of imagined speech-related motor dynamics.
- `S5` [A population code for semantics in human hippocampus](https://www.nature.com/articles/s41593-026-02436-4) — Nature Neuroscience; 2026-09-30; primary-research; URL supplied in structured research output. Primary human neuronal-recording study on semantic information in the hippocampus and its relationship to language-model embeddings.
- `S6` [Ceribell Receives FDA 510(k) Clearance for Quantitative EEG Trending and Amplitude-Integrated EEG Analysis](https://investors.ceribell.com/news-releases/news-release-details/ceribell-receives-fda-510k-clearance-quantitative-eeg-trending) — Ceribell; 2026-09-30; official-release; URL supplied in structured research output. First-party announcement of a U.S. FDA-cleared neural-signal analysis software update, including the intended functions and planned deployment timing.
- `S7` [Long-term independent use of an intracortical brain–computer interface for speech and cursor control](https://www.nature.com/articles/s41591-026-04414-6) — Nature Medicine; 2026-06-15; primary-research; URL supplied in structured research output. Primary human study documenting both the strongest long-term home-use result and the remaining hardware, caregiver, and infrastructure requirements.
- `S8` [External validation improves generalizability, replicability and reproducibility in predictive models for neuroimaging](https://www.nature.com/articles/s41592-026-03115-9) — Nature Methods; 2026; primary-research; URL supplied in structured research output. Authoritative analysis of external-validation failure, dataset shift, leakage, and generalizability problems in brain-prediction models.
- `S9` [Making brain–machine interfaces robust to future neural variability](https://www.nature.com/articles/ncomms13749) — Nature Communications; 2016-12-06; primary-research; URL supplied in structured research output. Primary BCI experiment documenting decoder failures and intermittent performance under future neural variability.
- `S10` [Assistive algorithms influence neural representations in motor brain-computer interfaces](https://www.nature.com/articles/s41467-026-76109-y) — Nature Communications; 2026-09-15; primary-research; URL supplied in structured research output. Primary experimental evidence that decoder assistance changes the neural representations produced during BCI use.
- `S11` [Spinal Cord Stimulator Recall: Boston Scientific Removes Infinion CX Lead](https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/spinal-cord-stimulator-recall-boston-scientific-removes-infinion-cx-lead) — U.S. Food and Drug Administration; 2026-06-17; regulatory; URL supplied in structured research output. Official FDA recall notice documenting mechanical failure, serious injuries, inadequate stimulation, and possible explant or replacement.
- `S12` [Class 2 Device Recall Vercise Deep Brain Stimulation Systems Surgical Implant Manual](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id=214651) — U.S. Food and Drug Administration; 2025-09-12; regulatory; URL supplied in structured research output. Official recall record documenting wire breaks, loss of therapy, undesired sensation, return of symptoms, and possible device removal or replacement in DBS systems.
- `S13` [Focal and Steerable Temporal Interference Stimulation of the Human Left Posterior Insula: A Proof-of-Concept Validation Using Intracranial Recordings in a Human Cadaver](https://visualize.jove.com/42791922-focal-and-steerable-temporal-interference-stimulation-of-the-human-left-posterior-insula-a-proof-of-concept-validation-using-intracranial-recordings-in-a-human-cadaver) — JoVE Visualize; 2026-09-26; primary-research; URL supplied in structured research output. Within-window proof-of-concept evidence whose cadaver design sharply limits claims about living-human neurostimulation.
- `S14` [Image-guided programming improves motor control in chronic subthalamic nucleus deep brain stimulation in Parkinson's disease: A prospective study](https://journals.sagepub.com/doi/10.1177/1877718X261492273) — Journal of Parkinson’s Disease; 2026-09-26; primary-research; URL supplied in structured research output. Within-window prospective clinical evidence showing mixed individual outcomes, short follow-up, and explicit generalizability limitations in software-guided neurostimulation.
- `S15` [Ethical considerations for implantable human brain–computer interfaces](https://www.nature.com/articles/s41593-026-02447-1) — Nature Neuroscience; 2026-09-07; reputable-secondary; URL supplied in structured research output. Expert ethical analysis of participant support, research-versus-care distinctions, disproportionate risk, and clinical-purpose requirements for implantable BCIs.
- `S16` [Advancing data protections for implantable brain-computer interfaces](https://www.nature.com/articles/s43856-026-01797-y) — Communications Medicine; 2026-07-27; reputable-secondary; URL supplied in structured research output. Review identifying gaps in HIPAA/GDPR protection and the lack of operational data standards for real-time implantable BCI systems.

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
  "id": "research_2026-10-01_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology 2026 Window Review: Decoding Progress, Deployment Limits, and Neuro-Rights Gaps",
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
