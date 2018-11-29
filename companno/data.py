import os
import pandas as pd

cogs_path = os.path.join(os.path.dirname(__file__), 'cognames.tsv')
COGS = pd.read_table(cogs_path, sep="\t", comment="#", index_col=0,
    names=["COG", "function", "name"])
