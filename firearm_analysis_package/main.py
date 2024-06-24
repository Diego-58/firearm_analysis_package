# main.py

from firearm_analysis.data_processing import (
    read_csv, clean_csv, rename_col, breakdown_date, erase_month,
    groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
)
from firearm_analysis.visualization import time_evolution
from firearm_analysis.state_analysis import (
    groupby_state, clean_states, merge_datasets, calculate_relative_values, analyze_kentucky
)
from firearm_analysis.map_generation import create_maps


def main():

    # Read the CSV file
    url = "./Data/nics-firearm-background-checks.csv"
    df = read_csv(url)

    # Rename column
    df_renamed = rename_col(df)
    
    # Clean the DataFrame
    df_clean = clean_csv(df_renamed)
    
    # Split the "month" column into "year" and "month"
    df_date = breakdown_date(df_clean)

    # Delete the "month" column
    df_no_month = erase_month(df_date)
    
    # Group the data by the "year" and "state" columns
    df_grouped = groupby_state_and_year(df_no_month)

    # Print out the biggest number of registered handguns
    df_max_handguns = print_biggest_handguns(df_grouped)

    # Print out the biggest number of registered long guns
    df_max_longguns = print_biggest_longguns(df_grouped)

    # Create temporal evolution graph
    time_evolution(url)

    # Group the DataFrame by states
    df_states = groupby_state(url)

    # Remove territories
    df_states_removed = clean_states(df_states)

    # Merge the DataFrames from another URL
    url2 = "./Data/us-state-populations.csv"
    df_merged = merge_datasets(df_states_removed)

    # Calculate relative values
    df_percent = calculate_relative_values(df_merged)

    # Analyze and remove outliers
    df_final = analyze_kentucky(df_percent)
    
    # Create choroplétic maps
    create_maps(df_final)


if __name__ == "__main__":
    main()
