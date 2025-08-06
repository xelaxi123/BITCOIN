def main():
    nul = num()
    print(f"The total is {nul}.")

def num():
    total = 0
    for _ in range(5):
        user = int(input("Enter a number: "))
        total += user
    return total

if __name__ == "__main__":
    main()
