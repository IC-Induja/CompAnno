import os
import pandas as pd

packagedir = os.path.dirname(yourpackage.__path__[0])
cogs_path = os.path.join(packagedir, '..', 'data', 'cognames.tsv')
COGS = pd.read_table(cogs_path, sep="\t", comment="#", index_col=0,
    names=["COG", "function", "name"])
