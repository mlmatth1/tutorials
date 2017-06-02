def test(string):
    """Stupid test function"""
    ' '.join(string.split())
    #L = []
    #for i in range(100):
    #    L.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test('Hi   I have   a    lot of spaces!')", setup="from __main__ import test"))
    

#class RemoveSpaces(object):
#    def __init__(self, string):
#        print timeit.timeit(' '.join(string.split()))

#    def print_string(self):
#        print self.string

#space = RemoveSpaces("Hi   I have   a    lot of spaces!")
