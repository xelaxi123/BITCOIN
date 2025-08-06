def bmi():
    height = float(input("Please enter your height: "))
    weight = float(input("Please enter your weight: "))
    b = weight/(height * height)
    if b >= 18.5 and b <= 25:
        var = "You are within the ideal weight range."
    elif b < 18.5:
        var = "Your weight is low."
    else:
        var = "You are overweight. You should see doctor."
    return var
print(bmi())
