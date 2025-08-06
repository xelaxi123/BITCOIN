def main():
    case = camelCase()
    print(case)

def camelCase():
    camelcase = input("camelCase: ")
    print("snakecase: ", end = "")
    var = ""
    for letters in camelcase:
        if letters.isupper():
            var += "_" + letters.lower()
        else:
            var += letters
    return var

if __name__ == "__main__":
    main()
