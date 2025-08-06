import random
def main():
    while True:
        try:
            a = []
            x = int(input("Level: "))
            for i in range(1,x + 1):
                a.append(i)
            g = random.choice(a)
            print(g)
            while True:
                try:
                    ask = int(input("Guess: "))
                    if ask == g:
                        print("Just right!")
                        break
                    elif ask > g:
                        print("Too large!")
                    else:
                        print("Too small!")
                except ValueError:
                    continue
        except:
            continue
        break
if __name__ == "__main__":
    main()



import random

def main():
    level = get_level()
    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

if __name__ == "__main__":
    main()



