# firearm_analysis/data_processing.py

import pandas as pd


def read_csv(url: str =
             "./Data/nics-firearm-background-checks.csv") -> pd.DataFrame:

    """
    Reads a CSV file from a specified URL and displays the first five
    rows and the information of the file.

    Args:
        (str, optional): URL of the CSV file. Must contain, at least, the
            columns "month", "state", "permit", "handgun" and "long_gun".
            Defaults to "./Data/nics-firearm-background-checks.csv".

    Returns:
        pd.DataFrame: DataFrame of the corresponding CSV file.
    """
    df = pd.read_csv(url)
    print("\nFirst five columns of the DataFrame:\n")
    display(df.head())
    print("\nStructure of the DataFrame:\n")
    display(df.info())
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame obtained from the CSV file obtained from the URL
    and cleans it by deleting all its columns except "month", "state",
    "permit", "handgun" and "long_gun".

    Args:
        df (pd.DataFrame): DataFrame from the CSV file.

    Returns:
        pd.DataFrame: DataFrame with the columns of interest.
    """
    columns_of_interest = ["month", "state", "permit", "handgun", "long_gun"]
    df_clean = df[columns_of_interest]
    print(f"\nColumns of the original DataFrame:\n{df.columns.tolist()}")
    print(f"\nColumns of the cleaned DataFrame:\n{df_clean.columns.tolist()}")
    return df_clean


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Modify the column name "longgun" for "long_gun" in the given DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with the original columns.

    Returns:
        pd.DataFrame: DataFrame with the modified column.
    """
    df.rename(columns={"longgun": "long_gun"}, inplace=True)
    print(f"\nOriginal DataFrame columns:\n{df.columns.tolist()}")
    print(f"\nColumns of DataFrame after renaming:\n{df.columns.tolist()}")
    return df


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Divides the "month" column of a given DataFrame into two columns:
    "year" and "month".

    Args:
        df (pd.DataFrame): DataFrame with the original "month" column
            in the format "YYYY-MM".

    Returns:
        pd.DataFrame: DataFrame with the columns "year" and "month".
    """
    month_index = df.columns.get_loc("month")  # find index of 'month' column
    df.insert(month_index, "year", "")  # insert 'year' col right before
    # Copy-on-Write recommended way to change the values of an object
    df.loc[:, ["year"]] = df["month"].str.split("-", expand=True)[0]
    df.loc[:, ["month"]] = df["month"].str.split("-", expand=True)[1]
    print("\nDataFrame with 'month' columns split into 'year' and 'month':")
    display(df.head())
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deletes the "month" column of a given DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with a "month" column.

    Returns:
        pd.DataFrame: DataFrame without the "month" column.
    """
    df = df.drop(columns=["month"])
    print("\nDataFrame without the 'month' column:")
    display(df.head())
    print(f"\nCurrent columns of the DataFrame:\n{df.columns.tolist()}")
    return df


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Groups the data by the "year" and "state" columns of a given DataFrame and
    calculates the sum of the "permit", "handgun" and "long_gun" columns.

    Args:
        df (pd.DataFrame): DataFrame with the columns "year", "state",
        "permit", "handgun" and "long_gun".

    Returns:
        pd.DataFrame: DataFrame grouped by "state" and "year" with cumulative
        values.
    """
    grouped_df = df.groupby(["state", "year"]).sum().reset_index()
    print("\nGrouped data by 'year' and 'state':")
    display(grouped_df.head())
    return grouped_df


def print_biggest_handguns(df: pd.DataFrame):
    """
    Prints out the state and year with the biggest number of registered
    handguns.

    Args:
        df (pd.DataFrame): DataFrame with the columns "year", "state",
            "permit", "handgun" and "long_gun" grouped by "state" and "year".

    Returns:
        None
    """
    indx = df["handgun"].idxmax()
    max_row = df.loc[indx]
    print(f"\nThe biggest number handguns was registered in "
          f"{max_row['state']} during the year {max_row['year']} "
          f"with a total of {max_row['handgun']} handguns.")


def print_biggest_longguns(df: pd.DataFrame):
    """
    Prints out the state and year with the biggest number of registered long
    guns.

    Args:
        df (pd.DataFrame): DataFrame with the columns "year", "state",
            "permit", "handgun" and "long_gun" groupped by "state" and
            "year".

    Returns:
        None
    """
    indx = df["long_gun"].idxmax()
    max_row = df.loc[indx]
    print(f"\nThe biggest number long guns was registered in "
          f"{max_row['state']} during the year {max_row['year']} "
          f"with a total of {max_row['long_gun']} long guns.")
