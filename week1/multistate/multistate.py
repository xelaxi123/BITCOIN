def ask():
    question1 = float(input("What is the order amount? "))
    question2 = input("what state do you live in? ").strip().title()
    if question2 == "Wisconsin":
        question3 = input("where? ")
        quest = question3.strip().title()
        if  quest == "Eau Claire" or quest == "Dun":
                tax = question1 * 5 / 100
                total = question1 + tax
                return tax, total
    elif  question2 == "Illionis":
            tax = question1 * 8 / 100
            total = question1 + tax
            return tax, total
    else:
        return 0, question1

tax, total = ask()
print(f"The tax is ${tax}\nThe total is ${total}")


