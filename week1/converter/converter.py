def temp():

    text = input("Press C to convert from Farenheit to Celsius.\n"\
                 "Press F to convert from Celsius to Farenheit.\n"\
                 "Your choice: ").upper()

    if text == "C":
        text = int(input("Please enter the temperature in Farenheit: "))
        f = (text - 32)*5/9
        return f"The temperatuer in Farenheit is {round(f)}."

    elif text == "F":
        text = int(input("Please enter the temperatuer in Celsius: "))
        c = (text - 9/5) + 32
        return f"the temperature in Celsius is {round(c)}"
    

text = temp()
print(text)
