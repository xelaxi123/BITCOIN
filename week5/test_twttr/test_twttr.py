from twttr import shorten

def main():
    test_xmovani()
    test_number()
    test_punktuacia()

def test_xmovani():
    assert shorten("hello") == "hll"
    assert shorten("HELL") == "HLL"
    assert shorten("HElo") == "Hl"
def test_number():
    assert shorten("123456789") == ("123456789")
def test_punktuacia():
    assert shorten("!.*,") == ("!.*,")

if __name__ == "__main__":
    main()
