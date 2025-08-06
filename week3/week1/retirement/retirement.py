age = int(input("What is you current age? "))
retire = int(input("At what age would you like to retire? "))
retirement = retire - age
year = 2025 + retirement

print(f"You have {retirement} years left until you can retire.\n"
      f"It's 2025, so you can retire in {year}.")
