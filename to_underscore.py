def to_underscore(string):
    """
    Complete the function/method so that it takes a PascalCase 
    string and returns the string in snake_case notation. 
    Lowercase characters can be numbers. If the method gets 
    a number as input, it should return a string.

    E.G

    "TestController"  -->  "test_controller"
    "MoviesAndBooks"  -->  "movies_and_books"
    "App7Test"        -->  "app7_test"
    1                 -->  "1"
    """
    # We will store a list of chars here...
    snake = []
    # If the input is an int, return it as a string...
    if isinstance(string, int):
        return str(string)
    else:
        # For each index, char enumerate string...
        for index, char in enumerate(string):
            # If char is numeric...
            if char.isnumeric():
                # Insert the char
                snake.insert(index, char)
                # Elif char is upper case, concat '_' with lower case
                # version of char 
            elif char.isupper():
                snake.insert(index, '_' + char.lower())
            else:
                # Insert all other chars at correct index...
                snake.insert(index, char)
    # Here we we convert the snake list back to a string...
    clean = ''.join(snake)
    # And return it less the first char '_'
    return clean[0:][1:]

print(to_underscore("My3CodeIs4TimesBetter")) # test_controller
print(to_underscore("MoviesAndBooks")) # movies_and_books
print(to_underscore("App7Test"))# app7_test
print(to_underscore(1)) # 1