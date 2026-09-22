# 🏅 Olympic Athlete Data Analysis

## Python Analysis of Olympic Athlete Trends

### Project Overview

This project uses Python to analyze historical Olympic athlete data and explore patterns in athlete height, age, and medal outcomes over time.

Using pandas for data manipulation and Matplotlib for visualization, I cleaned and organized athlete-level data, created grouped summaries, measured variation across Olympic events, and produced visualizations to examine how athlete characteristics have changed over time.

## Analytical Questions

The analysis explored questions such as:

- How has the average height of Olympic athletes changed over time?
- Which Olympic events show the greatest variation in athlete height?
- How do athlete height patterns differ by sex and season?
- How have gold medal counts varied by country and year?
- How has the average age of Olympic athletes changed over time?
- Are there differences in age trends between the Summer and Winter Games?

## Data Preparation

The Python script begins by loading the Olympic athlete dataset with pandas and examining:

- Dataset dimensions
- Column names
- Missing values
- Data completeness

Columns with insufficient non-null observations are removed before further analysis.

## Athlete Height Analysis

The data is separated by:

- Summer and Winter Games
- Female and male athletes
- Year
- Olympic event

Using pandas `groupby()` operations, I calculated mean athlete height by year and event.

I then calculated the variance of mean height across years to identify events where athlete height changed the most over time.

## Sports Examined

The analysis includes visual exploration of selected events such as:

- Women's Basketball
- Women's Volleyball
- Women's Individual All-Around Gymnastics
- Men's Basketball
- Men's 100-Meter Freestyle Swimming

For each event, the script calculates mean athlete height by year and generates a visualization showing how average height changed over time.

## Medal Analysis

The project also examines Olympic gold medals.

Gold-medal observations are filtered from the dataset and grouped by:

**Country (NOC) × Year**

This creates a historical summary of gold-medal outcomes across countries and Olympic Games.

## Athlete Age Analysis

Average athlete age is calculated by country and year.

The analysis also compares average athlete age across Summer and Winter Olympic Games over time and creates a visualization of those trends.

## Python Techniques Demonstrated

- Python
- pandas
- Matplotlib
- Data cleaning
- Missing-value analysis
- Data filtering
- `groupby()` aggregation
- Descriptive statistics
- Variance analysis
- Data visualization
- Trend analysis
- Reproducible analysis

## Why This Project Matters

Sports datasets often contain observations from different eras, events, countries, and athlete populations. Organizing those observations into meaningful groups makes it possible to identify trends that are difficult to see in raw data.

This project demonstrates my ability to move from a large athlete-level dataset to organized summaries, statistical comparisons, visualizations, and interpretable findings using Python.

## Source Code

The complete Python script for this analysis is included in this project folder.

### 💻 View Python Source Code

*The source-code link will be activated after `olympics.py` is uploaded to this folder.*

---

[← Back to Sports Analytics & Data Science Portfolio](../README.md)
