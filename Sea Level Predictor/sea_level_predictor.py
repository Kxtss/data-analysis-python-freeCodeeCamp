import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("Sea Level Predictor/epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", alpha=0.6, label="Original 1880-2013")

    # Create first line of best fit
    regress_first = linregress(x, y)

    x_first_pred = pd.Series([i for i in range(x.min(), 2051)])
    y_first_pred = regress_first.slope * x_first_pred + regress_first.intercept

    plt.plot(x_first_pred, y_first_pred, color="red", label="1880-2050")
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    x_recent = df_recent["Year"]
    y_recent = df_recent["CSIRO Adjusted Sea Level"]

    regress_second = linregress(x_recent, y_recent)

    x_second_pred = pd.Series([i for i in range(2000, 2051)])
    y_second_pred = regress_second.slope * x_second_pred + regress_second.intercept

    plt.plot(x_second_pred, y_second_pred, color="green", label="2000-2051")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("Sea Level Predictor/figures/sea_level_plot.png")
    return plt.gca()
