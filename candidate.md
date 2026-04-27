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
- Operated with high autonomy alongside PMs — drove features independently from discovery through launch with minimal direction
- Ran user interviews and analyzed PostHog session recordings to understand user behavior
- Queried BigQuery to trace navigation patterns across 4 core workflows
- Built behavioral funnel analysis identifying where users dropped off
- Brought roadmap recommendation to leadership — directly changed what team built next quarter
- Shipped production Ruby on Rails code: schema migrations, bug fixes, automated QA via GhostInspector
- Diagnosed systemic data quality issue — BigQuery anomaly detection revealed silent data corruption affecting thousands of caregiver records
- Traced root cause through the pipeline, coordinated fix with engineering, added monitoring to prevent recurrence

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
  - After fix: coordinated downstream cache recalculation across consumer systems; data integrity fully restored
  - Problem escalated to me; owned full scope diagnosis and remediation end-to-end
- Built developer-facing observability dashboards and monitoring tooling from scratch
- Rewrote onboarding documentation end-to-end
- Escalations dropped 25%, how-to ticket volume fell 20%
- Conducted 12+ technical interviews

#### Senior Tech Associate
**Dates:** Jan 2022 - Dec 2023

Facts & accomplishments:
- Drove root-cause analyses on production outages across distributed trading and portfolio management tools
- Partnered with quant analysts and traders to understand operational impact and prioritize fixes
- Shipped both immediate mitigations and durable architectural fixes that reduced recurring downtime
- Restructured operating model for a team of 8 engineers — redesigned task assignment and onboarding flow, reducing escalations to senior members by ~30% and cutting time-to-productivity for new engineers by ~25%
- Owned candidate evaluation end-to-end across hiring cycles
- Mentored junior engineers on code quality, system design, and delivery practices; several promoted to senior roles within 18 months

#### Tech Associate
**Dates:** June 2020 - Dec 2021

Facts & accomplishments:
- Primary on-call for core trading engine and portfolio management tools at a $60B quant fund
- Triaged 250+ high-priority incidents/month
- Drove 30% reduction in resolution time through improved tooling and runbooks
- Owned CI/CD pipeline, code releases, and trade report automation end-to-end
- Saved 10+ hrs/week through automation

---

### Oorvani Foundation — Bangalore, India
**Role:** Data Tech Intern
**Dates:** Apr 2018 - May 2018

Facts & accomplishments:
- Analyzed 20+ open city and election datasets
- Built data visualisations translating raw civic datasets into accessible narratives for non-technical audiences
- Visualisations published to thousands of readers

---

### UC Berkeley — Berkeley, CA
**Role:** Teaching Assistant, MEDIAST 114 (Media and Globalization)
**Dates:** Spring 2026

Facts & accomplishments:
- Awarded Outstanding GSI (Graduate Student Instructor) for the Media Studies department, 2025-26
- Led weekly discussion sections, bringing in contemporary themes and examples to make dated theory more relevant and accessible
- Fostered collaborative discussion environments where students engaged across different modes of learning
- Guided ~100 students across two semesters in narrowing scope, strengthening scholarly framing, and improving structure in their final papers
- Co-designed syllabus, curriculum, and in-class activities in close collaboration with the professor
- Contributed to meaningful improvements in the overall course offering across both semesters

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
- RAG pipeline with vector-based retrieval

### Full-stack Educational Web App (UC Berkeley IB 104 — Vertebrates Natural History)
- Stack: Node.js backend, React frontend
- 3 scientific API integrations: Wikipedia, Xeno-canto (bird audio), GBIF (biodiversity records)
- 36 configurable quiz modes
- Real-time leaderboard
- Granular per-user event analytics
- ~120 quiz attempts during pilot
- Piloted with approximately 12 students and professors
- Shipped initial version in 3 days; iterated based on direct user feedback
- Designed API integration layer to handle different schemas, rate limits, and reliability profiles
- Core challenge: making three APIs with different schemas feel like a single coherent data layer

### PDF Peer Evaluation Parser
- Language: Python
- Library: PyMuPDF (fitz)
- Built for UC Berkeley MEDIAST 114 peer evaluation forms
- Handles inconsistent student marking styles (highlights, bold, font color changes, deletions)
- Visual outlier detection on DigitToken objects
- Deployed in production across 10+ grading cycles, processing ~150 student PDFs per run and filtering to ~50 section-specific submissions per evaluation
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

## Volunteering

### Cal Habitat for Humanity
- UC Berkeley club focused on the Bay Area housing crisis through advocacy and volunteering
- Delivered a data backup and integrity presentation (3-2-1 rule) to the club
- Active member contributing to community advocacy efforts around affordable housing

---

## Skills & Technologies

### Languages
Python (primary), Java, JavaScript/Node.js, SQL, C/C++, Ruby on Rails, shell scripting, TypeScript

### AI & Agents
LangChain, OpenAI APIs, Anthropic APIs, RAG pipelines, agentic workflows, tool calling, LLM evaluation, prompt engineering, behavioral telemetry, multi-agent orchestration, context window optimization, HuggingFace, PyTorch, TensorFlow, scikit-learn, NumPy, pandas, SciPy

### Backend & Data
PostgreSQL, MongoDB, BigQuery, AWS (S3, Redshift), GCP, Kafka, Spark, Redis, Elasticsearch, ClickHouse, FastAPI, REST APIs, distributed systems, microservices, system design

### Frontend
React, Node.js, TypeScript, Next.js

### DevOps & Reliability
Docker, Kubernetes, CI/CD (Jenkins), monitoring & alerting, incident response, Git, Linux, observability tooling

### Networking & Security
TCP/IP, TLS, DNS, DHCP, NAT, VLANs, threat modeling, risk assessment

### BI & Analytics
SQL (advanced), A/B testing, causal inference, cohort analysis, statistical modeling, data visualization, Tableau, PostHog, dbt, Looker

### Tools & Platforms
Claude Code, Cursor, Figma, GhostInspector, Excel, Google Sheets

---

## Key Stories & Narratives

### D.E. Shaw Data Integrity Crisis (canonical version)
Two production bugs compounded over 2-3 months corrupting thousands of records/day. Second bug introduced in a patch attempting to fix the first. Connected data across SQL Server + PostgreSQL + local filesystem. Point-in-time data integrity required. Multi-stage SQL join + shell script remediation with rollback checkpoints. Queries were expensive and had to be terminated/rescheduled around cluster load to avoid impacting live production. After fix: coordinated downstream cache recalculation across consumer systems; data integrity fully restored. Problem escalated to me; owned full scope diagnosis and remediation end-to-end.

### Failed Real-Time Transcription Prototype
Built a court reporter transcription prototype that failed due to browser latency and routing issues. Lesson: demo within real constraints. Used in Gitwit interview prep as "something that didn't work."

### Why Forward Deployed Engineering
Skillset naturally marries technical depth + customer success + communication. Want to be embedded with customers, understand their real problems, and own the arc from discovery through deployed solution. Comfortable operating without a dedicated PM layer — at Mon Ami, took on independent PM scope even while working alongside senior PMs.

### Founder Ambition
Long-term goal is to found a company. FDE and high-agency engineering roles are the path there — building the skills to understand customer problems deeply and ship solutions end-to-end.

### Personal connection to healthcare access
Grew up in India, watched family navigate inaccessible healthcare — not because care didn't exist but because systems made it impossible to reach. Relevant for Fortuna Health, Mon Ami, healthcare-adjacent roles.

### Credit scoring / fintech personal connection
Credit rating systems feel blunt from personal experience with credit cards and student loans — a few missed payments define a borrowing profile regardless of actual financial picture. Relevant for Copperlane, fintech roles.

### Chess as hobby
Plays chess recreationally. Developed strong pattern recognition in complex systems — sensing when something is wrong before being able to articulate exactly why. Applies to debugging and production incident response.

### Why Koah / AI ad monetization
Curious about why specific things are recommended inside AI-native products like Poe or Perplexity. Thinks most companies (including OpenAI) are getting monetization wrong. AI-native ad intent signal is genuinely different from search or social — nobody has figured it out yet. Excited about Koah building that infrastructure at the right moment.
