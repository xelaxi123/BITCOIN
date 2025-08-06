def num():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))
    if a > b and a > c:
        var = a
    elif b > c:
        var = b
    else:
        var = c
    return var


print(f"The largest number is {num()}.")
