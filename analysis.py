import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# --------------------------------------------------
# Required Data Inspection Tasks
# --------------------------------------------------

# 1. Print the first 2 rows
print("1. First 2 rows:")
print(df.head(2))
print()


# 2. Print the first row
print("2. First row:")
print(df.iloc[0])
print()


# 3. Print rows 10-19
print("3. Rows 10-19:")
print(df.iloc[10:20])
print()


# 4. Print column names
print("4. Column names:")
print(df.columns.tolist())
print()


# 5. Print the first 10 values of one column
print("5. First 10 values of the Sex column:")
print(df["Sex"].head(10))
print()


# 6. Print the first 10 rows of three columns
print("6. First 10 rows of Name, Sex, and Age:")
print(df[["Name", "Sex", "Age"]].head(10))
print()


# --------------------------------------------------
# Three Data Questions
# --------------------------------------------------

# Question 1: How many passengers survived?
survived_count = df[df["Survived"] == 1].shape[0]

print("Question 1: How many passengers survived?")
print(survived_count)
print()


# Question 2:
# Among first-class passengers who survived,
# how many were male and how many were female?
first_class_survivors = df[
    (df["Survived"] == 1) & (df["Pclass"] == 1)
]["Sex"].value_counts()

print("Question 2: Among first-class passengers who survived,")
print("how many were male and how many were female?")
print(first_class_survivors)
print()


# Question 3:
# What was the average age of passengers in each passenger class?
average_age_by_class = df.groupby("Pclass")["Age"].mean().round(2)

print("Question 3: What was the average age of passengers in each passenger class?")
print(average_age_by_class)