def month():
    ask = int(input("Please enter the number of month: "))
    if ask == 1:
        var = "January"
    elif ask == 2:
        var = "February"
    elif ask == 3:
        var = "March"
    elif ask == 4:
        var = "April"
    elif ask == 5:
        var = "May"
    elif ask == 6:
        var = "June"
    elif ask == 7:
        var = "Jule"
    elif ask == 8:
        var = "August"
    elif ask == 9:
        var = "September"
    elif ask == 10:
        var = "Octomber"
    elif ask == 11:
        var = "November"
    elif ask == 12:
        var =  "December"
    return var
print("The name of the month is", month())
