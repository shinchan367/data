import pandas as pd
from datetime import datetime, timedelta

def analyze_employee_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert time columns to datetime objects
    df['time'] = pd.to_datetime(df['time'])
    df['timeout'] = pd.to_datetime(df['timeout'])

    # Sort the DataFrame by employee name and time
    df = df.sort_values(by=['employee name', 'time'])

    # Initialize variables for consecutive days and shift duration checks
    consecutive_days_count = 0
    for index, row in df.iterrows():
        # Check for consecutive days
        if consecutive_days_count == 6:
            print(f"Employee: {row['employee name']}, Position: {row['position id']}, Consecutive Days: 7")

        # Check for less than 10 hours between shifts but greater than 1 hour
        if index > 0:
            time_difference = row['time'] - df.at[index - 1, 'timeout']
            if timedelta(hours=1) < time_difference < timedelta(hours=10):
                print(f"Employee: {row['employee name']}, Position: {row['position id']}, Less than 10 hours between shifts")

        # Check for more than 14 hours in a single shift
        shift_duration = row['timeout'] - row['time']
        if shift_duration > timedelta(hours=14):
            print(f"Employee: {row['employee name']}, Position: {row['position id']}, Shift Duration: {shift_duration}")

        # Reset consecutive days count if there is a gap in days
        if index > 0 and (row['time'] - df.at[index - 1, 'time']).days > 1:
            consecutive_days_count = 0
        else:
            consecutive_days_count += 1


file_path = 'path/to/your/file.csv'
analyze_employee_data(file_path)
