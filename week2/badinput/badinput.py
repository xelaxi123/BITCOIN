def main():
    user = int(input("What is rate of return? "))
    var = is_valid(user)
    if var:
        year = 72 / str(var)
        print(f"It will takes {year} years to double initial investment.")
def is_valid(x):
    if x == 0:
        return "Invalid input"
    # else:
    #     return
    # if x == 0:
    #     return False

if __name__ == "__main__":
    main()
