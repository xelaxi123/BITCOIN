# from bank import value

# def main():
#     test_start_with()


# def test_start_with():
#     assert value("hello, how are you?") == 0
#     assert value("how, you doing?") == 20
#     assert value("name your is alex?") == 100


# if __name__ == "__main__":
#     main()

from bank import value

def main():
    test_value()

def test_value():
    h = ["Hey","How are you", "Hey yo", "HEY MAN", "Hi", "Holla"]
    for word in h:
        assert value(word) == 20
    hello = ["Hello","HeLlo", "Hello , how are you?", "Hello, what's up?", "Hello 123"]
    for word in hello:
        assert value(word) == 0
    elses = ["Yo", "Salute!", "What's up?", "123", "Gamarjoba!"]
    for word in elses:
        assert value(word) == 100

if __name__ == "__main__":
    main()



