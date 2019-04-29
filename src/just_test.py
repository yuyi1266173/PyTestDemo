

def test():
    while True:
        aaa = input("input:")

        if 'q' == aaa.lower():
            break
        print(aaa, type(aaa))


if __name__ == "__main__":
    test()
