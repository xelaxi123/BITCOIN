import emoji
def main():
    while True:
        x = input("Input: ")
        try:
            x = emoji.emojize(x, language = "alias")
        except ValueError:
            pass
        else:
            print("Output: ",x)
            break
main()
