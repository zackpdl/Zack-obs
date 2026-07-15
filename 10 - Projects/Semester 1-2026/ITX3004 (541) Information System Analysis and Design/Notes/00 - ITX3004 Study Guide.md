# 00 - Information System Analysis & Design Study Guide

> **Course:** ITX3004 (541) — Information System Analysis and Design
> **Instructor:** Dhirachat C. (dhirachatchy@msme.au.edu)
> **Textbook:** *System Analysis and Design* (Dennis, Wixom, Roth, 5th Ed.)
> **Supplement:** *O-O Analysis Design and Implementation* (Dathan, Ramnath)
> **Schedule:** Wed 13:30-16:30 @ VMES0314
> **Midterm:** Aug 4 (Mon) 15:00-17:00 — Chapters 1-6 + Supplement Ch 1, 3, 10, 13
> **Finals:** Sep 30 - Oct 12

---

## 📚 Materials Inventory

| File | Type | Pages/Slides | Status |
|------|------|-------------|--------|
| Intro-ISAD.pptx | Course intro + SDLC overview | 14 slides | ✅ |
| Chapter 1.pptx | SA and IS Development | 14 slides | ✅ |
| Chapter 2.pptx | Project Selection & Management | 13 slides | ✅ |
| Chapter 3.pptx | Requirements Determination | 8 slides | ✅ |
| Chapter 4.pptx | Use Case Analysis | 3 slides | ✅ |
| Chapter 5.pptx | Process Modeling (DFD) | 10 slides | ✅ |
| Chapter 6.pptx | Data Modeling (ERD, Normalization) | 9 slides | ✅ |
| Chapter 7.pptx | Moving to Design | 4 slides | ✅ |
| Chapter 8.pptx | Architecture Design | 8 slides | ✅ |
| Chapter 9.pptx | User Interface Design | 6 slides | ✅ |
| Supplement Book #1.pptx | OO Concepts, FSM, UML, MVC | 14 slides | ✅ |
| Use case diagram.pptx | Use case diagram drawing guide | 4 slides | ✅ |
| PERT Diagram crash course.pptx | PERT calculation method | 4 slides | ✅ |
| Quiz 1 and Project Proposal.pptx | Quiz + project requirements | 4 slides | ✅ |
| ITX3004 Syllabus 2026-1_v01.pdf | Full syllabus & schedule | — | ✅ |
| ITX3004 541 Class note.docx | Lecture notes (10 Jun - 14 Jul) | — | ✅ |
| Student Interactive Board.docx | Class Q&A board | — | ✅ |
| drawing_in_class_24JUN2026.pdf | In-class drawing | — | ✅ |

---

## 📖 Course Overview

**What is ISAD?** The study of how information systems are planned, analyzed, designed, and implemented to support business needs. A System Analyst bridges business problems and technical solutions.

**Key Reality:** Coding is only **10-20%** of development. Two-thirds of software project resources go to **maintenance**. The SA's job is everything *before* coding.

---

## 🧭 1. The Systems Analyst & SDLC (Ch 1)

### System Analyst Skills (6)
1. **Technical** — Understand technology enough to apply it
2. **Business** — Understand how the business runs
3. **Analytical** — Break problems into pieces
4. **Interpersonal** — Work with people at all levels
5. **Management** — Plan, organize, control
6. **Ethical** — Make responsible decisions

> SA = "Change Agent" — motivates organization members to adopt new systems

### System Analyst Roles
- Idea and suggestion
- Design new business processes and policies
- Requirements analyst
- Stakeholders and end-users liaison
- Infrastructure analyst
- Change management
- Project manager

### SA vs BA

| SA (System Analyst) | BA (Business Analyst) |
|---------------------|----------------------|
| Takes care of everything before implementation | SA + domain expert (e.g. Supply Chain, Retail) |
| Business + technical skills | Deep industry knowledge |
| Project coordination | Often also a developer |

### SDLC — 4 Phases

```
PLANNING → ANALYSIS → DESIGN → IMPLEMENTATION
```

| Phase | Key Activities | Deliverable |
|-------|---------------|-------------|
| **Planning** | Project initiation, feasibility (technical/economic/organizational), project selection, methodology choice, Gantt chart | Project plan |
| **Analysis** | Analysis strategy (as-is → to-be), requirement gathering | System proposal |
| **Design** | Acquisition strategy (in-house/outsource), architecture, interface, storage, program design | System specification |
| **Implementation** | Programming, testing, installation, training, support | Release note |

### Project Identification
- **Business needs / Pain points** → trigger projects
- Balance **first mover** vs **mature technology**
- **BPM** (Business Process Management) — continuous improvement
- **BPR** (Business Process Reengineering) — radical redesign

### System Request
A document for decision-makers containing:
- **Project sponsor** — who initiates it
- **Business need** — why
- **Business requirements** — what
- **Business value** — ROI, benefits
- **Special issues** — risks, constraints

### Feasibility Analysis (3 Types)

| Type | Focus |
|------|-------|
| **Technical** | Can we build it? Do we have the skills/tools? |
| **Economic** | Cashflow, ROI, Break-even, NPV |
| **Organizational** | Will the organization accept it? Culture, politics? |

---

## 🗂️ 2. Project Selection & Management (Ch 2)

### Project Portfolio Management
Map project information with business goals → select, prioritize, monitor results

### Development Methodology Options

| Methodology | Description | Best For |
|------------|-------------|----------|
| **Waterfall** | Sequential phases, one after another | Clear requirements, simple projects |
| **Parallel** | Subsystems developed simultaneously | Large projects with independent modules |
| **V-Model** | Verification & validation at each level | High-reliability systems |
| **Iterative** | Repeated cycles with feedback | Unclear requirements |
| **Prototype** | Build a model, refine based on feedback | When users can't articulate needs |
| **Agile** | Short iterations (sprints), adaptive | Evolving requirements, small teams |
| **Extreme Programming** | Pair programming, TDD, continuous integration | Rapid development, quality focus |

### Selection Criteria (Figure 2-9)
1. Clarity of user requirements
2. Familiarity with technology
3. System complexity
4. System reliability needs
5. Short time schedules
6. Schedule visibility
7. Project timeframe

### Work Plan
- **PERT Diagram** — task dependencies and critical path
- **Gantt Chart** — timeline visualization
- **Staffing Plan** — who does what

### Managing & Controlling
- **Scope creep** — "The more you do, the more you do"
- **Timeboxing** — fixed deadline, adjust scope
- **Risk assessment** — potential impacts + prevention/correction
- **Refining estimates** — "Prediction is always wrong"

### PERT Calculation

```
Expected Time = (Optimistic + 4×Most Likely + Pessimistic) / 6

Example: O=3, M=4, P=6
ET = (3 + 4×4 + 6) / 6 = 25/6 = 4.16 semesters
```

---

## 📋 3. Requirements Determination (Ch 3)

### The Analysis Phase (3 Steps)
1. Understand **"as-is system"**
2. **Improve** it
3. Define requirements for **"to-be system"**

> You can KEEP or DISCARD existing system features.

### What is a Requirement?
A description of a task needed to achieve a business goal.

**Hierarchy:**
```
Business requirements (why) → User requirements (who)
→ Functional requirements (what) → System requirements (how)
→ Non-functional requirements (performance, security, usability)
```

### Requirement Definition Statements
Must be **clear and precise**, using **business terminologies**

### Elicitation Techniques (How to Get Requirements)

| Technique | Best For |
|-----------|----------|
| **Interviews** | In-depth understanding |
| **JAD** (Joint Application Development) | Group consensus |
| **Questionnaires** | Large user base |
| **Document Analysis** | Existing system documentation |
| **Observation** | Understanding actual work practices |

### Selecting Appropriate Techniques
Consider: Type of info, Depth, Breadth, Integration, User involvement, Cost

### Requirement Analysis Strategies
- **Problem Analysis** — fix pain points
- **Root Cause Analysis** ★ — find underlying cause, not symptom
- **Duration Analysis** — time-based improvement
- **Activity-Based Costing** — cost per activity
- **Informal Benchmarking** — compare to competitors
- **Outcome Analysis** — desired outcomes
- **Technology Analysis** — what tech can enable

> **Symptom vs Problem:** Amazon Go stores closed because they worked technically but weren't profitable. The *problem* wasn't the technology — it was the business model.

---

## 🎭 4. Use Case Analysis (Ch 4)

### Elements of a Use Case (Long Version)
- **Basic Information** — name, ID, actors
- **Preconditions** — what must be true before
- **Normal Course** — main success flow
- **Alternative Courses** — variations
- **Post-condition** — what must be true after
- **Exception** — error handling
- **Summary and Issues** — notes

### Use Case Diagram Components
```
┌─────────────────────────┐
│   SYSTEM BOUNDARY       │
│                         │
│   ┌─────────────┐      │
│   │  Use Case   │      │
│   │  (Verb)     │      │
│   └──────┬──────┘      │
│          │              │
│          ▼              │
│     ┌────────┐         │
│     │ Actor  │         │
│     └────────┘         │
└─────────────────────────┘
```

### Rules
- Use cases = **verbs** (actions the system performs)
- Actors = **who** interacts (people, other systems)
- System boundary = scope of the system
- Skip: `include`, `extend`, `generalize` relationships (not required)

### Use Cases & Testing
Use cases map directly to test cases — each normal + alternative course = test scenario.

---

## 🔄 5. Process Modeling — DFD (Ch 5)

### Data Flow Diagram (DFD) Components
| Symbol | Represents |
|--------|-----------|
| **External Entity** | People, other systems outside our system |
| **Process** | Action/transformation (use case) |
| **Data Store** | Where data is stored |
| **Data Flow (Arrow)** | Movement of data |

### DFD Levels

```
Context Diagram (Level -)
  ↓
Level 0 DFD (Major subsystems)
  ↓
Level 1 DFD (Sub-processes of each subsystem)
  ↓
Level 2 DFD (Detailed sub-processes)
```

### Context Diagram
- Single process (0) = entire system
- Only **flows** + **external entities** (no data stores)
- Shows system boundary with outside world

### Level 0 DFD
- Processes numbered 1, 2, 3...
- Shows data flow between: EE↔Process, Process↔Data Store, Process↔Process

### Level 1 DFD
- Processes numbered 1.1, 1.2, 1.3...
- Inside ONE process from Level 0
- Sub-process details

### Level 2 DFD
- Processes numbered 1.1.1, 1.1.2...
- Deepest level of detail

### DFD Rules
- ❌ No arrow directly between EE↔EE
- ❌ No arrow directly between Data Store↔Data Store
- ❌ No arrow directly between EE↔Data Store
- All flows must connect through a Process

### DFD Validation
- Common errors: missing flows, mismatched levels, black holes (process with no output), miracles (output with no input)

---

## 💾 6. Data Modeling — ERD (Ch 6)

### Entity Relationship Diagram (ERD)
Since the 90s, DBMS based on **relational model** (2D tables)

### ERD Elements
| Element | Description |
|---------|-------------|
| **Entity** | A thing (table) |
| **Attribute** | Property of an entity (column) |
| **Relationship** | Association between entities |
| **Cardinality** | How many (1:1, 1:M, M:N) |
| **Modality** | Whether the relationship is mandatory or optional |

### Normalization

| Normal Form | Rule |
|-------------|------|
| **0NF** | Raw data — repetition and empty spaces |
| **1NF** | No repeating groups, no empty spaces |
| **2NF** | No M:N relationships (every non-key attribute depends on full PK) |
| **3NF** | One table = one entity (no transitive dependencies) |

### NoSQL / MongoDB
- **Not Only SQL** — alternative approach
- Document-based (JSON-like)
- Collection → Document (vs Table → Row)
- Flexible schema, good for semi-structured data

### Data Dictionary & Metadata
- Use tools to generate metadata/schema automatically
- Documents all data elements, types, relationships

---

## 🧱 7. Object-Oriented Concepts (Supplement)

### 4 Pillars of OOP
1. **Abstraction** — hide complexity, show only what's needed
2. **Encapsulation** — bundle data + methods, hide internal state
3. **Inheritance** — child class inherits from parent class
4. **Polymorphism** — one interface, many implementations

### OO Design Principles

| Concept | Meaning |
|---------|---------|
| **Cohesion** | How related are elements within a module? (High = good) |
| **Coupling** | How dependent are modules on each other? (Low = good) |
| **Modularity** | System divided into separate modules |
| **Abstract Data Type** | Data type defined by its behavior, not implementation |
| **Testability** | Can it be tested easily? |
| **Adaptable** | Can it be changed easily? |

### Class Diagram
```
┌──────────────────┐
│   Class Name     │
├──────────────────┤
│ - privateAttr    │
│ + publicAttr     │
├──────────────────┤
│ + publicMethod() │
│ - privateMethod()│
└──────────────────┘
```
- `+` = Public, `-` = Private
- Omit `get` and `set` methods
- Relationships: Association, Composition, Inheritance

### Relationships Between Classes
- **Association** — "uses-a" (e.g. Student takes Course)
- **Composition** — "has-a" (e.g. Car has Engine; part-of)
- **Inheritance** — "is-a" (e.g. Dog is an Animal)

### Finite State Machine (FSM)
Used when the system must handle all possible **states** and **transitions**.

**Application:** Electronic devices, GUI, Games, Microwave

**Microwave Example (Figure 10.1-10.2):**
- States: Idle, Cooking, Door Open
- Events: Press Start, Open Door, Timer Expires, Close Door

**In-class FSM — Refrigerator:**
- States: Door (open/close), Light (on/off), Thermostat (temperature)

### MVC Architecture
- **Model** — data and business logic
- **View** — user interface
- **Controller** — handles input, updates model
- **Sequence Diagram** — shows interaction over time

### Additional UML Diagrams (Chapter 13)
- **Activity Diagram (Swimlane)** — process flow by role. Vertical = documentation, Horizontal = presentation
- **Package Diagram** — grouping of classes
- **Deployment Diagram** — physical hardware/software layout

---

## 🚚 8. Moving to Design (Ch 7)

### Transition: Requirements → Design
```
Alternative Matrix → Architecture Design → Interface Design
→ Data Storage & CRUD → System Specification
```

### Acquisition Strategy (3 Options)

| Strategy | Description |
|----------|-------------|
| **Custom** | Build in-house — full control, higher cost |
| **Package** | Buy off-the-shelf — cheaper, may not fit perfectly |
| **Outsourcing** | Hire a third party — good for non-core systems |

### Influences on Strategy
- Budget, timeline, business criticality, availability of packages

---

## 🏗️ 9. Architecture Design (Ch 8)

### Key Warning
> "Most projects fail and/or go over budget because the developer didn't include all components."

**Beware:** Marketing campaigns and advertisements affect decision-making. E.g., cloud storage pricing was artificially low in 2010s — companies built businesses dependent on it, then couldn't survive when prices normalized.

### Architecture Elements

**Client-Server Model:**
- **Fat Client** — most processing on client side
- **Thin Client** — most processing on server side
- **Scalable** — can grow with demand
- **Middleware** (e.g. JDBC) — connects client and server

**Tiers:**
- 2-tier: Client ↔ Server
- 3-tier: Client ↔ Application Server ↔ Database
- N-tier: Multiple specialized servers

### Advanced Configurations
- **Virtualization** — run multiple VMs on one physical server
- **Cloud Computing** — IaaS, PaaS, SaaS

### Creating Architecture Design — Consider:

| Requirement Type | Questions |
|-----------------|-----------|
| **Operational** | Uptime, backup, disaster recovery |
| **Performance** | Response time, throughput, concurrent users |
| **Security** ⚠️ | Hire a professional — don't save money on security |
| **Cultural/Political** | Does it fit the organization culture? |
| **Legal/Norm** | Compliance with laws and regulations |

> ⚠️ **Customization trap:** Some ERP products let users alter fundamental principles (e.g. stock manipulation that breaks accounting rules). "It is recommended that you will never do it."

### Hardware & Software Specs
- Don't forget **End of Life** dates and **business stability** of vendors

---

## 🖥️ 10. User Interface Design (Ch 9)

### Principles (Figure 9-1)
1. **Layout** — organized, logical placement
2. **Awareness** — user knows what's happening
3. **Aesthetics** — visually pleasing
4. **User Experience** — easy and pleasant to use
5. **Consistency** — same patterns throughout
6. **Minimize User Effort** — fewest clicks possible

### UI Design Process (Spiral Model)
```
Scenario → Interface Structure Design (Sitemap)
→ Prototyping → Storyboard → Interface Evaluation
```

### Navigation Design
- Navigation controls (menus, breadcrumbs)
- Messages (feedback, errors, confirmations)

### Input Design
- Types of inputs (text, select, upload, etc.)
- **Input Validation** (Figure 9-15) — check data before processing

### Output Design
- Types of outputs (reports, dashboards, exports)
- Choose format based on audience and purpose

---

## 📝 Quiz 1 Info

| Detail | Value |
|--------|-------|
| **Weight** | 5% |
| **Topics** | Requirement analysis + Use case diagrams |
| **Format** | 1 essay (case study) + drawing |
| **Duration** | 1 hour (13:45-14:45) |
| **Materials** | Close book |
| **Drawing** | Pencil allowed, use **blue pen for text** |
| **Date (541)** | Jul 22 (Wed) |

## 📝 Midterm Info

| Detail | Value |
|--------|-------|
| **Date** | Aug 4 (Mon) 15:00-17:00 |
| **Concepts** | Textbook Chapter 1-6 + Supplement Ch 1, 3, 10, 13 |
| **Design + Drawing** | Use case diagram + Class diagram |

---

## 🧠 Key Vocabulary

| Term | Definition |
|------|-----------|
| **System** | A group of interacting components working together toward a common goal |
| **SDLC** | Systems Development Life Cycle — Planning, Analysis, Design, Implementation |
| **System Analyst** | Person who bridges business problems and technical solutions |
| **Feasibility** | Assessment of whether a project is technically, economically, and organizationally viable |
| **Requirement** | A description of a task needed to achieve a business goal |
| **Use Case** | A description of system behavior in response to an actor |
| **DFD** | Data Flow Diagram — shows how data moves through a system |
| **ERD** | Entity Relationship Diagram — shows data structure and relationships |
| **Normalization** | Process of organizing data to reduce redundancy |
| **PERT** | Program Evaluation Review Technique — task dependency diagram |
| **Gantt Chart** | Timeline-based project schedule |
| **Scope Creep** | Uncontrolled expansion of project scope |
| **Waterfall** | Sequential SDLC methodology |
| **Agile** | Iterative SDLC with short sprints and adaptive planning |
| **Encapsulation** | Bundling data + methods, hiding internal state |
| **Inheritance** | Child class inherits from parent class |
| **Polymorphism** | One interface, many implementations |
| **FSM** | Finite State Machine — models system states and transitions |
| **MVC** | Model-View-Controller architectural pattern |
| **Fat Client** | Client does most processing |
| **Thin Client** | Server does most processing |

---

## ⚡ Quick Reference: Diagrams You Need to Draw

### 1. Use Case Diagram
```
[User] ──→ (Login) ←── [Database]
                      (Register)
                      (Search Items)
```

### 2. Class Diagram
```
┌──────────┐       ┌──────────┐
│ Student  │       │ Course   │
├──────────┤       ├──────────┤
│ -name    │       │ -title   │
│ -id      │◄─────►│ -credits │
├──────────┤       ├──────────┤
│ +enroll()│       │ +getInfo│
└──────────┘       └──────────┘
```

### 3. DFD (Context Diagram)
```
[Student] ←→ Process 0 ←→ [Advisor]
             System
```

### 4. ERD
```
STUDENT ──── M:N ──── COURSE
  │                      │
  │ 1                    │ M
  │                      │
DEPARTMENT ──── 1:M ──── TEACHER
```

### 5. FSM Diagram
```
State A ──[event]──→ State B
  ↑                      │
  └─────[event]─────────┘
```

---

## 📝 Potential Exam Questions

### Short Answer
1. What are the 4 phases of SDLC? Briefly describe each.
2. List 3 types of feasibility analysis.
3. What is the difference between a requirement and a symptom?
4. What is scope creep and how do you manage it?
5. Explain the difference between Context DFD, Level 0, and Level 1.
6. What is normalization? What is the difference between 1NF, 2NF, and 3NF?
7. What is a Finite State Machine? Give an example.

### Essay Style
1. A company wants to build a new inventory system. Walk through the SDLC phases they would follow.
2. You are interviewing a client who wants a new library system. What elicitation techniques would you use? Why?
3. Compare Waterfall and Agile development. When would you use each?
4. Draw a use case diagram for a university registration system. Include at least 3 actors and 5 use cases.
5. A restaurant wants a reservation system. Draw the Context DFD, Level 0, and Level 1.
6. You've been asked to design the architecture for an e-commerce platform. What considerations would you make for security, performance, and scalability?

### Diagram Drawing (Midterm)
- Use case diagram scenario
- Class diagram from description
- DFD from business process description
- ERD from data requirements

---

*Last updated: July 2026*
