def main():
    while True:
        try:
            user = input("fraction: ")
            x,z = user.split("/")
            x = int(x)
            z = int(z)
            r = x / z
            if x > z:
                raise ValueError
            elif r >= 0.99:
                print("F")
                break
            elif r <= 0.1:
                print("E")
                break
        except (ZeroDivisionError,ValueError):
            pass
        else:
            var = r * 100
            var = round(var)
            var = str(var) + str("%")
            print(var)
            break

main()
