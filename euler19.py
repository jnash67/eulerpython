import datetime

date=datetime.datetime(1901,1,1)
endDate = datetime.datetime(2000, 12, 31)
c = 0
while date<=endDate:
    date += datetime.timedelta(days=1)
    if (date.weekday()==6) and (date.day==1):
        c += 1
        print("This date #{} is a sunday on the first of the month {}".format(c, date))
print("There were {} dates in the 20th century".format(c))