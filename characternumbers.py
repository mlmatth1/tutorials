def get_char_number(c):
    a = ord('a')
    print a
    z = ord('z')
    print z
    val = ord(c)
    print val
    if val >= a and val <= z:
        return val - a
    return -1

print get_char_number("-")
    
