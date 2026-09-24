from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(
    data_folder / "nse_three_stocks.csv",
    parse_dates=["date"]
)

df = df.sort_values(["CODE", "date"]).reset_index(drop=True)

for code in ["SCOM", "EQTY", "KEGN"]:
    stock = df[df["CODE"] == code].reset_index(drop=True)
    flagged = stock.index[stock["large_change_flag"] == True]

    for position in flagged:
        print(f"\n{code}: flagged change")
        nearby = stock.iloc[max(0, position - 2):position + 3]
        print(
            nearby[
                ["date", "CODE", "Day Price", "Previous",
                 "price_change_pct", "Volume"]
            ].to_string(index=False)
        )

print("\nFirst and last prices in the comparison:")
for code, stock in df.groupby("CODE"):
    print(
        f"{code}: {stock.iloc[0]['date'].date()} "
        f"{stock.iloc[0]['Day Price']:.2f} → "
        f"{stock.iloc[-1]['date'].date()} "
        f"{stock.iloc[-1]['Day Price']:.2f}"
    )