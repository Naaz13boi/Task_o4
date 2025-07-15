# Task_o4


## Overview

This project explores and visualizes 12-month unduplicated headcount enrollment data for U.S. postsecondary institutions. The dataset includes total enrollments as well as breakdowns by race/ethnicity and gender, following the definitions provided in the accompanying data dictionary.

## Key Findings


- **Demographic Breakdown:**  
  Enrollment numbers for groups such as White (`EFYWHITT`), Black or African American (`EFYBKAAT`), Hispanic or Latino (`EFYHISPT`), and Asian (`EFYASIAT`) are all much smaller than the total, but each group still represents a significant presence. Groups like American Indian or Alaska Native (`EFYAIANT`) and Native Hawaiian or Other Pacific Islanders (`EFYNHPIT`) have much smaller enrollments, consistent with national trends.

- **Gender Split:**  
  The data is split by men and women for each group, revealing interesting patterns—sometimes women outnumber men, sometimes it’s the reverse, depending on the group.

- **Distribution and Outliers:**  
  Boxplots and histograms show that most columns are right-skewed, with a few institutions having much higher enrollments than the rest. This suggests a small number of very large institutions and a long tail of smaller ones.

- **Comparing Means, Medians, and Sums:**  
  The mean and median values for most demographic columns are quite a bit lower than the total, reflecting the aggregate nature of the total. Bar charts make it easy to see which groups have higher average enrollments.

- **Proportional Representation:**  
  When scaling the sums of each group as a percentage of the total, it’s clear that some groups make up a much larger share of the student body than others. For example, White students (`EFYWHITT`) likely make up the largest single group, while groups like American Indian or Alaska Native are a much smaller slice.

- **Correlations:**  
  The correlation heatmap shows that many demographic columns are highly correlated with total enrollment, as expected. There may also be interesting relationships between certain groups, but nothing surprising stands out.

- **Other Notes:**  
  The data includes special categories, such as “gender unknown” or “another gender,” but these are typically very small or zero for most institutions.

## In Short

The dataset paints a familiar picture:
- A few big institutions dominate the totals,
- Most demographic groups are much smaller than the total,
- And the proportional breakdowns reflect broader trends in higher education.
