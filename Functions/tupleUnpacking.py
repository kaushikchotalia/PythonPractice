# stock_prices =  [('APPL',200),('GOOG',400),('MSFT',1000)]
# for item in stock_prices:
#     print(item)
# for ticker,price in stock_prices:
#     print(ticker)
#     print(price)

work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass # do nothing
    # Return
    return (employee_of_month, current_max)

print(employee_check(work_hours))

# tuple unplacking with function call
name, hours = employee_check(work_hours)
print(name)
print(hours)

# good way to get the tuple in single variable and then do unpacking as below
result = employee_check(work_hours)
print(result)