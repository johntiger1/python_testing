

def simplest_deco(func):
    def wrapped():
        print("pre")
        func()
        print("post")
    return wrapped

@simplest_deco
def basic_print():
    print("wrap this basic print")

print(basic_print())