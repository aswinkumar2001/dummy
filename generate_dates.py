import pandas as pd
from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2025, 8, 1, 0, 0)
end_date = datetime(2025, 8, 13, 0, 0)

# Generate date range with 15-minute intervals
date_list = []
current_date = start_date
while current_date <= end_date:
    date_list.append(current_date.strftime("%d/%m/%Y %H:%M"))
    current_date += timedelta(minutes=15)

# Create a DataFrame
df = pd.DataFrame(date_list, columns=["DateTime"])

# Save to CSV
df.to_csv("datetime_schedule.csv", index=False)

print("File 'datetime_schedule.csv' has been generated. Open it with Excel!")