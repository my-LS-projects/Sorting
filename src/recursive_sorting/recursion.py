# A recursive algorithm must have a base case
# A recursive algorithm must change its state and move toward the base case
# A recursive algorith must call itself, recursively.

# print every number, starting at number, until you reach 0
def recurse(number):
    if number <= 0:
        return
    print(number)
    number -= 1
    recurse(number)
    recurse(number)


# Fibonacci Sequence [1, 1, 2, 3, 5, 8, 13, 21, 34]
# return the nth fibonacci number
def fibonacci(number):
    if number < 0:
        print("Negative numbers are not valid")
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(6))
