# regular function:

def add(x, y):
    return x + y


print(add(4, 5))


# lambda as variable
add2 = lambda x, y: x + y
print(add2(3, 6))

# lambda
print((lambda x,y: x*y)(2,3))

# usage of lambda
# if I want to create a higher order function that accepts
# function as an argument or returns a function
# Create function that can take list as an input and also take in a function as an input
# and it will apply that function to each item


def my_map(my_func, my_iterable):
    result = []
    for item in my_iterable:
        new_item = my_func(item)
        result.append(new_item)
    return result


nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)
print(cubed)


