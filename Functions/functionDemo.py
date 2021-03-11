# def name_of_function():"
# for functions' name Python use sanke casing pattern
# Sanke casing is all lowercaser with underscores between words

def add_function(num1,num2):
    return num1 + num2
result = add_function(2,5)
print(result)

def say_hello():
    print("Hello")
say_hello()

def say_name(name):
    print(f'Hello {name}')
#say_name()
say_name("Kaushik")

def say_name(name='Default'):
    print(f'Hello {name}')
# If user do not pass the argument then defult value is called in below line
say_name()

