from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"

for file in sorted(data_folder.glob("NSE_data_all_stocks_*.csv")):
    sample = pd.read_csv(file, nrows=3)
    print(f"\n{file.name}")
    print("Columns:", sample.columns.tolist())

    if "Adjusted Price" in sample.columns:
        print(sample[["Adjusted Price"]].to_string(index=False))