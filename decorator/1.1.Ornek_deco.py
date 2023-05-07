def my_decorator(func):
    def wrapper():
        print("Öncesinde")
        func()
        print("Sonrasında")
    return wrapper
@my_decorator
def sayGoodbye():
    print("Goodbye")
@my_decorator
def sayHello():
    print("Hello")

sayGoodbye()
sayHello()