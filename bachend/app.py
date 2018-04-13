import inspect


print("Starting... \n")


### TZ decorator
def decorator_maker(opt):

    def decorator(function):

        def create_temp(*args, **keyargs):

            func_args = inspect.getargspec(function).args[1:]
            default_values = inspect.getargspec(function).defaults
            default_values = dict(zip(func_args[-len(default_values):], default_values))

            temp = dict(zip(func_args, list(args)))

            for i in keyargs:
                temp[i] = keyargs[i]

            for i in func_args:
                if i not in temp:
                    temp[i] = default_values[i]

            return temp.__str__()

        def wrapper(self, *args, **keyargs):

            temp = create_temp(*args, **keyargs)

            if temp in self.__dict__[opt]:
                print("Gotten from cache:")
            else:
                self.__dict__[opt][temp] = (function(self, *args, **keyargs))

            try:
                return self.__dict__[opt][temp]
            except:
                print("Cache getting Error")

            return function(self, *args, **keyargs)

        return wrapper

    return decorator


class SomeClass:

    def __init__(self):
        self.opt = {}

    def self(self):
        return self

    @decorator_maker("opt")
    def count(self, first, second=1, third=2, four=5):
        res = first + second + third + four
        return res



model = SomeClass()

print(model.count(1,2,third=3))
print(model.count(1,2,third=3)) # cached
print(model.count(1,second=1))
print(model.count(1, second=2, third=2, four=1))
print(model.count(1, second=2, four=1)) #cached
print(model.count(1,3,3))

# print(model.opt)
