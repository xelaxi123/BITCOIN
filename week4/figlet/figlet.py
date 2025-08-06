# from pyfiglet import Figlet
# try:
#     f = Figlet(font='slant')
#     user = input("Input: ")
# except ValueError:
#     print("Invalid usage")

# print(f"Output:\n{f.renderText(user)}")


from pyfiglet import Figlet
from sys import argv
from sys import exit
from random import choice

figlet = Figlet()


def check_input():
    if len(argv) == 1:
        user_input = input("Input:")
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(user_input))
    elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font") and argv[2] in figlet.getFonts():
        user_input = input("Input:")
        figlet.setFont(font=argv[2])
        print(figlet.renderText(user_input))
    else:
        exit("Invalid usage")

check_input()
