---
name: Izgin Ozdas
nationality: Turkish
base: London, United Kingdom
languages:
  - language: Turkish
    proficiency: native_or_bilingual
  - language: English
    proficiency: native_or_bilingual
  - language: French
    proficiency: elementary

# Compatibility fields used by existing skills. The fuller current-state record
# is under current_activity.
current_employer: Entrepreneurs First
current_role: Founder in Residence | The Bridge
# Accenture ended Aug 2026 (LinkedIn export, Positions.csv). Kept here because
# skills that read current_employer for outreach copy must not still say "at Accenture".
previous_employer: Accenture UK & Ireland (Sep 2025 - Aug 2026)
current_focus: Building at the intersection of AI, engineering, and industrial systems; currently in Entrepreneurs First's The Bridge residency in San Francisco; paired with cofounder Christian Bakhos (founders/christian-bakhos.md) on 2026-08-23.
last_updated: 2026-08-23

# Per-founder outreach identity. The single author for facts the outreach skills
# used to hardcode: which LinkedIn account this founder's contacts live on, the
# credibility hook used in copy, and a booking link (recorded only for contacts who
# ask for one — scheduling links are banned from outreach copy by the copy rules).
outreach_identity:
  linkedin_account: Izgin
  credibility_hook: "cambridge paper"
  booking_url: "https://calendly.com/0izzyozzy0/coffee-chat-w-izzie"
  # Every contact reads this before they read the message; copy should not contradict it.
  public_headline: "Founder @EF | Manufacturing & Robotics"
  listed_industry: Commercial and Service Industry Machinery Manufacturing
  # Unset on purpose: the export lists an IMTEK work address and a personal one,
  # and the founder uses a third elsewhere. Which address receives outreach replies
  # is a founder decision, not one to infer from LinkedIn's primary-address flag.
  # See private/linkedin-export/ for the addresses themselves.
  reply_email: ""

# Current or imminent commitments. "Incoming" is kept distinct from experience
# already completed.
current_activity:
  - organization: Accenture UK & Ireland
    role: Field Delivery Engineer (FDE)
    title_as_listed: AI Decision Science
    period: 2025-09 to 2026-08
    location: London, United Kingdom
    status: ended
    evidence:
      - existing_founder_record
      - public_profile
      - linkedin_data_export
    notes:
      - Enterprise delivery and applied-AI environment.
      - Ended Aug 2026 on departure for The Bridge; write about it in the past tense.
      - The founder record says "Field Delivery Engineer (FDE)"; LinkedIn lists the position as "AI Decision Science". Both are recorded because outreach copy and a contact's own view of the profile will not match otherwise.
      - Has acted as an AI-native reverse mentor to senior leadership, demonstrating practical AI workflows and how AI-native talent approaches work.

  - organization: ETH Agentic Systems Lab
    role: Builder / research collaborator
    period: 2026-present
    status: current
    evidence:
      - founder_public_announcement
    notes:
      - Publicly described as "currently building" at the lab before relocating to San Francisco.
      - Exact formal title and project scope are not yet recorded; do not infer either in outreach or founder-market-fit claims.

  - organization: Entrepreneurs First
    program: The Bridge (S26)
    role: Founder resident (solo 2026-08 → paired with Christian Bakhos 2026-08-23)
    period: 2026-08-03 to 2026-10-02
    location: San Francisco, California, United States
    status: current
    evidence:
      - founder_public_announcement
      - private_program_material
    notes:
      - Eight-week, full-time company-building residency focused on cofounder formation, market selection, customer evidence, building, and shipping; started 2026-08-03.
      - A first cofounder pairing formed early in the programme and ended in August 2026, along with its joint thesis; treat any pre-split direction as history. On 2026-08-23 Izgin paired with Christian Bakhos (founders/christian-bakhos.md) on the manufacturing-execution-layer idea, which predates the pairing — the current idea lineage is the one in reports/.
      - The programme culminates in an Investment Committee; participation is confirmed, but investment is not.

# Machine-readable affiliations used by scoring and outreach skills for
# affiliation_boost. Include only relationships Izgin can legitimately reference.
affiliations:
  - type: education
    institution: University of Cambridge
    school: Department of Engineering / Institute for Manufacturing
    program: MPhil Industrial Systems, Manufacturing & Management
    period: 2024-10 to 2025-08
    location: Cambridge, United Kingdom
    college: Hughes Hall
    degree_as_listed: Master of Philosophy - MPhil
    societies:
      - University Riding Club
    notes:
      - Mapped end-to-end manufacturing software stacks and the broken digital thread across disconnected CAD-CAM systems.
      - Built and validated a Python/LLM interoperability proof of concept using RAG and zero-/few-shot prompting.
      - Reported 100% F1 for DXF metadata annotation and 74% F1 for STEP metadata annotation.
      - Research was being prepared for publication with the Cambridge DIAL Group as of the latest public profile.

  - type: education
    institution: Georgia Institute of Technology
    program: BS Mechanical Engineering
    degree_as_listed: Bachelor of Applied Science - BASc
    period: 2018-08 to 2022-05
    location: Atlanta, Georgia, United States
    societies:
      - HighTech Racing
      - Alpha Kappa Psi
      - Reading Society
      - Philosophy Society
    notes:
      - Completed interdisciplinary engineering and robotics work.
      - HighTech Racing is hands-on student motorsport engineering; it is build experience, not coursework.
      - Returned to the Helping Hand assistive-device problem for the 2022 Capstone Design Expo.

  - type: work
    company: Accenture UK & Ireland
    role: Field Delivery Engineer
    title_as_listed: AI Decision Science
    period: 2025-09 to 2026-08
    location: London, United Kingdom
    notes:
      - Applied-AI and enterprise delivery exposure.
      - Practical experience communicating AI-native working methods to senior leaders.

  - type: research
    institution: ETH Agentic Systems Lab
    role: Builder / research collaborator
    period: 2026-present
    notes:
      - Exact title and project scope remain unverified.

  - type: founder_program
    institution: Entrepreneurs First
    program: The Bridge
    role: Founder in Residence | The Bridge
    period: 2026-08 to present
    location: San Francisco Bay Area, California, United States

  - type: work
    company: IMTEK Cryogenics
    role: Engineering and operations leadership
    period: 2017-2025
    location: Ankara, Türkiye
    date_note: Early documentation/configuration and part-time exposure began in 2017; the core full-time operating period recorded locally is 2022-2024; public project contributions continued into 2025.
    titles_recorded:
      - Documentation & Configuration Engineer
      - Lead Manufacturing Engineer
      - Lead Operations Engineer
      - Deputy General Manager / management responsibility
    notes:
      - Two years of hands-on manufacturing and operating experience during the core 2022-2024 period.
      - Led or contributed to CNC-line robot automation, ERP implementation, technical documentation, product configuration, planning, and operational process design.
      - Worked on cryogenic plants, Stirling/Joule-Thomson cryocoolers, precision manufacturing, thermal management, vacuum systems, automation, and process engineering.
      - Operated around sub-micron component manufacturing, multidisciplinary R&D, product testing, and field-service constraints.
      - Supported product positioning, technical content, international business development, customer communication, and the 2025 IMTEK website/product-configurator relaunch.
      - Published and presented technical work connected to IMTEK's cryocooler program.

  - type: global_science_leadership
    organization: Royal Academy of Science International Trust (RASIT)
    program: Girls in Science 4 SDGs / International Day of Women and Girls in Science Assembly
    role: Youth Representative, peer mentor, coordinating-committee member, and speaker
    title_as_listed: Emerging Technologies & Social Impact Engineer
    period: 2019-06 to present
    location_as_listed: New York City Metropolitan Area
    location: Greater New York City Area / international
    notes:
      - Spoke in the United Nations General Assembly Hall about integrating more women into science.
      - Helped develop policy-oriented questions and strategies concerning government support for women in science and engineering.
      - Participated in and helped coordinate international assemblies connecting science, policy, the SDGs, and youth representation.
      - In 2026, spoke on AI ethics, bias, data sovereignty, energy demands, equitable access to compute, and the need to embed social science early in policymaking.

  - type: research
    organization: Georgia Tech Research Institute (GTRI)
    role: Cryogenics Lab Research Intern
    period: 2021-08 to 2022-05
    location: Georgia, United States
    evidence:
      - linkedin_data_export
    notes:
      - Cryogenics research exposure predating IMTEK, inside a US research institute.
      - Ran concurrently with the Helping Hand capstone period.

  - type: research
    organization: Bilkent University
    role: Research Intern
    period: 2019-06 to 2019-07
    location_as_listed: Bursa, Türkiye
    evidence:
      - linkedin_data_export
    notes:
      - Listed on LinkedIn as Bilkent University, Jun-Jul 2019. The earlier record held "Ozensoy Research Group, May-Jun 2017, Ankara" from a legacy public profile; the Ozensoy group sits within Bilkent, so these are most likely the same internship with the legacy dates and organization label wrong.
      - Unresolved: whether this is one internship or two, and whether the location is Ankara (where Bilkent is) or Bursa as listed. Do not cite the dates in diligence without asking the founder.

  - type: venture
    company: Helping Hand
    role: Founder / inventor
    period: 2016-2022
    notes:
      - Designed an assistive smart-cane concept inspired by a visually impaired family member.
      - The concept used cameras and a tactile/Braille interface to help a visually impaired user interpret surroundings.
      - Filed a Turkish patent in 2017.
      - Continued the problem as an interdisciplinary Georgia Tech capstone project in 2022, focused on safety and independent navigation for visually impaired users.

  - type: leadership
    organization: Alpha Kappa Psi, Epsilon Sigma
    roles:
      - President of Finance
      - President of Marketing
    period: 2019
    location: Atlanta, Georgia, United States

  - type: volunteering
    organization: Rotary International
    role: Fundraising Coordinator
    period: 2016-2020
    cause: Human rights / refugee support
    notes:
      - Helped run fundraising projects providing food and shelter for Syrian refugees awaiting admission paperwork in Türkiye.

  - type: volunteering
    organization: Süleymanhacı Village Library Project
    role: Peer Mentor / project lead
    period: 2016-2017
    notes:
      - Collected 1,500 children's books and helped establish a school library.
      - Led the team that repainted the school environment.

  - type: nationality
    value: Turkish
    boost_rationale: Turkish contacts have responded at higher rates to Turkish outreach; this is a soft-affinity signal, not evidence of individual interest.
    sourcing_bias_cap: >-
      Founder rule 2026-08-26: this affinity affects REGISTER (write in Turkish, match
      the honorific) and nothing else. It must not act as a sourcing bonus — do not let
      it pull Turkish profiles into a batch ahead of better-fitting targets, because it
      had been doing exactly that. ICP fit is scored first and alone; language affinity
      is applied only once a contact already qualifies.

  - type: language
    codes: [en, tr, fr]
    note: English and Turkish are native/bilingual; French is elementary.

# Projects and outputs that demonstrate capabilities beyond titles.
selected_projects_and_outputs:
  - name: Manufacturing CAD-CAM interoperability layer
    context: University of Cambridge MPhil research
    period: 2024-2025
    problem: Repeated manual data entry and broken digital threads across disconnected manufacturing software.
    work:
      - Industry case-study mapping of end-to-end manufacturing software stacks.
      - Python prototype combining LLMs, RAG, and zero-/few-shot prompting.
      - DXF and STEP metadata annotation experiments.
    evidence_of_execution:
      - "DXF metadata annotation: 100% F1 reported."
      - "STEP metadata annotation: 74% F1 reported."

  - name: CNC-line robot automation and ERP implementation
    context: IMTEK Cryogenics operations
    period: 2022-2024
    problem: Manual manufacturing workflows, planning fragmentation, and operational coordination.
    work:
      - Robot automation on CNC production lines.
      - ERP rollout and operating-process implementation.
      - Hands-on manufacturing and cross-functional operations.

  - name: IMTEK digital product and website relaunch
    context: IMTEK Cryogenics
    period: 2025
    work:
      - Led or materially contributed to design iteration, technical copy, product configurators, system specifications, and product storytelling.
      - Coordinated with an external digital partner to translate an engineering-heavy portfolio into a usable commercial interface.

  - name: Helping Hand assistive smart cane
    context: Independent invention and Georgia Tech capstone
    period: 2016-2022
    work:
      - Originated the concept from direct family experience.
      - Developed the camera-to-tactile/Braille interface concept.
      - Filed a patent and later revisited the need through an interdisciplinary capstone team.

  - name: Cryocooler research and commercialization
    context: IMTEK Cryogenics / University of Cambridge
    period: 2023-2025
    work:
      - Technical work around miniature and mid-range Stirling cryocoolers, cold-finger heat losses, cooldown time, power consumption, vibration, and precision manufacture.
      - Helped communicate the product line to technical and commercial audiences.

  - name: Startup Assumption Lab
    context: Personal founder operating system
    period: 2026
    work:
      - Built a structured belief-to-hunch-to-assumption-to-evidence workflow.
      - Added reusable ideation, validation, mutation, interview, outreach, and public-signal-reconnaissance methods.
      - Integrated public-data research across procurement, company, research, hiring, energy, and community sources.

publications_patents_and_speaking:
  - type: conference_paper
    title: Cryocooler research at Imtek Cryogenics
    venue: SPIE Defense + Commercial Sensing
    year: 2025
    authors: [Izgin Ozdas, Engin Ozdas]

  - type: industry_article
    title: HeLIUM Cryogenics Redefines Cryogenic Technology
    venue: Cryogenic Society of America
    year: 2024
    author_role: Lead Manufacturing Engineer, IMTEK Cryogenics

  - type: article
    title: Becoming A Bride Before Becoming An Adult
    venue: Humanium
    year: 2017
    topic: Child marriage awareness in Türkiye

  - type: patent
    title: Braille Walking Stick
    filed: 2017-10-10
    jurisdiction: Türkiye
    identifier_as_publicly_listed: TR 17283JAWI19019268-128868
    verification_note: The LinkedIn data export (2026-08-18) lists the same identifier and a 2017-10-10 filing date, so the two records agree. Both are founder-entered, so this is corroboration, not verification — still check the official patent record before legal or investor use.

  - type: speaking
    venue: United Nations General Assembly Hall / International Day of Women and Girls in Science Assembly
    period: 2019-present
    topics:
      - Women and girls in science
      - Youth representation
      - Science policy and the SDGs
      - AI ethics, bias, data sovereignty, energy demand, and equitable compute access

# Durable, cross-idea technological worldview. Distilled 2026-08-23 from the founder's
# own reflection across many sessions; the founder confirmed it as their view by asking
# for the pitch to be built on it. Ideas move; these mostly do not. Use for pitch framing
# and idea evaluation — never as evidence for any market claim.
worldview:
  one_sentence: >
    AI is making intelligence cheap and general, but the physical world is messy,
    fragmented and stubbornly specific. The next enormous companies will make that
    intelligence usable — connecting it to machines, software, people and infrastructure
    until humans express intent and complex systems execute it.
  contrarian_theses:
    - id: mess_is_the_market
      claim: Brownfield beats greenfield as the real Physical AI opportunity. The installed base — old PLCs, legacy machines, odd ERPs, proprietary protocols, tribal knowledge — is not temporary noise; the mess is the market.
    - id: deployment_scarcer_than_intelligence
      claim: Intelligence generalizes; deployment doesn't. Model capability may improve faster than the world's ability to install, integrate, validate, monitor and maintain it, so value migrates to handling local physical specificity.
    - id: platform_is_the_execution_layer
      claim: Physical AI's dominant platform may be an orchestration / interoperability / execution company rather than a robot maker — the Stripe/AWS layer beneath the robots.
  supporting_beliefs:
    - The world changes when technology can be deployed, not when it is invented.
    - Physical heterogeneity is permanent; whoever abstracts over it gains leverage.
    - Semantic interoperability (intent → interpretation → coordination → execution) is a control point, not middleware.
    - AI moves from tool to operating layer; the intermediate software becomes invisible.
    - Humanoids are downstream of infrastructure, not the whole thesis.
    - Tacit knowledge locked in people is industry's hidden liability; AI can make it persistent, queryable, executable.
    - Infrastructure should adapt to the human, not the reverse — a factory manager should not need to become an ML engineer.
    - SMEs and the long tail matter more to the industrial transition than frontier robotics assumes.
    - The ultimate manufacturing interface is intent ("make this part"), not software navigation.
    - Substance over narrative: the company needs something genuinely hard underneath (industrial knowledge, integration, operational data), with story amplifying it, not substituting for it.
    - Reality over consensus: go touch the system.
  counterweight: >
    Vision without a wedge is dangerous. Every idea must start from a painful problem
    with a buyer, a budget, urgency and measurable ROI — "who signs the first $50k cheque
    and why?" The best ideas appear where the vision and the operator meet.
  moral_direction: >
    Advanced capability should become broadly accessible (SMEs, abundance, reducing
    dependence on scarce experts) rather than concentrated in a handful of giants;
    unresolved on the economics, consistent on the direction.

# Founder-market-fit inputs for belief intake and idea evaluation.
capability_domains:
  - industrial operations
  - brownfield manufacturing
  - high-precision machining
  - cryogenic systems and cryocoolers
  - robotics and production automation
  - ERP and operational process implementation
  - manufacturing software and CAD-CAM interoperability
  - Python prototyping
  - LLM applications, RAG, and prompt-based information extraction
  - enterprise AI delivery
  - hardware product development
  - technical product communication and industrial marketing
  - international business development and partnerships
  - science policy, public speaking, and global convening

# Named tools the founder has personally operated. Kept apart from
# capability_domains, which names domains rather than software. Sourced from the
# LinkedIn skills list, so it records claimed fluency, not assessed depth.
tool_fluency:
  cad_cam:
    - SOLIDWORKS
    - Siemens NX
    - AutoCAD
  simulation_and_analysis:
    - ANSYS
    - Finite Element Analysis (FEA)
    - MATLAB
  manufacturing_floor:
    - CMM operation
    - 3D printing
  rendering:
    - KeyShot
  note: Direct operating experience with the CAD/CAM tools the interoperability work is about is itself a credibility signal with manufacturing contacts.

firsthand_problem_environments:
  - Family-run industrial manufacturer moving from expert-led processes toward scalable systems.
  - CNC and high-precision production where drawings, machine data, ERP records, and operator knowledge do not connect cleanly.
  - Cryogenic hardware sold, installed, and supported across international markets.
  - Brownfield factories where automation must coexist with legacy equipment and tacit operator knowledge.
  - Enterprise delivery environments adopting AI while redesigning how people work.
  - Assistive hardware developed from a close user's lived need.
  - International science-policy forums where technical systems meet ethics, access, and implementation.

founder_market_fit_assets:
  - asset: Rare bridge between physical engineering and applied AI.
    basis: Mechanical engineering, industrial operations, CAD-CAM interoperability research, and enterprise AI delivery.
  - asset: Direct operator empathy in manufacturing.
    basis: Hands-on CNC-line automation, ERP rollout, planning, documentation, testing, and field constraints.
  - asset: Can span prototype, operations, and commercialization.
    basis: Patent/prototype work, manufacturing systems, technical writing, website/product configuration, customer and partner communication.
  - asset: Access to industrial buyers and technical practitioners.
    basis: IMTEK network across cryogenics, laboratories, industrial gases, aerospace/defense, precision manufacturing, and international customers.
  - asset: Cross-border institutional network.
    basis: Türkiye, United Kingdom, United States; Cambridge, Georgia Tech, Accenture, RASIT/UN, ETH, and Entrepreneurs First.
  - asset: Public communication and convening ability.
    basis: UN/RASIT speaking, coordinating committees, technical articles, product storytelling, and founder-community content ideas.
  - asset: Personal motivation toward ambitious, technically difficult company-building.
    basis: Repeated return to hardware, industrial systems, frontier engineering, and founder programs from adolescence through the present.

likely_unfair_access:
  sectors:
    - cryogenics
    - laboratory and industrial gas generation
    - precision manufacturing
    - industrial automation
    - manufacturing software
    - aerospace and defense supply chains
    - AI-enabled enterprise transformation
  geographies:
    - Türkiye
    - United Kingdom
    - United States
  institutions:
    - IMTEK Cryogenics
    - University of Cambridge / Institute for Manufacturing
    - Georgia Institute of Technology
    - Accenture UK & Ireland
    - Royal Academy of Science International Trust
    - ETH Agentic Systems Lab
    - Entrepreneurs First

known_constraints_and_cautions:
  - Do not treat family-company access as proof that other manufacturers share IMTEK's pains.
  - Do not generalize high-precision cryogenic manufacturing workflows to all factories without customer evidence.
  - Do not claim deep production-software engineering solely from prototype or AI-assisted development work.
  - Do not list The Bridge as completed experience or imply EF investment before it occurs.
  - Do not carry the pre-split joint thesis into any idea's context. It is not in this repo, and the founder's current belief lineage supersedes it.
  - Do not infer an ETH title, project, or institutional endorsement beyond the public statement that Izgin is building there.
  - Verify the Helping Hand patent identifier before legal, fundraising, or diligence use.
  - Dates for positions listed on LinkedIn now come from the founder's own data export and supersede the legacy public-profile ranges. Anything NOT listed there (the IMTEK 2017-2025 span, Helping Hand from 2016) still rests on legacy profiles and may be stale; use those ranges for context, not formal background checks.

# Warm-intro contact whitelist — 1st-degree contacts explicitly approved for
# reference as mutuals in outreach copy. Extend only with founder approval.
warm_intro_paths: []

# Signals that may upgrade response_likelihood. These are outreach heuristics,
# not claims about a person's interests or willingness to reply.
affiliation_scoring:
  cambridge_match: +1
  hughes_hall_match: +1
  georgia_tech_match: +1
  accenture_match: +1
  imtek_match: +2
  eth_match: +1
  entrepreneurs_first_match: +1
  rasit_or_girls_in_science_match: +1
  turkish_name_hint: +1

source_registry:
  - id: linkedin_data_export
    kind: local
    title: LinkedIn basic data export, requested 2026-08-18
    path: private/linkedin-export/
    reliability: first_party_self_reported
    note: The founder's own archive, gitignored because it also holds connections' personal data and private message content. Parse it with scripts/data/linkedin_export.py; counts and network shape come from `inspect`, never hand-copied into a file.
  - id: existing_founder_record
    kind: local
    title: Original founder.md
    reliability: founder_provided
  - id: public_profile
    kind: web
    title: Izgin Ozdas LinkedIn public profile
    url: https://uk.linkedin.com/in/izgin-ozdas-500894170
    reliability: self_reported_public
  - id: founder_public_announcement
    kind: web
    title: Entrepreneurs First / ETH Agentic Systems Lab announcement
    url: https://www.linkedin.com/posts/izgin-ozdas_this-summer-ill-be-joining-entrepreneurs-activity-7479792566960472064-f7g0
    reliability: self_reported_public
  - id: private_program_material
    kind: local
    title: The Bridge Program - what to expect
    reliability: first_party_private
  - id: cambridge_research_description
    kind: web
    title: University of Cambridge education/research description on public profile
    url: https://uk.linkedin.com/in/izgin-ozdas-500894170
    reliability: self_reported_public
  - id: gatech_capstone
    kind: web
    title: Georgia Tech Spring 2022 Capstone Design Expo - Helping Hand
    url: https://expo.gatech.edu/prod1/portal/portal.jsp?c=17462&g=413665329&id=416288704&p=413142918
    reliability: institutional
  - id: rasit_profile
    kind: web
    title: RASIT Media team profile
    url: https://rasit.media/about.html
    reliability: organizational
  - id: un_2024_program
    kind: web
    title: 9th International Day of Women and Girls in Science Assembly agenda
    url: https://www.un.org/sites/un2.un.org/files/2024/02/2024_idwgis_agenda_-_210124.pdf
    reliability: institutional
  - id: csa_article
    kind: web
    title: HeLIUM Cryogenics Redefines Cryogenic Technology
    url: https://www.cryogenicsociety.org/index.php?day=07&id=273%3Ahelium-cryogenics-redefines-cryogenic-technology&month=01&option=com_dailyplanetblog&view=entry&year=2024
    reliability: industry_publication
  - id: legacy_student_profile
    kind: web
    title: WayUp student profile
    url: https://www.wayup.com/profile/IZGIN-OZDAS-756ab436e7/
    reliability: self_reported_legacy
    caution: Useful for early roles only; "present" dates are stale.
---

# Founder profile

This file is the durable, cross-idea record of Izgin's experience, access, and
founder-market-fit inputs. It exists so onboarding and ideation work can ask
specific questions instead of requesting another CV recital.

Use the record as context, not proof. Firsthand experience can justify where to
look and whom Izgin can reach; it does not validate a market, pain, buyer, or
willingness-to-pay assumption.