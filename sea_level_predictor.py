import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", usecols=[0, 1])

    # Create scatter plot
    fig, axs = plt.subplots(figsize=(20,10))

    df.plot.scatter(x="Year", y="CSIRO Adjusted Sea Level", ax=axs, label="Adjusted Sea Levels")

    years_to_2050 = pd.Series(list(range(1880, 2051)))
    # Create first line of best fit
    slope, intercept, *rest = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    levels_1880_2050 = years_to_2050*slope+intercept
    axs.plot(years_to_2050, levels_1880_2050, "r-", label="Line of best fit from year 1880")

    # Create second line of best fit
    slope2000, intercept2000, *rest = linregress(df.loc[df.Year>=2000, "Year"], df.loc[df.Year>=2000, "CSIRO Adjusted Sea Level"])
    levels_2000_2050 = years_to_2050[years_to_2050 >= 2000]*slope2000+intercept2000
    axs.plot(years_to_2050[years_to_2050 >= 2000], levels_2000_2050, "r--", label="Line of best fit from year 2000")

    # Add labels and title
    title_font = {"fontsize": 18, "fontweight": "bold"}
    labels_font= {"fontsize": 16}

    axs.set_title("Rise in Sea Level", fontdict=title_font)
    axs.set_xlabel("Year", fontdict=labels_font)
    axs.set_ylabel("Sea Level (inches)", fontdict=labels_font)
    axs.legend(loc="upper left", fontsize=12)

    plt.annotate(f"{levels_1880_2050.iloc[-1]:.2f}", xy=(2050+0.2, levels_1880_2050.iloc[-1]+0.2), size=12)
    plt.annotate(f"{levels_2000_2050.iloc[-1]:.2f}", xy=(2050+0.2, levels_2000_2050.iloc[-1]+0.2), size=12)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()