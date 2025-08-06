user = int(input("What is the length of the room in feet? "))
user2 = int(input("What is the width of the room in feet? "))

area = user * user2

m = area * 0.09290304

print(f"You entered dimension of {user} feet by {user2} feet.\n"
      f"the area is\n"
      f"{area} square feet\n"
      f"{m} square meters")
