import re
import string

def pig_it(text):
    """
    Move the first letter of each word to the end of it, then add "ay" to 
    the end of the word. Leave punctuation marks untouched.
    """
    # First we split our string into words in a list
    textList = re.split('\s+', text)
    # We will store our list of pig latin words here.
    pigLatin = []
    for i in textList:
        # First we check if we are dealing with punctuation, in which case, 
        # we simply append the punctuation to pigLatin list without any additions.
        if i in string.punctuation:
            pigLatin.append(i)
        else:
            # For each element in textList append to pigLatin the word minus the 1st
            # char + the first char (at the end) + the string 'ay'
            pigLatin.append(i[1:] + i[0] + 'ay')
    # Return the joined list as a string.
    return ' '.join(pigLatin)

print(pig_it("Pig Latin is cool!"))