import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

base_df = pd.read_csv(
    "/tmp/error/radiuss_develop.csv",
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
    "/tmp/error/radiuss_error_single.csv",
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

merged_df = pd.merge(
    base_df,
    target_df,
    on=["pkg"],
    suffixes=("_base", "_target")
)

df = merged_df.loc[:, ("pkg", "total_base", "total_target")]
df["Speedup [%]"] = (df["total_base"] - df["total_target"]) *100 / df["total_base"]
df = df.rename(
    columns={
        "pkg": "Spec solved",
        "total_base": "Total time [develop, secs.]",
        "total_target": "Total time [PR, secs.]"
    })

print(df.head())
df.to_markdown(buf="table.mk", index=False, tablefmt="github")



