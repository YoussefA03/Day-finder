def find_day():

    print("** Use the month's number instead of name \n ** The program works for years between 1000 and 9999 \n ** If the year is a leap year, using 29 as your day will instead give you the day for the 28th")
    year = int(input('year '))
    month = int(input('month '))
    day = int(input('day '))
    zerod = year//100
    leap = True if year%4 == 0 else False
    while zerod != 19 and zerod != 20 and zerod != 21 and zerod != 22:
        if zerod < 19:
            zerod += 4
        elif zerod > 22:
            zerod -=4
    if month == 1:
        if leap:
            key = 4
        else:
            key = 3
    elif month == 2:
        if leap:
            key = 29
        else:
            key = 28
    elif month == 3:
        key = 14
    elif month == 4:
        key = 4
    elif month == 5:
        key = 9
    elif month == 6:
        key = 6
    elif month == 7:
        key = 11
    elif month == 8:
        key = 8
    elif month == 9:
        key = 5
    elif month == 10:
        key = 10
    elif month == 11:
        key = 7
    elif month == 12:
        key = 12
    last2 = year%100
    y = last2 + last2//4
    final = y%7
    # start wednesday
    if zerod == 19:
        d = {0 : 'Wednesday', 1 : 'Thursday' , 2 : 'Friday', 3 : 'Saturday', 4 : 'Sunday' , 5: 'Monday' , 6: 'Tuesday'}
        ans = (final + (day-key)) % 7
        print(d[ans])
    elif zerod == 20:
        d = {0 : 'Tuesday', 1 : 'Wednesday' , 2 : 'Thursday', 3 : 'Friday', 4 : 'Saturday' , 5: 'Sunday' , 6: 'Monday'}
        ans = (final + (day-key)) % 7
        print(d[ans])
    elif zerod == 21:
        d = {0 : 'Sunday', 1 : 'Monday' , 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday' , 5: 'Friday' , 6: 'Saturday'}
        ans = (final + (day-key)) % 7
        print(d[ans])
    elif zerod == 22:
        d = {0 : 'Friday', 1 : 'Saturday' , 2 : 'Sunday', 3 : 'Monday', 4 : 'Tuesday' , 5: 'Wednesday' , 6: 'Thursday'}
        ans = (final + (day-key)) % 7
        print(d[ans])


find_day()
