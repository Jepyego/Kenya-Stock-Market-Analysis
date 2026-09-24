from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(
    data_folder / "nse_analysis.csv",
    parse_dates=["date"]
)

stocks = df[
    df["CODE"].isin(["SCOM", "EQTY", "KEGN"])
    & (df["date"] >= "2008-04-23")
].copy()
stocks = stocks.sort_values(["CODE", "date"])

# Adjust Equity's prices before its 2009 10-for-1 split.
stocks["comparison_price"] = stocks["Day Price"]
before_split = (
    (stocks["CODE"] == "EQTY")
    & (stocks["date"] < "2009-03-26")
)
stocks.loc[before_split, "comparison_price"] /= 10

first_price = stocks.groupby("CODE")["comparison_price"].transform("first")
stocks["price_index"] = stocks["comparison_price"] / first_price * 100

stocks["price_change_pct"] = (
    stocks.groupby("CODE")["comparison_price"].pct_change() * 100
)
stocks["large_change_flag"] = stocks["price_change_pct"].abs() > 50

output = data_folder / "nse_three_stocks.csv"
stocks.to_csv(output, index=False)

print(f"Saved rows: {len(stocks):,}")
print(f"Price changes over 50%: {stocks['large_change_flag'].sum():,}")
print(f"Saved to: {output}")
print("\nLast price index by stock:")
print(stocks.groupby("CODE")["price_index"].last().round(2).to_string())