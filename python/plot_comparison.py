from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project_folder = Path(__file__).resolve().parents[1]
df = pd.read_csv(
    project_folder / "data" / "nse_three_stocks.csv",
    parse_dates=["date"]
)

plt.figure(figsize=(12, 6))

for code, stock in df.groupby("CODE"):
    stock = stock.sort_values("date")
    monthly = (
        stock.set_index("date")["price_index"]
        .resample("ME")
        .last()
        .dropna()
    )
    plt.plot(monthly.index, monthly.values, label=code, linewidth=2)

plt.title("NSE Stock Price Comparison: Safaricom, Equity and KenGen")
plt.ylabel("Price index (starting value = 100)")
plt.xlabel("Year")
plt.legend(title="Stock")
plt.grid(alpha=0.3)
plt.tight_layout()

output = project_folder / "images" / "stock_price_comparison.png"
output.parent.mkdir(exist_ok=True)
plt.savefig(output, dpi=200)
print(f"Chart saved to: {output}")
plt.show()