import inspect


print("Starting... \n")


def decorator_maker(opt):


    def decorator(function):

        func_args = inspect.getargspec(function).args[1:]
        default_values = inspect.getargspec(function).defaults

        print(func_args)
        print(default_values)

        temp = {}

        def create_temp():
            for i in func_args:
                print(i)
            print (", ".join(func_args))

        def wrapper(self, *args, **keyargs):


            if (args, keyargs).__str__() in self.__dict__[opt]:
                print("Get hashed!")
            else:
                create_temp()
                self.__dict__[opt][(args, keyargs).__str__()] = (function(self, *args, **keyargs))

            try:
                return self.__dict__[opt][(args, keyargs).__str__()]
            except:
                print("Cashe getting Error")

            return function(self, *args, **keyargs)

        return wrapper

    return decorator


class SomeClass:

    def __init__(self):
        self.opt = {}

    def self(self):
        return self

    @decorator_maker("opt")
    def count(self, first, second=2):
        return first + second

# @decorator(hash)
# def hello():
#     print('hello')

model = SomeClass()

res = model.count(1,2)

res = model.count(1)

res2 = model.count(1, 1)

res2 = model.count(1, 1)
res = model.count(1,2)

print(model.opt)
print(model.__module__)