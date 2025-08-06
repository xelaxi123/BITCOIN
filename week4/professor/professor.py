# import random
# def main():
#  print(get_level())

# def get_level():
#     while True:
#         score = 0
#         questions = 0
#         try:
#             lev = int(input("Level: "))
#             if lev == 1:
#                 while questions < 10:
#                     number1 = random.randint(0,9)
#                     number2 = random.randint(0,9)
#                     try:
#                         questions += 1
#                         print(f"What is {number1} + {number2} = ", end = "")
#                         answer = int(input())
#                         while answer.isdigit() == False:
#                             continue
#                         if answer.isdigit() == True:
#                             sum = number1 + number2
#                             if answer == sum:
#                                 score += 1
#                             else:
#                                 print("EEE")
#                     except ValueError:
#                         continue
#                 print(f"your score is {score}")
#             elif lev == 2:
#                 while questions < 10:
#                     number1 = random.randint(10, 99)
#                     number2 = random.randint(10, 99)
#                     try:
#                         questions += 1
#                         print(f"What is {number1} + {number2} = ", end = "")
#                         answer = int(input())
#                         sum = number1 + number2
#                         if answer == sum:
#                             score += 1
#                         else:
#                             print("EEE")
#                     except ValueError:
#                         continue
#                 print(f"your score is {score}")
#             elif lev == 3:
#                 while questions < 10:
#                     number1 = random.randint(100,999)
#                     number2 = random.randint(100,999)
#                     try:
#                         questions += 1
#                         print(f"What is {number1} + {number2} = ", end = "")
#                         answer = int(input())
#                         sum = number1 + number2
#                         if answer == sum:
#                             score += 1
#                         else:
#                             print("EEE")
#                     except ValueError:
#                         continue
#                 print(f"your score is {score}")
#             break
#         except Exception:
#             continue



# if __name__ == "__main__":
#     main()

import random


def main():
    # Get the difficulty level
    level = get_level()

    # Track the user's score
    score = 0

    # Generate and solve 10 math problems
    for _ in range(10):
        # Generate two random integers based on the level
        x = generate_integer(level)
        y = generate_integer(level)

        # Track attempts for this problem
        attempts = 0
        correct = False

        # Allow up to 3 attempts per problem
        while attempts < 3 and not correct:
            try:
                # Prompt user to solve the problem
                user_input = input(f"{x} + {y} = ")

                # Check if input is a valid integer
                user_answer = int(user_input)

                # Check if answer is correct
                if user_answer == x + y:
                    correct = True
                    score += 1
                else:
                    print("EEE")
                    attempts += 1

            except ValueError:
                # Handle non-numeric input
                print("EEE")
                attempts += 1

        # If no correct answer after 3 attempts, show solution
        if not correct:
            print(f"{x} + {y} = {x + y}")

    # Print final score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()

# import random



# for _ in range(10):
#     number1 = random.randint(0,9)
#     number2 = random.randint(0,9)
#     count = 0
#     point = 0
#     for _ in range(3):
#         num = input(f"{number1} + {number2} = ")
#         count+=1
#         if (int(num) == number1 + number2) and count < 4:
#             print("Just right!")
#             point += 1
#             break
#         elif count != 3:
#             print("Wrong!!!")
#         elif count == 3:
#             print("Wrong!!")
#             break


