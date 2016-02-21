class P():
    def __init__(self):
        print("P.__init__(self) method invoked.")


class C(P):
    def __init__(self):
        print("C.__init__(self) method invoked.")


class RoundFloat(float):
    pass

if __name__ == "__main__":
    c = C()
