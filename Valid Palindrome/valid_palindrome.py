def isPalindrome(self, s):
    lowerText = s.lower()
    print(lowerText)

    new = ''.join(char for char in lowerText if char not in string.punctuation)
    print(new)

    spacesRemoved = ''.join(new.split())
    print(spacesRemoved)

    if spacesRemoved == spacesRemoved[::-1]:
        return True
    else:
        return False
    
# idea is to first make the string to lower case and then join the string with various cases like,
    # if the chat is not a punchuvation mark
    # by removing white spaces
# so we left with a clear string and then we need to check the reverse one is same as the original one. 
# for that we include this line "if spacesRemoved == spacesRemoved[::-1]:"
#  time complexity is O(n). and can be improved more.