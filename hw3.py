'''
Taire Tebite
CSE 163
This file analyzes educational attainment data using pandas and seaborn.
It includes functions to compare bachelor's degree attainment by sex, compute
average educational attainment by minimum degree over time, and generate line
and bar plots visualizing these trends.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


# Define your functions here
def compare_bachelors_year(data: pd.DataFrame, year: int) -> pd.Series:
    """
    Returns a Series containing the percentages of males and females who earned
    at least a bachelor's degree in the given year.
    Parameters:
        data (pd.DataFrame): Educational attainment data indexed by
            (Year, Sex, Min degree).
        year (int): The year to retrieve data for.
    Returns:
        pd.Series: A two-row Series with Total percentages for males ("M")
            and females ("F") with a bachelor's degree in the given year.
    """
    return data.loc[(year, ["M", "F"], "bachelor's"), "Total"]


def mean_min_degrees(
    data: pd.DataFrame,
    start_year: int | None = None,
    end_year: int | None = None,
    category: str = "Total"
) -> pd.Series:
    """
    Returns a Series indicating, for each minimum degree level, the average
    percentage of educational attainment for the specified category over the
    given year range for all students.

    Parameters:
        data (pd.DataFrame): Educational attainment data indexed by
            (Year, Sex, Min degree).
        start_year (int | None): The starting year (inclusive). If None,
            all years from the beginning of the dataset are included.
        end_year (int | None): The ending year (inclusive). If None,
            all years up to the end of the dataset are included.
        category (str): The column name to average (default "Total").

    Returns:
        pd.Series: A Series indexed by minimum degree level containing
            the average percentages over the specified year range.
    """
    selected_data = data.loc[(slice(start_year, end_year), "A", slice(None)),
                             category]
    result = selected_data.groupby("Min degree").mean()
    return result


def line_plot_min_degree(data: pd.DataFrame, min_degree: str) -> None:
    """
    Creates and saves a line plot showing the percentage of all students ("A")
    who earned at least the specified minimum degree over time.

    Parameters:
        data (pd.DataFrame): Educational attainment data indexed by
            (Year, Sex, Min degree).
        min_degree (str): The minimum degree level to plot("bachelor's").
    """
    filtered_data = data.loc[(slice(None), "A", min_degree),
                             ["Total"]]
    sns.relplot(data=filtered_data, x="Year", y="Total", kind="line")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title(f"Percentage earning {min_degree} over time")
    plt.savefig("line_plot_min_degree.png", bbox_inches="tight")


def bar_plot_high_school(data: pd.DataFrame, year: int) -> None:
    """
    Creates and saves a bar plot comparing the percentage of all
    students ("A"), males ("M"), and females ("F") who earned at
    least a high school degree in the specified year.

    Parameters:
        data (pd.DataFrame): Educational attainment data indexed by
            (Year, Sex, Min degree).
        year (int): The year to plot data for.
    """
    filtered_data = data.loc[(year, slice(None), "high school"), ["Total"]]
    sns.catplot(data=filtered_data, x="Sex", y="Total", kind="bar", hue="Sex")
    plt.xlabel("Sex")
    plt.ylabel("Percentage")
    plt.title(f"High school completion in {year}")
    plt.savefig("bar_plot_high_school.png", bbox_inches="tight")


def main():
    data = pd.read_csv(
        "nces-ed-attainment.csv",
        na_values=["---"],
        index_col=["Year", "Sex", "Min degree"]
    ).sort_index(level="Year", sort_remaining=False)

    # Call your functions here
    compare_bachelors_year(data, 1980)
    mean_min_degrees(data)
    line_plot_min_degree(data, "bachelor's")
    bar_plot_high_school(data, 2009)


if __name__ == '__main__':
    main()
