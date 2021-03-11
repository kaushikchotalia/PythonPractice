def even_check(number):
    return number % 2 == 0
print(even_check(20))

def check_even_list(num_list):
    # return all the even numbers in a list
    # placeholder variable
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass # means do not do anything
    return even_numbers

print(check_even_list([2,3,5]))
print(check_even_list([2,4,6,7]))

