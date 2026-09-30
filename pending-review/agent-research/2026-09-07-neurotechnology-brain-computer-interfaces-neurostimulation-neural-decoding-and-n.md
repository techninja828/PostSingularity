# Neurotechnology Evidence Review: Neural Interfaces, Neurostimulation, Neural Decoding, and Neuro-Rights
Tags: [research], [pending-review], [neurotechnology]

> **Status:** Non-canonical research draft pending human review.
> **Mode:** LIVE web research
> **Generated:** 2026-09-07
> **Model:** CrewAI/gpt-5.6-luna

## Research Question

brain-computer interfaces, neurostimulation, neural decoding, and neuro-rights

## Executive Summary

The supplied evidence materially improves the case for neural telemetry, adaptive neural-state inference, and investigational bidirectional therapeutic devices, but it does not demonstrate mature human neural communication carrying rich affective or sensory information. Governance and neural-privacy concerns are better substantiated, while technology-specific protections remain incomplete. No audited evidence was supplied to update the AI provenance, off-world settlement, or analog-practice assumptions. The recommended canon changes are conservative qualifications to Neural Links and The Bliss Divergence; the assumption registry and canon remain unchanged pending human review.

## Research Scope

- Lane: `neurotechnology`
- Research window: 2026-08-31 through 2026-09-07
- Tracked assumptions: `PS-NEURO-001`, `PS-NEURO-002`, `PS-AI-003`, `PS-SPACE-001`, `PS-SOCIAL-002`

## Observed Developments

### High-bandwidth transdural telemetry targets a major bottleneck for bidirectional implants

- Event date: 2026-09-01
- Sources: `S1`
- Observed fact: A peer-reviewed Communications Engineering paper published September 1, 2026 described a two-stage wireless architecture for intracortical BCIs. The proposed system uses transdural galvanic-coupled body-channel communication between a free-floating microelectrode array and an intracranial unit, followed by a transcutaneous link to an external device. Phantom and ex vivo human-cadaver-head tests demonstrated transmission up to 500 Mbps at 20% duty cycling with bit-error rates below 10⁻⁵. A send-on-delta encoder achieved up to 11.4× data compression. Brain-on-a-chip tests reported no unintended neural activity from the telemetry system.
- Significance: This is directly relevant to PS-NEURO-001 because channel count and wireless power/data constraints are central limits on safe, high-bandwidth, bidirectional neural interfaces. The measured result addresses telemetry capacity and thermal burden, rather than neural decoding or sensory feedback itself.

### Generative AI reconstructs deep-brain biomarkers from cortical recordings for closed-loop stimulation

- Event date: 2026-09-01
- Sources: `S2`
- Observed fact: A study published September 1, 2026 developed a deep-learning framework using spectral processing and generative diffusion models to reconstruct subcortical neural signals from cortical electrocorticography. The authors validated the approach across 723 hours of simultaneous cortico-subcortical recordings from 49 patients with movement disorders at three international centers. The model inferred activity across the subthalamic nucleus, globus pallidus internus, and thalamus, across rest, movement, sleep, medication-on/off, and stimulation-on/off conditions, with performance above chance in every tested condition.
- Significance: This is a material closed-loop-neurostimulation development. It could reduce dependence on direct deep-brain sensing and potentially simplify adaptive DBS architectures, while also increasing the role of inferred neural states in clinical control systems. It bears on PS-NEURO-002 because reliable inferred biomarkers are a prerequisite for more adaptive mood, movement, or cognitive-state interventions.

### CorTec receives a second FDA Breakthrough Device designation for an investigational fully implantable BCI

- Event date: 2026-08-31
- Sources: `S3`, `S4`
- Observed fact: CorTec announced on August 31, 2026 that the FDA had granted a second Breakthrough Device designation to its Brain Interchange system, extending the designated use from stroke rehabilitation to communication for people with non-progressive quadriplegia. The company describes one platform supporting movement-intention decoding for computer-cursor control and therapeutic cortical stimulation for motor recovery. The announcement explicitly states that Brain Interchange is investigational and not approved for commercial use.
- Significance: The designation is a regulatory signal that fully implantable, bidirectional systems are being treated as potentially important for both communication and rehabilitation. It supports the near-term clinical translation portion of PS-NEURO-001, but it is not evidence of marketing approval, efficacy, or safe long-term human performance.

### Needle-injectable, battery-free peripheral nerve stimulation reaches rat proof of concept

- Event date: 2026-09-03
- Sources: `S5`
- Observed fact: University of Florida researchers reported on September 3–4, 2026 that a needle-injectable implant placed beside the sciatic nerve in rats could be powered wirelessly by a removable external transmitter and reliably activate the nerve, producing muscle responses. The team reported that the implant remained in position with minimal visible tissue response during the study. The transmitter was described as smaller than a baseball card, while the implant itself required no battery or implanted wire.
- Significance: This is a material neurostimulation development because it targets the invasiveness, battery size, and lead-placement problems of conventional peripheral and spinal stimulators. If translated, similar architectures could broaden deployment of stimulation for pain and neurological disorders. It is more directly relevant to neurostimulation than to brain-computer interfaces, and it does not yet demonstrate central nervous system control.

### Exploratory secondary analysis claims domain-specific cognitive gains from non-invasive stimulation in mild Alzheimer’s disease

- Event date: 2026-09-03
- Sources: `S6`
- Observed fact: Nexalin Technology announced September 3, 2026 an exploratory item-level analysis of data from a completed randomized, double-blind, sham-controlled trial of its 15 mA Gen-2 SYNC deep intracranial frequency stimulation device in people with mild Alzheimer’s disease. The company reported that one-half of evaluable active-arm participants achieved an improvement of at least four points on ADAS-Cog and that gains in comprehension, memory, and language remained evident three months after treatment ended. The analysis was presented as informing the design of a planned U.S. pilot study after an FDA Q-submission meeting.
- Significance: The signal is relevant to PS-NEURO-002 because it concerns non-invasive stimulation aimed at altering cognitive function, with possible implications for therapeutic mood or cognition control. It also illustrates the distinction between a post hoc or exploratory analysis and a prospectively validated neuromodulation effect.

### Neurotechnology agency and trust receive renewed formal treatment in bioethics research

- Event date: 2026-08-31
- Sources: `S7`
- Observed fact: A paper published August 31, 2026 examined self-trust as a unifying principle for agency in neurotechnology. It addressed concerns arising from BCIs and deep-brain stimulation across responsibility, privacy, authenticity, and trust, arguing that these dimensions should be analyzed together rather than as separate ethical issues.
- Significance: This is a governance and neuro-rights signal rather than a technical performance milestone. It strengthens the evidentiary basis for treating agency, mental privacy, authenticity, and control as linked design and oversight problems as BCIs become more adaptive and potentially bidirectional. It is relevant to PS-NEURO-002 and to the neuro-rights portion of the lane.

### A new clinical neurostimulation biomarker remains preliminary, small-sample, and unreplicated

- Event date: 2026-09-02
- Sources: `S8`
- Observed fact: A Molecular Psychiatry study published September 2, 2026 analyzed TMS-EEG data from only 24 participants, divided equally between active and sham treatment, in a prior randomized trial of Stanford Neuromodulation Therapy for treatment-resistant depression. The authors reported an exploratory association between baseline estimated subgenual anterior cingulate activity and clinical response, but explicitly stated that the correlation was based on an active-arm sample of 12 participants, involved uncorrected exploratory testing, and required replication in larger independent cohorts before clinical use. The study also noted that scalp-EEG source localization of deep medial structures has limited spatial precision and that no healthy control group was included.
- Significance: This narrows optimistic claims about reliable AI-mediated control of mood or other mental states under PS-NEURO-002. The result is a mechanistic signal associated with an intensive therapeutic protocol, not a validated biomarker or dependable closed-loop controller. It shows that even clinically promising neuromodulation may lack the sample size, independent replication, anatomical precision, and prospective validation needed for individualized state control.

### A September neuromodulation perspective proposes amplification principles but reports no new experimental data

- Event date: 2026-09-04
- Sources: `S9`
- Observed fact: A Nature Neuroscience perspective published September 4, 2026 proposed restorative normalization and compensatory amplification as frameworks for future neuromodulation. It identified multiple realizability, multiscale neuroplasticity, precision readiness, and activity selectivity as conditions for effective amplification. The article states that no new data were generated or reported.
- Significance: This is counterevidence against treating cognitive amplification or engineered mental states as an established capability. The article frames enhanced or redirected brain function as a design hypothesis requiring target selection, stratified treatment, and testable protocols. It supports the interpretation that reliable control of complex mental states remains dependent on unresolved precision and selectivity problems rather than demonstrated general-purpose capability.

### A federal biotechnology commission identifies signal degradation, implant limitations, regulatory uncertainty, and absent reimbursement as commercialization bottlenecks

- Event date: 2026-09-02
- Sources: `S10`
- Observed fact: On September 2, 2026, the National Security Commission on Emerging Biotechnology published an analysis of U.S. BCI development. It identified signal degradation, current implant approaches, microchip functionality, inadequate shared data infrastructure, an unclear FDA approval pathway, and the absence of active CMS reimbursement coverage for implantable BCIs as barriers to commercialization. The commission recommended new federal coordination, additional research, clearer FDA guidance, faster but rigorous clinical trials, and explicit inclusion of BCIs in FDA and CMS programs.
- Significance: This is direct counterevidence to assumptions that impressive laboratory demonstrations will naturally become widely deployable systems. The bottlenecks affect technical reliability, clinical evidence generation, regulatory approval, payment, and investment incentives simultaneously. They also weaken the near-term case for high-bandwidth bidirectional BCIs becoming broadly available outside highly supported research environments.

### Neural-data governance is still being drafted rather than operationalized as enforceable neuro-rights protection

- Event date: 2026-09-07
- Sources: `S11`
- Observed fact: The United Kingdom Information Commissioner’s Office lists neurotechnology and neurodata guidance as still in the drafting stage. Its public consultation is scheduled for October 2026 and final publication is listed for winter 2026–2027. During the September 7, 2026 priority-window endpoint, the guidance therefore had not yet been issued as final operational guidance.
- Significance: This narrows optimistic interpretations of PS-NEURO-002 and the neuro-rights lane by showing that institutional governance is lagging behind technological development. The absence of final guidance does not prove that neural data are unprotected, but it indicates that detailed, technology-specific interpretation of existing data-protection law remains incomplete in at least one major regulatory jurisdiction.

### Neural-data protection concerns extend beyond ordinary health-data privacy because raw recordings may support unintended retrospective inference

- Event date: 2026-07-27
- Sources: `S12`
- Observed fact: A Communications Medicine review explains that implantable BCI data can include raw neural recordings, processed features, decoded inferences, and personalized model parameters. It identifies gaps in existing protections involving conventional de-identification, individual control, conflated consent, misuse guardrails, and ownership. It further notes that real-time safeguards such as keyword unlocking do not reduce the sensitivity of raw signals, because a separate model could potentially be applied retrospectively to infer information the user did not intend to communicate.
- Significance: Although published before the priority window, this is a material counterevidence source for the neuro-rights assumptions because it shows why technical capability and governance risk may scale together. High-bandwidth decoding can increase not only useful communication but also the possibility of secondary inference, function creep, and loss of control over mental privacy. This challenges the assumption that consent interfaces or decoder-level safeguards alone can preserve agency.

### The strongest September evidence still concentrates on narrow therapeutic or motor use cases rather than affective or sensory-rich two-way communication

- Event date: 2026-09-07
- Sources: `S10`, `S8`
- Observed fact: The September 2026 search identified clinical and policy materials focused on motor rehabilitation, cursor or assistive-device control, therapeutic stimulation, neural biomarkers, and infrastructure constraints. The newly identified September 2 neurostimulation study concerned treatment-resistant depression biomarkers, while the September 2 federal analysis described BCI examples such as prosthetic-limb control and sensory restoration but emphasized unresolved commercialization barriers. No independently verified study located in the priority window demonstrated durable human two-way communication carrying decoded affect, emotion, or rich sensory experience between a person and an AI system.
- Significance: This is a negative search result that materially narrows PS-NEURO-001. High telemetry bandwidth or bidirectional hardware announcements should not be treated as evidence that the complete chain—stable neural recording, robust decoding, meaningful stimulation, user learning, long-term safety, and affective or sensory usefulness—has been demonstrated in humans.

## Assumption Assessments

### PS-NEURO-001: High-bandwidth neural interfaces connect people and AI

- Proposed verdict: **mixed**
- Confidence: **high**
- Sources: `S1`, `S2`, `S3`, `S4`, `S10`, `S12`
- Evidence: Evidence strengthens the telemetry and clinical-translation components: a peer-reviewed study reported up to 500 Mbps transmission in phantom and ex vivo tests, while an investigational fully implantable BCI received a second FDA Breakthrough Device designation for communication and rehabilitation. Generative reconstruction of subcortical signals from cortical recordings also supports progress toward closed-loop systems. However, these findings do not demonstrate chronic human implantation, end-to-end bidirectional operation, durable sensory or emotional exchange, long-term safety, or clinically useful affective decoding. Regulatory, reimbursement, signal-degradation, and commercialization barriers remain substantial.
- Real-world implication: High-bandwidth neural interfaces are technically advancing, but current evidence supports narrow research and therapeutic applications rather than safe, broadly deployable neural communication with AI. Claims about rich sensory or emotional two-way communication remain unverified, and chronic safety, privacy, reliability, and access require further evidence.
- PostSingularity implication: A post-singularity setting could plausibly support rich human-AI neural exchange if the unresolved translation chain is solved, but the present evidence does not justify treating that capability as established. The storyworld should distinguish telemetry capacity and investigational bidirectional devices from mature, safe, emotionally or sensorially rich interfaces.

### PS-NEURO-002: Engineered mental states become a governance problem

- Proposed verdict: **strengthened**
- Confidence: **medium**
- Sources: `S2`, `S6`, `S7`, `S8`, `S9`, `S11`, `S12`
- Evidence: Bioethics research directly links BCIs and deep-brain stimulation to agency, privacy, authenticity, responsibility, and trust. Neural-data governance analysis identifies risks involving raw recordings, unintended retrospective inference, consent, ownership, control, and misuse. The ICO still listed neurotechnology and neurodata guidance as under development. Technical evidence shows progress toward adaptive neural-state inference and cognitive neuromodulation, but mood and complex mental-state control remain preliminary, exploratory, and insufficiently precise or replicated.
- Real-world implication: The governance problem is becoming more concrete even before reliable general-purpose mental-state control exists. Policymakers and developers face emerging questions about mental privacy, consent, dependency, responsibility, data ownership, and the legitimacy of adaptive stimulation, while enforceable technology-specific protections remain incomplete.
- PostSingularity implication: If post-singularity systems make mood, reward, or immersive-state control reliable, the existing agency and neural-privacy concerns would become central political and social institutions rather than peripheral clinical ethics. The evidence supports a storyworld in which governance pressure precedes, and may shape, mature mental-state engineering.

### PS-AI-003: AI influence drives stronger provenance and audit systems

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: The supplied evidence addresses BCI performance, neural-data protection, regulatory barriers, and neurotechnology governance, but it does not document a material development in AI provenance systems, content authentication, model audit adoption, verification rituals, or graduated oversight. No supplied source establishes that AI influence has produced stronger general provenance and audit systems.
- Real-world implication: The assumption remains unassessed on the current record. Existing neural-data and BCI governance concerns may be relevant by analogy, but they do not establish broader societal adoption of AI provenance or audit infrastructure.
- PostSingularity implication: A post-singularity society might require extensive provenance and audit systems, but the supplied evidence cannot determine whether those systems emerge, how widely they are adopted, or whether they remain effective under highly capable AI.

### PS-SPACE-001: AI and abundant energy enable sustained off-world settlement

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: No supplied source provides audited evidence about launch costs, orbital station duration, closed-loop life support, in-space manufacturing, autonomous mission operations, propulsion improvements, or sustained off-world communities. The evidence set is concentrated on neurotechnology and does not assess this assumption.
- Real-world implication: There is no basis in the supplied record to update the forecast for practical long-duration orbital or off-world settlement. The claim remains dependent on unresolved engineering, health, reliability, and economic milestones not covered here.
- PostSingularity implication: The assumption may remain plausible in a post-singularity setting with advanced autonomy, energy, and manufacturing, but no supplied evidence supports a directional update or establishes that such settlement is practical.

### PS-SOCIAL-002: Analog practices persist as a counterweight to integration

- Proposed verdict: **insufficient-evidence**
- Confidence: **low**
- Sources: None
- Evidence: The supplied evidence does not report trends in device-free spaces, right-to-disconnect policy, analog-media growth, tactile practices, or low-technology communities. Neurotechnology privacy and agency concerns provide a possible rationale for resistance to integration, but they do not demonstrate that analog practices are persisting or expanding.
- Real-world implication: The assumption cannot be updated from the audited record. Cultural persistence or revival of analog practices requires separate social, market, and policy evidence rather than inference from neurotechnology governance concerns alone.
- PostSingularity implication: Analog practices could function as deliberate safeguards for agency and meaning in a highly integrated society, but the supplied evidence does not establish their prevalence, durability, or social importance in a post-singularity world.

## Canon Implementation Plan

### `worldbible/technologies/neural-links.md` -> Summary

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S10`, `S12`
- Why this location: The evidence supports major progress in neural telemetry, inferred deep-brain signals, and investigational bidirectional devices, but it does not establish chronic human implantation, end-to-end operation, rich sensory or affective exchange, or broad deployment. The existing summary presents neural links as safe, deeply personalized shared realities without distinguishing demonstrated capability from mature storyworld capability.
- Proposed change: Retain the existing claims about direct nervous-system communication and shared realities, but add a qualification stating that high-bandwidth telemetry and bidirectional systems remain dependent on unresolved chronic-implant safety, signal stability, power, decoding, stimulation, privacy, regulatory, and access constraints in the evidence base. Clarify that rich affective or sensory exchange is an established storyworld capability rather than a capability demonstrated by the cited real-world developments.
- Implementation steps:
  1. Insert the qualification immediately after the existing Summary description of neural links, using the Summary heading as the anchor.
  2. Preserve the existing capability list and emotional-regulation claim; add a distinct sentence separating telemetry capacity and investigational therapeutic systems from validated end-to-end human neural communication.
  3. Cross-reference Trust Fabrics or relevant consent material only if the repository already provides an appropriate existing link; do not introduce an unsupported new technology claim.
  4. Review the final wording against the Function and Philosophical Tensions sections so that safety and consent language does not imply that all neural-link use is clinically validated or universally safe.
- Dependencies or conflicts:
  - The statement that neural links are safe and bound by emotional regulation systems may conflict with the evidence’s unresolved long-term safety, tissue-response, and failure-mode limitations; reviewers must decide whether that statement is fictional mature-canon technology or should be narrowed.
  - The 500 Mbps result concerns phantom, ex vivo, and brain-on-a-chip testing rather than a complete human neural link; it must not be represented as chronic human performance.
  - The existing Story Use examples presume reliable neural-link functionality and can remain valid as post-singularity canon, but they should not be used as evidence that current real-world systems already support immersive affective exchange.
  - Privacy Drift and Trust Fabrics contain related claims about exposure, consent, and oversight that may need terminology alignment if this qualification is expanded.

### `worldbible/technologies/neural-links.md` -> Function

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **extends**
- Assumptions: `PS-NEURO-001`
- Sources: `S1`, `S2`, `S3`, `S4`, `S10`, `S12`
- Why this location: The audited evidence adds specific intermediate capabilities that fit the neural-link function: high-capacity telemetry, cortical reconstruction of subcortical signals, and investigational movement-intention decoding with therapeutic stimulation. These developments extend the technical pathway without proving the existing document’s full sensory, emotional, or identity-shifting capability as a real-world analogue.
- Proposed change: Add a short subsection or bullet group under Function describing neural links as including high-bandwidth telemetry, inferred neural-state reconstruction, and bidirectional therapeutic or communication pathways in advanced research contexts. Mark these as intermediate or investigational capabilities and explicitly state that reliable decoding of affect, rich sensory exchange, chronic safety, and end-to-end human performance remain unresolved outside the post-singularity setting.
- Implementation steps:
  1. Place the new bullets within Function after the existing list of neural-link uses, using Function as the exact insertion anchor.
  2. Use terminology consistent with the existing document: neural links, streamed emotional states, sensory input, and emotional regulation systems.
  3. Add a cross-reference to Trust Fabrics or AI Agents only where it clarifies consent, auditability, or emergency override; avoid implying that the cited studies demonstrated those social systems.
  4. Review Summary and Story Use after insertion to ensure the new technical distinctions do not duplicate or contradict the existing narrative examples.
- Dependencies or conflicts:
  - AI Agents states that significant actions require explicit intent pings and that emergency overrides are rare; any new neural-link control language should preserve that consent model.
  - Trust Fabrics presents transparency and resonance oversight as established social infrastructure, whereas S10 and S12 describe real-world regulatory and data-governance gaps; the repository should distinguish fictional institutions from contemporary evidence.
  - PS-NEURO-001 is mixed rather than wholly challenged: the proposed edit should preserve mature post-singularity capability while narrowing any implication that present-day research has already achieved it.

### `philosophy/bliss-divergence.md` -> Philosophical Tensions

- Priority: **medium**
- Recommendation: **revise**
- Evidence relationship: **qualifies**
- Assumptions: `PS-NEURO-002`
- Sources: `S2`, `S6`, `S7`, `S8`, `S9`, `S11`, `S12`
- Why this location: The evidence strengthens the relevance of agency, authenticity, mental privacy, consent, ownership, secondary inference, and adaptive-stimulation governance to bliss technologies. At the same time, preliminary biomarkers and unresolved precision constraints show that reliable individualized mood or complex mental-state control is not established in the audited record.
- Proposed change: Add a paragraph to Philosophical Tensions explaining that the debate over bliss is also a debate over agency and neural-data control: adaptive systems may infer or alter states beyond a user’s explicit intention, while raw neural data can support later unintended inference. Qualify the existing premise of safe, regulated bliss by distinguishing fictional mature regulation from the unresolved real-world validation, precision, consent, and governance problems identified by the evidence.
- Implementation steps:
  1. Insert the new paragraph after the existing questions about effort, social limits, and civilization, using Philosophical Tensions as the anchor.
  2. Retain the existing concepts of Emotional Integrity Contracts and Memory Threads, but explain that these mechanisms address consent and accountability rather than automatically solving decoder error, retrospective inference, ownership, or dependency.
  3. Cross-reference Neural Links and Trust Fabrics if links are available in the repository’s established terminology; the cross-references should point to existing files rather than create new ones.
  4. Review Cultural Effects after the philosophical edit so the social split between permanent exit, periodic bliss, and refusal reflects both voluntary choice and concerns about coercion, authenticity, and data-mediated influence.
- Dependencies or conflicts:
  - The existing Function heading says bliss exits are regulated and recorded; this may conflict with the evidence’s observation that technology-specific neurodata protections remain incomplete, unless the regulation is explicitly treated as mature post-singularity canon.
  - The existing Summary calls neural immersion safe and restorative; reviewers should decide whether safety is an in-world settled fact or whether the summary should acknowledge residual risks for contested or experimental bliss systems.
  - PS-NEURO-002 is strengthened primarily as a governance and ethical concern, not as evidence that reliable mood, reward, or immersive-state engineering already exists.
  - AI Trust and Trust Fabrics may need terminology alignment if Emotional Integrity Contracts are intended to provide stronger protections than the repository’s general provenance and oversight systems.

### `philosophy/bliss-divergence.md` -> Cultural Effects

- Priority: **low**
- Recommendation: **debate**
- Evidence relationship: **extends**
- Assumptions: `PS-NEURO-002`
- Sources: `S6`, `S7`, `S8`, `S9`, `S11`, `S12`
- Why this location: The existing cultural split around permanent exit and periodic bliss can be extended by the evidence’s concrete concerns about agency, responsibility, privacy, authenticity, and unequal governance maturity. These concerns do not prove a new social faction, but they provide a defensible basis for adding one as a debated cultural consequence.
- Proposed change: Add a bullet stating that some citizens oppose bliss systems because neural-state inference, adaptive stimulation, and persistent neural records may weaken mental privacy or make authentic consent difficult to verify. Add a contrasting bullet for advocates who treat audit trails, consent contracts, and adaptive safeguards as sufficient protection, while noting that the adequacy of those safeguards remains contested.
- Implementation steps:
  1. Append the two cultural-effect bullets under Cultural Effects without removing the existing three-way social split.
  2. Use the terms mental privacy, authenticity, consent, and adaptive stimulation consistently with the Philosophical Tensions addition.
  3. Review AI Trust and Trust Fabrics for existing language about public logs, verification, and accountability before finalizing any duplicated cultural terminology.
  4. Keep the additions framed as in-world factions or debates rather than as claims that a specific real-world regulation has been enacted.
- Dependencies or conflicts:
  - The proposed factions could overlap with the existing group that refuses bliss as emotional suicide; reviewers should distinguish refusal of emotional substitution from refusal of neural-data surveillance or uncertain consent.
  - The evidence does not establish a binding neuro-rights regime, so the text should not imply that the fictional Emotional Integrity Contracts are universally accepted or legally sufficient.
  - No new population-level evidence establishes the prevalence of these factions; the change is a thematic extension suitable for debate, not a quantified demographic claim.

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

- Whether the 500 Mbps telemetry result can survive chronic human implantation while maintaining safety, power efficiency, signal integrity, and stable tissue response.
- Whether above-chance reconstruction of subcortical signals can achieve clinically adequate accuracy and robustness under distribution shift, stimulation artifacts, and prospective closed-loop use.
- Whether any current investigational BCI will demonstrate durable, useful two-way communication involving decoded affect, emotion, or rich sensory experience.
- The size, duration, replication, and causal status of reported neuromodulation effects on cognition or depression.
- How quickly neurotechnology-specific governance moves from conceptual analysis and draft guidance to enforceable rights and operational standards.
- Whether AI influence is producing measurable adoption of provenance, audit, and verification systems outside the supplied neurotechnology context.
- Whether autonomous systems, launch economics, life-support closure, and human health constraints permit sustained off-world communities.
- Whether analog and low-technology practices are growing, stable, or declining across generations and jurisdictions.
- No direct contradiction was identified between the two packets’ measured findings. The packets are complementary: one reports technical, clinical, regulatory, and bioethics developments, while the other narrows their interpretation through preliminary biomarkers, policy barriers, draft governance, and negative search results.
- The CorTec announcement reports an FDA Breakthrough Device designation, while the available evidence does not include a public FDA designation record containing clinical performance details. This is a source-verification limitation, not a demonstrated contradiction.
- The telemetry paper reports up to 500 Mbps in phantom and ex vivo tests, while the counterevidence packet reports no independently verified human demonstration of durable, high-bandwidth two-way communication involving decoded affect, emotion, or rich sensory experience. These claims concern different stages of translation and are not contradictory.
- The ICO source indicates that neurotechnology and neurodata guidance remained under development; this does not contradict the existence of existing UK data-protection law, but it does limit claims about finalized technology-specific neuro-rights protection.
- The evidence window is August 31–September 7, 2026. The Communications Medicine source was published July 27, 2026 and is retained as background evidence rather than a new priority-window event.
- The telemetry result is from phantom tests, ex vivo cadaver-head experiments, and brain-on-a-chip models; it is not a human or chronic-animal implant demonstration.
- The telemetry paper reports a telemetry subsystem, not an end-to-end bidirectional BCI that records, decodes, stimulates, and supports useful behavior.
- Long-term tissue response, implant migration, power delivery, electromagnetic compatibility, and clinical reliability remain untested.
- The generative model’s performance was above chance, but the finding does not establish clinically adequate accuracy, robustness, or stimulation benefit.
- The model reconstructs neural signals; it does not demonstrate prospective human closed-loop stimulation controlled by the reconstructed signals.
- The patient data came from people already undergoing invasive procedures, so generalization to implanted therapeutic systems and routine outpatient use is unresolved.
- Inference errors, distribution shift, stimulation artifacts, and model failure modes could produce inappropriate stimulation.
- The CorTec source is a company announcement rather than an FDA public authorization record or peer-reviewed clinical-results paper.
- Breakthrough Device designation accelerates interaction and review; it does not establish safety, effectiveness, or approval.
- The CorTec announcement provides no new quantitative decoding performance, participant count, follow-up duration, stimulation outcomes, or adverse-event data.
- Commercial availability and long-term support remain unresolved.
- The University of Florida evidence is from rats, not humans.
- The device is reported near the sciatic nerve rather than implanted in the brain or spinal cord.
- The researchers state that large-animal or human testing is the next step and that miniaturization for human testing remains in progress.
- The release does not provide detailed stimulation-dose, durability, functional-benefit, or long-term biocompatibility data.
- The Nexalin source is a company announcement about a secondary analysis of previously published trial data, not the primary peer-reviewed report of the new analysis.
- The announcement does not provide the full sample size, confidence intervals, multiplicity controls, effect sizes by domain, or complete adverse-event analysis.
- The result is not evidence that the device can reliably engineer subjective mood, reward, emotion, or immersive experience.
- The planned U.S. pilot study had not yet established efficacy or regulatory approval in the cited announcement.
- The bioethics paper is conceptual and does not establish a new legal right, regulation, technical safeguard, or measured population-level effect.
- It does not test whether users actually experience reduced agency under a particular implant or stimulation protocol.
- The connection to enforceable neuro-rights policy remains indirect.
- The work does not resolve how responsibility should be allocated among patients, clinicians, manufacturers, and adaptive algorithms.
- The TMS-EEG finding concerns treatment-resistant depression and TMS-EEG, not implantable BCI control of mood, reward, emotion, or immersive experience.
- The reported predictor was exploratory and uncorrected for multiple correlational tests.
- The neural estimate was indirect because deep medial source localization was performed with 64-channel scalp EEG.
- The finding was not prospectively validated and was not replicated across sites or independent cohorts.
- The study did not establish that the physiological change caused the clinical improvement.
- The Nature Neuroscience source is a perspective rather than a new clinical or laboratory experiment.
- It does not quantify effect sizes, safety margins, durability, or replication rates for amplification.
- Its framework is primarily relevant to therapeutic restoration and compensation, not consumer or coercive mental-state engineering.
- The article does not test subjective experience, reward, emotional valence, dependency, or consent outcomes.
- The NSCEB analysis is an expert-policy assessment derived from a prior convening rather than a controlled empirical study.
- The commission’s statement that the FDA pathway is unclear is an institutional judgment and may not apply equally to every BCI architecture or indication.
- The release does not provide device-specific failure rates, cost estimates, or reimbursement projections.
- The findings primarily concern the U.S. policy and commercialization environment and may not generalize to China, Europe, or other jurisdictions.
- The ICO timetable is not evidence that all existing UK data-protection law fails to apply to neural data.
- The page describes planned guidance rather than a legal ruling, enforcement action, or statutory gap analysis.
- The finding concerns the United Kingdom and cannot be generalized to every jurisdiction.
- A pending consultation can itself be evidence of active governance development rather than permanent regulatory failure.
- The Communications Medicine review was published before August 31, 2026 and is included as background evidence rather than a new priority-window event.
- The article describes plausible governance and security risks; it does not report a demonstrated real-world attack on an implanted BCI dataset.
- The severity of the risk varies by sensor type, decoder, effector, recording duration, and intended use.
- Some claims about retrospective inference remain technically contingent on future models and data quality.
- No clearly verified new statute, regulation, treaty, or binding standard specifically establishing neuro-rights was identified within August 31–September 7, 2026.
- The search found discussion of European neurodata governance and existing GDPR/EU AI Act mechanisms, but no primary government record in the window confirming a new neuro-rights rule or enforcement action.
- No new human clinical dataset in the window was found that demonstrated durable, high-bandwidth two-way communication involving decoded affect, emotion, or sensory experience beyond motor, communication, or therapeutic stimulation use cases.
- Several high-visibility company claims surfaced, including consumer brain wearables and proposed nanoparticle BCIs, but the available evidence was announcement-level or preclinical and did not meet the threshold for a material measured finding.
- The September 7, 2026 Brain2Qwerty event listing described a reported non-invasive MEG decoding result, but the underlying peer-reviewed study was published June 29, 2026, outside the priority window; it was not counted as a new window-period development.
- No priority-window failed replication was located that directly invalidated a named intracortical BCI decoding result; the strongest negative evidence instead concerned small samples, exploratory biomarkers, absent external validation, and unresolved deployment barriers.
- No verified safety incident, explantation dataset, chronic tissue-response study, or long-term adverse-event report specific to a newly announced September 2026 high-bandwidth BCI system was identified.
- No public FDA record located in this search provided device-specific clinical performance, adverse-event, or reimbursement information for the investigational systems discussed in September announcements.
- No binding international neuro-rights treaty or new federal U.S. statute enacted during August 31–September 7, 2026 was identified. The strongest governance evidence consisted of draft guidance, policy analysis, and recommendations rather than enforceable new rights.
- The ICO page provides a regulatory timetable but not a final legal interpretation of whether existing UK law adequately protects neural data; a future consultation record and final guidance are needed.
- The search did not establish whether any commercial BCI company has achieved sustainable unit economics, insurance coverage, maintenance logistics, or equitable access at population scale.
- The search did not resolve whether wireless telemetry architectures that perform well in phantom, ex vivo, or model systems can maintain safety and performance under chronic human implantation, tissue growth, motion, power constraints, and repeated stimulation.
- A telemetry subsystem demonstrated an end-to-end bidirectional BCI that records, decodes, stimulates, and supports useful behavior in humans.
- The 500 Mbps telemetry result demonstrated chronic human implant performance, long-term tissue safety, reliable power delivery, electromagnetic compatibility, implant stability, or clinical reliability.
- Generative reconstruction of subcortical signals demonstrated clinically adequate accuracy, prospective human closed-loop stimulation, stimulation benefit, or routine outpatient deployment.
- CorTec’s Breakthrough Device designation established FDA approval, marketing authorization, efficacy, safety, commercial availability, or long-term support.
- The injectable peripheral nerve implant demonstrated human, brain, spinal-cord, or durable functional-benefit outcomes.
- The Nexalin exploratory secondary analysis demonstrated reliable engineering of subjective mood, reward, emotion, or immersive experience, or established efficacy of the planned U.S. pilot study.
- The bioethics paper established a new legal right, regulation, technical safeguard, or enforceable neuro-rights protection.
- The exploratory TMS-EEG biomarker demonstrated a validated biomarker, causal mechanism, independent replication, or dependable closed-loop controller for individualized mood or mental-state control.
- The Nature Neuroscience perspective demonstrated cognitive amplification, engineered mental states, subjective experience modification, reward control, emotional-valence control, dependency, or consent outcomes.
- The NSCEB policy analysis established device-specific failure rates, cost estimates, reimbursement projections, or a universally applicable FDA pathway assessment.
- The ICO timetable demonstrated that existing UK data-protection law fails to protect neural data or that final enforceable neuro-rights guidance was in place during the priority window.
- The Communications Medicine review demonstrated a real-world attack on an implanted BCI dataset or established that retrospective inference is inevitable across all sensor types, decoders, effectors, recording durations, or intended uses.
- No independently verified September 2026 human study was found demonstrating durable, high-bandwidth two-way communication involving decoded emotion, affect, or rich sensory experience.
- No priority-window failed replication was located that directly invalidated a named intracortical BCI decoding result.
- No verified safety incident, explantation dataset, chronic tissue-response study, or long-term adverse-event report specific to a newly announced September 2026 high-bandwidth BCI system was identified.
- No binding international neuro-rights treaty or new federal U.S. statute enacted during August 31–September 7, 2026 was identified.
- The search did not establish whether any commercial BCI company has achieved sustainable unit economics, insurance coverage, maintenance logistics, or equitable access at population scale.
- PS-AI-003 was assessed as insufficient-evidence with low confidence. The supplied sources do not document developments in AI provenance, content authentication, model-audit adoption, verification rituals, or graduated oversight, so no repository edit is warranted. The existing Trust Fabrics and AI Trust files remain relevant canon but should not be revised on the basis of analogy to neural-data governance alone.
- PS-SPACE-001 was assessed as insufficient-evidence with low confidence. None of the supplied sources addresses launch costs, orbital habitation, life-support closure, in-space manufacturing, propulsion, autonomous missions, or sustained off-world communities. No directional repository change is supported.
- PS-SOCIAL-002 was assessed as insufficient-evidence with low confidence. The evidence does not measure device-free spaces, right-to-disconnect policy, analog-media growth, tactile practices, or low-technology communities. Neural-privacy concerns may motivate such practices in fiction, but they do not justify editing the timeline or analog-revival canon without separate social evidence.
- The assessed NEURO-001 and NEURO-002 developments are mixed or qualifying rather than direct contradictions of the post-singularity canon. The proposed edits preserve the storyworld’s mature capabilities while separating them from present-day evidence about telemetry, investigational systems, preliminary biomarkers, and incomplete governance.
- No supplied evidence supports adding a new timeline event. The developments are too narrow, preliminary, or externally focused to justify changing PS Timeline chronology, and doing so would risk converting research signals into established historical canon.

## Watchlist

- Chronic human-implant studies reporting channel count, bandwidth, thermal load, tissue response, migration, explantation, and adverse events.
- Prospective demonstrations of end-to-end bidirectional BCI operation, especially sensory feedback, affect decoding, and AI-mediated neural stimulation.
- Independent replication and clinical validation of reconstructed subcortical biomarkers and adaptive stimulation controllers.
- Final neurotechnology and neurodata guidance from the UK ICO, along with binding laws, enforcement actions, or standards addressing neural-data ownership, consent, and secondary inference.
- FDA authorization records, clinical outcomes, reimbursement decisions, and long-term follow-up for fully implantable BCI systems.
- Audited evidence of AI provenance standards, model-audit requirements, content-authentication adoption, and institutional oversight of high-impact AI.
- Launch-cost trends, habitat-duration records, life-support closure rates, in-space manufacturing demonstrations, and autonomous off-world mission performance.
- Surveys, market data, policy enactments, and demographic studies tracking device-free spaces, right-to-disconnect rules, analog media, and low-technology communities.

## Sources

- `S1` [An Event based Body Coupled Transdural Telemetry for Intracortical Brain Computer Interfaces](https://www.nature.com/articles/s44172-026-00735-z) — Communications Engineering / Nature Portfolio; 2026-09-01; primary-research; URL supplied in structured research output. Primary research reporting quantitative bandwidth, error-rate, compression, thermal, and safety results for a telemetry architecture intended for high-density intracortical BCIs.
- `S2` [Generative deep learning reconstructs subcortical neural signals from cortical recordings for closed-loop brain stimulation](https://www.nature.com/articles/s41746-026-03173-5) — npj Digital Medicine / Nature Portfolio; 2026-09-01; primary-research; URL supplied in structured research output. Primary clinical-data study quantifying reconstruction across 723 hours and 49 patients, directly addressing adaptive DBS and neural-state decoding.
- `S3` [CorTec Receives Second FDA Breakthrough Device Designation for Brain Interchange](https://www.webdisclosure.com/press-release/cortec-gmbh-etr-cortec-receives-second-fda-breakthrough-device-designation-for-brain-interchange-MkxNs0M6Rmp) — CorTec GmbH / EQS News; 2026-08-31; official-release; URL supplied in structured research output. First-party announcement of the FDA designation and the device’s proposed communication and rehabilitation indications.
- `S4` [Breakthrough Devices Program](https://www.fda.gov/medical-devices/how-study-and-market-your-device/breakthrough-devices-program) — U.S. Food and Drug Administration; unknown; regulatory; URL supplied in structured research output. Provides the regulatory meaning and limitations of Breakthrough Device designation, including that designation is distinct from marketing authorization.
- `S5` [Pioneers in pain relief: UF-led research team tests injectable, battery-free neural implants](https://news.ufl.edu/2026/09/neural-implants/) — University of Florida; 2026-09-03; official-release; URL supplied in structured research output. Institutional release reporting the animal results, wireless-power architecture, tissue response, and stated translation limits.
- `S6` [Nexalin Technology Announces New Secondary Analysis of Previously Published Clinical Trial Data](https://nexalin.com/nexalin-technology-announces-new-secondary-analysis-of-previously-published-clinical-trial-data-reveals-previously-unreported-improvements-in-memory-comprehension-and-language-function-in-alzheimer/) — Nexalin Technology; 2026-09-03; official-release; URL supplied in structured research output. First-party report of the exploratory cognitive-domain analysis and the company’s proposed next clinical step.
- `S7` [Self-Trust as a Unifying Principle for the Dimensions of Agency in Neurotechnology](https://visualize.jove.com/42671286-self-trust-as-a-unifying-principle-for-the-dimensions-of-agency-in-neurotechnology) — AJOB Neuroscience / JoVE Visualize; 2026-08-31; primary-research; URL supplied in structured research output. Primary bioethics research directly addressing agency, privacy, authenticity, trust, BCIs, and DBS.
- `S8` [Neurophysiological signatures of Stanford Neuromodulation Therapy in treatment resistant depression](https://www.nature.com/articles/s41380-026-03837-4) — Molecular Psychiatry / Nature Portfolio; 2026-09-02; primary-research; URL supplied in structured research output. Primary randomized-trial secondary analysis that directly documents the small sample, exploratory biomarker status, source-localization limits, and need for independent replication.
- `S9` [Neuromodulation for restoring and amplifying brain function](https://www.nature.com/articles/s41593-026-02434-6) — Nature Neuroscience; 2026-09-04; primary-research; URL supplied in structured research output. Peer-reviewed perspective published inside the priority window that explicitly identifies unresolved precision and selectivity conditions and confirms that it contains no new data.
- `S10` [NSCEB Releases Analysis for Securing U.S. Leadership in Brain-Computer Interfaces](https://www.biotech.senate.gov/press-releases/nsceb-releases-analysis-for-securing-u-s-leadership-in-brain-computer-interfaces/) — National Security Commission on Emerging Biotechnology / U.S. Senate; 2026-09-02; official-release; URL supplied in structured research output. Official policy analysis listing technical, data, regulatory, reimbursement, and commercialization barriers for implantable BCIs.
- `S11` [Technology: ICO plans for new and updated guidance](https://ico.org.uk/about-the-ico/what-we-do/our-plans-for-new-and-updated-guidance/technology/) — Information Commissioner’s Office; unknown; regulatory; URL supplied in structured research output. Official regulatory planning page showing that neurotechnology and neurodata guidance remained under development, with consultation and finalization scheduled after the priority window.
- `S12` [Advancing data protections for implantable brain-computer interfaces](https://www.nature.com/articles/s43856-026-01797-y) — Communications Medicine / Nature Portfolio; 2026-07-27; primary-research; URL supplied in structured research output. Peer-reviewed governance analysis identifying concrete gaps in consent, ownership, individual control, de-identification, and misuse protection for implantable BCI data.

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
  "id": "research_2026-09-07_brain-computer-interfaces-neurostimulation-neura",
  "type": "research_brief",
  "name": "Neurotechnology Evidence Review: Neural Interfaces, Neurostimulation, Neural Decoding, and Neuro-Rights",
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
