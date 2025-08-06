def main():
    # Prompt user for input
    text = input("Input: ")
    # Remove vowels
    no_xmovani = shorten(text)
    # Print result
    print("Output:", no_xmovani)

def shorten(word):
    xmovani = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in xmovani:
            result += char
    return result

if __name__ == "__main__":
    main()

