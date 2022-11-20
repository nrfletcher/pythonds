# Recursion is the act of solving problems by breaking them down into smaller problems until reaching a base case
# We then recursively (function calling itself) iterate through steps of the solution until reaching said base case
from stack import  Stack


def recursive_sum(n):
    # Our base case is 1, since that is the starting value for our sequence summation
    if n == 1:
        return 1
    # Our total sum will be our original n, plus all other values following (n - 1)
    return n + recursive_sum(n - 1)


# Same result, different implementation
def recursive_sum_list(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + recursive_sum_list(nums[1:])


# Similar logic, for products instead
def factorial(n):
    if n <= 2:
        return n
    return n * factorial(n - 1)


# Base case is 1, after that we add the value before and the value before it until reaching 1
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Sum of each digit added together. Base case is the first digit, then we recursively iterate each character after [1:]
def sum_digits(n):
    s = str(n)
    if len(s) == 1:
        return int(n)
    return int(s[0]) + sum_digits(s[1:])


# Floor division to get remainder and append each piece of the new representation to the first piece
def base_conversion(n, base):
    values = "0123456789ABCDEF"
    if n < base:
        return values[n]
    else:
        return base_conversion(n//base, base) + values[n % base]


def stack_conversion(n, base):
    stack = Stack()

    values = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            stack.push(values[n])
        else:
            stack.push(values[n % base])
        n = n // base
    res = ''
    while not stack.is_empty():
        res += str(stack.pop())
    return res


def reverse_string(s):
    if len(s) == 1:
        return s[0]
    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
    # A convenient and Pythonic one liner solution is in fact just: return s == s[::-1]


def power(base, exponent):
    if exponent == 1:
        return base * 1
    if exponent == 2:
        return base * base
    return base * power(base, exponent - 1)


def tower_of_hanoi(height, from_pole, to_pole, with_pole):
    def move_disk(fp, tp, h):
        print('Moving disk', h, 'from', fp, 'to', tp)
    if height > 0:
        tower_of_hanoi(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, with_pole, height)
        tower_of_hanoi(height - 1, to_pole, from_pole, with_pole)


def recursive_reverse_list(lst):
    if len(lst) == 1:
        return [lst[0]]
    return [lst[len(lst)-1]] + recursive_reverse_list(lst[:-1])


# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

