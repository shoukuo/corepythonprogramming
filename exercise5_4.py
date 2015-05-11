def isLeap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

while True:
    yearstr = raw_input("Enter a year number('.' quit): ")
    if(yearstr == "."): break
    bleap = isLeap(year)
    print "%d is %s a leap year" % (year, "" if bleap else "not")
