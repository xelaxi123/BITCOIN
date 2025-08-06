# def main():
#     while True:
#         try:
#             x,z = user.split("/")
#             x = int(x)
#             z = int(z)
#             r = x / z
#             if x > z:
#                 raise ValueError
#             elif r >= 0.99:
#                 print("F")
#                 break
#             elif r <= 0.1:
#                 print("E")
#                 break
#         except (ZeroDivisionError,ValueError):
#             pass
#         else:

#             break

# main()
def main():
    while True:
        try:
            user = input("fraction: ")
            var = convert(user)
            num = gauge(var)
            print(num)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
        x,z = fraction.split("/")
        x = int(x)
        z = int(z)
        r = x / z
        if x > z:
            raise ValueError
        return r
def gauge(percentage):
    var = percentage * 100
    var = round(var)
    if var >= 99:
        return "F"
    elif var <= 1:
        return "E"
    else:
        return f"{var}%"



if __name__ == "__main__":
    main()
