# We need to create a function that takes in the string as a parameter
# We need to initialize a dictionary
# We need to initialize a counter variable
# We need to iterate the string and count characters - maybe a method
# we need to find the first character with the value of 1
#
def non_repeat(word):
    ch = dict()
    for i in word:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1

    found = find_char(ch, word)
    return found
    
def find_char(chars, word):
    for i in word:
        if chars.get(i, 0) == 1:
            return i
        
print non_repeat('MMorning')
