
def say_hello(name):
    print("I want to say hello with your, {}".format(name))
    print("Hello, {}".format(name))
    print("Done..............")


if __name__ == '__main__':
    print("***" * 10)
    name = input("Please input your name: ")
    say_hello(name=name)
    print("@@@" * 10)
