# Education Data Analysis

1. While writing test cases, one of your coworkers noticed that some calls to `mean_min_degrees` produce `NaN` values and wanted your opinion on whether or not this is a bug with the function. Here is the code she used:

```python
mean_min_degrees(data, category="Pacific Islander")
```

**Using what you know about the data, explain why a `NaN` value appears in the result of your coworker's code cell.**

A NaN appears because the NCES dataset does not consistently report values for the “Pacific Islander” category across all years and degree levels. In earlier years especially, this group was either not reported separately or had suppressed/missing data due to small sample sizes. When mean_min_degrees computes the average, pandas propagates missing values, resulting in NaN for degree categories where no valid data exists. This reflects limitations in the original data, not a bug in the function.

2. Between the scatter plot and the bar plot for the high school completion visualization, **which visualization do you prefer, and why?** Be sure to include at least one reference to the reading to support your answer.

I prefer the bar plot for high school completion because it is better suited for comparing discrete categories like sex (“A”, “M”, “F”) at a single point in time. According to the course reading on data visualization, bar charts are effective for categorical comparisons, while scatter or line plots are more appropriate for showing trends or relationships over continuous variables like time. The bar plot makes it easier to quickly compare completion rates across groups without unnecessary visual complexity.

3. **Describe a possible bias present in this dataset and why it might have occurred.** You may refer to the original data source, or look up any outside information to support your answer. If you are using additional sources, make sure to list them as part of your answer. We do not require formal citations, but your sources should be specific so that a staff member can find them! (i.e., don't say something broad like "Wikipedia")

One possible bias in this dataset is the underrepresentation or inconsistent reporting of smaller racial and ethnic groups, such as Pacific Islanders or American Indian/Alaska Native populations. This likely occurred because earlier surveys had smaller sample sizes for these groups, leading NCES to suppress or omit estimates to avoid unreliable statistics. As a result, trends for these populations may appear incomplete or misleading compared to larger groups like White or Black populations.
