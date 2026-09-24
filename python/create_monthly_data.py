from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(
    data_folder / "nse_three_stocks.csv",
    parse_dates=["date"]
)

df = df.sort_values(["CODE", "date"])
df["month"] = df["date"].dt.to_period("M")

monthly = df.groupby(["CODE", "month"], sort=False).tail(1).copy()
monthly = monthly.drop(columns="month")
monthly = monthly.sort_values(["CODE", "date"])

output = data_folder / "nse_monthly_stocks.csv"
monthly.to_csv(output, index=False)

print(f"Monthly rows saved: {len(monthly):,}")
print(monthly.groupby("CODE").size().to_string())
print(f"Saved to: {output}")