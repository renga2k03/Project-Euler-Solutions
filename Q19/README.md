# Q19 - Counting Sundays

**Required Output :** Number of Sundays between two given dates that fall on the first of a month


## Idea & Approach :-
* Iterating through all dates and checking would be incredibly tedious and hence can increment over only Sundays by ignoring other 6 days
* But iterating from Jan 1, 1900 all over to the given start date to find the first Sunday occurence would consume lot of time
* Since Jan 1, 1900 is given as Monday, the first Sunday occurence is Jan 7. Hence a day would be Sunday if the total number of days till the given date is divisible by 7 (Hypothetically Jan 0 is Sunday)
* But even computing the first Sunday within the given dates is far from optimal in case of very huge year numbers as the upper bound of test case can go as far as $10^{16}$
* Instead of iterating over to find the Sunday, compute the total number of days till the given start date
* Find out the number of leap years till the given start date and multiply the leap year count with 366 and non-leap year count with 365 excluding the year of the start date
* Since the Gregorian calendar repeats every 400 years, assign the nearest century year that follows the same pattern as the year 1900 as the starting year and count the number of leap years from there to avoid huge numbers
* For calculating the number of days within the same year till the date, use an array containing the maximum days per month. Slice the array upto the given month and add the summation to the total days and also the given day count
* After computing the total number of days, check its divisibility with 7. If divisible, then consider the given start date itself as the first Sunday within the bounds. Otherwise add the given date's day count with (7 - remainder of total days over 7) and convert to "yyyy mm dd" format for easier comparison
* Starting from the first Sunday date, iterate by 7 to find out other Sundays till the given end date and increment a counter variable if the day falls on 1st of that month. Hence display the final count for each bound

## Note :- 
1. **As the question considers its beginning from 1900, the subsequent repeating calendars begin every 400 years from there**
2. **Assign the days as 29 for February whenever the year encountered during iteration or while finding the start date is a leap year**
3. **Also while the leap year is considered to be divisible by 4, century years in particular have to be divisible by 400**
4. **When converting to the "yyyy mm dd", include 0s when the months and days are single digits to ensure proper comparison with dates**
5. **Whenever the iterative day variables exceeds the months maximum days, subtract the maximum value from the day variable and increment the month variable by 1**
6. **Similarly when the month variable exceeds 12, re-initialize to 1 and increment the year variable by 1**

## Complexity :
**$O(t)$** (Since the test cases have only a maximum distance of 1000 years between start and end dates, the number of iterations is around 50k and can round upto O(1) complexity)
