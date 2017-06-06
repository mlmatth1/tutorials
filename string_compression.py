class Compress:
    def __init__(self, str_arg):
        self.str_arg = str_arg
        
    def count(self, arg):
        str_list = []
        countConsecutive = 0
        str_len = len(arg)
        for i in xrange(0, str_len):
            countConsecutive = countConsecutive + 1
            if(i + 1 >= str_len or arg[i] is not arg[i + 1]):
                str_list.append(arg[i])
                str_list.append(countConsecutive)
                countConsecutive = 0

        return ''.join([str(x) for x in str_list])

if __name__ == '__main__':
    t = Compress('aabcccccaa')
    b = t.count('aabcccccaa')
    print b
