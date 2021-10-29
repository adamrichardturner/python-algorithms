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
    # We store our parenthesis in order, stripped of anything else in the string.
    paren = []
    # We keep our stack here, it should be empty if the paranthesis are valid.
    stack = []
    # Appending only parenthesis to the paren variable.
    for char in string:
        if '(' in char or ')' in char:
            paren.append(char)
    for char in paren:
        # If open parenthesis, push ontop the stack.
        if char == '(':
            stack.append(char)
        else:
        # If other, check if stack is empty return False.
            if not stack:
                return False
            # If not empty, store last index of stack in top.
            else:
                top = stack[-1]
            # If the next char is closing and top is opening, pop
            # last char off the stack.
                if char == ')' and top == '(':
                    stack.pop()
    # Final test, check if stack is empty or not. If empty return True, else False.
    if not stack:
        return True
    else:
        return False

print(valid_parentheses("()")) # True
print(valid_parentheses(")(()))")) # False
print(valid_parentheses("(")) # False
print(valid_parentheses("(())((()())())")) # True