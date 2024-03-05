from datetime import date
date1='2019-06-29'
date2='2019-06-30'
date11=date.fromisoformat(date1)
date22=date.fromisoformat(date2)
print(abs(date22-date11).days)