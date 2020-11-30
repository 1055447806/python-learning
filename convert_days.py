DAYS_PRE_YEAR = 365
DAYS_PRE_WEEK = 7
days = input("Please give me the days:")
days = int(days)
years = days // DAYS_PRE_YEAR
weeks = days % DAYS_PRE_YEAR // DAYS_PRE_WEEK
remaining_days = days % DAYS_PRE_YEAR % DAYS_PRE_WEEK
print("years:", years)
print("weeks:", weeks)
print("days:", remaining_days)
