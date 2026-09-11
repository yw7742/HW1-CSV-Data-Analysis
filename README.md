# Titanic Dataset Analysis

## Why I Chose This Dataset

I chose the Titanic passenger dataset because it contains clear and structured information about passengers, including their age, sex, passenger class, fare, and survival status. The dataset is easy to understand and contains both numerical and categorical data. It also allows me to ask meaningful questions about passenger characteristics and survival.

## Dataset Description

The Titanic dataset contains information about passengers who were aboard the Titanic. Each row represents one passenger, and each column represents an attribute of that passenger.

Some important columns in the dataset include:

* `PassengerId`: A unique ID for each passenger
* `Survived`: Whether the passenger survived (1 = survived, 0 = did not survive)
* `Pclass`: Passenger class (1, 2, or 3)
* `Name`: Passenger name
* `Sex`: Passenger sex
* `Age`: Passenger age
* `Fare`: Ticket fare
* `Embarked`: Port where the passenger boarded the Titanic

## Three Data Questions

### Question 1: How many passengers survived?

Output:
342

The dataset can answer this question because each row represents one passenger and the `Survived` column records whether that passenger survived. By filtering the dataset to include only rows where `Survived` equals 1 and then counting those rows, we can determine the total number of survivors.

### Question 2: Among first-class passengers who survived, how many were male and how many were female?

Output:
female    91
male      45

The dataset can answer this question because it contains information about survival status, passenger class, and sex. We can use two conditions to select passengers whose `Survived` value is 1 and whose `Pclass` value is 1. We can then use the `Sex` column to count the number of male and female passengers in this group.

### Question 3: What was the average age of passengers in each passenger class?

Output:
Pclass
1    38.23
2    29.88
3    25.14

The dataset can answer this question because it contains both passenger class information in the `Pclass` column and passenger age information in the `Age` column. By grouping the rows according to passenger class and calculating the mean of the `Age` column, we can compare the average age across the three passenger classes.

## What the Data Cannot Answer

One question I would like to answer is why some passengers were able to reach lifeboats while others were not. The dataset does not contain detailed information about each passenger's location on the ship, their distance from lifeboats, the evacuation process, or their actions during the sinking. Without this information, it would be misleading to assume that survival was caused only by characteristics such as sex, age, or passenger class. The dataset can show relationships between these variables and survival, but it cannot by itself explain why a particular passenger survived.
