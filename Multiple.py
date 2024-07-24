def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
print(multiply(2, 3, 4))  
print(multiply(1.5, 2, 10))  
print(multiply(5))  
print(multiply())