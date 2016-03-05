import struct
class P():
    def __init__(self):
        print("P.__init__(self) method invoked.")


class C(P):
    def __init__(self):
        print("C.__init__(self) method invoked.")


class RoundFloat(float):
    pass

if __name__ == "__main__":
    testStr = "0000057d".decode("hex")
    print(type(testStr))
    print(testStr)

    val = struct.unpack("!I", "0000057d".decode("hex"))
    print(val)
    print(type(val))
