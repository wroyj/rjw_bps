import pandas as pd
import os
from datetime import datetime

INPUT_PATH = os.path.join('data', 'input', 'bp_data.csv')
BACKUP_PATH = os.path.join('data', 'input', 'bp_data_original_backup.csv')

COLUMN_RENAME_MAP = {
    'date': 'date',
    'time': 'time',
    'sysbp': 'systolic',
    'diabp': 'diastolic',
    'pulse': 'heart_rate',
    'weight': 'notes'
}

def normalize_datetime(df):
    df.columns = [col.strip().lower() for col in df.columns]
    df.rename(columns=COLUMN_RENAME_MAP, inplace=True)

    if 'date' in df.columns and 'time' in df.columns:
        print("🔍 Found separate 'date' and 'time' columns. Merging into 'datetime'...")
        df['datetime'] = df['date'].astype(str).str.strip() + ' ' + df['time'].astype(str).str.strip()
        df.drop(['date', 'time'], axis=1, inplace=True)
    elif 'datetime' in df.columns:
        print("✔ Found existing 'datetime' column. No merge needed.")
    else:
        raise ValueError("No recognizable datetime columns found.")

    # Clean up 'wt': convert 0 or blank to NaN
    if 'wt' in df.columns:
        df['wt'] = pd.to_numeric(df['wt'], errors='coerce')
        df['wt'].replace(0, pd.NA, inplace=True)# Clean up 'wt': convert 0 or blank to NaN
    if 'wt' in df.columns:
        df['wt'] = pd.to_numeric(df['wt'], errors='coerce')
        df['wt'].replace(0, pd.NA, inplace=True)

    print("\n🔍 Sample datetime strings (before parsing):")
    print(df['datetime'].head(10))

    failed_rows = []
    parsed_datetimes = []
    for idx, dt_str in enumerate(df['datetime']):
        try:
            dt_obj = datetime.strptime(dt_str.strip(), '%Y-%m-%d %H:%M')
            parsed_datetimes.append(dt_obj.strftime('%Y-%m-%d %H:%M'))
        except Exception as e:
            failed_rows.append((idx, dt_str, str(e)))
            parsed_datetimes.append(None)

    if failed_rows:
        print("\n❌ Failed to parse the following datetime values:")
        for row in failed_rows:
            print(f"  Row {row[0]}: '{row[1]}' -> {row[2]}")

        confirm = input(f"⚠ {len(failed_rows)} rows failed. Skip them and continue? (y/n): ").strip().lower()
        if confirm != 'y':
            raise ValueError("Aborting due to invalid datetime entries. Please fix manually.")

        df['datetime'] = parsed_datetimes
        df = df[df['datetime'].notnull()]

    else:
        df['datetime'] = parsed_datetimes

    return df[['datetime', 'systolic', 'diastolic', 'heart_rate', 'notes']]

def main():
    print("📂 Loading:", INPUT_PATH)
    if not os.path.exists(INPUT_PATH):
        print("❌ File not found:", INPUT_PATH)
        return

    df = pd.read_csv(INPUT_PATH)
    print("✅ Loaded file. Columns:", list(df.columns))

    print("📁 Creating backup:", BACKUP_PATH)
    df.to_csv(BACKUP_PATH, index=False)

    df_normalized = normalize_datetime(df)

    print("\n🔄 Preview normalized data:")
    print(df_normalized.head())

    confirm = input("\nOverwrite original file with normalized data? (y/n): ").strip().lower()
    if confirm == 'y':
        df_normalized.to_csv(INPUT_PATH, index=False)
        print("✅ Normalized data saved to", INPUT_PATH)
    else:
        print("❌ Aborted. No changes made.")

if __name__ == '__main__':
    main()
