# 📊 Presentation & Data Visualization — CSX4601 / ITX2009 Study Guide

**Course:** Selected Topic in Presentation and Data Visualization Techniques  
**Instructor:** Assoc. Prof. Dr. Sasithorn Chookaew (sasithornchk@au.edu)  
**Source Lectures:** Chapters 1–3

---

## 📑 Table of Contents
1. [Chapter 1 — Introduction to Principles & Techniques](#chapter-1--introduction-to-the-principles-and-techniques-for-data-visualization)
2. [Chapter 2 — Design Principles for Charts & Graphs](#chapter-2--design-principles-for-charts-and-graphs)
3. [Chapter 3 — Visual Presentation Methods & Techniques](#chapter-3--visual-presentation-methods-and-techniques)
4. [Vocabulary & Key Terms](#vocabulary--key-terms)
5. [Potential Exam Questions](#potential-exam-questions)
6. [Materials Inventory](#materials-inventory)

---

## Chapter 1 — Introduction to the Principles and Techniques for Data Visualization

### 1.1 Course at a Glance

| Item | Detail |
|------|--------|
| **Course Code** | ITX2009 & CSX4601 |
| **Chapters** | 1. Introduction → 2. Design Principles → 3. Visual Methods → 4. Tools → 5. Patterns → 6. Trends & Differences → 7. Multimedia |
| **Evaluation** | Assignments (30%), Attendance (10%), Final Project (10%), Midterm (20%), Final Exam (30%) |

### 1.2 Data Fundamentals

| Term | Definition |
|------|-----------|
| **Data** | Raw, unstructured information collected/observed/generated for analysis, decision-making, or reference. Can be quantitative or qualitative. |
| **Information** | Data given context and insight (e.g., a trend analysis showing increasing satisfaction over time). |
| **Data Presentation** | Organizing, formatting, and displaying data for easy understanding and interpretation. |

> **Key distinction:** Data = raw & unstructured; Information = contextualized & insightful.

### 1.3 Types of Data

| Type | Subtype | Examples |
|------|---------|---------|
| **Quantitative** (numerical, measurable) | Discrete | Number of cars, students in a class |
| | Continuous | Height, weight, time, temperature |
| **Qualitative** (descriptive, non-numerical) | — | Colors, names, labels, opinions |

### 1.4 Uses & Sources of Data

**Uses:**
- Research & analysis
- Business decision-making
- Policy formulation
- Technology development
- Monitoring & evaluation

**Sources:**
- Surveys & questionnaires
- Experiments & observations
- Transactions & records
- Sensors & IoT devices
- Online activity (social media, websites)

### 1.5 Types of Data Presentation

| Method | Description | Best For |
|--------|-------------|----------|
| **Textual** | Data described in words | Small datasets, explaining trends/summaries |
| **Tabular** | Data in rows & columns | Comparison, precise numerical values |
| **Graphical** | Visual representation via charts/graphs | Simplifying complex data, highlighting patterns |

### 1.6 What is Data Visualization?

> **Data visualization** is the representation of data through graphics — charts, plots, infographics, animations — to communicate complex data relationships in an understandable way.

**Why it matters:**
- **Enhanced Understanding** — intuitive grasp of insights
- **Improved Communication** — accessible to non-technical audiences
- **Faster Insights** — quick identification of patterns, trends, outliers
- **Better Decision-Making** — data-driven choices enabled
- **Increased Engagement** — memorable and compelling

> *Historical note:* Earliest forms from pre-17th century Egypt (navigation). Edward Tufte's 1983 *The Visual Display of Quantitative Information* was a landmark publication.

### 1.7 Types of Data Visualizations

| Type | Description | Best Use Case |
|------|-------------|--------------|
| **Tables** | Rows & columns of data | Comparing precise values; can overwhelm for high-level trends |
| **Pie Charts / Donut Charts** | Segments representing parts of a whole | Showing proportions with few categories |
| **Bar Charts** | Vertical, horizontal, grouped, or stacked bars | Comparing categories |
| **Line Charts** | Data points connected by lines | Trends over time |
| **Area Charts** | Line chart with filled area | Cumulative totals over time |
| **Histograms** | Bar chart (no gaps) showing data distribution | Frequency distributions, identifying outliers |
| **Scatter Plots** | Points showing relationship between 2 variables | Correlation analysis |
| **Bubble Charts** | Scatter plot with point size = 3rd variable | 3-variable relationships |
| **Heat Maps** | Color gradients showing data intensity | Behavioral data, geographical patterns, correlation matrices |
| **Tree Maps** | Nested rectangles for hierarchical data | Part-to-whole in hierarchies |
| **Dashboards** | Multi-source visual display in one place | Real-time tracking, team performance visibility |

### 1.8 Data Visualization Best Practices

1. **Set the Context** — Ground the audience with background info.
2. **Know Your Audience** — Fit the visualization to their needs, questions, and role.
3. **Choose an Effective Visual** — Match chart type to data (scatter → relationships, line → time series).
4. **Keep It Simple** — Be deliberate; eliminate distractions (excess labels, too many colors).

### 1.9 Five Principles of Effective Data Visualization

| Principle | Description |
|-----------|-------------|
| **Clarity** | Avoid clutter; make the message obvious |
| **Accuracy** | Never distort the data |
| **Simplicity** | Use the simplest form that conveys the message |
| **Context** | Always label axes, include units and source |
| **Visual Hierarchy** | Use color and size to guide attention |

---

## Chapter 2 — Design Principles for Charts and Graphs

### 2.1 Effective Data Visualization

> *"Good visualizations start with good data."*

**Three hallmarks of effective visualization:**
- **Appropriate** — for the intended audience
- **Accurate** — in presentation of data and meaning
- **Actionable** — the information is clarifying and useful

### 2.2 Data Sources

| Type | Description | Examples |
|------|-------------|----------|
| **Primary** | Collected by yourself | Surveys, classroom experiments, observation logs, sensor readings |
| **Secondary** | Collected by others, publicly available | Government databases, World Bank/WHO data, research articles |
| **Online & Real-Time** | Live or frequently updated via APIs | Weather API, Google Trends, social media analytics, Google Analytics |

**Data Formats & Visualizations:**

| Format | Visualization Types |
|--------|-------------------|
| CSV / Excel (tabular) | Line, bar, pie charts |
| SQL databases (structured tables) | Dashboards, heat maps |
| APIs (JSON / XML) | Real-time graphs, maps |
| Surveys (categorical/rating) | Pie charts, Likert scales |
| Sensor data (time-series) | Line charts, area charts |

### 2.3 Surveys & Questionnaires

**Questionnaire** = the set of questions (the instrument).  
**Survey** = the broader method (collect + analyze + interpret).

#### Principles of Constructing a Questionnaire — 6 Steps

1. Define your objective
2. Identify the target population
3. Decide on question types
4. Plan layout & flow
5. Pilot the questionnaire
6. Revise and finalize

#### Principles of Constructing Effective Questions (A–F)

| Principle | Rule | Example (Bad → Good) |
|-----------|------|----------------------|
| **A. Clarity** | Simple language, no jargon, short & direct | |
| **B. Relevance** | Every question ties to the objective | |
| **C. Brevity** | One thing at a time (no double-barreled) | ❌ "How satisfied with salary and hours?" → ✅ Ask separately |
| **D. Neutrality** | No leading/loaded questions | ❌ "Don't you agree our service is excellent?" → ✅ "How would you rate our service?" |
| **E. Answerability** | Ask what respondents *can* and *will* answer | Avoid forgotten or uncomfortable topics |
| **F. Balanced Response Options** | Full range (e.g., Likert), include "Other" / "N/A" | Strongly Disagree → Strongly Agree |

#### Types of Questions

| Type | Description | Examples |
|------|-------------|----------|
| **Closed-ended** | Predefined answer options | Yes/No, Multiple Choice, Likert Scale, Dichotomous, Ranking |
| **Open-ended** | Respondents answer in own words | "What do you like most about this product?" |
| **Demographic** | Background info | Age, gender, education, occupation, ethnicity |
| **Matrix** | Grid — rate multiple items on same scale | Statements × Agreement scale |
| **Filter / Contingency** | Route respondents to different sections | "Do you own a car? If Yes → Q5, If No → Q7" |

#### Steps to Define a Survey Topic

1. **Start with a Broad Idea** — "Student life at university"
2. **Narrow It Down** — "Students' satisfaction with online learning during exams"
3. **Set a Clear Objective** — "To measure how satisfied university students are with online learning platforms used during final exams"
4. **Identify Target Group** — "First- and second-year engineering students"
5. **Formulate Key Questions** — What info is needed to achieve the goal?

#### Choosing the Correct Chart Type

| Chart Type | Use Case |
|------------|----------|
| Bar chart | Comparing categories |
| Line graph | Showing trends over time |
| Pie chart | Showing proportions |
| Scatter plot | Showing relationships |
| Histogram | Showing frequency distribution |

#### Common Questionnaire Categories

- Customer/User Feedback
- Market Research
- Employee Engagement/Satisfaction
- Public Opinion/Social Issues
- Academic/Research Studies
- Event Feedback
- Health and Wellness
- Educational Needs/Effectiveness

### 2.4 Teamwork & Assignments

**Benefits of teamwork:** Communication skills, collaboration, problem-solving, responsibility & accountability, confidence & leadership, workplace preparation, respect for diversity.

**Learning Activity:** Group survey project (4–5 members) — define topic, design questionnaire (5 demographic + 15 specific items), create in Google Forms.

---

## Chapter 3 — Visual Presentation Methods and Techniques

### 3.1 What Are Visual Presentation Methods?

> Techniques and tools used to convey information through **visual elements** to enhance comprehension, engagement, and impact.

### 3.2 Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Visual Elements** | Images, graphics, charts, diagrams, videos, non-textual components |
| **Enhanced Comprehension** | Simplifies complex data / abstract concepts |
| **Increased Engagement** | Breaks monotony, captures attention, prevents fatigue |
| **Memorability** | People remember what they see better than what they hear |
| **Storytelling** | Creates compelling narrative guiding the audience |

### 3.3 Common Visual Presentation Methods

| Method | Description | Tips |
|--------|-------------|------|
| **Slideshows** | Digital slides (PowerPoint, Canva, Google Slides, Keynote) | Minimal text, high-quality visuals, consistent design, animations sparingly |
| **Infographics** | Text + images + graphics summarizing data/processes concisely | Excellent for data summaries and processes |
| **Video Presentations** | Pre-recorded or real-time video with visual + auditory elements | Highly engaging |
| **Charts & Graphs** | Bar, line, pie, scatter for numerical data | Visualize trends, comparisons, relationships |
| **Whiteboards / Flip Charts** | Real-time, informal, interactive | Great for brainstorming, spontaneity |
| **Poster Presentations** | Large physical poster (text + images + graphics) | Common in academic/research settings |
| **Handouts** | Supplementary printed material | Takeaway references, detailed explanations |
| **Interactive Presentations** | Clickable elements, quizzes, polls, embedded multimedia | Audience participation |

### 3.4 Visualizing Complex Models: Flowcharts

> A **flowchart** is a visual representation of the sequence of steps and decisions needed to perform a process. It uses standard symbols to represent logic, linked by connecting lines and directional arrows.

#### Flowchart Symbols (Elements)

| Symbol | Shape | Meaning |
|--------|-------|---------|
| **Terminal** | Oval / Rounded rectangle | Start or end of program |
| **Process** | Rectangle | Mathematical operations / processing step |
| **Decision** | Diamond | Yes/No or multi-way branching |
| **Input/Output** | Parallelogram | Data input or output |
| **Document** | Rectangle with wavy base | Document or report |
| **Manual Input** | Rectangle with slanted top | User prompted for manual input |
| **Connector** | Arrow | Flow direction / sequence |
| **On-page Connector** | Circle | Connects parts on the same page |
| **Off-page Connector** | Pentagon / arrow shape | Connects parts across different pages |

#### Types of Flowcharts

| Type | Purpose |
|------|---------|
| **Swimlane Flowcharts** (Cross-functional) | Show responsibilities by role/department using parallel lanes |
| **Data Flow Diagrams (DFD)** | Show how data moves through a system (sources, transformations, storage) |
| **Influence Diagrams** | Show decision problems: key elements (decisions, uncertainties, objectives) as nodes with influence arrows |
| **Workflow Diagrams** | Sequence of tasks and activities in a project |
| **Process Flow Diagrams** | Steps in a manufacturing or business process |
| **Yes/No Flowcharts** | Binary decision paths |
| **Decision Flows** | Logical breakdown of complex decisions |

#### Uses of Flowcharts

- Manufacturing & assembly line structuring
- Project planning & management (roadmap, dependencies)
- Algorithm visualization (program logic)
- Business process documentation
- Education, science, medicine, government

#### Worked Example — Instant Noodle Preparation System

**Scenario:** A smart kitchen automates instant noodle prep. User selects noodle type & flavor. System checks ingredients (noodles, seasoning, hot water). If available → boil water → add noodles → wait 3 min → add seasoning → notify user. If not → re-check.

| Component | Examples |
|-----------|----------|
| **Inputs** | Noodle type, flavor, water level |
| **Decisions** | Water available? Noodles in stock? |
| **Processes** | Boil water → Add noodles → Wait 3 min → Add seasoning |
| **Output** | "Noodles ready" notification |

---

## Vocabulary & Key Terms

| Term | Definition |
|------|-----------|
| **Data** | Raw, unprocessed facts collected from various sources |
| **Information** | Data processed with context to provide meaning and insight |
| **Quantitative Data** | Numerical data that can be measured/counted (discrete or continuous) |
| **Qualitative Data** | Descriptive, non-numerical data (colors, labels, opinions) |
| **Data Visualization** | Graphic representation of data (charts, plots, infographics) |
| **Dashboard** | Unified display of multiple visual data sources for real-time tracking |
| **Textual Presentation** | Describing data in words and sentences |
| **Tabular Presentation** | Data organized in rows and columns |
| **Graphical Presentation** | Visual representation via charts, graphs, maps |
| **Primary Data Source** | Data collected by yourself (surveys, experiments) |
| **Secondary Data Source** | Data collected by others (government, research, databases) |
| **Real-Time Data Source** | Live data via APIs (weather, social media, analytics) |
| **Likert Scale** | Rating scale (e.g., 1–5, Strongly Disagree → Strongly Agree) |
| **Double-Barreled Question** | Question that asks about two things at once (should be avoided) |
| **Filter/Contingency Question** | Question that routes respondents based on their answer |
| **Matrix Question** | Grid asking respondents to rate multiple items on the same scale |
| **Infographic** | Visual representation combining text, images, and graphics to convey complex info concisely |
| **Flowchart** | Step-by-step visual diagram of a process using standard symbols |
| **Swimlane Flowchart** | Flowchart using parallel lanes to show responsibilities by role |
| **Data Flow Diagram (DFD)** | Visual of how data moves through a system |
| **Influence Diagram** | Graphical representation of a decision problem showing influences between variables |
| **Heat Map** | Color-coded visualization showing data intensity across regions or grids |
| **Tree Map** | Nested rectangles showing hierarchical part-to-whole relationships |
| **Scatter Plot** | Graph plotting points to show correlation between two variables |
| **Bubble Chart** | Scatter plot where point size encodes a third variable |
| **Edward Tufte** | Author of *The Visual Display of Quantitative Information* (1983), pioneer of data visualization principles |

---

## Potential Exam Questions

### Short Answer / Concept Questions

1. **Distinguish between data and information.** Give an example of each.
2. **What are the three types of data presentation?** Describe when each is most appropriate.
3. **Explain the five principles of effective data visualization.** Why is accuracy especially critical?
4. **What is the difference between a histogram and a bar chart?**
5. **List four best practices for data visualization** and explain why each matters.
6. **Differentiate between primary, secondary, and real-time data sources.** Give an example of a visualization for each.
7. **What are the A–F principles of constructing effective survey questions?** Give an example of a poorly written question and how to fix it.
8. **Compare closed-ended and open-ended questions.** When would you use each?
9. **What is a Likert scale?** What is the danger of not providing balanced response options?
10. **List at least five common visual presentation methods.** Which is best for summarizing complex data concisely?

### Application / Design Questions

11. **Chart selection:** Which chart type would you use for each scenario?
    - Comparing market share of 5 companies → ?
    - Showing global temperature change from 1900–2024 → ?
    - Displaying the correlation between study hours and exam scores → ?
    - Showing frequency distribution of test results → ?
    - Displaying hierarchical budget allocation across departments → ?

12. **Questionnaire design:** Write three survey questions for the topic "Student satisfaction with campus food services." Include at least two different question types. Criticize one of your own questions using the A–F principles.

13. **Flowchart creation:** Draw a flowchart (as pseudocode or symbol description) for: "A vending machine that accepts coins, checks if the selected item is in stock and costs ≤ the amount inserted, dispenses the item, and returns change."

14. **Visual critique:** Find a real-world chart (or imagine one). How would you evaluate it using the five principles of effective data visualization?

15. **Dashboard design:** What visualizations would you include on a dashboard tracking a university's enrollment trends, and why?

### Case Study Questions

16. **The Instant Noodle System:** For the smart kitchen example, identify each flowchart element (inputs, decisions, processes, outputs). What would change if you added an "optional add-ins" step?

17. **Survey topic refinement:** Take the broad topic "Student mental health" and walk through all 5 steps to define a focused survey topic with a clear objective and three specific questions.

18. **Chart appropriateness:** A student creates a pie chart with 12 categories to show budget allocation. Critique this choice using the principles of effective visualization. What alternative chart type would you suggest?

---

## Materials Inventory

| # | File | Chapter | Pages | Status |
|---|------|---------|-------|--------|
| 1 | `Chapter1-1 Introduction to the principles.pdf` | Ch. 1 — Introduction | 41 slides | ✅ Analyzed |
| 2 | `Chapter2-1 Design principles.pdf` | Ch. 2 — Design Principles | 27 slides | ✅ Analyzed |
| 3 | `Chapter3-1 Visual presentation methods and techniques that increase the understanding of complex data and models.pdf` | Ch. 3 — Visual Methods | 24 slides | ✅ Analyzed |
| — | *Chapter 4 — Common tools* | *Not yet covered* | — | ⏳ TBD |
| — | *Chapter 5 — Identification of patterns* | *Not yet covered* | — | ⏳ TBD |
| — | *Chapter 6 — Trends and differences* | *Not yet covered* | — | ⏳ TBD |
| — | *Chapter 7 — Practical uses of multimedia* | *Not yet covered* | — | ⏳ TBD |

**Vault location:** `10 - Projects/Semester 1-2026/CSX4601 (541) Selected Topic in Presentation and Data Visualization Techniques/Materials/`

---

> **"Data visualization is not just about making things look good. It is about making data make sense."** — *Course Summary, Ch. 1*
