t = int(input())
digits = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
tenths = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
sp = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
others = ['Thousand','Million','Billion']
for i in range(t):
    n = int(input())
    s = ""
    others_i = 0
    while n > 0:
        d = n % 1000
        s_three = ""
        if d >= 100:
            s_three += " " + digits[d // 100 - 1] + " Hundred"
        if d % 100 >= 10:
            if d % 100 == 10:
                s_three += " Ten"
            elif d % 100 < 20:
                s_three += " " + sp[d % 100 - 11]
            else:
                s_three += " " + tenths[(d % 100) // 10 - 1]
                if d % 10 > 0:
                    s_three += " " + digits[d % 10 - 1]
        else:
            if d % 100 > 0:
                s_three += " " + digits[d % 100 - 1]
        if others_i > 0 and d % 1000 > 0:
            s = " " + others[others_i - 1] + s
        s = s_three + s
        others_i += 1
        n = n // 1000
    if s[0] == ' ':
        print(s[1:])
