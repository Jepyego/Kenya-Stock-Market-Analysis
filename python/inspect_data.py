from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
files = sorted(data_folder.glob("NSE_data_all_stocks_*.csv"))

print(f"CSV files found: {len(files)}")
if not files:
    raise FileNotFoundError(f"No CSV files found in {data_folder}")

sample = pd.read_csv(files[0], low_memory=False)
print(f"\nFirst file: {files[0].name}")
print("Columns:", sample.columns.tolist())
print("\nFirst five rows:")
print(sample.head().to_string(index=False))