import csv
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

working_directory = pathlib.Path("/tmp/versions")

reference_csv = working_directory / "radiuss-develop.csv"
candidate_csv = working_directory / "radiuss-versions.csv"

figure = "radiuss.png"

plt.rcParams.update({'font.size': 48})

base_df = pd.read_csv(
    str(reference_csv),
    header=None,
    names=[
        "pkg",
        "cfg",
        "iter",
        "setup",
        "load",
        "ground",
        "solve",
        "total",
        "dep_len",
    ],
)
print(base_df.head())
target_df = pd.read_csv(
    str(candidate_csv),
    header=None,
    names=[
        "pkg",
        "cfg",
        "iter",
        "setup",
        "load",
        "ground",
        "solve",
        "total",
        "dep_len",
    ],
)

print(target_df.head())

merge_df = pd.merge(
    base_df,
    target_df,
    on=["pkg"],
    suffixes=("_base", "_target")
)
print(merge_df.head())

cols = [
    ("pkg", "setup_base", "setup_target"),
    ("pkg", "ground_base", "ground_target"),
    ("pkg", "solve_base", "solve_target"),
    ("pkg", "total_base", "total_target"),
]
titles = [
    "Setup", "Ground", "Solve", "Total"
]
fig, axes = plt.subplots(1, 4, sharex=True, sharey=True, figsize=(128, 32), layout="constrained")
for ax, keys, title in zip(axes, cols, titles):
    current = merge_df.loc[: , keys]
    current.plot(
        x="pkg",
        ax=ax,
        kind="bar",
        width=.6,
        title=title,
        grid=True
    )
    ax.set(xlabel=None, ylabel="Time [sec.]", ylim=[0, 41])
    ax.legend(["develop", "PR"])
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

#plt.tight_layout()
plt.savefig(figure)
#plt.show()
