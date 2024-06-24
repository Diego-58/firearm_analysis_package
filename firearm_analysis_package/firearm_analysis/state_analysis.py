# firearm_analysis/state_analysis.py

import pandas as pd
import textwrap


def groupby_state(url: str =
                  "./Data/nics-firearm-background-checks.csv") -> pd.DataFrame:
    """
    Reads a CSV file from a specified URL, renames some columns, modifies the
    "month" column, groups the DataFrame by the "state" column and calculates
    the sum of the "permit", "handgun" and "long_gun" columns.

    Args:
        (str, optional): URL of the CSV file. Must contain, at least, the
            columns "month", "state", "permit", "handgun" and "long_gun".
            Defaults to "./Data/nics-firearm-background-checks.csv"

    Returns:
        pd.DataFrame: DataFrame grouped by "state" with cumulative values.
    """
    df = pd.read_csv(url)
    df.rename(columns={"longgun": "long_gun"}, inplace=True)
    df = df[["month", "state", "permit", "handgun", "long_gun"]]
    # Extract the year out of the 'month' column
    month_index = df.columns.get_loc("month")  # find index of 'month' column
    df.insert(month_index, "year", "")  # insert 'year' col right before
    # Copy-on-Write recommended way to change the values of an object
    df.loc[:, ["year"]] = df["month"].str.split("-", expand=True)[0]
    df = df.drop(columns=["month"])
    df_grouped = df.groupby('state').sum().reset_index()
    df_grouped.drop(columns=["year"], inplace=True)
    display(df_grouped.head(5))
    return df_grouped


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows corresponding to specific U.S. territories from the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing a "state" column.

    Returns:
        pd.DataFrame: A DataFrame with specified U.S. territories removed.
    """
    print(f"Number of states before removing undesired data: "
          f"{df['state'].nunique()}")
    states_to_remove = ["Guam", "Mariana Islands",
                        "Puerto Rico", "Virgin Islands"]
    df_cleaned = df[~df["state"].isin(states_to_remove)]
    print(f"Number of states after removing undesired data: "
          f"{df_cleaned['state'].nunique()}")
    return df_cleaned


def merge_datasets(df: pd.DataFrame,
                   url2: str = "./Data/us-state-populations.csv"
                   ) -> pd.DataFrame:
    """
    Merges the input DataFrame with a population DataFrame from a URL
    based on the "state" column.

    Args:
        df (pd.DataFrame): The input DataFrame containing, at least, a
            "state" column.
        url2 (str, optional): The URL of the population CSV file.
            Defaults to "./Data/us-state-populations.csv".

    Returns:
        pd.DataFrame: A merged DataFrame containing data from the input
            DataFrame and the DataFrame from the URL.
    """
    pop_df = pd.read_csv(url2)
    merged_df = pd.merge(df, pop_df, on="state")
    print("\nFirst rows of the merged DataFrames:")
    display(merged_df.head(5))
    return merged_df


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates values for the columns "permit", "long_gun", and "hand_gun"
    as percentages of the population.

    Args:
        df (pd.DataFrame): The input DataFrame containing, at least, the
            columns "permit", "long_gun", "hand_gun", and the "pop_2014"
            columns.

    Returns:
        pd.DataFrame: The DataFrame with additional columns for the relative
            values.
    """
    df["permit_perc"] = round((df["permit"] * 100) / df["pop_2014"], 3)
    df["longgun_perc"] = round((df["long_gun"] * 100) / df["pop_2014"], 3)
    df["handgun_perc"] = round((df["handgun"] * 100) / df["pop_2014"], 3)
    # TODO: comment out the next line
    display(df.head(5))
    return df


def analyze_kentucky(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes the colum "permit_perc" for the state of Kentucky and
    adjusts its value to the mean of the other states if it is an outlier.

    Args:
        df (pd.DataFrame): The input DataFrame containing, at least, the
            columns of "state" and "permit_perc".

    Returns:
        df (pd.DataFrame): The DataFrame with modified mean for outliers.
    """
    mean_permit_perc = round(df["permit_perc"].mean(), 2)
    print(f"Mean of registered firearms permits (permit_perc): "
          f"{mean_permit_perc}")
    print("\nData of the state of Kentucky:")
    display(df.loc[df["state"] == "Kentucky", :])
    # Replace Kentucky mean value with the mean of the other states
    df.loc[df["state"] == "Kentucky", "permit_perc"] = mean_permit_perc
    new_mean_permit_perc = round(df["permit_perc"].mean(), 2)
    print(f"\nNew mean of registered firearms permits (permit_perc): "
          f"{new_mean_permit_perc}")
    # Draw conclusions for the mean change in outliers
    if new_mean_permit_perc != mean_permit_perc:
        print("\nConclusions:\n")
        text = f"""
        The new mean is
        {round(abs((new_mean_permit_perc-mean_permit_perc)/mean_permit_perc),
        2)*100}% different than the mean containing the outlier, corresponding
        to the state of Kentucky. The mean is a statistical metric that can be
        prone to significant variations when accounting for outlying values.
        In contrast, the median is a more robust metric to measure central
        tendency of the data. Therefore, care must be taken when using the
        mean to extract conclusions.
        """
        # Wrap the text to fit within 79 characters per line
        wrapped_lines = textwrap.wrap(textwrap.dedent(text), width=79)
        print("\n".join(wrapped_lines))
    return df
