def xxx(x):
    if x.startswith("hello"):
        return ("$0")
    elif x.startswith("h"):
        return ("$20")
    else:
        return ("$100")

num = input ("Greeting: ").lower().strip()



print (xxx(num))
