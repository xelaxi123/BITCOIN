ask = int(input("How many people? "))
ask2 = int(input("How many pizzas do you have? "))
ask3 = int(input("How many slices per pizza? "))

get = (ask3 * ask2) / ask

nashti = (ask3 * ask2) - (ask * get)

print(f"{ask} people with {ask2} pizzas\n"
      f"Each person gets {get} piece of pizza.\n"
      f"there are {nashti} leftover pieces.")



