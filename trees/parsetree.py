from stack import Stack
from trees import BinaryTree
import operator

''' Parse trees are a tree type structure that are used to analyze strings '''


def parse_tree(expr):
    tokens = expr.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    curr = tree

    for i in tokens:
        if i == '(':
            curr.insert_left('')
            stack.push(curr)
            curr = curr.get_left_child()

        elif i in '+-*/':
            curr.set_root(i)
            curr.insert_right('')
            stack.push(curr)
            curr = curr.get_right_child()

        elif i == ')':
            curr = stack.pop()

        else:
            try:
                curr.set_root(int(i))
                parent = stack.pop()
                curr = parent

            except ValueError:
                raise ValueError('Not an integer')

    return tree


def evaluate(tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        f = operators[tree.get_root()]
        return f(evaluate(left), evaluate(right))
    else:
        return tree.get_root()
