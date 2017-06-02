def test(string):
    
    for idx, string in enumerate(string):
        print idx
       # print string[idx]
    
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test('HiIhavealotofspaces!')", setup="from __main__ import test"))
    

