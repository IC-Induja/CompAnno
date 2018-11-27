import pandas as pd

COGS = pd.read_table("data/cognames.tsv", sep="\t", comment="#", index_col=0,
    names=["COG", "function", "name"])
