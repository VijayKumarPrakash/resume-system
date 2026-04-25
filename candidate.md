# candidate.md - Vijay Kumar Prakash - Full Work History & Accomplishments
# This is the source of truth for all resume content.
# No formatting constraints. Pull from here when generating resumes.
# Last updated: 2026-04-25

---

## Personal Info

- Name: Vijay Kumar Prakash
- Email: vkp@berkeley.edu
- Phone: +1 (510) 365-3885
- GitHub: https://github.com/VijayKumarPrakash
- LinkedIn: https://linkedin.com/in/vijay-kumar-prakash
- Location: San Jose, CA (Bay Area)

---

## Education

### UC Berkeley
- Degree: Master of Information Systems and Management (MIMS)
- Dates: Aug 2024 - May 2026
- GPA: 3.88 (display as 3.9)
- Focus: Product, Data & Engineering
- Relevant coursework: Agentic AI, Applied GenAI, Machine Learning, NLP, Web App Dev, Causal Inference, Quantitative Data Analysis, Public Interest Cybersecurity Clinic (INFO 289)
- Teaching Assistant: MEDIAST 114 (Media and Globalization)
- Club: Cal Habitat for Humanity (member, advocacy and volunteering around Bay Area housing crisis)

### Christ University, Bangalore
- Degree: B.Sc. Computer Science, summa cum laude
- Dates: June 2017 - June 2020
- GPA: 3.96
- Relevant coursework: Data Structures & Algorithms, Math & Statistics, Operating Systems, Computer Networks, DBMS, Cloud Computing, Object-Oriented Design

---

## Work Experience

### Mon Ami (B2B SaaS for caregivers) — Palo Alto, CA
**Role:** Product Management Intern
**Dates:** May 2025 - Aug 2025

Facts & accomplishments:
- Worked in a founder-led team with no dedicated PM layer — owned features end-to-end
- Ran user interviews and analyzed PostHog session recordings to understand user behavior
- Queried BigQuery to trace navigation patterns across 4 core workflows (not 6)
- Built behavioral funnel analysis identifying where users dropped off
- Brought roadmap recommendation to leadership — directly changed what team built next quarter
- Shipped production Ruby on Rails code: schema migrations, bug fixes, automated QA via GhostInspector
- Diagnosed systemic data quality issue — BigQuery anomaly detection revealed silent data corruption affecting thousands of caregiver records
- Traced root cause through the pipeline, coordinated fix with engineering, added monitoring to prevent recurrence
- Partnered with engineering and design to deliver features from discovery through launch

---

### D.E. Shaw — Hyderabad, India
**Total tenure:** June 2020 - July 2024 (4 years, 1 month)

#### Lead Tech Associate
**Dates:** Jan 2024 - Jul 2024

Facts & accomplishments:
- Owned critical financial data ETL pipeline serving analysts, portfolio managers, and trading desk daily
- Pipeline spanned SQL Server + PostgreSQL + local filesystem (multi-system complexity)
- Cut turnaround from 2 days to ~6 hours (~70% reduction) through query optimization and architectural re-engineering
- Coordinated across vendors, analysts, PMs, and Compliance to execute changes
- Resolved months-long data integrity crisis from two compounding production bugs:
  - Second bug introduced in a patch attempting to fix the first
  - Thousands of records/day corrupted over 2-3 month window
  - Point-in-time data integrity requirement added significant complexity
  - Designed multi-stage SQL joins + shell script remediation
  - Distinguished records affected by each bug separately
  - Built rollback checkpoints at each stage
  - Expensive queries had to be scheduled around cluster load to avoid impacting live production
  - After fix: downstream cache recalculation required, consumer data forecasting models improved marginally
  - Was handed the problem, not self-identified
- Built developer-facing observability dashboards and monitoring tooling from scratch
- Rewrote onboarding documentation end-to-end
- Escalations dropped 25%, how-to ticket volume fell 20%
- Conducted 12+ technical interviews (not "10+")

#### Senior Tech Associate
**Dates:** Jan 2022 - Dec 2023

Facts & accomplishments:
- Drove root-cause analyses on production outages across distributed trading and portfolio management tools
- Partnered with quant analysts and traders to understand operational impact and prioritize fixes
- Shipped both immediate mitigations and durable architectural fixes that reduced recurring downtime
- Restructured team operating model for a team of 8 engineers
- Conducted 12+ technical interviews (shared count with Lead period), owned candidate evaluation end-to-end
- Mentored junior engineers on code quality, system design, delivery practices

#### Tech Associate
**Dates:** June 2020 - Dec 2021

Facts & accomplishments:
- Primary on-call for core trading engine and portfolio management tools at a $60B quant fund
- Triaged 250+ high-priority incidents/month
- Drove 30% reduction in resolution time through improved tooling and runbooks
- Owned CI/CD pipeline, code releases, and trade report automation end-to-end
- Saved 10+ hrs/week through automation
- Owned the deployment process and release management

---

### Oorvani Foundation — Bangalore, India
**Role:** Data Tech Intern
**Dates:** Apr 2018 - May 2018

Facts & accomplishments:
- Analyzed 20+ open city and election datasets
- Built data visualizations using Fusion Tables and Timeline JS
- Visualizations published to thousands of readers
- Translated raw civic data into accessible, decision-relevant narratives for non-technical audience

---

### UC Berkeley — Berkeley, CA
**Role:** Teaching Assistant, MEDIAST 114 (Media and Globalization)
**Dates:** Spring 2026

Facts & accomplishments:
- TA for undergraduate course on media and globalization
- Graded student proposals and final papers (~30 students)
- Ran sections and supported professor with course logistics

---

## Projects

### LLM-as-a-Judge Benchmark Framework
- Language: Python
- Tools: LangChain, OpenAI APIs, Anthropic APIs, PyTorch
- Built end-to-end evaluation system for AI agents performing hypothesis-testing tasks
- Analogous to SWE-bench
- Engineered judge prompts, tool-calling pipelines, and scoring rubrics
- Mixed procedural tests with LLM-based grading for ambiguous ground truth settings
- Iterated on grader fairness by sampling agent transcripts
- Identified systematic failure modes: hallucinated confidence, shortcut behaviors, context degradation
- Built regression checks and behavioral telemetry to detect model drift across versions
- Designed for multi-step agent orchestration with state management across steps
- RAG retrieval with vector-based search included

### Full-stack Educational Web App (UC Berkeley IB 104 — Vertebrates Natural History)
- Stack: Node.js backend, React frontend
- 3 scientific API integrations: Wikipedia, Xeno-canto (bird audio), GBIF (biodiversity records)
- 36 configurable quiz modes
- Real-time leaderboard
- Granular per-user event analytics
- ~120 quiz attempts during pilot
- Piloted with approximately 12 students and professors
- NOT yet live in the course
- Built in a couple of days; iterated based on direct user feedback
- Designed API integration layer to handle different schemas, rate limits, and reliability profiles
- Core challenge: making three APIs with different schemas feel like a single coherent data layer

### PDF Peer Evaluation Parser
- Language: Python
- Library: PyMuPDF (fitz)
- Built for UC Berkeley MS 114 peer evaluation forms
- Handles inconsistent student marking styles (highlights, bold, font color changes, deletions)
- Visual outlier detection on DigitToken objects
- Tested across 6 PDFs
- Designed for multi-file aggregation with pandas

---

## UC Berkeley Cybersecurity Clinic (INFO 289)
- Course: Public Interest Cybersecurity
- Role: Clinic Consultant, Spring 2026
- Providing pro-bono cybersecurity consulting to a civil society NGO
- Conducting threat modeling, risk assessment
- Developing pragmatic security recommendations for under-resourced organization
- Presenting findings to non-technical stakeholders

---

## Cal Habitat for Humanity
- UC Berkeley club
- Focus: Bay Area housing crisis through volunteering and advocacy
- Delivered a data backup and integrity presentation (3-2-1 rule) to the club
- Built HTML/Reveal.js presentation for the talk

---

## Skills & Technologies

### Languages
Python (primary), Java, JavaScript/Node.js, SQL, C/C++, Ruby on Rails, shell scripting, TypeScript (familiar), Go (learning)

### AI & Agents
LangChain, OpenAI APIs, Anthropic APIs, RAG pipelines, agentic workflows, tool calling, LLM evaluation, prompt engineering, behavioral telemetry, multi-agent orchestration, context window optimization, HuggingFace, PyTorch, TensorFlow, scikit-learn, NumPy, pandas, SciPy

### Backend & Data
PostgreSQL, MongoDB, BigQuery, AWS (S3, Redshift), GCP (familiar), Kafka, Spark, Redis (familiar), Elasticsearch (familiar), ClickHouse (familiar), REST APIs, distributed systems, microservices, system design

### Frontend
React, Node.js, TypeScript (familiar), Next.js (familiar)

### DevOps & Reliability
Docker, Kubernetes (familiar), CI/CD (Jenkins), monitoring & alerting, incident response, Git, Linux, observability tooling

### Networking & Security
TCP/IP, TLS, DNS, DHCP, NAT, VLANs, threat modeling, risk assessment

### BI & Analytics
SQL (advanced), A/B testing, causal inference, cohort analysis, statistical modeling, data visualization, Tableau, PostHog, dbt (familiar), Looker (familiar)

### Tools & Platforms
Claude Code, Cursor, Figma, GhostInspector, MongoDB

---

## Key Stories & Narratives

### D.E. Shaw Data Integrity Crisis (canonical version)
Two production bugs compounded over 2-3 months corrupting thousands of records/day. Second bug introduced in a patch attempting to fix the first. Connected data across SQL Server + PostgreSQL + local filesystem. Point-in-time data integrity required. Multi-stage SQL join + shell script remediation with rollback checkpoints. Queries were expensive and had to be terminated/rescheduled around cluster load to avoid impacting live production. After fix: cache recalculation downstream; consumer data forecasting models improved marginally. Was handed the problem, not self-identified.

### Failed Real-Time Transcription Prototype
Built a court reporter transcription prototype that failed due to browser latency and routing issues. Lesson: demo within real constraints. Used in Gitwit interview prep as "something that didn't work."

### Why Forward Deployed Engineering
Skillset naturally marries technical depth + customer success + communication. Want to be embedded with customers, understand their real problems, and own the arc from discovery through deployed solution.

### Founder Ambition
Long-term goal is to found a company. FDE and high-agency engineering roles are the path there — building the skills to understand customer problems deeply and ship solutions end-to-end.

### Personal connection to healthcare access
Grew up in India, watched family navigate inaccessible healthcare — not because care didn't exist but because systems made it impossible to reach. Relevant for Fortuna Health, Mon Ami, healthcare-adjacent roles.

### Credit scoring / fintech personal connection
Credit rating systems feel blunt from personal experience with credit cards and student loans — a few missed payments define a borrowing profile regardless of actual financial picture. Relevant for Copperlane, fintech roles.

### Chess as hobby
Plays chess but stuck in same rating bracket for a long time. Bots beat him regularly. Lesson learned: pattern recognition in complex systems, sensing when something is wrong before being able to articulate exactly why. Useful for debugging and production incident response.

### Why Koah / AI ad monetization
Curious about why specific things are recommended inside AI-native products like Poe or Perplexity. Thinks most companies (including OpenAI) are getting monetization wrong. AI-native ad intent signal is genuinely different from search or social — nobody has figured it out yet. Excited about Koah building that infrastructure at the right moment.
