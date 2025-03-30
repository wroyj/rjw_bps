import pandas as pd
from datetime import datetime
import os

# Set path to CSV file
BASE_DIR = os.path.join(os.getcwd(), 'data', 'input')
os.makedirs(BASE_DIR, exist_ok=True)
CSV_PATH = os.path.join(BASE_DIR, 'bp_data.csv')

def get_valid_datetime():
    while True:
        dt_input = input('Enter date and time (YYYY-MM-DD HH:MM): ').strip()
        try:
            datetime.strptime(dt_input, '%Y-%m-%d %H:%M')
            return dt_input
        except ValueError:
            print('Invalid format. Please enter in format YYYY-MM-DD HH:MM.')

def main():
    print("""
    ===============================
      Blood Pressure Data Entry
    ===============================
    """)
    date_time = get_valid_datetime()
    systolic = input('Enter systolic pressure: ').strip()
    diastolic = input('Enter diastolic pressure: ').strip()
    heart_rate = input('Enter heart rate: ').strip()
    notes = input('Enter notes (optional): ').strip()

    # Create entry DataFrame
    entry = pd.DataFrame([[date_time, systolic, diastolic, heart_rate, notes]],
                         columns=['datetime', 'systolic', 'diastolic', 'heart_rate', 'notes'])

    print('\nYou entered:')
    print(entry.to_string(index=False))

    confirm = input('\nSave this entry? (y/n): ').strip().lower()
    if confirm == 'y':
        header = not os.path.exists(CSV_PATH)
        entry.to_csv(CSV_PATH, mode='a', header=header, index=False)
        print(f'✅ Entry saved to {CSV_PATH}')
    else:
        print('❌ Entry discarded.')

if __name__ == '__main__':
    main()