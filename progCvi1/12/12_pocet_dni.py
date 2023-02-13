import datetime

dayOne,monthOne,yearOne,dayTwo,monthTwo,yearTwo = (int(i) for i in input().split())

dateOne = datetime.date(yearOne,monthOne,dayOne)
dateTwo = datetime.date(yearTwo,monthTwo,dayTwo)

print((dateTwo - dateOne).days)
