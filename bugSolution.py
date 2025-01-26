def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return 0 # Or raise a custom exception
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0,0)
print(result) #This will return 0