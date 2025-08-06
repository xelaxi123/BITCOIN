amountdue = 50
while amountdue > 0:
    user = int(input(f"Amount due: {amountdue}\nInsert coin: "))
    if user in [25, 10, 5]:
        amountdue -= user
        print(f"Change owed: {abs(amountdue)}")
    else:
        print("Invalid")




