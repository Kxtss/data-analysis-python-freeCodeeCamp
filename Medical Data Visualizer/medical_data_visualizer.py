import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = df = pd.read_csv("Medical Data Visualizer/medical_examination.csv", sep=",")

# 2
df["overweight"] = np.where(df["weight"] / np.square(df["height"] / 100) > 25, 1, 0)

# 3
df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # 6
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )

    # 7 & 8
    fig = sns.catplot(
        data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar"
    ).figure

    # 9
    fig.savefig("Medical Data Visualizer/figures/catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(
        data=corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # 16
    fig.savefig("Medical Data Visualizer/figures/heatmap.png")
    return fig
