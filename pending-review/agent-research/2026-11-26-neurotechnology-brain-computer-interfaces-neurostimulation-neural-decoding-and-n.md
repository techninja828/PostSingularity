# Neurotechnology Evidence Review: Useful Communication Gains, Persistent Deployment and Neuro-Rights Gaps
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-11-26
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The audited evidence produces a mixed update for brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights during 2026-11-19 through 2026-11-26. Communication performance and enabling hardware improved, including faster constrained noninvasive communication, intracortical speech decoding, brain-to-voice synthesis, and preclinical optical recording. However, the strongest results remain constrained, single-participant, preclinical, offline, or early-feasibility findings. Chronic decoder drift, recalibration, limited generalization, significant-risk regulation, specialist support, post-trial dependency, incomplete neurodata standards, and unequal access remain substantial constraints. No reliable human evidence demonstrated unrestricted thought decoding, affective exchange, or closed-loop control of mood, reward, dependency, or immersive experience. The evidence supports qualifying rather than replacing the relevant canon assumptions: neural links can plausibly become increasingly capable communication systems, but mature deployment requires maintenance, consent, privacy, governance, and continuity of support; Bliss Divergence remains a conditional storyworld premise; and Trust Fabrics should more explicitly cover neurodata provenance and decoder accountability. The assumption registry and canon remain unchanged pending human review.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-11-19 through 2026-11-26
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### AI-assisted noninvasive BCI nearly triples semantic communication speed in healthy-participant testing

- Event date: 2026-11-20
- Sources: `S1`
- Observed fact: Rutgers reported ChatBCI-Assist, a noninvasive EEG-based brain-computer communication system that uses a locally deployed language model to suggest words and phrases. The university reported nearly twice the communication speed of a conventional dictionary-based predictive system in copy spelling and nearly three times the baseline speed in semantic spelling. The system detects deliberate P300-based selections rather than unrestricted thoughts, and the language model operates locally rather than through a cloud service.
- Significance: This is a concrete signal for PS-NEURO-001 and PS-AI-003: AI can increase effective communication bandwidth without increasing neural signal bandwidth by converting sparse selections into intent-level phrases. Local processing also provides a privacy-preserving design pattern for neurodata. The result supports a near-term path toward more usable BCIs, but it does not demonstrate high-bandwidth unconstrained thought decoding.

### Intracortical speech decoding extended to pontine-stroke dysarthria with one 64-channel array

- Event date: 2026-11-20
- Sources: `S2`
- Observed fact: A report updated on November 21 described intracortical brain-to-text decoding for people with long-standing dysarthria and tetraplegia following pontine stroke. The work reported that neural activity from as few as one 64-channel microelectrode array in orofacial motor cortex could support speech decoding. For two participants, median word error rates were reported as 19.4% and 10.6% on a 125,000-word vocabulary, and 10.0% and 2.25% on a 1,024-word vocabulary, with signal stability reported for more than two years in one participant and two months in another after adjustment for signal changes.
- Significance: The result broadens the clinical population for which intracortical speech neuroprostheses may be relevant beyond ALS. It also suggests that useful decoding may not require very large cortical coverage, which matters for implantation burden, targeting, and long-term system design. The reported need for ongoing adjustment directly bears on the safety, durability, and deployment constraints in PS-NEURO-001.

### Brain-to-voice decoding reports a five-point-two-four-percent listener word-error rate in offline evaluation

- Event date: 2026-11-20
- Sources: `S3`, `S4`
- Observed fact: The Brain2voice 2.0 preprint describes a causal multimodal Transformer that converts intracortical neural signals into synthesized voice, acoustic features, and phoneme predictions at ten-millisecond time steps. On a prior benchmark dataset from one participant with ALS, naive human listeners produced a mean word error rate of 5.24% for continuous acoustic output and 5.65% for tokenized output, compared with a previously reported 43.75% benchmark. Simulated inference was reported to run within the ten-millisecond processing interval.
- Significance: This is a material step toward naturalistic two-way communication because it targets voice rather than only text. It supports PS-NEURO-001's decoded-speech signal and suggests that neural interfaces may eventually carry richer timing and paralinguistic information. The result is still a research prototype and does not establish reliable emotional or affective decoding.

### Graphene-photonic neural sensors demonstrate multiplexed optical recording and faster recovery from stimulation artifacts

- Event date: 2026-11-23
- Sources: `S5`
- Observed fact: Carnegie Mellon University reported an ion-gated, graphene-integrated photonic platform that converts extracellular electrical signals into wavelength-multiplexed optical signals without genetic modification or fluorescent dyes. Initial measurements reported a detection limit of approximately 20 microvolts at a signal-to-noise ratio of 3 decibels. The platform recorded evoked neurophysiological signals from mouse brain tissue, supported multiple sensors on one optical waveguide, and reportedly recovered from stimulation artifacts almost 25 times faster than a conventional recording amplifier.
- Significance: This is an enabling-hardware signal for PS-NEURO-001 and for closed-loop neurostimulation. Optical multiplexing could reduce wiring, electromagnetic interference, and stimulation artifacts, potentially improving channel density and simultaneous record-stimulate operation. It is relevant to the long-term bandwidth question, but the evidence is still preclinical.

### Neuralink's VOICE study remains an early-feasibility recruiting trial for robotic implantation and communication restoration

- Event date: 2026-11-20
- Sources: `S6`
- Observed fact: The VOICE study record was updated on November 20. It describes a recruiting early-feasibility study sponsored by Neuralink, with an intended enrollment of six participants and an October 2025 to October 2028 study period. The study evaluates the wireless N1 implant and R1 robotic inserter for adults with severe speech impairment and impaired upper-limb function associated with ALS, stroke, spinal-cord injury, or related conditions. The record identifies the device as a skull-mounted, rechargeable implant connected to electrode threads implanted in the brain.
- Significance: The important signal is clinical translation rather than a new performance record: invasive BCI development is moving through formal human feasibility studies with defined eligibility criteria, a specified robotic implantation workflow, and a multi-year follow-up horizon. This directly tests the safety and durability constraints that could either support or falsify PS-NEURO-001.

### China announces a planned national BCI data platform and Youren 1.1 foundation data release

- Event date: 2026-11-20
- Sources: `S7`
- Observed fact: The Shanghai municipal government reported on November 20 that the Pujiang Innovation Forum 2026 Brain-Computer Interface Conference, scheduled for December 3 through December 6, would begin preparations for a national BCI data platform and release Youren 1.1, described as the data foundation supporting that platform. The announcement also described planned invasive-BCI algorithm and systems-engineering challenges intended to test technologies against real-world needs.
- Significance: This is a governance and infrastructure signal rather than a validated technical result. Shared data infrastructure, benchmark challenges, and national coordination could improve reproducibility, accelerate algorithm comparison, and increase the strategic scale of BCI development. It also raises neuro-rights and data-governance questions because centralized or national neurodata systems can affect consent, access, ownership, cross-border use, and accountability.

### Cross-session and cross-person neural decoding remains a benchmark problem rather than a deployment result

- Event date: 2026-11-21
- Sources: `S8`, `S9`
- Observed fact: The 2026 EEG/EMG Foundation Challenge evaluated decoding across new stimuli, recording sessions, and participants, including a sealed final phase and a planned reproducibility audit. In the BCI decoding track, the leading reported balanced-accuracy score was 0.872, with lower scores among other submissions. The benchmark therefore tests generalization beyond the training distribution, but its leaderboard is still a research competition rather than evidence of reliable clinical or consumer deployment.
- Significance: This narrows optimistic interpretations of PS-NEURO-001. High scores on curated tasks do not establish stable decoding across days, users, disease states, electrode shifts, changing environments, or spontaneous behavior. The need for sealed evaluation and reproducibility auditing is itself evidence that apparent progress remains sensitive to benchmark design, leakage controls, and generalization assumptions.

### Chronic decoder drift and recalibration remain central barriers to independent use

- Event date: 2026-11-20
- Sources: `S10`, `S11`
- Observed fact: A 2026 systematic review of implantable BCI recalibration reported that long-term performance is affected by signal drift and variability in recorded neural units. A separate 2026 clinical-scalability review identified biological responses, micromotion, changes in electrode impedance, and progressive decoder drift as fundamental barriers, and stated that prospective home-use evaluation is still needed to determine whether adaptive decoding and supporting infrastructure provide acceptable benefit at acceptable burden.
- Significance: This is direct counterevidence against treating isolated high-accuracy demonstrations as evidence of durable neural bandwidth. Even when a decoder works in a laboratory, ongoing recalibration, expert intervention, or adaptive software may be required. That creates practical, safety, and equity constraints for PS-NEURO-001, especially if systems are expected to operate continuously or support two-way interaction with AI.

### Exceptional long-term home use remains a single-participant result, while most clinical programs are still feasibility studies

- Event date: 2026-11-20
- Sources: `S12`, `S6`, `S13`
- Observed fact: A major 2026 report demonstrated more than 3,800 hours of independent home use over 19 months by one person with ALS, but the same report framed independent operation and long-term signal stability as previously unmet clinical-translation requirements. During the priority window, Neuralink’s VOICE program was still described as a recruiting early-feasibility study with a planned enrollment of six participants, and early human data from Axoft’s temporary probes were reported through conference and company materials without a peer-reviewed publication.
- Significance: The field has produced an important proof of feasibility, but the evidence base remains highly concentrated in exceptional participants, small cohorts, and early-stage studies. This limits claims that invasive BCIs are already scalable clinical infrastructure. Generalization to broader paralysis populations, routine care settings, and long-term maintenance remains unproven.

### Implanted BCI devices remain significant-risk investigational technologies under the U.S. regulatory pathway

- Event date: 2026-11-24
- Sources: `S14`, `S15`
- Observed fact: FDA guidance identifies implanted BCI devices for paralysis or amputation as significant-risk devices. Human studies generally require an Investigational Device Exemption, institutional review-board approval, informed consent, monitoring, and safety and effectiveness data before marketing authorization. FDA also states that the safety and effectiveness of investigational devices are not known during the study phase.
- Significance: Regulatory status constrains claims of near-term broad deployment. Even strong laboratory decoding results do not establish authorization for routine clinical use, and the required evidence package imposes substantial time, cost, manufacturing, human-factors, cybersecurity, and follow-up burdens. This is a direct deployment constraint for PS-NEURO-001 and a reason why research demonstrations should not be treated as mature products.

### Post-trial support, maintenance, explantation, and cost create an unresolved neuro-rights and access problem

- Event date: 2026-11-20
- Sources: `S16`, `S17`
- Observed fact: A 2026 multidisciplinary consensus study found that continued support for people with investigational implantable neural devices requires specialist care, technical expertise, tertiary clinical infrastructure, and substantial financial resources. It also noted that continued access may become impossible if a trial shows no benefit, commercial viability fails, or safety concerns lead to suspension or early termination. A 2026 neurotechnology review similarly identified specialized surgery, programming, long-term technical support, reimbursement, and post-trial commitments as barriers to equitable access.
- Significance: This challenges the assumption that successful implantation automatically creates durable autonomy. A device can remain in a person’s body while the software, hardware support, clinical team, or funding disappears. That creates concrete neuro-rights questions involving bodily integrity, dependency, withdrawal of support, data continuity, explantation, maintenance obligations, and unequal access. It directly bears on PS-NEURO-002 and PS-NEURO-001.

### Operational neurodata governance is not yet designed for real-time closed-loop implants

- Event date: 2026-11-20
- Sources: `S18`, `S19`
- Observed fact: A 2026 data-protection analysis reported that existing neurodata standards such as Neurodata Without Borders and BIDS were designed primarily for retrospective research datasets and do not standardize decoder architectures and parameters, closed-loop or effector-control signals, device-specific timing, or synchronization metadata. The analysis also described model passports, machine unlearning, and blockchain-based consent or audit systems as largely untested for implantable BCI data.
- Significance: This narrows optimistic claims associated with PS-NEURO-002 and PS-AI-003. Privacy is not solved merely by keeping a language model local or de-identifying recordings. Real-time neurotechnology requires governance over raw neural data, derived intent labels, decoder updates, stimulation commands, access logs, model retraining, revocation, and post-trial data retention. Without interoperable audit and consent mechanisms, accountability may lag technical capability.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S8`, `S9`, `S10`, `S11`, `S12`, `S14`, `S15`, `S16`, `S17`, `S18`, `S19`
- Evidence: Evidence materially strengthens the feasibility of useful neural-to-AI communication: Rutgers reported faster semantic communication with noninvasive EEG, intracortical systems reported speech decoding with 64-channel arrays, Brain2voice reported low listener word-error rates in offline evaluation, and new optical hardware offers a possible channel-density and stimulation-artifact improvement. However, the strongest results remain constrained, single-participant, preclinical, offline, or early-feasibility findings. Chronic decoder drift, recalibration, limited generalization, regulatory requirements, post-trial support, and the absence of reliable unrestricted thought or affective decoding remain substantial counterevidence to the full claim of safe, rich, two-way communication.
- Real-world implication: Neural interfaces are progressing toward clinically useful communication aids, but they are not yet mature high-bandwidth general-purpose interfaces. Near-term deployment will likely remain limited by calibration, specialist support, safety evidence, privacy governance, and unequal access. The evidence does not yet establish durable sensory or emotional exchange between humans and AI.
- PostSingularity implication: A post-singularity setting can reasonably depict neural-AI links as technically capable of rich two-way exchange only if it also accounts for maintenance, signal drift, bodily risk, consent, data continuity, and support obligations. Broad deployment should not be treated as an automatic consequence of laboratory decoding results; infrastructure and governance remain part of the technology.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: `S16`, `S17`, `S18`, `S19`
- Evidence: The supplied evidence documents neurodata governance gaps, post-trial dependency concerns, and policy complexity for implantable systems, but it does not report a priority-window human result demonstrating reliable AI-mediated control of mood, reward, affect, dependency, or immersive experience. The available demonstrations concern communication, recording hardware, and early feasibility rather than engineered mental states. Therefore the downstream governance concern is plausible but not directly evidenced as an emerging social problem.
- Real-world implication: Neuro-rights, consent, access, withdrawal of support, and data governance are already identifiable policy questions for implantable neurotechnology, but the record does not show that reliable mental-state engineering has reached a level producing broad collective effects. Clinical use remains more relevant to communication and monitoring than to general mood or reward control.
- PostSingularity implication: A post-singularity story may explore engineered mental states as a governance problem, but should frame this as a conditional consequence of a future capability rather than an evidence-backed present trajectory. The key institutions would need to govern consent, dependency, reversibility, privacy, access, and the legitimacy of participation in altered experience.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S1`, `S7`, `S8`, `S9`, `S14`, `S15`, `S18`, `S19`
- Evidence: The evidence strengthens the direction of the claim that increasing AI and neurotechnology influence will require provenance, verification, audit, and graduated oversight. Relevant signals include sealed and reproducibility-audited neural benchmarks, planned national BCI data infrastructure, FDA requirements for safety and effectiveness evidence, and analyses identifying missing standards for decoder parameters, closed-loop commands, consent, model updates, machine unlearning, and auditability. However, the evidence more clearly establishes governance need and standards gaps than broad adoption of effective provenance systems across AI systems generally.
- Real-world implication: Organizations and regulators are likely to place greater emphasis on traceable data lineage, model and decoder documentation, independent evaluation, access logs, consent records, and risk-tiered oversight. Current systems remain uneven: local processing can reduce exposure, but it does not by itself resolve provenance, revocation, accountability, or post-trial governance.
- PostSingularity implication: In a post-singularity world, provenance and audit rituals can function as core legitimacy infrastructure for AI-mediated decisions and neural systems. The setting should distinguish between technically inspectable systems, systems that merely claim transparency, and institutions capable of enforcing audits or responding when provenance is incomplete.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: No supplied development or source addresses launch economics, propulsion, life-support closure, in-space manufacturing, orbital duration, human health limits, or autonomous off-world operations. The audited evidence is concentrated on neural interfaces and neurotechnology governance, so it cannot directionally assess sustained off-world settlement.
- Real-world implication: The supplied record provides no basis for updating the forecast of practical long-duration orbital or off-world communities. Those components require separate evidence on transportation, habitat reliability, radiation, life support, maintenance, economics, and human factors.
- PostSingularity implication: The assumption remains available as a storyworld premise, but its plausibility cannot be inferred from the current evidence packet. A post-singularity setting would still need to specify which bottlenecks were solved and how autonomous systems, energy abundance, and closed-loop habitats interact.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **high**
- Sources: None
- Evidence: No supplied development or source measures device-free spaces, right-to-disconnect policy, analog-media growth, low-technology communities, or cultural resistance to pervasive integration. The quality notes explicitly state that the relationship between neurotechnology adoption and privacy-preserving or device-free practices remains unassessed in the priority window.
- Real-world implication: The evidence does not establish either the persistence or disappearance of analog practices. Claims about cultural backlash, revival, or negligible resistance require social, market, policy, or demographic data not present here.
- PostSingularity implication: Analog and low-technology practices remain a plausible social counterweight in a post-singularity setting, but their scale, durability, and political significance should not be treated as evidence-backed forecasts from this packet. Their role would depend on whether people retain meaningful choices, protected privacy, and accessible non-integrated institutions.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S8`, `S9`, `S10`, `S11`, `S12`, `S14`, `S15`, `S16`, `S17`, `S18`, `S19`
- Why this location: The evidence supports useful neural-to-AI communication and improving hardware, but it does not support treating neural links as mature, unrestricted, or maintenance-free high-bandwidth interfaces. Results remain constrained by task design, small cohorts, offline evaluation, preclinical hardware, decoder drift, recalibration, regulation, specialist support, and unresolved operational neurodata governance.
- Proposed change: Add a qualification to the Summary stating that neural links can support increasingly capable communication and shared experiences, while reliable deployment depends on calibration, signal stability, consent, privacy, regulatory approval, specialist maintenance, and continuity of technical and clinical support. Explicitly distinguish constrained speech or intent decoding from unrestricted thought, emotional-state, or affective decoding.
- Implementation steps:
  1. Insert the qualification in the Summary after the existing description of direct nervous-system communication and before the list of capabilities, so it frames the scope of all subsequent claims.
  2. Retain the existing claims about shared realities, emotional streaming, identity shifts, and sensory input unless separately supported by future evidence; do not recast the current research results as proof of those capabilities.
  3. Cross-reference Trust Fabrics for audit, provenance, and oversight implications, and AI Agents for consent and override behavior.
  4. Review the final wording against the existing emotional-regulation safeguard and the Story Use examples so maintenance or calibration constraints do not contradict the established narrative uses.
- Dependencies or conflicts:
  - The existing Summary presents emotional streaming, identity shifts, and sensory-input changes as available capabilities, while the audited evidence did not demonstrate reliable human affective or immersive-state decoding.
  - The existing statement that neural links are safe and deeply personalized may conflict with evidence describing significant-risk investigational implants, recalibration, signal drift, and unresolved long-term support.
  - The proposed qualification must preserve the distinction between noninvasive systems such as Rutgers's constrained EEG interface and invasive intracortical or preclinical optical systems.
  - Any later chronology update should reconcile the existing Cycle 3 Neural Link Age with the evidence that comparable real-world systems remain early-stage or investigational.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **watch**
- Recommendation: **no-change**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-002`
- Sources: `S16`, `S17`, `S18`, `S19`
- Why this location: The sources substantiate governance concerns around implant dependency, post-trial support, consent, access, and neurodata accountability, but they do not demonstrate reliable human control of mood, reward, affect, dependency, or immersive experience. The existing philosophical framing can remain, provided it is not presented as an evidence-backed near-term development.
- Proposed change: Leave the file unchanged for now. Do not add a claim that engineered bliss, affective control, or immersive neural states have emerged from the audited evidence. If a future revision is approved, add only a conditional qualification under Philosophical Tensions stating that such governance problems depend on a capability not yet demonstrated in the reviewed record.
- Implementation steps:
  1. Preserve the existing discussion of perpetual AI-mediated joy as a storyworld premise rather than updating it with current neurotechnology performance claims.
  2. Add this assumption to the watchlist for independently replicated, closed-loop human evidence involving mood, reward, affect, dependency, or immersive experience.
  3. If later evidence warrants an edit, place the qualification under Philosophical Tensions and cross-reference Neural Links and Trust Fabrics rather than changing the historical or functional description of Bliss Divergence.
  4. Require review of consent, reversibility, withdrawal of support, access, and data-retention implications before converting the conditional premise into established canon.
- Dependencies or conflicts:
  - The existing file describes safe neural immersion and regulated bliss exits, while the reviewed evidence does not validate reliable mental-state engineering or the safety of such systems.
  - Post-trial support concerns in S16 and S17 may inform the dependency theme, but they do not establish that bliss technologies produce broad social effects.
  - Any stronger claim would need to be reconciled with the audited finding that no priority-window human evidence demonstrated reliable closed-loop control of mood, reward, affect, or immersive experience.

### `worldbible/technologies/trust-fabrics.md` -> 🔐 Verification Layers

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **supports**
- Assumptions: `PS-AI-003`
- Sources: `S1`, `S7`, `S8`, `S9`, `S14`, `S15`, `S18`, `S19`
- Why this location: The evidence strengthens the need for provenance, consent records, independent evaluation, access controls, and auditability. It also qualifies the existing trust model: local processing and visible outputs do not by themselves solve decoder governance, model updates, revocation, closed-loop command logging, or post-trial data continuity.
- Proposed change: Add a verification-layer bullet stating that neurotechnology and AI systems must document raw-data provenance, derived intent labels, decoder versions and parameters, model updates, stimulation or effector commands, consent and revocation events, access logs, and retention or deletion decisions. State that local processing reduces exposure but does not independently establish accountability or machine-unlearning capability.
- Implementation steps:
  1. Insert the new bullet under Verification Layers after Provenance Trails, because it expands provenance from ordinary AI outputs to real-time neurodata and decoder operations.
  2. Retain the existing Transparency Protocols, Provenance Trails, and Emotive Integrity Tags; the addition should specify their application to neural systems rather than replace them.
  3. Cross-reference Neural Links for calibration, consent, and support constraints, and AI Trust for community review and accountability rituals.
  4. Review whether Oversight Systems should later name a specialist neural-device or clinical review role; do not add that role until the repository establishes it elsewhere.
  5. Check any index or metadata effects only if the repository requires new terminology such as decoder provenance, neurodata governance, or post-trial continuity to be added to tags or navigation.
- Dependencies or conflicts:
  - The existing claim that all decision-making logic is viewable by bonded citizens may be stronger than the audited evidence, which identifies missing standards for decoder architectures, closed-loop signals, synchronization metadata, machine unlearning, and operational audit systems.
  - The existing Resonance Drift Alerts concern AI behavioral deviation, while neural decoder drift and electrode changes involve a related but technically distinct maintenance problem; terminology should not imply that one alert system solves the other.
  - The existing Trust Fabrics model emphasizes public transparency, but neurodata governance may require graduated access and privacy protections rather than unrestricted public visibility.
  - The proposed addition should not imply that the planned national BCI platform or Youren 1.1 release was operational, validated, consented, or interoperable during the priority window.

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

- The strongest neural-decoding demonstrations are concentrated in single participants, small cohorts, preprints, institutional releases, or offline evaluations, with limited independent replication.
- Long-term safety, biocompatibility, signal stability, recalibration burden, home operation, and post-trial support remain incompletely measured for implantable systems.
- No reliable human evidence in the supplied record demonstrates unrestricted thought decoding or two-way decoding of emotional or affective states.
- The operational status, consent model, provenance, interoperability, and governance of the proposed national BCI data infrastructure are not established.
- The evidence for AI provenance and audit adoption is stronger for identified governance needs and research controls than for broad, mature implementation across high-impact AI.
- No evidence in the packet addresses sustained off-world settlement or the persistence of analog practices.
- No denominator-based public dataset establishes rates of implant failure, explantation, abandonment, signal degradation, or loss of post-trial care.
- No binding neuro-rights rule specifically governing decoder outputs, stimulation commands, mental privacy, or lifetime neural-device support was identified in the stated priority window.
- The Brain2voice 2.0 development is dated 2026-11-20 for the priority-window presentation/update, while its underlying bioRxiv source was published on 2026-06-30; this is a presentation/update date distinction, not a contradiction in the research result.
- The pontine-stroke report states signal stability for more than two years in one participant and two months in another after adjustment for signal changes, while the counterevidence sources identify chronic drift and recalibration as continuing barriers. These claims are compatible: individual long-duration stability does not establish drift-free or maintenance-free deployment.
- The Rutgers result reports nearly three times baseline speed in semantic spelling and nearly twice the speed of a conventional dictionary-based predictive system in copy spelling. These are different comparison conditions and should not be combined into a single threefold general performance claim.
- The Shanghai source is described as reporting on November 20, while the URL contains 20261123 and the announcement concerns a future December conference. The evidence supports a planned activity, not an operational platform or completed data release.
- The long-term home-use result is a strong positive single-participant demonstration, whereas the feasibility-study and regulatory sources show that broad clinical deployment remains incomplete. This is a difference in evidence scope, not a direct contradiction.
- Claims that ChatBCI-Assist decodes unrestricted inner speech, unrestricted thoughts, or high-bandwidth unconstrained thought were excluded.
- Claims that ChatBCI-Assist has been clinically validated in people living with ALS were excluded because clinical testing was still being planned.
- Claims that the Brain2voice 2.0 result demonstrates real-time closed-loop clinical communication, spontaneous speech decoding, complete speech-loss decoding, or reliable emotional or affective decoding were excluded.
- Claims that the pontine-stroke intracortical decoder is a fully independent, home-operable clinical product were excluded.
- Claims that the graphene-photonic platform demonstrated thousands of channels, human implantation, clinical safety, therapeutic efficacy, long-term biocompatibility, or durable surgical reliability were excluded.
- Claims that Neuralink’s VOICE study has demonstrated efficacy, safety, long-term channel stability, speech accuracy, independence, quality-of-life benefit, or routine clinical availability were excluded.
- Claims that China’s national BCI data platform or Youren 1.1 was operational, independently validated, consented, interoperable, or governed during the priority window were excluded.
- Claims that the EEG/EMG Foundation Challenge leaderboard establishes reliable clinical or consumer deployment, broad generalization, or failure of the leading systems were excluded.
- Claims that one long-term home-use participant demonstrates scalable clinical infrastructure across broader paralysis populations were excluded.
- Claims that Axoft’s preliminary human observations establish a peer-reviewed clinical result, validated consciousness detection, or clinical deployment were excluded.
- Claims that FDA guidance constitutes a new 2026 adverse event, denial, or device-specific regulatory action were excluded.
- Claims that post-trial abandonment, explantation, or loss of care occurs at a known rate were excluded because no denominator-based public dataset was located.
- Claims that local language-model processing alone resolves neurodata privacy, consent, access, ownership, decoder-governance, audit, revocation, or post-trial data-retention issues were excluded.
- Claims of reliable human closed-loop control of mood, reward, affect, dependency, immersive experience, or unrestricted emotional state during the priority window were excluded.
- Claims of a priority-window binding neuro-rights law, court ruling, or regulator-issued operational standard specifically governing decoder outputs, stimulation commands, mental privacy, or post-trial neural-device support were excluded.
- PS-SPACE-001 is assessed as insufficient-evidence. No supplied source addresses propulsion, launch economics, closed-loop life support, radiation, in-space manufacturing, autonomous maintenance, or long-duration settlement, so no repository edit is warranted in worldbible/technologies/aerospace-systems.md. The existing premise remains unmodified and should be revisited only when relevant space-development evidence is audited.
- PS-SOCIAL-002 is assessed as insufficient-evidence. The supplied record contains no measures of device-free spaces, right-to-disconnect policies, analog-media growth, low-technology communities, or resistance to pervasive integration, so no edit is warranted in worldbible/timeline.md. The existing chronology and cultural claims should remain unchanged rather than being inferred from neural-interface developments.
- The reviewed evidence does not establish reliable unrestricted thought decoding, affective exchange, or human closed-loop control of mood, reward, dependency, or immersive experience. Those absent results do not justify adding capability claims to Neural Links or Bliss Divergence beyond the scoped qualification plans above.
- The evidence does not establish completed clinical efficacy, routine availability, broad generalization, or durable home operation for invasive BCIs. No separate chronology, technology-index, or story-use edit is proposed because adding such claims would exceed the audited evidence.
- No binding priority-window neuro-rights law or operational regulator-issued standard was identified. Governance implications can be represented through the proposed Trust Fabrics qualification, but the packet does not support adding a new legal institution, statute, or historical event.
- The plan does not propose changing the PS Technology Index, Philosophy Index, or timeline. Existing links remain usable, and the assessed evidence does not require a new canon category or chronology entry.

## Watchlist

- Prospective multi-site human BCI studies reporting long-term safety, independent home use, recalibration frequency, quality of life, and failure rates.
- Human demonstrations of bidirectional sensory or affective exchange, especially with independently replicated and closed-loop evaluations.
- Clinical translation of optical or high-channel-count neural sensors, including packaging, biocompatibility, power, thermal behavior, and durable signal quality.
- Operational results from the proposed BCI data platform, including dataset provenance, participant consent, access controls, interoperability, auditability, and cross-border governance.
- Adoption of AI provenance standards, model and decoder audit requirements, disclosure rules, and enforceable mechanisms for revocation and post-deployment accountability.
- Evidence on launch cost, closed-loop life support, radiation protection, autonomous maintenance, and in-space manufacturing for long-duration settlements.
- Survey, market, policy, and demographic evidence on device-free spaces, right-to-disconnect rules, analog media, and low-technology communities.

## Sources

- `S1` [How Rutgers Engineers Developed a Noninvasive Brain-Computer Communication System](https://soe.rutgers.edu/news/how-rutgers-engineers-developed-noninvasive-brain-computer-communication-system) — Rutgers School of Engineering; 2026-11-20; official-release; URL supplied in structured research output. First-party account of the system architecture, measured speed comparisons, privacy design, participant population, and clinical-translation limitations.
- `S2` [Restoring intended speech in people with dysarthria from pontine stroke using an intracortical brain-computer interface](https://visualize.jove.com/43059861-restoring-intended-speech-in-people-with-dysarthria-from-pontine-stroke-using-an-intracortical-brain-computer-interface) — JoVE Visualize / medRxiv; 2026-11-20; primary-research; URL supplied in structured research output. Provides the reported participant population, channel count, vocabulary sizes, word-error rates, and duration of signal stability.
- `S3` [Brain2voice 2.0: High-performance voice synthesis brain-computer interface](https://www.biorxiv.org/content/10.64898/2026.06.30.735633v1.full) — bioRxiv; 2026-06-30; primary-research; URL supplied in structured research output. Contains the model design, participant and electrode details, listener word-error rates, latency measurements, and explicit limitations; the work was highlighted in the priority window through November 2026 conference materials.
- `S4` [Brain2voice 2.0: High-performance voice synthesis brain-computer interface](https://visualize.jove.com/43059673-brain2voice-20-high-performance-voice-synthesis-brain-computer-interface) — JoVE Visualize / bioRxiv; 2026-11-20; primary-research; URL supplied in structured research output. Provides the priority-window presentation/update record for the same brain-to-voice research and summarizes its reported intelligibility result.
- `S5` [Streaming Brain Activity at the Speed of Light](https://www.cmu.edu/ni/news-events/2026/streaming-brain-activity-at-the-speed-of-light) — Carnegie Mellon University Neuroscience Institute; 2026-11-23; official-release; URL supplied in structured research output. First-party report of the device architecture, detection limit, mouse-tissue recording, multiplexing approach, and stimulation-artifact recovery measurement.
- `S6` [VOICE: An Early Feasibility Study of a Precise Robotically Implanted Brain-Computer Interface for Communication Restoration](https://www.smartpatients.com/trials/NCT07224256) — Smart Patients, based on ClinicalTrials.gov data; 2026-11-20; reputable-secondary; URL supplied in structured research output. Reports the November 20 registry update, trial status, sponsor, enrollment, device description, target population, and study dates.
- `S7` [Brain-Computer Interface Conference to be held in Shanghai](https://english.shanghai.gov.cn/en-Latest-WhatsNew/20261123/171f91d6171f41cca3ac3cca1fad1077.html) — Shanghai Municipal Commission of Science and Technology / Shanghai Municipal Government; 2026-11-20; official-release; URL supplied in structured research output. Reports the proposed national BCI data platform, Youren 1.1 release, conference timing, and planned algorithm and systems-engineering challenges.
- `S8` [EEG/EMG Leaderboards: Foundation Challenge 2026](https://neural-interfaces26.github.io/leaderboard.html) — Neural Interfaces 2026 / NINE Lab; 2026-11-21; primary-research; URL supplied in structured research output. Provides the sealed-track design, cross-session and cross-participant evaluation criteria, leaderboard scores, and planned reproducibility audit.
- `S9` [EEG/EMG Foundation Challenge 2026 at NeurIPS](https://nine.ucsd.edu/post/neurips-challenge-2026/) — NINE Lab, University of California San Diego; 2026-10-20; official-release; URL supplied in structured research output. Documents the challenge’s generalization targets, hidden datasets, competition dates, and distinction between warm-up and final evaluation.
- `S10` [Recalibration of implantable brain–computer interfaces to enable long-term independent use: a systematic review](https://doi.org/10.1088/1741-2552/ae7694) — Journal of Neural Engineering; 2026-06-23; primary-research; URL supplied in structured research output. Systematically reviews recalibration requirements, signal drift, and the clinical implications of maintaining long-term independent iBCI use.
- `S11` [Generalizable neural decoding for clinically scalable brain-computer interfaces](https://www.nature.com/articles/s44385-026-00119-0) — Nature; 2026-10-01; primary-research; URL supplied in structured research output. Identifies biological instability, micromotion, decoder drift, and the need for prospective home-use evaluation as clinical-scaling barriers.
- `S12` [Long-term independent use of an intracortical brain–computer interface for speech and cursor control](https://www.nature.com/articles/s41591-026-04414-6) — Nature Medicine; 2026-06-15; primary-research; URL supplied in structured research output. Shows both the unusually strong single-participant result and the previously unmet requirements of independent home use and long-term performance.
- `S13` [Axoft wants its brain probe to tell doctors whether a patient is conscious](https://insidebci.com/news/2026-11-20-axoft-fleuron-probe-disorders-of-consciousness-mgb-panama-clinic/) — Inside BCI; 2026-11-20; reputable-secondary; URL supplied in structured research output. Reports Axoft’s preliminary human probe data and explicitly notes that the results had not yet appeared in a peer-reviewed journal.
- `S14` [Implanted Brain-Computer Interface (BCI) Devices for Patients with Paralysis or Amputation: Non-clinical Testing and Clinical Considerations](https://www.fda.gov/media/120362/download) — U.S. Food and Drug Administration; 2023-01-01; regulatory; URL supplied in structured research output. Defines implanted BCIs as significant-risk devices and outlines the preclinical and clinical evidence expectations for human investigations.
- `S15` [Investigational Device Exemption (IDE)](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide) — U.S. Food and Drug Administration; 2024-01-01; regulatory; URL supplied in structured research output. Explains the IDE requirements for investigational medical devices, including safety and effectiveness data collection, IRB approval, informed consent, monitoring, and reporting.
- `S16` [Recommendations on post-trial responsibility in implantable neural device research: a multidisciplinary consensus study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13440073/) — BMC Medical Ethics; 2026-05-12; primary-research; URL supplied in structured research output. Provides expert evidence on post-trial care, technical support, financial responsibility, safety-related discontinuation, and continuity of access for implant recipients.
- `S17` [From deep brain stimulation to brain–computer interfaces: current progress in implantable neurotechnology](https://pmc.ncbi.nlm.nih.gov/articles/PMC13534989/) — PMC / peer-reviewed review article; 2026-08-01; reputable-secondary; URL supplied in structured research output. Identifies long-term stability, missing failure reporting, specialized expertise, high device costs, reimbursement, and post-trial commitments as translational and equity barriers.
- `S18` [Advancing data protections for implantable brain-computer interfaces](https://doi.org/10.1038/s43856-026-01797-y) — Communications Medicine; 2026-07-01; primary-research; URL supplied in structured research output. Examines gaps in existing neurodata standards and the untested status of lineage, machine-unlearning, consent, and audit mechanisms for operational iBCI systems.
- `S19` [Neurodata governance: Evidence from innovators for public policy](https://www.oecd.org/en/publications/neurodata-governance_0ba61a20-en/full-report/component-3.html) — Organisation for Economic Co-operation and Development; 2026-10-06; official-release; URL supplied in structured research output. Documents the sensitivity and governance complexity of neurodata and the need for coherent safeguards as neurotechnology moves across research, clinical, and commercial settings.

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
  "id": "research_2026-11-26_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology Evidence Review: Useful Communication Gains, Persistent Deployment and Neuro-Rights Gaps",
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
