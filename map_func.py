# map function - map(function, iterable)
# returns an iterator that applies function to every item of iterable

def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [551, 641, 891, 122, 453, 223, 234, 343, 562, 115, 554, 111, 679, 516]

# 1st solution for loop
# y = []
# for num in x:
#     y.append(make_even(num))
# print(y)

# 2nd solution map()
y = map(make_even, x)
# this will display map object
print(y)
print(list(y))

print()

z = list(map(make_even, x))
print(z)

print()

# 3rd solution list comprehension
w = [make_even(num) for num in x]
print(w)


