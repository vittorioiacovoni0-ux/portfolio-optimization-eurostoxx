# Data

The original dataset is not redistributed (it was assembled from a licensed terminal and the course database).

Expected file: `data/DATABASE.xlsx`, one sheet, first row = headers.

| Column | Content |
|---|---|
| `Date` | Month-end date |
| 25 asset columns | Month-end prices of Euro Stoxx 50 constituents (lower-case short names: `asml`, `mc`, `sap`, ...) |
| `sx5e_price` | Euro Stoxx 50 index level (benchmark / market factor) |
| `bund10y` | German 10Y yield in percent (the last value is used as the risk-free rate) |

To try the notebook without the original data run `python make_sample_data.py` from the repository root: it creates a
**synthetic** file with the same layout. You can also build your own file from any price source (the sector lists in
section 2.1 refer to the column names above, so adapt them if you change the universe).
