import pandas as pd


# --------------------------------------------------
# Load the CSV dataset
# --------------------------------------------------

df = pd.read_csv("2015_Street_Tree_Census_-_Tree_Data_20260909.csv")


# --------------------------------------------------
# Required Task 1: Print the first 2 rows
# --------------------------------------------------

print("1. First 2 rows:")
print(df.head(2))


# --------------------------------------------------
# Required Task 2: Print the first row
# --------------------------------------------------

print("\n2. First row:")
print(df.iloc[0])


# --------------------------------------------------
# Required Task 3: Print rows 10-19
# --------------------------------------------------

print("\n3. Rows 10-19:")
print(df.iloc[10:20])


# --------------------------------------------------
# Required Task 4: Print column names
# --------------------------------------------------

print("\n4. Column names:")
print(df.columns.tolist())


# --------------------------------------------------
# Required Task 5:
# Print the first 10 values of one column
# --------------------------------------------------

print("\n5. First 10 values of the borough column:")
print(df["borough"].head(10))


# --------------------------------------------------
# Required Task 6:
# Print the first 10 rows of three columns
# --------------------------------------------------

print("\n6. First 10 rows of borough, health, and species:")
print(df[["borough", "health", "spc_common"]].head(10))


# --------------------------------------------------
# Three Data Questions
# --------------------------------------------------


# Question 1:
# How many street trees are recorded in each borough?

print("\nQuestion 1: How many street trees are recorded in each borough?")

borough_counts = df["borough"].value_counts()

print(borough_counts)


# Explanation:
# The dataset can answer this question because each row represents
# a street tree and the "borough" column identifies the borough
# where that tree is located.


# --------------------------------------------------


# Question 2:
# What are the 10 most common tree species in the dataset?

print("\nQuestion 2: What are the 10 most common tree species?")

species_counts = df["spc_common"].value_counts().head(10)

print(species_counts)


# Explanation:
# The dataset can answer this question because the "spc_common"
# column records the common species name for each tree.
# Counting the number of occurrences of each species allows me
# to identify the most common species.


# --------------------------------------------------


# Question 3:
# Among trees that are alive and in good health,
# how many are located in each borough?

print(
    "\nQuestion 3: Among trees that are alive and in good health, "
    "how many are located in each borough?"
)

good_alive_trees = df[
    (df["status"] == "Alive") &
    (df["health"] == "Good")
]

good_alive_by_borough = good_alive_trees["borough"].value_counts()

print(good_alive_by_borough)


# Explanation:
# The dataset can answer this question because it contains separate
# columns for tree status, tree health, and borough.
# I can filter the data using two conditions:
# status must be "Alive" and health must be "Good".
# After filtering, we can count the trees in each borough.