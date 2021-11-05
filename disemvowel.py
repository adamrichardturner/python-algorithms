import re

def disemvowel(string_):
    """
    Write a function that takes a string and return a new string
    with all the vowels removed.
    For example, the string "This website is for losers LOL!" would 
    become "Ths wbst s fr lsrs LL!".
    """
    # Use regex to split the string into a list of chars without the 
    # vowels.
    noVowel = re.split(r'a|A|e|E|i|I|o|O|u|U', string_)
    # Join the char list as a string and return it.
    return ''.join(noVowel)

print(disemvowel("This website is for losers LOL!")) # Outputs Ths wbst s fr lsrs LL!