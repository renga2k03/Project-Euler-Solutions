days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = int(input())
tdates = []
first_sun = []
for i in range(t):
    startdate = input().split()
    if len(startdate[1]) == 1:
        startdate[1] = "0" + startdate[1]
    if len(startdate[2]) == 1:
        startdate[2] = "0" + startdate[2]
    enddate = input().split()
    if len(enddate[1]) == 1:
        enddate[1] = "0" + enddate[1]
    if len(enddate[2]) == 1:
        enddate[2] = "0" + enddate[2]
    startdate = ' '.join(startdate)
    enddate = ' '.join(enddate)
    tdates.append((startdate, enddate))
for i in range(t):
    days_from_start = 0
    start_year = 1900
    y, m, d = map(int, tdates[i][0].split())
    if y % 4 == 0:
        l1 = y - 4
    else:
        l1 = y - (y % 4)
    if y % 100 == 0:
        l2 = y - 100
    else:
        l2 = y - (y % 100) 
    if y % 400 == 0:
        l3 = y - 400
    else:
        l3 = y - (y % 400)
    if (y // 100) % 4 == 3:
        start_year = (y // 100) * 100
    else:
        y_100 = y // 100
        start_year = (y_100 - ((y_100 % 4) + 1)) * 100
    n1 = n2 = n3 = 0
    if l1 >= start_year:
        n1 = (l1 - start_year) // 4 + 1
    if l2 >= start_year:
        n2 = (l2 - start_year) // 100 + 1
    if l3 >= start_year:
        n3 = (l3 - start_year) // 400 + 1
    nlpyr = n1 - n2 + n3
    days_from_start += nlpyr * 366 + ((y - start_year) - nlpyr) * 365
    if (l1 == y - 4 and l2 != y - 100) or (l1 == y - 4 and l2 == y - 100 and l3 == y - 400):
        days[1] = 29
    days_from_start += sum(days[:(m - 1)]) + d
    if days_from_start % 7 == 0:
        first_sun.append(tdates[i][0])
    else:
        d += (7 - (days_from_start % 7))
        if d > days[m-1]:
            d -= days[m-1]
            if m >= 12:
                m = 1
                y += 1
            else:
                m += 1
        stdate = str(y)
        if m < 10:
            stdate += " 0" + str(m)
        else:
            stdate += " " + str(m)
        if d < 10:
            stdate += " 0" + str(d)
        else:
            stdate += " " + str(d)
        first_sun.append(stdate)
    days[1] = 28
for i in range(t):
    ct = 0
    curdate = first_sun[i]
    y, m, d = map(int, curdate.split())
    enddate = tdates[i][1]
    while curdate <= enddate:
        if (y % 100 == 0 and y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
            days[1] = 29
        else:
            days[1] = 28
        if d > days[m - 1]:
            d -= days[m - 1]
            if m >= 12:
                m = 1
                y += 1
            else:
                m += 1
        if m < 10:
            if d < 10:
                curdate = str(y) + " 0" + str(m) + " 0" + str(d)
            else:
                curdate = str(y) + " 0" + str(m) + " " + str(d)
        else:
            if d < 10:
                curdate = str(y) + " " + str(m) + " 0" + str(d)
            else:
                curdate = str(y) + " " + str(m) + " " + str(d)
        if d == 1 and curdate <= enddate:
            ct += 1
        days[1] = 28
        d += 7
    print(ct)
