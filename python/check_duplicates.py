from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(data_folder / "nse_cleaned.csv")

repeated = df[df.duplicated(["date", "CODE"], keep=False)].copy()
fields = [
    "date", "CODE", "NAME", "Day Price", "Previous",
    "Day Low", "Day High", "Volume"
]
exact_copies = repeated.duplicated(fields, keep="first")

print(f"Rows in repeated date/code groups: {len(repeated):,}")
print(f"Extra exact copies: {exact_copies.sum():,}")
print(
    "Repeated groups with different values: "
    f"{repeated[~exact_copies].duplicated(['date', 'CODE']).sum():,}"
)
print("\nFirst 12 repeated rows:")
print(repeated.head(12).to_string(index=False))