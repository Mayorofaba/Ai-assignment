# store my fullname in a variable
MyName = "Nwabuko Micheal Chinedu"
MyFirstName = "Nwabuko"

FirstNameLen = len(MyFirstName)
StoreShiftedName = ""
for x in MyName:
    # is the character an alphabet?
    if x.isalpha():
    # shift the character by the ShiftInterval by using ord() to covert the character to its ASCII value,
    # perform the shift, and then convert it back to a character using chr()
    #note a = 97 in ascii which is the starting point of the alphabet.
        shifted_char = chr((ord(x.lower()) - ord('a') + FirstNameLen) % 26 + ord('a'))
        if x.isupper():
            shifted_char = shifted_char.upper()
        StoreShiftedName += shifted_char
    else:
        StoreShiftedName += x
print(StoreShiftedName)