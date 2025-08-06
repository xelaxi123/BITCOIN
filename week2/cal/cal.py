mun = ["1: ", "2: ", "3: ", "4: ","5: ","6: ","7: "]
for num in mun:
    nu = int(input(f"Enter number bro: {num}"))
    print("The number is: ", nu)
    if len(str(nu)) > 6:
        num1 = nu * 7
        print("The total is: ",num1)


