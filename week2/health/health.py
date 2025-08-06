# def main():
#     total = get_step()
#     print(sum(total))


# def get_step():
#     ans = []
#     week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#     for day in week:
#         m = input(f"Enter steps for {day}: ")

#             ans.append(int(m))
#         else:
#             continue
#     return ans

def stocker():
    message = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    values = []
    for i in message:
        v = user_input(f"Enter steps for {i}: ")
        values.append(int(v))
    print(sum(values))

def user_input(x):
    while True:
        result = input(x)
        if result.isdigit():
            return result
        else:
            print("Invalid input!")
            continue

stocker()
# if __name__ == "__main__":
#     main()
