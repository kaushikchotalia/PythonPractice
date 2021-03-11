# def hello():
#     return "Hello Kaushik!"
#
# def other(some_def_func):
#     print('Other func code runs here!')
#     print(some_def_func())

#other(hello)

def new_dcecorator(original_func):

    def wrap_func():

        print("Some extra code, before the original fuction")

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

@new_dcecorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

#func_needs_decorator = new_dcecorator(func_needs_decorator)
#print(func_needs_decorator())