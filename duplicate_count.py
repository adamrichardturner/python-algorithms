def duplicate_count(text):
    """
    Write a function that will return the count of distinct case-insensitive alphabetic 
    characters and numeric digits that occur more than once in the input string. The input 
    string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric 
    digits.
    """
    # Your code goes here
    # We will append our duplicates with this list.
    duplicates = []
    for char in text.lower():
        # text.count(char) returns the # of times a char appears in the string.
        if text.lower().count(char) > 1:
            if char not in duplicates:
                # append to the list the char if it hasn't already been listed as a duplicate.
                duplicates.append(char)
    # return the length of the duplicates list, this provides summary of num of duplicates
    return len(duplicates)


print(duplicate_count("abcdeaB")) # Outputs 2