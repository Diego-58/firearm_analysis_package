# firearm_analysis/visualization.py

import matplotlib.pyplot as plt
import pandas as pd
import textwrap


def time_evolution(url: str = "./Data/nics-firearm-background-checks.csv",
                   analysis: bool = False) -> None:
    """
    Reads a CSV file from a specified URL, renames some columns, modifies
    the "month" column and creates a plot showing the temporal evolution of the
    total number of "permit", "handgun", and "long_gun" per year.

    Args:
        (str, optional): URL of the CSV file. Must contain, at least, the
            columns "month", "state", "permit", "handgun" and "long_gun".
            Defaults to "./Data/nics-firearm-background-checks.csv".

    Returns:
        None
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
    df_grouped = df.groupby('year').sum().reset_index()
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped["year"], df_grouped["permit"], label="Permits",
             linestyle="dashed", color="#003f5c")
    plt.plot(df_grouped["year"], df_grouped["handgun"], label="Handguns",
             color="#bc5090", linewidth=2)
    plt.plot(df_grouped["year"], df_grouped["long_gun"], label="Long Guns",
             color="#ffa600", linewidth=2)
    # Labels properties
    plt.xlabel("Year")
    plt.ylabel("# Quantity")
    plt.title("Time Evolution of Firearms and Permits in the US (1998-2020)")
    plt.legend()
    plt.grid(True)
    # Set grid properties
    ax = plt.gca()
    ax.set_axisbelow(True)  # Draw grid lines behind other elements
    ax.xaxis.grid(color="gray", linestyle="dotted")  # grey dotted grid lines
    ax.yaxis.grid(color="gray", linestyle="dotted")  # grey dotted grid lines
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    # Set thicker border for the plot
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)  # Adjust the thickness as needed
        spine.set_color("black")  # Adjust the color as needed
    # Add outer tick marks for x and y axes
    ax.tick_params(axis='x', direction='out', length=6, width=1.5)
    ax.tick_params(axis='y', direction='out', length=6, width=1.5)
    plt.show()
    # Toggle the plot analysis to display the text
    if analysis:
        text = """
        The amount of permits and firearms have been increasing over the
        recent years. While the number of permits always stay below the sum
        of the number of firearms, there is a direct correlation between
        the number of firearms and the number of permits. Nevertheless, the
        Covid pandemic, which struck in 2020, led to a decrease in both the
        number of firearms and the number of permits. This trend is in
        agreement with the information about mass shootings, reported in:
        https://cnnespanol.cnn.com/2024/02/15/cultura-armas-estados-unidos-mundo-trax/
        """
        # Wrap the text to fit within 79 characters per line
        wrapped_lines = textwrap.wrap(textwrap.dedent(text), width=79)
        print("\n".join(wrapped_lines))
