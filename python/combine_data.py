from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
files = sorted(data_folder.glob("NSE_data_all_stocks_*.csv"))

if not files:
    raise FileNotFoundError("No yearly CSV files found in the data folder.")

tables = []

for file in files:
    table = pd.read_csv(file, low_memory=False)
    table.columns = table.columns.str.strip()
    table = table.rename(columns={
        "Date": "DATE",
        "Adjusted": "Adjust",
    })
    table["source_file"] = file.name
    tables.append(table)
    print(f"{file.name}: {len(table):,} rows")

combined = pd.concat(tables, ignore_index=True, sort=False)
output = data_folder / "nse_combined_raw.csv"
combined.to_csv(output, index=False)

print(f"\nCombined rows: {len(combined):,}")
print(f"Combined columns: {len(combined.columns)}")
print("Columns:", combined.columns.tolist())
print(f"Saved to: {output}")