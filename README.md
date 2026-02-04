# Homework 3: 311 Service Request Analysis

> [!CAUTION]
> Make sure the name of this repository / directory has your GitHub username in it. Otherwise, you will not be able to submit any work. You can find the repository with your GitHub username through Pawtograder.

## Due Wednesday, February 18 at 6pm Pacific / 9pm Eastern

## Learning Outcomes

* Using lists, sets, and dictionaries for data manipulation
* Applying the accumulator pattern for data aggregation
* Analyzing real-world datasets using Pandas and NumPy
* Creating data visualizations to reveal patterns

## NOTE: Open the entire folder in VSCode, not individual files
In VSCode, open this assignment through `File` > `Open Folder...` > open the entire repo. Do not open individual files. Opening the entire folder makes it so that:
- the `import` statements can find the pages
- Python runs the code "from" the right location
- the `.vscode` settings automatically get applied
- the terminal opens at the right location

In general, open the entire folder for all assignments in this course, rather than individual files.

## Overview
This assignment is an extension to the previous assignment (HW 2), in which you loaded and searched a dataset of 311 service request data. In this assignment, you will analyze that data and create a visualization tool to plot the case locations on a map.

### Dataset Options
As with HW2, there are two datasets in the `data` folder. They are formatted versions of data from these websites:

* **Oakland/San Francisco**: https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/data_preview
* **Boston**: https://data.boston.gov/dataset/311-service-requests

Your code should work on both provided files, though you will need to submit your code having selected one for analysis in the code.

## Instructions

### 0. Read `main.py`

You do not need to write any code in `main.py`. It is there for you to run your code and see its output.

### 1. Require columns in the dataset

As with Homework 2, the constructors of the below classes should load the dataset from the given file. They should raise a `KeyError` if the provided file doesn't contain the correct column names. You should place this constant in an appropriate place in a file, and use it to check for the correct column names in each constructor:

```python
    REQUIRED_COLUMNS = [
        'CaseID', 'Status', 'Category', 'Street', 'Supervisor District',
        'Neighborhood', 'Police District', 'Latitude', 'Longitude', 'Point',
        'point_geom', 'OpenedDate', 'ClosedDate', 'days_open', 'selected'
    ]
```

These are the "default" required column names. As specified in the constructor comments, the client can also specify their own required columns, if they wish.

We recommend putting this column in only one file, and importing it in other places.

### 2. Data Processing and Sorting (`sorting.py`)

There are comments with instructions in the file, but in summary, you will:

1. Sort the dataset by the number of days the case has been open
2. Create an "urgency ranking" where you choose how urgent each 311 case cateogy is.
    You must rank at least 10 categories. In your ranking, a higher score must indicate
    more urgency, and a lower score must indicate less urgency.
3. Filter the dataset to only include categories for which you have determined an
    urgency ranking, and sort it by urgency ranking

Don't forget to test these methods in `test_sorting.py`.

### 3. Data Analysis (`analysis.py`)

You will write methods that:

1. Count the total number of cases per neighborhood
2. Calculate the average number of days that a case stays open
3. Count the number of cases that stay open longer than average, for each neighborhood
4. For each neighborhood, determine the percentage of days that stay open longer than average

Don't forget to test these methods in `test_analysis.py`.

### 4. Visualization (`visualization.py`)

You will write methods that:

1. Display a bar graph that shows, for each neighborhood, the percentage of cases that stay open longer than the overall average case
2. Display a scatterplot of cases, with longitude on the horizontal axis and latitude on the vertical axis (like a map)

Make sure to include the parts mentioned in the comments, such as axis labels and titles.

You are not required to test visualizations.

Good luck!
