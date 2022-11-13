# Stack data structure
# Very useful for algorithms which require a memory of the order in which values were dealt with
# Text processing, memory, and math evaluations (Polish and reverse Polish)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Utilize the stack structure to reverse a string
def reverse_string(s):
    stack = Stack()
    for i in s:
        stack.push(i)

    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()

    return reverse


# Balanced parentheses problem
def proper_parentheses(s):
    curr = Stack()
    for i in s:
        if i == '(':
            curr.push(i)
        elif curr.size() >= 1:
            curr.pop()
        else:
            return False

    return curr.is_empty()


def other_parentheses(s):
    s = Stack()
    balanced = True
    index = 0
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


# For a more general case of different types of brackets, we can either use a helper function or a hashmap
def balanced_brackets(s):
    def matches(open, close):
        opens = "([{"
        closes = "}])"
        return opens.index(open) == closes.index(close)

    stack = Stack()
    balanced = True
    index = 0
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol in "[{(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


# Divide by 2 algorithm for converting decimal value to binary
def decimal_to_binary(dec):
    s = Stack()

    while dec > 0:
        rem = dec % 2
        s.push(rem)
        dec = dec // 2

    bin_string = ""
    while not s.is_empty():
        bin_string = bin_string + str(s.pop())

    return int(bin_string)


# Treating our modulo value as a variable and adding support for hexadecimal we can do any base conversion to 16
def decimal_to_base(number, base):
    digits = "0123456789ABCDEF"
    s = Stack()

    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base

    new_base = ""
    while not s.is_empty():
        new_base = new_base + digits[s.pop()]

    return new_base


# Infix notation to postfix notation conversion (reverse Polish)
def infix_to_postfix(infix):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    op_stack = Stack()
    post_fix_list = []
    token_list = infix.split()

    for token in token_list:
        # Variables simply get added to our new expression
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWQYZ' or token in '1234567890':
            post_fix_list.append(token)
        # If we see an opening brace, add it
        elif token == '(':
            op_stack.push(token)
        # If we see a closing brace, we pop all current operations within that same level of precedence via parentheses
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                post_fix_list.append(top_token)
                top_token = op_stack.pop()
        # If an operation, before pushing the new operation, pop all current operations with higher precedence first
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                post_fix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        post_fix_list.append(op_stack.pop())
    return ' '.join(post_fix_list)


# Postfix conversion to infix value (post -> in)
def postfix_to_infix(postfix):
    def do_operation(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

    op_stack = Stack()
    token_list = postfix.split()

    for token in token_list:
        if token in '1234567890':
            op_stack.push(int(token))
        else:
            # Since we are dealing with a stack, the order is reverse of the infix notation
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            result = do_operation(token, op1, op2)
            # Add our resultant back to the stack
            op_stack.push(result)
    # Our single remaining value is our infix result
    return op_stack.pop()
