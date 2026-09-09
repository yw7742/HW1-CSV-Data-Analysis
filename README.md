# 2015 NYC Street Tree Census Analysis

## Why I Chose This Dataset

I chose the 2015 NYC Street Tree Census dataset because I was interested in learning more about the distribution and condition of street trees in New York City. The dataset contains information about tree species, location, health, and status, which allows me to ask several different questions about New York City's street trees. It also includes both categorical and numerical variables, making it useful for practicing data exploration with pandas.

## Three Data Questions

### Question 1: How many street trees are recorded in each borough?

The dataset can answer this question because each row represents a street tree and the `borough` column identifies the borough where the tree is located. By counting the values in this column, we can compare the number of recorded trees across the five boroughs.

Output:
Queens           250551
Brooklyn         177293
Staten Island    105318
Bronx             85203
Manhattan         65423

According to the dataset, Queens has the largest number of recorded street trees.

### Question 2: What are the 10 most common tree species in the dataset?

The dataset can answer this question because the `spc_common` column contains the common species name of each tree. By counting how often each species appears, we can determine which tree species are most common.

Output:
London planetree     87014
honeylocust          64264
Callery pear         58931
pin oak              53185
Norway maple         34189
littleleaf linden    29742
cherry               29279
Japanese zelkova     29258
ginkgo               21024
Sophora              19338

The most common tree species in the dataset is the London planetree.

### Question 3: Among trees that are alive and in good health, how many are located in each borough?

The dataset can answer this question because it contains separate columns for tree status, health, and borough. I can first filter the dataset to include only trees whose status is `Alive` and whose health is `Good`, and then count those trees by borough.

Output:
Queens           194008
Brooklyn         138212
Staten Island     82669
Bronx             66603
Manhattan         47358

Queens has the largest number of trees that are both alive and in good health.

## What the Data Cannot Answer

One question I would like to answer is why some boroughs have more healthy street trees than others. The dataset can show the number, location, species, and condition of trees, but it does not contain enough information about factors such as maintenance spending, environmental conditions, pollution levels, soil quality, or neighborhood investment. Without these additional variables, it would be misleading to assume that differences in tree health are caused by any one factor. The dataset can identify patterns, but it cannot by itself explain the causes of those patterns.
