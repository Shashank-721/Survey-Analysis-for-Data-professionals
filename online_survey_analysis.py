import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("Online_Survey.xlsx")

# Basic information
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

# -------------------------
# 1. Job roles
# -------------------------

roles = df["Q1 - Which Title Best Fits your Current Role?"].value_counts().head(10)

print("\nTop 10 job roles:")
print(roles)

plt.figure(figsize=(8, 5))
sns.barplot(x=roles.values, y=roles.index)
plt.title("Top 10 Job Roles")
plt.xlabel("Number of People")
plt.ylabel("Job Role")
plt.show()

# -------------------------
# 2. Programming languages
# -------------------------

languages = df["Q5 - Favorite Programming Language"].value_counts()

print("\nProgramming languages:")
print(languages)

plt.figure(figsize=(8, 5))
sns.barplot(x=languages.values, y=languages.index)
plt.title("Favorite Programming Languages")
plt.xlabel("Number of People")
plt.ylabel("Language")
plt.show()

# -------------------------
# 3. Salary
# -------------------------

salary = df["Q3 - Current Yearly Salary (in USD)"].value_counts()

print("\nSalary ranges:")
print(salary)

plt.figure(figsize=(9, 5))
sns.barplot(x=salary.index, y=salary.values)
plt.title("Salary Distribution")
plt.xlabel("Salary Range")
plt.ylabel("Number of People")
plt.xticks(rotation=45)
plt.show()

# -------------------------
# 4. Age
# -------------------------

df["Q10 - Current Age"] = pd.to_numeric(
    df["Q10 - Current Age"], errors="coerce"
)

print("\nAge statistics:")
print(df["Q10 - Current Age"].describe())

plt.figure(figsize=(8, 5))
sns.histplot(df["Q10 - Current Age"].dropna(), bins=15, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()

# -------------------------
# 5. Career switch
# -------------------------

career = df["Q2 - Did you switch careers into Data?"].value_counts()

print("\nCareer switch:")
print(career)

plt.figure(figsize=(6, 5))
sns.barplot(x=career.index, y=career.values)
plt.title("Career Switch Into Data")
plt.xlabel("Switched Career?")
plt.ylabel("Number of People")
plt.show()

# -------------------------
# 6. Job satisfaction
# -------------------------

satisfaction_columns = [
    "Q6 - How Happy are you in your Current Position with the following? (Salary)",
    "Q6 - How Happy are you in your Current Position with the following? (Work/Life Balance)",
    "Q6 - How Happy are you in your Current Position with the following? (Coworkers)",
    "Q6 - How Happy are you in your Current Position with the following? (Management)",
    "Q6 - How Happy are you in your Current Position with the following? (Upward Mobility)",
    "Q6 - How Happy are you in your Current Position with the following? (Learning New Things)"
]

# Convert satisfaction columns to numbers
for column in satisfaction_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

average_satisfaction = df[satisfaction_columns].mean()

print("\nAverage satisfaction:")
print(average_satisfaction)

plt.figure(figsize=(9, 5))
sns.barplot(x=average_satisfaction.values, y=average_satisfaction.index)
plt.title("Average Job Satisfaction")
plt.xlabel("Average Score")
plt.ylabel("Satisfaction Area")
plt.xlim(0, 10)
plt.show()

# -------------------------
# 7. Satisfaction correlation
# -------------------------

plt.figure(figsize=(8, 6))
sns.heatmap(
    df[satisfaction_columns].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Job Satisfaction Correlation")
plt.show()

print("\nAnalysis finished!")
