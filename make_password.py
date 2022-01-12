def make_password(phrase):
    """
    One suggestion to build a satisfactory password is to start with a memorable phrase 
    or sentence and make a password by extracting the first letter of each word.

    Even better is to replace some of those letters with numbers (e.g., the letter O can 
    be replaced with the number 0):

    instead of including i or I put the number 1 in the password;
    instead of including o or O put the number 0 in the password;
    instead of including s or S put the number 5 in the password.
    Examples:
    "Give me liberty or give me death"  --> "Gml0gmd"
    "Keep Calm and Carry On"            --> "KCaC0"
    """
    words = phrase.split(' ')
    pword = ''
    for char in words:
        if char[0] == 'i' or char[0] == 'I':
            pword += '1'
        elif char[0] == 'o' or char[0] == 'O':
            pword += '0'
        elif char[0] == 's' or char[0] == 'S':
            pword += '5'
        else:
            pword += char[0]
    return pword
    
print(make_password("Give me liberty or give me death")) # Gml0gmd
print(make_password("Keep Calm and Carry On")) # KCaC0