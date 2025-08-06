def main():
    num = input ("Greeting: ")
    nul = value(num)
    print (f"${nul}")
def value(greetings):
    if greetings.startswith("hello"):
        return 0
    elif greetings.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


# def main():
#     greeting = input("Greeting: ")
#     print(f"${value(greeting)}", end="")


# def value(greeting):

#     if greeting.startswith("hello"):
#         x = 0
#     elif greeting[0] == "h":
#         x = 20
#     else:
#         x = 100
#     return x
# if __name__ == "__main__":
#     main()
