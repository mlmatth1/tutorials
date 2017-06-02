class FindDuplicateCharacters(object):
    def __init__(self, word):
        self.word = word

    def printDuplicateCharacters(self):
        characters = {}
        
        
        for i in self.word:
            dup_counter = 0
            if i in characters.keys():
                my_p = characters.get(key, default=None)
                print my_p
                counter += 1
                characters[i] = counter
            else:
                counter += 1
                characters[i] = counter
                
        return characters
if __name__ == '__main__':
    mark = FindDuplicateCharacters('Programming')
    print mark.printDuplicateCharacters()

