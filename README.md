# 📊 Data Professionals Survey Analysis | Power BI

## 👋 About the Project

I wanted to understand what working in the data industry actually looks like — not just in terms of salary, but also the day-to-day experience of people working in different data roles.

For this project, I used survey data from **630 data professionals** and built an interactive Power BI dashboard to explore questions around **salary, job roles, countries, programming languages, career entry, and job satisfaction**.

The project is split into two main parts:

* **Career & Salary Analysis** — Who are the respondents, what roles do they have, what do they earn, and what skills do they use?
* **Satisfaction Analysis** — How satisfied are they with their salary, management, and work-life balance?

The main idea was to take a collection of survey responses and turn it into a story that someone can actually understand and learn from.

---

# 🎯 Problem Statement

The data industry has grown rapidly, but there are still a lot of questions for people trying to understand it.

For example:

* Which data roles tend to have higher salaries?
* Which programming languages are most commonly used?
* Where are data professionals located?
* Is it difficult to get into the data industry?
* Are people actually happy with their jobs?
* Is salary the biggest factor affecting job satisfaction?
* Does management satisfaction change depending on someone's role or industry?

The survey contains the answers, but looking at hundreds of individual responses makes it difficult to see the bigger picture.

### My objective

I wanted to use **Power BI to turn the raw survey data into an interactive dashboard** that could answer these questions and highlight the patterns hidden in the data.

---

# 🔎 Questions I Wanted to Answer

### Career & Salary

1. Which job titles have the highest average salary?
2. Where are the survey respondents from?
3. Which programming languages are most popular?
4. How is the survey population distributed by gender?
5. How difficult do people find it to get into the data industry?

### Job Satisfaction

1. How satisfied are people with their work-life balance?
2. How satisfied are they with their salary?
3. How satisfied are they with management?
4. Does management satisfaction vary by job title?
5. Does management satisfaction vary by industry?
6. Is there a clear relationship between salary and management satisfaction?

---

# 📂 Dataset

The dataset contains survey responses from people working in or interested in the data field.

Some of the information included in the dataset is:

* Job Title
* Salary
* Country
* Industry
* Favorite Programming Language
* Gender
* Age
* Work-Life Balance Satisfaction
* Salary Satisfaction
* Management Satisfaction
* Difficulty Getting into Data
* And other survey responses

The survey contains **630 respondents**, with an average respondent age of approximately **29.87 years**.

> **Note:** These results represent the people included in this particular survey. They should not be treated as representative of every data professional worldwide.

---

# 🧹 My Approach

I followed a fairly simple data-analysis workflow:

```text
Raw Survey Data
       ↓
Data Preparation
       ↓
Data Transformation
       ↓
Exploratory Analysis
       ↓
DAX Measures / KPIs
       ↓
Dashboard Design
       ↓
Insights
       ↓
Recommendations
```

### Data Preparation

I imported the survey data into Power BI and prepared it so that the responses could be compared across different categories such as job title, country, industry, programming language, and satisfaction.

### Analysis

I then looked at the data from two different angles:

**1. Career & Compensation**

Understanding the people in the survey and the career landscape they represent.

**2. Job Satisfaction**

Understanding how people feel about different aspects of their work.

### Dashboard Design

I tried to keep the dashboard focused on questions rather than just filling the page with charts.

Different visuals were used depending on what I was trying to compare:

* Bar charts for comparing job roles and satisfaction
* Donut charts for categorical distributions
* KPI cards for headline numbers
* Gauge charts for overall satisfaction scores
* Treemap for country distribution

---

# 📊 Dashboard — Page 1

## Career & Salary Analysis

The first page gives an overview of who the respondents are and what their careers look like.

### What can we see?

**630 survey respondents**

**29.87 average age**

The page also looks at:

* Average salary by job title
* Country distribution
* Favorite programming languages
* Gender distribution
* Difficulty getting into the data industry

### 💰 Salary by Job Title

One of the clearest differences in the dashboard is salary across job titles.

The dashboard compares:

* Data Scientist
* Data Engineer
* Data Architect
* Data Analyst
* Database Developer
* Other
* Student / Looking / None

Among the job categories shown, **Data Scientist has the highest average salary**.

This gives us a quick look at how compensation differs across the different career paths represented in the survey.

### 💻 Favorite Programming Languages

One result that immediately stands out is **Python**.

Python is by far the most commonly selected programming language among the respondents, with R and other languages following behind.

For someone trying to get into data, this is an interesting indication of the technical skills represented most heavily in this survey.

### 🌎 Where Are the Respondents From?

The survey includes respondents from several countries, with the dashboard highlighting:

* Canada
* India
* United Kingdom
* United States
* Other

This gives some geographic context to the rest of the analysis.

### 🚪 How Difficult Is It to Get Into Data?

The respondents were also asked how difficult it is to get into the data industry.

The responses range from:

* Very Easy
* Easy
* Neither Easy nor Difficult
* Difficult
* Very Difficult

The largest group selected **"Neither easy nor difficult"**, while a considerable number of respondents also described the process as difficult.

---

# 😊 Dashboard — Page 2

## Satisfaction Analysis

After looking at salaries, roles, and other career characteristics, I wanted to answer another question:

> **Are data professionals actually satisfied with their jobs?**

For this page, I focused on three main satisfaction metrics.

| Satisfaction Metric | Average Score |
| ------------------- | ------------: |
| Work-Life Balance   | **5.74 / 10** |
| Management          | **5.33 / 10** |
| Salary              | **4.27 / 10** |

The first thing that stands out is that **salary satisfaction is the lowest of the three**, at 4.27/10.

Work-life balance has the highest average score at 5.74/10.

This made me interested in digging a little deeper instead of stopping at the overall averages.

---

# 🔍 Going Beyond the Overall Average

The second page breaks management satisfaction down by different groups.

### 🏢 Management Satisfaction by Industry

Management satisfaction is compared across industries such as:

* Healthcare
* Real Estate
* Finance
* Technology
* Agriculture
* Telecommunications
* Education
* Construction
* Other

This helps show that the experience of working in data isn't necessarily the same across every industry.

### 👨‍💻 Management Satisfaction by Job Title

I also compared management satisfaction across different roles:

* Database Developer
* Data Scientist
* Data Analyst
* Data Engineer
* Data Architect
* Other
* Student / Looking / None

This gives us another perspective on whether people in different positions are experiencing management differently.

### 💰 Salary vs. Management

Finally, I compared salary and management satisfaction across job titles.

This was an interesting part of the analysis because it asks a simple question:

> **Does a higher-paying role automatically mean a better experience with management?**

The dashboard suggests that the relationship isn't that simple.

This is a good example of why looking at only one KPI can sometimes give an incomplete picture.

---

# 💡 Key Takeaways

After exploring the dashboard, these were the main things that stood out to me.

### 1. Different data roles have noticeably different salary levels

The average salary isn't the same across the different job titles in the survey.

**Data Scientist** appears at the top of the salary comparison, while other roles sit at different levels.

---

### 2. Python is extremely common

Python clearly dominates the programming-language responses.

If you're looking at the technical skills represented by this survey, Python is the obvious standout.

---

### 3. Getting into data isn't necessarily easy

While the largest group of respondents chose **"Neither easy nor difficult,"** a significant number also reported that getting into data was difficult or very difficult.

That suggests that entering the industry can be challenging for a meaningful portion of the respondents.

---

### 4. Salary satisfaction is relatively low

The average salary satisfaction score is only **4.27/10**.

Compared with:

* **5.74/10** for work-life balance
* **5.33/10** for management

salary is the lowest-rated of the three major satisfaction measures.

---

### 5. Management experience varies

Management satisfaction isn't identical across every job title or industry.

This suggests that job satisfaction is influenced by more than just compensation.

---

### 6. Salary isn't the whole story

One of the biggest things I took away from the project is that **salary and job satisfaction shouldn't be looked at in isolation**.

Someone can have a well-paying role and still have a different experience when it comes to management or work-life balance.

That's why I wanted the second dashboard page to go beyond simply showing salary numbers.

---

# 🎯 What Could Organizations Take From This?

Since this is survey data rather than data from one specific company, these aren't direct recommendations to a particular organization.

However, the results do suggest a few areas that could be worth looking at.

### 💰 Compensation

With salary satisfaction averaging **4.27/10**, companies could look at whether employees feel their compensation matches their responsibilities and expectations.

### 👥 Management

Since management satisfaction differs between roles and industries, organizations could look more closely at areas such as:

* Communication
* Leadership
* Employee support
* Career development
* Relationship between managers and teams

### ⚖️ Look Beyond Salary

The dashboard shows why employee satisfaction is more complicated than simply asking:

> "How much do you get paid?"

Work-life balance, management, and compensation all tell different parts of the story.

---

# 📈 What This Dashboard Is Really Trying to Show

I didn't want this project to be just a collection of Power BI charts.

The story I wanted to tell was:

```text
Who are the people working in data?
              ↓
What roles do they have?
              ↓
What do their salaries look like?
              ↓
What skills are they using?
              ↓
How difficult is it to enter the industry?
              ↓
Are they satisfied with their jobs?
              ↓
What might be influencing that satisfaction?
```

That progression is what makes the dashboard useful to me as an analyst.

Instead of looking at individual survey responses, we can use the dashboard to quickly move from **descriptive information** to **comparisons and insights**.

---

# 🖥️ Dashboard Preview

## Page 1 — Career & Salary Analysis

![Career & Salary Analysis](images/dashboard-page-1.png)

This page focuses on salary, job roles, countries, programming languages, demographics, and difficulty entering the data industry.

## Page 2 — Satisfaction Analysis

![Satisfaction Analysis](images/dashboard-page-2.png)

This page focuses on work-life balance, salary satisfaction, management satisfaction, and comparisons across industries and job titles.

---

# 🛠️ Tools Used

* **Power BI Desktop**
* **Power Query**
* **DAX**
* **Microsoft Excel**
* **Data Cleaning & Transformation**
* **Exploratory Data Analysis**
* **Data Visualization**

---

# 📁 Project Structure

```text
Data-Professionals-Survey-PowerBI/
│
├── Online_Survey.xlsx
├── Survey Dashboard final.pbix
├── Survey Dashboard final.pbit
├── Survey Dashboard final.pdf
│
├── images/
│   ├── dashboard-page-1.png
│   └── dashboard-page-2.png
│
└── README.md
```

---

# 🚀 How to Use the Project

### 1. Download or clone the repository

```bash
git clone https://github.com/Shashank-721
```

### 2. Open the Power BI file

Open:

```text
Survey Dashboard final.pbix
```

using **Power BI Desktop**.

### 3. Explore the dashboard

The report contains two pages:

**Page 1 → Career & Salary Analysis**

**Page 2 → Satisfaction Analysis**

Click around the different visualizations and explore the data from different perspectives.

---

# ⚠️ Limitations

There are a few things worth keeping in mind when interpreting this analysis.

### Survey sample

The results are based only on the respondents included in the survey and shouldn't be treated as representative of the entire data industry.

### Self-reported information

Salary and satisfaction are based on what respondents reported, so there may be differences in how people interpreted or answered the questions.

### Correlation isn't causation

The dashboard shows relationships and differences in the survey data.

It does **not** prove that one factor causes another.

For example:

> A higher salary does not necessarily cause higher job satisfaction.

### Original survey

This project analyzes an existing survey dataset. I did not design or conduct the original survey, so the methodology and respondent selection are outside the scope of this project.

---

# 🎓 What I Learned From This Project

This project gave me a chance to practice the complete process of turning raw data into a finished analytical product.

I worked on:

* Cleaning and preparing survey data
* Exploring different dimensions of the dataset
* Creating KPIs and measures
* Comparing groups using Power BI
* Choosing appropriate visualizations
* Designing a dashboard around a story
* Turning visual findings into insights
* Thinking about how the results could be useful to a decision-maker

More importantly, it helped me understand that **a good dashboard isn't just about making charts look good**.

The real value comes from asking the right questions, finding useful patterns, and presenting those findings in a way that someone else can quickly understand.

---

# 👤 About Me

**Shashank Pandey**

Aspiring Data Analyst | Power BI | SQL | Excel | Data Visualization

I'm building projects like this to improve my skills in **data analysis, visualization, and turning raw data into useful insights.**

### Connect with me

🔗 **LinkedIn:** [linkedin.com/in/shashank-pandey-data](https://www.linkedin.com/in/shashank-pandey-data/)

💻 **GitHub:** [github.com/Shashank-721](https://github.com/Shashank-721)

---

## ⭐ Like the Project?

If you found the project interesting, feel free to **star the repository** ⭐

Thanks for checking it out!
