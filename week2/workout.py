# def main():
#     registrered_peoples = [] #[(...,..)(..,..)(..,..)(...,..)(...,..)]
#     while len(registrered_peoples) < 5:
#         name = input("Add your name: ")
#         mail = input("Add your email: ")
#         if "@" not in mail:
#             print("incorect E-mail format")
#             continue
#         registration = (name, mail)

#         if registration in registrered_peoples:
#             print("you are already registrered")
#         else:
#             registrered_peoples.append(registration)
#         print(f"{name} you have registrered successfuly")

#     for i, (name, mail) in enumerate(registrered_peoples, 1):
#         print(f"{i}. {name}. ({mail})")

# if __name__== "__main__":
#     main ()


# def main():
#     user = get_user_data()
#     fibonachi = generate_fibonachi(user)
#     converted_fibonachi = [str(num) for num in fibonachi]   #a = []
#                                                             #for num in fibonachi:
#                                                                 #a.append(num)
#     result = " ".join( converted_fibonachi)
#     print(result)



# def generate_fibonachi(n):
#     array = [0,1]
#     for _ in range(2,n):
#         array.append(array[-1]+array[-2])
#     return array

# def get_user_data():
#     while True:
#         user = input("Add the number: ")
#         if user.isdigit() and int(user)>3:
#             return int(user)


# if __name__ == "__main__":
#     main()


def main():
    candidates = get_candidates()
    candidat_dictionary = get_candidate_dictionary(candidates)
    guest_number = get_guest_number()
    result = voting(candidates, candidat_dictionary, guest_number)
    result_values = list(result.values())
    max_value = max(result_values)
    max_value_index = result_values.index(max_value)

    winners = [candidat for candidat, point in result.items() if point == max_value]
    if len(winners)>1:
        print(f"We have multiple winners  {' <3 '.join(winners)} whit point {max_value}")
    else:
        print(f"whe winner is {candidates[max_value_index]} with points {max_value}")



def voting(candidats, candit_dict, guest):
    counter = 0
    while counter < guest:
        print("Our candidate: ")
        for id, name in enumerate(candidats,1 ):
            print(f"{id} {name}")
        user = input("Add candidate name: ").title()
        if user in candidats:
            candit_dict[user] += 1
            counter +=1
            print("vouted succesfully")
        else:
            print("This candidant is not in list")
    return candit_dict
def get_guest_number():
    while True:
        user = input("Add guest number: ")
        if user.isdigit():
            return int(user)
        else:
            print("Wrong input bliad")

def get_candidate_dictionary(candidat_list):
    '''
    შემოდის სია და აბრუნებს ამ სიისგან წარმოებულ ლექსიკონს მნიშვნელობით 0
    '''
    candidat_dictionary = {}
    for candidant in candidat_list:
        candidat_dictionary[candidant] = 0
    return candidat_dictionary
def get_candidates():
    """
    აგროვებს კანდიდატებს და ტოვებს მომხმარებელი ჩაწერს ok მაშინ დაბრუნდება სრული სია
    """
    candidates = []
    while True:
        user = input("Add candidate name or write Ok: ").title()
        if user == "Ok" and len(candidates) > 1:
            return candidates
        elif user in candidates:
            print("candidate already registrered")
        elif user != "Ok":
            candidates.append(user)



if __name__ == "__main__":
    main()
