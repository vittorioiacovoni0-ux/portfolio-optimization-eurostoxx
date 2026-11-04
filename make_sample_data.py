"""Generate a SYNTHETIC monthly dataset in the format the notebook expects.

The original dataset (25 Euro Stoxx 50 constituents, the index and the 10Y Bund yield, monthly, 2016-04 to 2026-03)
is not redistributed. This script creates random data with the same layout so the notebook runs end to end.
Numbers produced from it are illustrative only and do NOT reproduce the results stored in the notebook.

Usage:  python make_sample_data.py   ->   data/DATABASE.xlsx
"""
from pathlib import Path

import numpy as np
import pandas as pd

TICKERS = ["asml", "mc", "sap", "or", "tte", "sie", "rms", "air", "alv", "san", "su", "ai", "itx", "dte", "ibe",
           "bnp", "mbg", "muv2", "isp", "eni", "enel", "race", "bmw", "bas", "una"]

rng = np.random.default_rng(42)
dates = pd.date_range("2016-04-30", "2026-03-31", freq="ME")
n = len(dates)

r_m = rng.normal(0.006, 0.045, n)                       # monthly market log-return
prices = {}
for t in TICKERS:
    beta = rng.uniform(0.6, 1.4)
    alpha = rng.normal(0.002, 0.003)
    r = alpha + beta * r_m + rng.normal(0, 0.05, n)
    prices[t] = 100 * np.exp(np.cumsum(r))

df = pd.DataFrame(prices, index=dates)
df["bund10y"] = np.clip(2.5 + np.cumsum(rng.normal(0, 0.12, n)), 0.1, 4.5)   # percent
df["sx5e_price"] = 3500 * np.exp(np.cumsum(r_m))
df.index.name = "Date"

out = Path(__file__).parent / "data" / "DATABASE.xlsx"
out.parent.mkdir(exist_ok=True)
df.reset_index().to_excel(out, index=False)
print(f"Wrote {out}  ({df.shape[0]} rows x {df.shape[1]} columns)")
