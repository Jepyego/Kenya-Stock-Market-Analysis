from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(data_folder / "nse_cleaned.csv")

fields = [
    "date", "CODE", "NAME", "Day Price", "Previous",
    "Day Low", "Day High", "Volume"
]
without_copies = df.drop_duplicates(subset=fields).copy()

conflict_mask = without_copies.duplicated(["date", "CODE"], keep=False)
conflicts = without_copies[conflict_mask].copy()
analysis = without_copies[~conflict_mask].copy()

conflicts.to_csv(data_folder / "nse_conflicts.csv", index=False)
analysis.to_csv(data_folder / "nse_analysis.csv", index=False)

print(f"Exact extra copies removed: {len(df) - len(without_copies):,}")
print(f"Conflicting rows set aside: {len(conflicts):,}")
print(f"Rows ready for analysis: {len(analysis):,}")
print(
    "Remaining repeated date/code pairs: "
    f"{analysis.duplicated(['date', 'CODE']).sum():,}"
)