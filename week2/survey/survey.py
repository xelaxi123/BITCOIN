def main():
    counter = 0
    count = 0
    user = ["Do you like python? (yes/no): ",
            "Do you enjoy coding? (yes/no): ",
            "Are you a student? (yes/no): ",
            "Do you work remotely? (yes/no): ",
            "Is this survey helpfull? (yes/no): "]
    for ask in user:
        y = input(ask).lower()
        if y == "yes":
            counter += 1
        elif y == "no":
            count += 1
    print (f"Summary: {counter} yes, {count} no.")


if __name__ == "__main__":
    main()

