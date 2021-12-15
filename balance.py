def balance(left, right):
    """
    Each exclamation mark's weight is 2; each question mark's weight is 3. 
    Putting two strings left and right on the balance - are they balanced?

    If the left side is more heavy, return "Left"; if the right side is more 
    heavy, return "Right"; if they are balanced, return "Balance". E.G...
    "!!", "??"     -->  "Right"
    "!??", "?!!"   -->  "Left"
    "!?!!", "?!?"  -->  "Left"
    "!!???!????", "??!!?!!!!!!!"  -->  "Balance"
    """
    # Define a function which returns the score of the list based on num of 
    # Exclamation Marks or Question marks.
    def charCount(lst):
        # Store our totals here..
        excTotal = 0
        questTotal = 0
        # For each char in the lst...
        for char in lst:
            # Add respective scores dependant on if ! or ?
            if char == "!":
                excTotal += 2
            elif char == "?":
                questTotal += 3
        # Return the total of the two added...
        return excTotal + questTotal
    # Return Left, Right or Balance dependant on which one has
    # the higher score...
    if charCount(left) > charCount(right):
        return "Left"
    elif charCount(right) > charCount(left):
        return "Right"
    else:
        return "Balance"

print(balance("!!", "??")) # Right
print(balance("!??", "?!!")) # Left
print(balance("!?!!", "?!?")) # Left
print(balance("!!???!????", "??!!?!!!!!!!")) # Balance
print(balance("!!", "??")) # Right

