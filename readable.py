def readable(phoneNum):
    """
    Validates and formats a phone number into a readable form with
    brackets and hyphens to deleniate parts of the number.

    Params: phoneNum(string) which should be 10 digits long...

    Returns: The 10 digit phone number in a more readable form, e.g.
    (415)555-1212
    """
    # Validate the phone number, if not 10 digits in length...
    if len(phoneNum) != 10:
        # Print error...
        print("Phone number must be 10 digit long")
    # Validate numbers have been entered, if not decimal numbers...
    elif not phoneNum.isdecimal():
        # Print error...
        print("Input must be all digits")
    # Format the phone number using string slicing to be more readable, separating
    # digits of the phone number with brackets and hyphen.
    else:
        return "(" + phoneNum[:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:]

print(readable("4155551212")) # (415)555-1212
print(readable("5656391452")) # (565)639-1452
print(readable("5307343711")) # (530)734-3711
print(readable("41555451212")) # Phone number must be 10 digit long