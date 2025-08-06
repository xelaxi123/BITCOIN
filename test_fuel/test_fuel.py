from fuel import convert, gauge

def main():
    test_gayofa()
    test_procenti()
def test_gayofa():
    assert convert("1/2") == 0.5
    assert convert("3/4") == 0.75
    assert convert("2/3") == 0.6666666666666666
def test_procenti():
    assert gauge(1) == "F"
    assert gauge(99) == "F"
    assert gauge(0.5) == "50%"

if __name__ == "__main__":
    main()
