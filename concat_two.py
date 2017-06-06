import timeit

loop_count = 20000
#Naive appending
# 1.8 secs
def method():
    out_str = ''
    for num in xrange(loop_count):
        out_str += `num`
    return out_str
#MutableString class
#2 seconds
def method2():
    from UserString import MutableString
    out_str = MutableString()
    for num in xrange(loop_count):
        out_str += `num`
    return out_str
#Character arrays
#6 seconds
def method3():
    from array import array
    char_array = array('c')
    for num in xrange(loop_count):
        char_array.fromstring(`num`)
    return char_array.tostring()
#Build a list of strings, then join it
# 3.01 seconds
def method4():
    str_list = []
    for num in xrange(loop_count):
        str_list.append(`num`)
    return ''.join(str_list)

# Write to a pseudo file
# 6.94 seconds
def method5():
    from cStringIO import StringIO
    file_str = StringIO()
    for num in xrange(loop_count):
        file_str.write(`num`)
    return file_str.getvalue()
#List comprehensions
#1.94 seconds
def method6():
    return ''.join([`num` for num in xrange(loop_count)])
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("method()", setup="from __main__ import method"))
    print method()
