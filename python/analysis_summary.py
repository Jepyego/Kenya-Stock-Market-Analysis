from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(data_folder / "nse_analysis.csv", parse_dates=["date"])

print(f"Rows: {len(df):,}")
print(f"Stocks: {df['CODE'].nunique():,}")
print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")
print(f"Missing volume: {df['Volume'].isna().sum():,}")
print(f"Zero or negative prices: {(df['Day Price'] <= 0).sum():,}")

print("\nRows by year:")
print(df.groupby(df["date"].dt.year).size().to_string())

print("\nStocks for our comparison:")
for code in ["SCOM", "EQTY", "KEGN"]:
    stock = df[df["CODE"] == code]
    if stock.empty:
        print(f"{code}: not found")
    else:
        print(
            f"{code}: {stock['NAME'].iloc[-1]}, "
            f"{len(stock):,} rows, "
            f"{stock['date'].min().date()} to {stock['date'].max().date()}"
        )