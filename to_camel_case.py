# Complete the method/function so that it converts dash/underscore delimited
# words into camel casing. The first word within the output should be
# capitalized only if the original word was capitalized..
# (known as upper Camel Case, also often referred to as Pascal Case)

def to_camel_case(text):
    # strSpaced will contain our string manipulated to replace the chars
    # dash or underscore with a space character. We do this so that we 
    # can capitalize the word (that method uses the spaces to determine 
    # where words are..)
    strSpaced = ''
    # camel will contain our final camel case string.
    camel = ''
    # Sanitize input first, if the string is empty we simply return it.
    if len(text) <= 0:
        return text
    # Check next if the word is capitalized, if so loop through each char
    # in the string. If the char is a - or _, replace with a blank space.
    elif text[0].isupper():
        for char in text:
            if char == '-':
                strSpaced += ' '
            elif char == '_':
                strSpaced += ' '
            else:
                strSpaced += char
        # We replaced the necessary chars with spaces so that we could then
        # capitalize the word. In this condition (the word was already ...
        # capitalized) we make all words capitalized and replace the spaces
        # with no-spaces.
        camel = strSpaced.title()
        return camel.replace(' ', '')
    else:
        # In this condition the word was not already capitalized. We check
        # again for - or _, replace with spaces. Capitalize the word with the
        # title method, then return the first char lower case + the rest of 
        # the correctly capitalized string.
        for char in text:
            if char == '-' or char == '_':
                strSpaced += ' '
            else:
                strSpaced += char
        camel = strSpaced.title()
        camel = camel.replace(' ', '')
        return camel[0].lower() + camel[1:]

print(to_camel_case("")) # Prints nothing
print(to_camel_case("The_Cat_Is-cute")) # Prints "TheCatIsCute"
print(to_camel_case("The_Stealth_Warrior")) # Prints "TheStealthWarrior"
print(to_camel_case("the-stealth-warrior")) # Prints "theStealthWarrior"
    