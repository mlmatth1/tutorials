import timeit

def method():
    out_str = ''
    for num in xrange(20):
        out_str += `num`
    return out_str

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("method()", setup="from __main__ import method"))
    print method()
