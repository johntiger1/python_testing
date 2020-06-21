

"""
One way of using the fixtures is to use annotated stuff.
But the main way is to simply ensure string matching.

"""
class MyDemoClass:
    @staticmethod
    def function_to_inject():
        print("original, network intensive function call")
        return "og funct"

    @staticmethod
    def ancillary_function():
        print(MyDemoClass.function_to_inject())
        return

    @staticmethod
    def fixture_demo(function_to_inject):
        print("we are using an injected function")
        print("the function which is injected will replace the function call in the appropriate scope")
        MyDemoClass.ancillary_function()
        print("end the previous function")
