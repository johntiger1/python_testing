

class MyClass:
    def __init__(self):
        pass

    def myStaticMethod():
        print("a static method")

    @staticmethod
    def myStaticMethodWithArg(my_arg):
        print(my_arg)
        print("a static method")


MyClass.myStaticMethod()
MyClass.myStaticMethodWithArg("skhsdkj")
abc = MyClass()
abc.myStaticMethodWithArg("avc")