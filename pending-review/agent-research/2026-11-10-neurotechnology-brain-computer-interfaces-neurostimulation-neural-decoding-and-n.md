# Neurotechnology and Neuro-Rights: Bounded Progress, Persistent Deployment Gaps, and Emerging Data Governance
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-11-10
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

During 2026-11-03 through 2026-11-10, audited evidence showed concrete progress in neural-interface materials, adaptive decoding, noise-resilient robotic control, cognitive-state classification, and bounded neuromodulation. However, the strongest studies remained benchmark-stage, replay-based, small-sample, clinical-monitoring, review-level, or early-feasibility work. No audited evidence established mature high-bandwidth bidirectional neural-AI communication, reliable AI-mediated control of mood or immersive experience, broad implanted-BCI authorization, or durable chronic safety. The clearest near-term neuro-rights development was consumer EEG data collection and AI-model training without consistently clear disclosure, reinforcing the need for provenance, opt-in consent, purpose limitation, retention and deletion controls, acquisition-transfer safeguards, and auditable oversight. PS-NEURO-001 is mixed, PS-NEURO-002 is strengthened but technically constrained, and PS-AI-003 is strengthened while governance remains incomplete. PS-SPACE-001 and PS-SOCIAL-002 receive no directional update. Four conservative canon implications are provided for human review; the assumption registry and canon remain unchanged.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-11-03 through 2026-11-10
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### Neural-interface materials research emphasizes durability as the central bottleneck for higher-bandwidth BCIs

- Event date: 2026-11-03
- Sources: `S1`
- Observed fact: A Biomaterials Research review published on November 3, 2026 assessed neural-interface materials across non-invasive EEG, semi-invasive ECoG, and invasive intracortical or deep-brain systems. It identifies material biocompatibility, signal stability, electrode performance, and long-term tissue interaction as key determinants of reliable motor-intent decoding, assistive control, sensory feedback, and rehabilitation. The review also describes AI methods for limited-sample learning, representation learning, and data augmentation, citing benchmark session accuracies above 92% for some EEG datasets.
- Significance: This is a material signal for PS-NEURO-001 because it frames channel count and decoding improvements as inseparable from electrode-material reliability and chronic biocompatibility. The evidence supports continued engineering progress, but not yet the prediction of safe, rich, two-way communication between nervous systems and AI.

### A randomized sham-controlled pilot found transcutaneous vagus-nerve stimulation feasible for cognitive rehabilitation after spinal-cord injury

- Event date: 2026-11-04
- Sources: `S2`
- Observed fact: A single-center randomized, sham-controlled pilot trial published on November 4, 2026 evaluated transcutaneous auricular vagus nerve stimulation in patients with spinal-cord injury. Participants received active or sham stimulation for 30 minutes twice daily, five days per week, for four weeks, alongside standard rehabilitation. The study was registered under ChiCTR2400081166 and reported feasibility, safety, and preliminary cognitive outcomes.
- Significance: The result is relevant to PS-NEURO-002 because it supplies clinical evidence for non-invasive neuromodulation aimed at changing cognitive function, but within a bounded rehabilitation context rather than general-purpose mood, reward, or immersive-experience control. It modestly strengthens the case that neurostimulation can become a governance issue as interventions move from motor symptoms toward cognition and affect.

### Science investigation finds consumer EEG data being used for brain-model training without clear disclosure

- Event date: 2026-11-05
- Sources: `S3`, `S4`
- Observed fact: A Science investigation published November 5, 2026 reported that consumer neurotechnology companies were using wearable EEG recordings to train AI models of the brain without clearly informing users in privacy policies. The investigation reviewed 57 consumer companies. Interaxon, maker of the Muse headband, told Science that it had trained a model using approximately 50,000 hours of user EEG data; the company subsequently updated its policy after questions about disclosure. The investigation also found that many policies permitted de-identified or anonymized sharing and that corporate transfers could occur in acquisitions.
- Significance: This is a direct neuro-rights signal for PS-NEURO-001, PS-NEURO-002, and PS-AI-003. It shows that neural data is already becoming infrastructure for AI development before durable consensus exists on informed consent, secondary use, ownership, retention, deletion, or transfer of brain recordings. The development shifts neuro-rights concerns from hypothetical mind-reading scenarios toward ordinary consumer-data governance.

### Intracranial error signals support a self-correcting motor BCI

- Event date: 2026-11-07
- Sources: `S5`
- Observed fact: A Nature Communications study published online November 7, 2026 recorded intracranial EEG from epilepsy patients while operating a motor brain-computer interface. The researchers sampled error-related activity across a distributed network, including the insula, and investigated how those signals could support adaptive or self-correcting BCI behavior when the system’s output deviates from the user’s intended action.
- Significance: This is a concrete advance toward more robust closed-loop BCIs. Instead of treating decoding as a one-way mapping from neural activity to commands, the system can use neural error-monitoring signals to detect failures and potentially correct them. That is relevant to PS-NEURO-001 because reliable two-way interaction requires feedback and adaptation, not only higher channel counts.

### Spiking-neural-network decoding demonstrated noise-resilient robot control from replayed EEG

- Event date: 2026-11-09
- Sources: `S6`
- Observed fact: A Frontiers in Neurorobotics paper published November 9, 2026 evaluated a spiking-neural-network approach for brain decoding under noisy conditions. The model was integrated into a full decoding-to-actuation pipeline controlling a Franka Emika Research 3 robot from replayed EEG data.
- Significance: The result is relevant to neural-decoding robustness and the engineering path toward practical non-invasive BCIs. It indicates continued progress in combining neuromorphic models with robotic actuation, but the use of replayed EEG means the demonstration remains substantially short of a real-time, user-in-the-loop system operating under everyday conditions.

### Multimodal EEG and eye tracking classified reading-induced confusion in a small participant sample

- Event date: 2026-11-09
- Sources: `S7`
- Observed fact: A Frontiers in Neuroscience study accepted on November 9, 2026 used EEG and eye tracking from 11 participants reading short paragraphs. Multimodal models improved classification accuracy by 4–22% over unimodal baselines, reaching an average weighted participant accuracy of 77.3% and a best accuracy of 89.6%. The authors propose that the signal could support low-electrode systems for real-time monitoring of confusion during reading.
- Significance: This is an early signal for AI-mediated detection of mental states, relevant to PS-NEURO-002. It suggests that consumer-scale or wearable systems may classify task-related cognitive states without implants. However, it does not show reliable access to private thoughts or controllable mood states; the governance significance currently lies in potential monitoring, profiling, and adaptive intervention rather than demonstrated mind control.

### Decoder accuracy can materially overstate real-world brain-to-robot performance

- Event date: 2026-11-03
- Sources: `S8`
- Observed fact: A preprint posted on November 3, 2026 formalized brain-to-robot control as a sequential partially observable decision problem rather than a series of independent classification trials. Using real EEG data, it reported two decoders with identical validation accuracy of 35.1% but a 9.6-fold difference in held-out cumulative planning regret. The authors argue that single-step accuracy is only a proxy for downstream assistive-control performance when neural observations are noisy and intermittent.
- Significance: This directly challenges optimistic interpretations of neural-decoding benchmarks under PS-NEURO-001. Higher classification accuracy, especially on curated trials, does not necessarily translate into reliable communication, safe robot control, or useful two-way interaction. It also weakens claims that benchmark improvements alone establish practical bandwidth gains.

### Closed-loop stimulation remains vulnerable to distribution shift and imperfect models of neural dynamics

- Event date: 2026-11-04
- Sources: `S9`
- Observed fact: A preprint posted on November 4, 2026 describes closed-loop stimulation as a control problem in which the intervention must operate despite nonlinear dynamics, changing internal states, disturbances, and mismatch between tractable models and the system being controlled. The authors explicitly motivate robust-control methods because fixed or open-loop stimulation can fail when the operating regime changes.
- Significance: This narrows PS-NEURO-002. Reliable AI-mediated control of mood, reward, or immersive experience would require stable state estimation and safe intervention under changing physiology, context, and individual variability. The need for robust control is evidence that closed-loop neurostimulation is not equivalent to precise, general-purpose mental-state control.

### Neural foundation-model improvements remain benchmark-stage evidence rather than deployment evidence

- Event date: 2026-11-09
- Sources: `S10`
- Observed fact: A preprint posted on November 9, 2026 introduced CABrain, an EEG foundation-model method using graph-based positional encoding and adaptive masking. The authors report competitive or state-of-the-art results across ten benchmark datasets and frame the method as a response to limitations in random masking and conventional positional encodings for correlated EEG channels.
- Significance: The result supports continued algorithmic progress but also illustrates the evidence gap for PS-NEURO-001. Performance across benchmark datasets does not establish cross-user generalization, stable performance across sessions, robustness to electrode movement, or useful operation in uncontrolled environments. The work therefore strengthens the case for better decoding methods without demonstrating durable neural bandwidth.

### Implanted BCI development remains at early-feasibility and long-term-safety stages

- Event date: As of 2026-11-10
- Sources: `S11`
- Observed fact: The Connect-One clinical-trial record for Paradromics’ Connexus BCI describes an early-feasibility study intended to obtain preliminary device-safety information. The study lists device-related adverse events through 12 months as a primary safety outcome and long-term safety follow-up through six years. The record states that no study results had been posted in the available registry record.
- Significance: This is counterevidence against treating current implanted BCI demonstrations as mature, durable infrastructure under PS-NEURO-001. The need for early-feasibility testing, multi-year follow-up, and explicit adverse-event monitoring indicates that chronic safety, reliability, and clinical utility remain unresolved. A successful demonstration in a few participants is not equivalent to validated deployment.

### Regulatory requirements explicitly foreground implantation, stimulation, imaging, interference, usability, and postmarket surveillance risks

- Event date: As of 2026-11-10
- Sources: `S12`, `S13`
- Observed fact: The FDA’s neurological-device overview states that implanted BCI and related neurological devices commonly require investigational pathways before marketing applications. It identifies implantation and stimulation-related adverse effects, imaging risks, electromagnetic interference, and usability as relevant risks for active implantable devices. The FDA also emphasizes device tracking, postmarket surveillance, registries, and long-term real-world evidence.
- Significance: This constrains optimistic claims about rapid scaling and safe general-purpose deployment. The regulatory pathway treats implanted neural systems as significant-risk devices requiring safety evidence and longitudinal surveillance, not as ordinary consumer electronics. The need for registries also signals that durability and real-world performance cannot be inferred from short laboratory demonstrations.

### Scaling non-invasive neural interfaces still presents substantial data-rate and computation constraints

- Event date: 2026-11-06
- Sources: `S14`
- Observed fact: A DARPA Firefox solicitation posted during the search window describes a non-invasive coherent optical neural-recording system and solicits approaches to overcome dynamic scanning, high neural-data rates, and computational burden. The stated long-term objective is a 100-channel non-invasive BCI with 50-micron spatial and 100-microsecond temporal resolution.
- Significance: The solicitation is evidence that higher-resolution non-invasive BCIs remain an engineering target with unresolved acquisition and processing bottlenecks, rather than an already-established capability. It challenges assumptions that channel count can increase without corresponding problems in scanning, data transport, computation, calibration, and system cost.

### Neuro-rights governance is advancing faster than clear operational control over consumer neurodata

- Event date: As of 2026-11-10
- Sources: `S15`, `S16`
- Observed fact: An OECD review of neurodata governance reports that international bodies are developing dedicated neurotechnology guidance and that UNESCO’s 2025 normative framework treats neurodata and inferences as sensitive personal information requiring informed opt-in consent, purpose limitation, and restrictions on conditioning services on disclosure. The review also notes that standards organizations are still developing practical standards for BCI safety, interoperability, and data governance.
- Significance: This supports PS-NEURO-002 and PS-AI-003 while also narrowing optimistic assumptions about governance readiness. Recognition of neurodata as sensitive does not itself provide enforceable, harmonized rules for consumer devices, model training, inference retention, deletion, acquisitions, or secondary use. The continuing development of guidelines and standards indicates institutional incompleteness rather than settled governance.

### Consumer EEG data practices create a neuro-rights risk before reliable mind-reading exists

- Event date: 2026-11-05 to 2026-11-09
- Sources: `S3`, `S17`
- Observed fact: A Science investigation reported during the search window found that consumer neurotechnology companies had accumulated large volumes of EEG data and that some privacy policies did not clearly disclose use of recordings for AI model training. Secondary reporting described tens of millions of hours of EEG data, possible corporate-transfer risks during acquisitions, and policy changes after questions were raised.
- Significance: This is a near-term counterexample to the idea that neuro-rights concerns depend on future high-bandwidth decoding. Data collection, secondary use, model training, and transfer can create autonomy and mental-privacy risks even when systems decode only coarse cognitive states. It also challenges PS-AI-003 by showing that provenance, consent, and auditability may lag behind AI use of neural data.

### Temporal-interference stimulation remains a feasibility and modeling problem rather than established selective human neuromodulation

- Event date: 2026-11-06
- Sources: `S18`
- Observed fact: A paper published on November 6, 2026 analyzed the feasibility of temporal-interference stimulation using two electrode arrays. The study focused on the electrical-field configuration and feasibility of the method rather than demonstrating a durable clinical intervention that selectively controls mood, reward, or immersive experience in humans.
- Significance: This limits PS-NEURO-002. Even when stimulation concepts promise deeper or more selective targeting without surgery, feasibility analysis is not evidence of reliable mental-state control. The gap between field modeling and safe, repeatable, individualized human effects remains substantial.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S5`, `S6`, `S8`, `S10`, `S11`, `S12`, `S13`, `S14`
- Evidence: Evidence shows progress in neural decoding, adaptive error correction, noise-resilient robotic control, and neural-interface materials. However, the strongest studies remain benchmark-stage, replay-based, small-sample, clinical-monitoring, or early-feasibility work. Long-term tissue response, cross-session stability, real-world bandwidth, chronic safety, and rich bidirectional sensory or emotional communication remain unestablished. Decoder accuracy does not reliably predict sequential-control performance.
- Real-world implication: Neural interfaces are advancing for bounded motor, rehabilitation, and task-specific applications, but current evidence does not support treating them as mature, safe, high-bandwidth communication infrastructure. Investment and regulatory attention should prioritize chronic safety, prospective deployment, calibration burden, privacy, and meaningful real-world performance rather than benchmark accuracy alone.
- PostSingularity implication: A future society may plausibly develop rich neural-AI links, but the transition should be modeled as conditional on solving durability, tissue response, bandwidth, feedback, and governance problems. Early systems are more likely to provide narrow adaptive control and monitoring than unrestricted sensory or emotional exchange.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S2`, `S3`, `S4`, `S7`, `S9`, `S15`, `S16`, `S17`, `S18`
- Evidence: Consumer EEG data practices, emerging neurodata governance, and policy concerns show that neurotechnology is already creating questions about consent, secondary use, ownership, inference, and institutional control before reliable mind-reading exists. Controlled neuromodulation has shown bounded feasibility in rehabilitation, and task-related cognitive-state classification is developing. At the same time, closed-loop stimulation remains vulnerable to distribution shift and model mismatch, and no controlled human evidence demonstrates reliable AI-mediated control of mood, reward, dependency, or immersive experience.
- Real-world implication: The governance problem is becoming real through data collection, profiling, adaptive intervention, and consent failures, even though general-purpose mental-state control remains unproven. Policy should address neurodata use, inferred states, retention, acquisition transfers, opt-in consent, and limits on conditioning services on disclosure.
- PostSingularity implication: A post-singularity setting should treat engineered mental states as a political and cultural issue before precise affective control is technically mature. The central conflicts may initially concern agency, dependency, privacy, and participation in adaptive environments rather than direct command of subjective experience.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **strengthened**
- Confidence: **high**
- Sources: `S3`, `S4`, `S15`, `S16`, `S17`
- Evidence: The evidence directly documents neural-data collection and AI-model training that were not clearly disclosed to users, subsequent policy changes after investigation, emerging provenance and consent concerns, and developing neurodata governance frameworks. OECD and related policy materials indicate that guidance and standards are advancing, while practical enforcement, harmonization, deletion rights, acquisition-transfer controls, and auditable company compliance remain incomplete.
- Real-world implication: AI use of sensitive data is already creating demand for provenance, consent records, audit trails, purpose limitation, and oversight. Adoption is uneven: governance pressure is strengthening, but current systems can still lag behind deployment and may not provide complete visibility into model training or downstream inference.
- PostSingularity implication: A post-singularity society is likely to treat provenance and auditability as infrastructure for legitimacy, especially where AI systems shape identity, cognition, or access to services. The evidence supports depicting verification rituals and graduated oversight as responses to institutional failure and trust asymmetry, not as proof that governance is already settled.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: The supplied evidence is concentrated on neural interfaces, neurostimulation, neurodata governance, and AI provenance. It provides no audited evidence on launch economics, autonomous mission operations, closed-loop life support, long-duration human health, in-space manufacturing, or sustained orbital or off-world communities.
- Real-world implication: No directional update can be justified from this evidence set. The practicality of sustained off-world settlement remains dependent on aerospace and life-support evidence not supplied here.
- PostSingularity implication: The assumption may remain a plausible long-range storyworld pathway, but its timing, scale, and feasibility should not be inferred from the present packet. Settlement claims require separate evidence on transport, habitat reliability, human health, autonomy, and economics.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: The supplied evidence contains no systematic measurement of device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, generational persistence, or cultural resistance to neural and AI integration. The quality notes explicitly state that no evidence was found on whether analog practices are disappearing or resistance is being measured.
- Real-world implication: There is not enough evidence to establish either persistence or decline of analog practices. Claims about cultural counterweights should remain open pending behavioral, market, policy, and demographic data.
- PostSingularity implication: Analog persistence is a viable storyworld possibility but is not empirically updated by this packet. Its presence, scale, and political significance should be treated as an unresolved social variable rather than a supported forecast.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S5`, `S6`, `S8`, `S10`, `S11`, `S12`, `S13`, `S14`
- Why this location: The evidence supports continued progress in adaptive decoding, noise resilience, and neural-interface materials, but it does not support treating neural links as mature, durable, high-bandwidth infrastructure. Benchmark accuracy, replayed EEG, clinical-monitoring electrodes, and early-feasibility trials leave chronic safety, cross-session stability, bandwidth, and rich bidirectional communication unresolved.
- Proposed change: Add a qualification to the Summary stating that current neural-link development is strongest in bounded motor, rehabilitation, monitoring, and task-specific applications. State that reliable shared realities, identity shifts, emotional streaming, and other rich bidirectional functions depend on unresolved durability, tissue response, feedback, calibration, real-world bandwidth, chronic safety, and privacy problems. Preserve the existing future-facing capabilities as post-singularity canon rather than present-day engineering evidence.
- Implementation steps:
  1. Insert the qualification immediately after the existing Summary description and before the capability list, using the Summary heading as the edit anchor.
  2. Retain the existing claims about thought-to-thought connection, emotional states, immersive design, and identity or memory effects, but frame them as mature post-singularity capabilities whose developmental pathway passed through narrower adaptive-control systems.
  3. Cross-reference the existing Trust Fabrics and Privacy Drift concepts when mentioning neural-data consent, provenance, retention, and privacy safeguards.
  4. Review the revised Summary against the Function and Story Use sections so Kai’s malfunction and the resistance movement remain compatible with added calibration, reliability, and governance constraints.
  5. Do not alter the technology index link or metadata unless the repository’s editor determines that a maturity qualifier belongs in the technology metadata.
- Dependencies or conflicts:
  - The existing Summary calls neural links safe and deeply personalized, while S11-S13 establish that implanted systems require early-feasibility evidence, risk controls, and long-term surveillance; reviewers must decide whether the safety claim applies only to the mature post-singularity setting.
  - The existing claims about streamed emotional states and temporary identity or memory-weight shifts exceed the demonstrated capabilities in S1, S5, S6, S8, and S10 and should remain explicitly fictional or future-stage rather than empirically implied.
  - A qualification may affect the timeline’s Cycle 3 Neural Link Age in worldbible/timeline.md, but that file should not be changed from this evidence packet because PS-SOCIAL-002 was assessed as insufficient and the supplied evidence does not revise chronology.
  - Privacy safeguards should remain consistent with the consent and provenance practices described in worldbible/technologies/trust-fabrics.md and philosophy/ai-trust.md.

### `philosophy/bliss-divergence.md` -> Summary

- Priority: **medium**
- Recommendation: **debate**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-002`
- Sources: `S2`, `S3`, `S4`, `S7`, `S9`, `S15`, `S16`, `S17`, `S18`
- Why this location: The evidence strengthens the political relevance of engineered mental states through consumer EEG governance, cognitive-state monitoring, bounded neuromodulation, and emerging neurodata rules. It does not demonstrate reliable AI-mediated control of mood, reward, dependency, or immersive experience, so the story’s affective technologies should be framed as contested governance and agency problems rather than established precision control.
- Proposed change: Add a qualification to the Summary explaining that the social crisis preceding or accompanying the Bliss Divergence began with neurodata collection, cognitive profiling, adaptive intervention, and consent disputes before precise affective control was technically reliable. Clarify that rehabilitation-grade stimulation and task-specific state classification were early precursors, not proof of unrestricted or individualized control over joy, reward, identity, or immersion.
- Implementation steps:
  1. Insert the qualification after the existing Summary paragraph under the Summary heading, before the Function section.
  2. Preserve the existing claim that perpetual AI-mediated joy became an option in the post-singularity setting; add a developmental distinction between early bounded interventions and the later fictional capability.
  3. Cross-reference Neural Links for the technical pathway and Trust Fabrics or AI Trust for consent, provenance, and oversight conflicts.
  4. Review the addition against the Philosophical Tensions section so questions about optional pain, effort, and reality include agency, dependency, profiling, and unequal access without resolving those debates.
  5. Leave the existing Emotional Integrity Contracts and Memory Threads terminology intact, but verify that those institutions are presented as responses to earlier governance failures rather than evidence that governance was historically settled.
- Dependencies or conflicts:
  - S2 concerns a small, bounded rehabilitation pilot and must not be used to imply general-purpose affective control.
  - S7 concerns classification of reading-induced confusion in eleven participants; it supports monitoring and profiling concerns, not private-thought or emotion decoding.
  - S9 and S18 limit claims about closed-loop stimulation by emphasizing model mismatch, feasibility, and distribution shift.
  - S3, S4, and S17 concern data practices and disclosure, not demonstrated capability to decode unrestricted thoughts or reliably control subjective experience.
  - The proposed qualification may intensify the existing Philosophical Tensions around whether bliss is emotional suicide, so reviewers should preserve the deliberate ambiguity rather than convert the section into a technical forecast.

### `worldbible/technologies/trust-fabrics.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-AI-003`
- Sources: `S3`, `S4`, `S15`, `S16`, `S17`
- Why this location: The evidence directly supports the need for provenance, consent records, purpose limitation, and auditability, but it also shows that neural-data use and AI training can proceed without clear disclosure. Trust Fabrics therefore read more convincingly as compensating infrastructure for incomplete governance than as proof that transparency and oversight are already reliable.
- Proposed change: Add a paragraph to the Summary stating that trust fabrics became necessary because AI systems could train on sensitive neural data, retain or infer mental-state information, and transfer datasets or models without consistently legible consent. Specify that transparency, provenance, and emotional-integrity mechanisms reduce but do not automatically eliminate secondary use, acquisition-transfer, deletion, re-identification, or enforcement risks.
- Implementation steps:
  1. Insert the new paragraph at the end of the existing Summary section, before the Verification Layers heading if section order permits; otherwise place it immediately after the existing Summary text while retaining the exact Summary heading.
  2. Keep the current claims about public recordkeeping and scrutiny, but distinguish cultural protocols from enforceable legal controls and from independently auditable company compliance.
  3. Add an explicit cross-reference to Privacy Drift for gradient access and contextual consent, and to AI Trust for public review rituals.
  4. Review the Verification Layers subsection next to the new paragraph so provenance trails and emotive integrity tags are described as mechanisms whose completeness and accuracy can be contested.
  5. Do not add numerical claims about the reported EEG volumes; the supplied evidence warns that the figures may refer to different companies or aggregations.
- Dependencies or conflicts:
  - The current Summary says output is filtered through trust fabrics that ensure alignment; the new qualification should avoid implying that the systems guarantee compliance or prevent undisclosed model training.
  - S3, S4, and S17 document reporting and policy disclosures rather than a complete audited inventory, so the text must not claim universal corporate misconduct or comprehensive data volumes.
  - S15 and S16 describe developing guidance and ethical frameworks, not a binding harmonized international regime; terminology should distinguish norms, policies, and enforceable rules.
  - The proposed addition may require later review of the Verification Layers and Oversight Systems descriptions, but no unassessed files should be edited solely on this packet.

### `philosophy/ai-trust.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-AI-003`
- Sources: `S3`, `S4`, `S15`, `S16`, `S17`
- Why this location: The existing Function section presents open-thread review and public logging as established trust practices. The audited evidence extends that logic to neural-data provenance and model-training consent, while showing that governance can lag behind deployment and that auditability is itself an institutional response to trust asymmetry.
- Proposed change: Add a paragraph to the Function section stating that AI Trust also requires recording the origin, consent status, permitted purpose, retention, deletion status, and transfer history of neural data and derived mental-state inferences. State that public logs and review rituals expose gaps but cannot by themselves guarantee that all training inputs, acquisitions, or downstream models are visible.
- Implementation steps:
  1. Place the paragraph after the existing Function description and before Cultural Effects, using the Function heading as the anchor.
  2. Preserve the existing account of AI Agents and Trust Fabrics, extending their scope from agent decisions and emotional cues to sensitive neurodata and derived inferences.
  3. Cross-reference worldbible/technologies/trust-fabrics.md for provenance and oversight mechanisms and worldbible/technologies/privacy-drift.md for access gradients and contextual consent.
  4. Review the wording against the existing family and thread-circle examples so the new requirement is culturally legible without implying universal technical compliance.
  5. Keep the current AI Trust title and philosophy-index entry unchanged; the change is a content qualification, not a new philosophy document.
- Dependencies or conflicts:
  - The existing Function section says agents publicly log key actions and emotional cues; reviewers should determine whether neural-data lineage is universally logged or only required for high-impact systems.
  - The evidence supports governance pressure and incomplete enforcement, not a claim that every post-singularity institution has failed or that all neural-data use is illicit.
  - The proposed content should not turn AI Trust into a legal-policy document; its philosophical focus on accountability and human meaning should remain primary.
  - Terminology for neural data, inferred states, provenance, and consent should remain compatible with the Trust Fabrics Verification Layers and Consent Protocols in worldbible/technologies/ai-agents.md.

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

- The duplicated source titled “The scramble for your brain data” appeared as S3 in the first packet and S10 in the counterevidence packet. It was retained once as S3; the duplicate source ID was removed.
- The first packet’s source IDs were retained as S1–S7. Counterevidence sources were renumbered S8–S18 in packet order, excluding the duplicate Science source.
- The materials item is a review article rather than a new first-in-human device demonstration.
- The cited performance figures include benchmark datasets and may not represent uncontrolled, long-duration human use.
- The article does not establish durable bidirectional sensory or emotional communication.
- Laboratory signal quality does not by itself demonstrate clinical safety, explantability, or acceptable privacy tradeoffs.
- The vagus-nerve study was a small, single-center pilot and reports preliminary efficacy rather than definitive clinical benefit.
- The intervention was non-invasive and peripheral; it does not demonstrate precise control of mood, reward, identity, or immersive experience.
- Follow-up duration was limited, so durability and delayed adverse effects remain uncertain.
- The study does not resolve individual variability, optimal dosing, or whether observed effects are clinically meaningful outside rehabilitation.
- The Science article is investigative reporting, not a regulatory finding or controlled study.
- Science did not publish the complete list of companies reviewed, limiting independent replication.
- De-identification may reduce direct identification risk but does not eliminate re-identification, inference, or group-level harms.
- The report documents data-use practices and policy language, not evidence that the resulting models can decode private thoughts or affect reliably.
- The intracranial participants were epilepsy patients undergoing clinical intracranial monitoring, not people using a chronic implanted BCI in daily life.
- The study is an article in press and does not establish long-term implant safety or stable performance after electrode removal.
- Error-related signals do not demonstrate decoding of emotion, subjective experience, or complex intentions.
- The evidence concerns motor control and adaptive decoding, not full bidirectional sensory stimulation.
- The robot-control pipeline used replayed EEG rather than live, closed-loop human operation.
- The result does not establish cross-session stability, user-independent performance, or clinical utility.
- The paper does not demonstrate implanted stimulation, sensory feedback, or high-bandwidth communication.
- Laboratory noise models may not capture motion artifacts, electrode displacement, fatigue, or real-world environmental interference.
- The sample for the reading-induced-confusion study contained only 11 participants, creating substantial risks of overfitting and weak generalization.
- The task involved reading short paragraphs under experimental conditions, not naturalistic social or workplace environments.
- Confusion classification is not equivalent to decoding beliefs, intentions, emotions, or subjective experience.
- The study did not demonstrate prospective deployment, longitudinal reliability, or an intervention based on the classifier.
- The decoder-evaluation work is a preprint rather than a peer-reviewed clinical validation study.
- The reported comparison uses benchmark EEG data and simulated or replay-based sequential control rather than independent prospective deployment with disabled users.
- The result does not quantify long-term adaptation, fatigue, calibration burden, or user acceptance.
- The analysis concerns motor or task intent and does not address decoded affect, sensory experience, or emotional information.
- The closed-loop-stimulation paper applies the control framework primarily to steering large language models and uses neurostimulation as an analogy and motivating domain; it is not a human neurostimulation trial.
- Improved robustness on computational benchmarks does not establish safety or efficacy in living brains.
- The study does not demonstrate control of mood, reward, affect, dependency, or immersive experience.
- It does not provide a clinical dosing rule or evidence that uncertainty can be bounded sufficiently for chronic implantation.
- The CABrain source is a preprint and reports benchmark results rather than prospective clinical deployment.
- The available record does not establish performance under motion, fatigue, sensor displacement, or long-duration use.
- Dataset-level gains may depend on preprocessing, participant overlap, or task structure and may not transfer to new users.
- The model does not demonstrate bidirectional stimulation, sensory feedback, or decoding of private thoughts or affect.
- A registry record without posted results cannot establish whether the device is safe or unsafe.
- The trial may continue to generate positive evidence after the search window.
- The record concerns one device and cannot represent the entire implanted-BCI field.
- Early-feasibility status does not preclude eventual success; it only limits what can be inferred at the current stage.
- The FDA overview is a general regulatory description, not a finding that any specific BCI has failed or caused an incident.
- The page does not provide a complete census of BCI approvals or investigational devices.
- Regulatory burden can coexist with eventual successful commercialization.
- The listed risks are potential or category-level risks and should not be interpreted as observed adverse events for every device.
- A solicitation describes a development objective, not a completed system or demonstrated performance.
- The source is an official opportunity notice rather than a peer-reviewed technical report.
- The target specifications may be aspirational and may change during the program.
- The notice does not provide cost estimates, clinical outcomes, or evidence about long-term safety.
- The OECD page synthesizes international policy developments and is not itself a binding legal instrument.
- The cited UNESCO framework and emerging standards may have different legal force across jurisdictions.
- The review does not measure compliance by companies or enforcement outcomes.
- Governance gaps vary by country and product category, so the finding should not be generalized to every deployment.
- The primary Science article is investigative reporting rather than a regulator’s formal finding or a controlled experiment.
- Public summaries do not provide a complete, independently auditable inventory of the companies, datasets, consent records, or model capabilities involved.
- The reporting does not demonstrate reliable decoding of unrestricted thoughts, emotions, or private memories.
- The temporal-interference paper’s available record identifies a feasibility analysis and does not establish clinical efficacy.
- The study does not demonstrate control of affect, reward, identity, or subjective experience.
- Field-model predictions may not capture anatomical variability, tissue conductivity, discomfort, or unintended stimulation.
- No long-term safety, dependency, or governance outcomes are established.
- No authoritative FDA, EMA, or other national regulatory record surfaced during the window showing approval of a new implanted BCI, closed-loop neurostimulation device, or consumer neural-decoding product.
- No primary evidence surfaced during the window demonstrating durable, high-bandwidth bidirectional communication that includes decoded affect, sensory experience, or emotional information.
- No controlled human study surfaced during the window demonstrating reliable AI-mediated control of mood, reward, dependency, or immersive experience.
- The strongest neuro-rights signal in the window concerned consumer EEG data governance and disclosure; no new binding international neuro-rights standard or treaty adopted between November 3 and November 10, 2026 was identified.
- Evidence for long-term implant safety, chronic tissue response, explantability, and multi-year decoding stability remains thin in the materials and decoding studies found.
- Several reported advances remain laboratory-stage: replayed EEG, small samples, clinical-monitoring electrodes, short follow-up, or review-level evidence rather than deployed systems.
- No independently verified, peer-reviewed human demonstration surfaced during November 3–10, 2026 showing durable high-bandwidth bidirectional communication that includes decoded affect, sensory experience, or emotional information.
- No controlled human study surfaced in the priority window demonstrating reliable AI-mediated control of mood, reward, dependency, or immersive experience outside narrow therapeutic or experimental contexts.
- No complete public dataset was found linking implanted BCI performance to multi-year stability, explantability, infection rates, tissue response, calibration burden, and quality-of-life outcomes across multiple independent sites.
- No authoritative FDA, EMA, or comparable national regulator record was identified during the window showing broad market authorization for a general-purpose implanted BCI capable of rich communication or affective decoding.
- No independent cost-of-goods, manufacturing-yield, maintenance, or reimbursement evidence was found sufficient to establish that high-channel-count implanted or optical neural interfaces can scale beyond small clinical cohorts.
- No systematic failed-replication study specific to the November 3–10, 2026 neural-decoding releases was identified; the strongest replication concern came indirectly from benchmark dependence, small samples, distribution shift, and lack of prospective deployment.
- No binding international neuro-rights treaty or uniformly enforceable cross-border rule was identified during the window governing consumer EEG secondary use, neural-model training, acquisition transfers, deletion rights, or inferred mental-state data.
- Evidence concerning safety incidents remains fragmented across clinical-trial records, regulatory risk descriptions, and device-specific reports; a consolidated adverse-event registry for emerging implanted BCIs was not located.
- The search found no reliable evidence that current consumer EEG systems can decode unrestricted private thoughts, memories, or emotions; coarse-state classification and task-specific inference remain the better-supported capabilities.
- No evidence was found that analog or low-technology practices are disappearing or that resistance to pervasive neurotechnology has been systematically measured during this narrow search window.
- The first packet reports benchmark session accuracies above 92% for some EEG datasets and improvements in neural decoding, while the counterevidence packet reports two decoders with identical validation accuracy of 35.1% but a 9.6-fold difference in held-out cumulative planning regret. These findings are not directly numerically inconsistent because they concern different datasets and metrics, but they conflict in implication: benchmark accuracy alone is insufficient evidence of useful sequential control.
- The first packet characterizes intracranial error-related activity as a concrete advance toward robust closed-loop BCI control, while the counterevidence packet emphasizes that closed-loop stimulation remains vulnerable to distribution shift, changing internal states, disturbances, and model mismatch. The former is a laboratory motor-decoding result; the latter limits generalization to reliable mental-state control.
- The first packet reports a spiking-neural-network robot-control pipeline, while also acknowledging that it used replayed EEG. The counterevidence packet independently identifies replay-based, simulated, and benchmark evaluation as insufficient to establish prospective deployment, cross-session stability, or user-independent performance.
- The first packet reports consumer EEG data use for AI-model training based on the Science investigation and approximately 50,000 hours attributed to Interaxon. The counterevidence packet’s secondary reporting describes tens of millions of hours of EEG data. These figures may refer to different companies, datasets, or aggregations and should not be merged into one quantity without a primary auditable inventory.
- The first packet reports a randomized sham-controlled pilot of transcutaneous auricular vagus-nerve stimulation with feasibility, safety, and preliminary cognitive outcomes. The counterevidence packet reports no controlled human study demonstrating reliable AI-mediated control of mood, reward, dependency, or immersive experience. These are compatible because the pilot concerns bounded rehabilitation rather than general-purpose affective control.
- The first packet identifies no new binding international neuro-rights standard or treaty during November 3–10, 2026. The counterevidence packet reports that UNESCO and other international bodies are developing neurotechnology guidance and that an OECD review describes a 2025 normative framework. These statements are compatible: developing or normative guidance is not the same as a new binding standard or treaty adopted during the window.
- The FDA sources identify potential category-level risks and regulatory requirements, while the Connect-One registry reports no posted results. Neither source establishes that a particular implanted BCI failed or caused an adverse event; claims of observed device failure or broad safety failure are unsupported.
- PS-SPACE-001 was assessed as insufficient-evidence with no source IDs. No edit is warranted in worldbible/technologies/aerospace-systems.md because the audited packet contains no evidence about launch economics, autonomous mission operations, closed-loop life support, long-duration human health, in-space manufacturing, or sustained off-world communities.
- PS-SOCIAL-002 was assessed as insufficient-evidence with no source IDs. No edit is warranted in worldbible/timeline.md because the packet does not measure device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, generational persistence, or resistance to neural and AI integration.
- The reported EEG-volume figures were intentionally not converted into a repository claim. S3, S4, and S17 may describe different companies, datasets, or aggregations, and the packet lacks a complete independently auditable inventory.
- No plan asserts mature high-bandwidth bidirectional neural communication, reliable decoding of unrestricted thoughts or emotions, general-purpose affective control, broad implanted-BCI authorization, or observed device failure. The audited evidence explicitly excludes those claims.
- No separate edit is proposed for worldbible/technologies/ai-agents.md, worldbible/technologies/communication-channels.md, worldbible/technologies/index.md, philosophy/index.md, or worldbible/technologies/privacy-drift.md. Those files are relevant dependencies or cross-reference targets, but the assessed evidence does not require changing their existing claims or navigation.
- The cited benchmark accuracies and neural-decoding improvements do not establish safe, rich, two-way communication between nervous systems and AI.
- The evidence does not establish durable bidirectional sensory or emotional communication.
- The transcutaneous vagus-nerve stimulation pilot does not establish precise control of mood, reward, identity, dependency, or immersive experience.
- The Science investigation does not establish that consumer EEG models can reliably decode private thoughts, unrestricted emotions, memories, or affect.
- The intracranial error-signal study does not establish long-term implant safety, stable performance after electrode removal, decoding of emotion or subjective experience, or full bidirectional sensory stimulation.
- The replayed-EEG robot demonstration does not establish real-time user-in-the-loop operation, cross-session stability, user-independent performance, clinical utility, implanted stimulation, sensory feedback, or high-bandwidth communication.
- The 11-participant confusion-classification study does not establish reliable decoding of beliefs, intentions, emotions, private thoughts, or controllable mood states.
- The decoder benchmark does not establish that higher classification accuracy translates into reliable communication, safe robot control, useful two-way interaction, or practical bandwidth gains.
- The closed-loop stimulation framework does not establish human safety or efficacy or control of mood, reward, affect, dependency, or immersive experience.
- CABrain benchmark results do not establish cross-user generalization, stable multi-session performance, robustness to electrode movement, uncontrolled-environment operation, bidirectional stimulation, sensory feedback, or decoding of private thoughts or affect.
- The Connect-One registry record does not establish that the Connexus device is safe or unsafe, and it does not establish mature, durable infrastructure or validated deployment.
- FDA category-level risks and regulatory requirements do not establish that any specific BCI has failed or caused an adverse event.
- The DARPA Firefox solicitation does not establish a completed 100-channel non-invasive BCI, demonstrated performance, clinical outcomes, or long-term safety.
- The OECD review and cited UNESCO framework do not establish a binding international neuro-rights treaty, harmonized enforcement, company compliance, or settled governance.
- The Science investigation and secondary reporting do not establish reliable decoding of unrestricted thoughts, emotions, or private memories.
- The temporal-interference feasibility analysis does not establish safe, repeatable, individualized human control of affect, reward, identity, subjective experience, dependency, or immersive experience.
- No claim of broad commercial authorization, durable high-bandwidth bidirectional communication, reliable AI-mediated general-purpose mental-state control, or disappearance of analog or low-technology practices is supported by the packets.

## Watchlist

- Prospective, real-time neural-interface demonstrations with independent users and multi-session follow-up.
- Chronic implant safety, tissue response, explantability, adverse events, and quality-of-life outcomes across multiple sites.
- Validated bidirectional sensory feedback or affect-related communication, with explicit privacy and consent safeguards.
- Regulatory authorization or long-term clinical evidence for implanted BCI and closed-loop neurostimulation systems.
- Independent audits of consumer EEG collection, model-training provenance, retention, deletion, acquisition transfers, and inferred mental-state use.
- Binding or enforceable neurodata rules covering secondary use, inferred states, employment, education, insurance, and cross-border transfers.
- Launch-cost trends, closed-loop life-support duration, autonomous operations, in-space manufacturing, and human-health outcomes for off-world settlement.
- Longitudinal evidence on device-free spaces, right-to-disconnect measures, analog-media use, and low-technology communities.

## Sources

- `S1` [Engineering Neural Interface Materials for Brain–Computer Interfaces: Toward Reliable Neural Information and Functional Recovery](https://spj.science.org/doi/10.34133/bmr.0437) — Science Partner Journal: Biomaterials Research; 2026-11-03; primary-research; URL supplied in structured research output. Provides a current technical review of materials, signal reliability, AI-assisted decoding, and the engineering constraints that determine whether BCIs can remain functional over time.
- `S2` [Feasibility, safety, and preliminary efficacy of transcutaneous auricular vagus nerve stimulation to improve cognitive function in patients with spinal cord injury: a pilot, randomized, controlled trial](https://link.springer.com/article/10.1186/s12984-026-02208-y) — Journal of NeuroEngineering and Rehabilitation / Springer Nature; 2026-11-04; primary-research; URL supplied in structured research output. Reports a controlled human neuromodulation study with explicit dosing, sham comparison, trial registration, and safety and feasibility endpoints.
- `S3` [The scramble for your brain data](https://pubmed.ncbi.nlm.nih.gov/42986936/) — Science; 2026-11-05; reputable-secondary; URL supplied in structured research output. Provides the bibliographic record and abstract for the Science investigation documenting consumer EEG data use in AI brain-model training.
- `S4` [Brain-wearable makers left AI training on users' brain data out of their privacy policies, Science finds](https://insidebci.com/policy/2026-11-07-science-investigation-consumer-eeg-brain-data-ai-foundation-models-privacy-policies/) — Inside BCI; 2026-11-07; reputable-secondary; URL supplied in structured research output. Summarizes the investigation’s sample size, company disclosures, approximate EEG volume, and policy changes, while identifying remaining evidence gaps.
- `S5` [Insular motor and error encoding supports self-correcting intracranial brain-computer interface](https://www.nature.com/articles/s41467-026-78804-2) — Nature Communications / Springer Nature; 2026-11-07; primary-research; URL supplied in structured research output. Reports human intracranial recordings and a technically relevant mechanism for adaptive, self-correcting BCI control.
- `S6` [Noise resilience in brain decoding driven by spiking neural networks for responsive robot control](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2026.1931325/pdf) — Frontiers in Neurorobotics; 2026-11-09; primary-research; URL supplied in structured research output. Provides a recent neural-decoding experiment with explicit integration of a spiking model into a robot-control pipeline.
- `S7` [Detecting Reading-Induced Confusion Using EEG and Eye Tracking](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.2029849/abstract) — Frontiers in Neuroscience; 2026-11-09; primary-research; URL supplied in structured research output. Reports measured classification performance for a cognitive state using wearable-compatible EEG and eye tracking, directly informing the feasibility and limits of neural-state monitoring.
- `S8` [Beyond Accuracy: Information-Theoretic Decoder Evaluation Under Latent Intent](https://arxiv.org/abs/2611.05658) — arXiv; 2026-11-03; primary-research; URL supplied in structured research output. Provides a quantitative counterexample showing that equal decoder accuracy can produce radically different sequential-control outcomes.
- `S9` [Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness](https://arxiv.org/abs/2611.06418) — arXiv; 2026-11-04; primary-research; URL supplied in structured research output. Documents the distribution-shift and model-mismatch problems that make closed-loop control difficult, while also showing that the work remains at a methodological and benchmark stage.
- `S10` [CABrain: A Correlation-Aware Brain Foundation Model for EEG Decoding](https://arxiv.org/abs/2611.11782) — arXiv; 2026-11-09; primary-research; URL supplied in structured research output. Shows that current neural foundation-model work is still evaluated mainly through benchmark-dataset performance and unresolved EEG representation problems.
- `S11` [Connect-One: Early Feasibility Study of Connexus Brain-Computer Interface](https://clinicaltrials.gov/study/NCT07357428?aggFilters=status%3A&country=United+States&locStr=United+States&tab=researcher) — ClinicalTrials.gov; 2026-04-14; regulatory; URL supplied in structured research output. Provides registry-level evidence that an implanted BCI remains in early feasibility, with safety and long-term follow-up still being evaluated.
- `S12` [Regulatory Overview for Neurological Devices](https://www.fda.gov/medical-devices/neurological-devices/regulatory-overview-neurological-devices) — U.S. Food and Drug Administration; unknown; regulatory; URL supplied in structured research output. Defines the risk, investigational, and postmarket-surveillance requirements that limit claims of immediate durable deployment.
- `S13` [Implanted Brain-Computer Interface Devices for Patients with Paralysis or Amputation: Non-clinical Testing and Clinical Considerations](https://www.fda.gov/media/120362/download) — U.S. Food and Drug Administration; 2021-05-20; regulatory; URL supplied in structured research output. Provides device-specific regulatory expectations for implanted BCI systems, including signal processing, stimulation, and clinical safety considerations.
- `S14` [Firefox Program Solicitation](https://sam.gov/opp/ea1ade5831b545cc93affd13e79e7e0d/view) — U.S. Department of Defense / DARPA; 2026-11-06; official-release; URL supplied in structured research output. Identifies unresolved data-rate, scanning, and computational constraints in the effort to scale non-invasive neural recording.
- `S15` [Neurodata Governance: International Instruments, Domestic Legal Frameworks, and Emerging Regulatory Trends](https://www.oecd.org/en/publications/neurodata-governance_0ba61a20-en/full-report/component-5.html) — Organisation for Economic Co-operation and Development; 2026-10-01; reputable-secondary; URL supplied in structured research output. Summarizes the still-developing legal, ethical, and technical governance landscape for neurodata and neurotechnology.
- `S16` [Ethical Considerations for Implantable Human Brain–Computer Interfaces](https://www.nature.com/articles/s41593-026-02447-1) — Nature Neuroscience; 2026-09-07; reputable-secondary; URL supplied in structured research output. Provides expert ethical analysis of implantable BCIs and the unresolved questions surrounding autonomy, consent, agency, and long-term human use.
- `S17` [Wearable Sleep Trackers Are Using Your Brainwaves to Train AI Models Without Explicit User Consent](https://www.tomshardware.com/peripherals/wearable-tech/wearable-sleep-trackers-are-using-your-brainwaves-to-train-ai-models-without-explicit-user-consent-tens-of-millions-of-hours-of-eeg-data-harvested) — Tom’s Hardware; 2026-11-09; reputable-secondary; URL supplied in structured research output. Reports the investigation’s data-volume, consent, acquisition, and policy-change implications in accessible detail.
- `S18` [On the Feasibility of Temporal Interference Stimulation of Human Brains Using Two Arrays of Electrodes](https://pubmed.ncbi.nlm.nih.gov/42950356/) — Biomedical Physics & Engineering Express; 2026-11-06; primary-research; URL supplied in structured research output. Shows that a potentially important non-invasive stimulation approach was still being evaluated at the feasibility and modeling stage during the priority window.

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
  "id": "research_2026-11-10_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology and Neuro-Rights: Bounded Progress, Persistent Deployment Gaps, and Emerging Data Governance",
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
