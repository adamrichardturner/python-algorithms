def valid_parentheses(string):
    """
    Write a function that takes a string of parentheses, and determines if 
    the order of the parentheses is valid. The function should return true 
    if the string is valid, and false if it's invalid.
    E.G
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
    Note:
    Along with opening (() and closing ()) parenthesis, input may contain any 
    valid ASCII characters. Furthermore, the input string may be empty and/or 
    not contain any parentheses at all. Do not treat other forms of brackets as 
    parentheses (e.g. [], {}, <>).
    """

    # Empty Stack
    stack = []
    for char in string:
        # If open parenthesis, push ontop the stack.
        if char == '(':
            stack.append(char)
        else:
        # If other, check if stack is empty return False
            if not stack:
                return False
            # If not empty, store last index of stack in top
            else:
                top = stack[-1]
            # If the next char is closing and top is opening, pop
            # last char off the stack.
                if char == ')' and top == '(':
                    stack.pop()
    # If stack is empty, we have valid parenthesis, otherwise False.
    if not stack:
        return True
    else:
        return False

print(valid_parentheses("((hello()))"))