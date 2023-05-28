from datetime import datetime, timedelta

start_date = datetime(2023, 2, 1)
end_date = datetime(2023, 3, 1)

current_date = start_date

while current_date <= end_date:
    print(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)
