from pathlib import Path
import pandas as pd

data_folder = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(data_folder / "nse_combined_raw.csv", low_memory=False)

df["CODE"] = df["CODE"].fillna(df["Code"])
df["NAME"] = df["NAME"].fillna(df["Name"])

date_text = df["DATE"].astype("string").str.strip()
slash_dates = date_text.str.contains("/", na=False)

df["date"] = pd.NaT
df.loc[slash_dates, "date"] = pd.to_datetime(
    date_text[slash_dates], format="%m/%d/%Y", errors="coerce"
)
df.loc[~slash_dates, "date"] = pd.to_datetime(
    date_text[~slash_dates], format="%d-%b-%y", errors="coerce"
)

for column in ["Day Price", "Previous", "Day Low", "Day High", "Volume"]:
    text = df[column].astype("string").str.replace(",", "", regex=False).str.strip()
    df[column] = pd.to_numeric(text, errors="coerce")

df["CODE"] = df["CODE"].astype("string").str.strip()
df["NAME"] = df["NAME"].astype("string").str.strip()

cleaned = df[
    ["date", "CODE", "NAME", "Day Price", "Previous",
     "Day Low", "Day High", "Volume", "source_file"]
].copy()

print(f"Starting rows: {len(cleaned):,}")
print(f"Invalid dates: {cleaned['date'].isna().sum():,}")
print(f"Missing codes: {cleaned['CODE'].isna().sum():,}")
print(f"Missing day prices: {cleaned['Day Price'].isna().sum():,}")
print(f"Repeated date and code pairs: {cleaned.duplicated(['date', 'CODE']).sum():,}")

cleaned = cleaned.dropna(subset=["date", "CODE", "Day Price"])
cleaned = cleaned.sort_values(["CODE", "date"])

output = data_folder / "nse_cleaned.csv"
cleaned.to_csv(output, index=False)

print(f"\nSaved rows: {len(cleaned):,}")
print(f"Date range: {cleaned['date'].min().date()} to {cleaned['date'].max().date()}")
print(f"Companies/codes: {cleaned['CODE'].nunique():,}")
print(f"Saved to: {output}")