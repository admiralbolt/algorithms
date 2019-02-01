# There's probably a mathy way to do this but fuck it.
from datetime import date

sundays = 0
for year in range(1901, 2001):
  for month in range(1, 13):
    # Mondays == 0, Sundays == 6.
    if date(year, month, 1).weekday() == 6:
      sundays += 1
print(sundays)
