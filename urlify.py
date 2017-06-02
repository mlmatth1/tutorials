#name = "Mr John Smith"
#name = name.split()
#url_name = "%20".join(name)

#print url_name

#Brute Force
class urlify(object):
    def __init__(self, name):
        self.name = name
    def urlify_b(self):
        if not self.name:
            raise ValueError('could not find any data in name')
        lst = []
        name = self.name.strip()
        print name
        for i in name:
            if i == ' ':
                lst.append('%20')
            else:
                lst.append(i)
        name = ''.join(lst)
        return name
    def urlify_o(self):
        return "%20".join(self.name.split())
    #Books Solution
    def replace_spaces(self):
        name = self.name[:]
        space_count = 0
        index = 0
        
        for i in name:
            print i
                

urlify = urlify("Mr John smith  ")
urlify.replace_spaces()
print urlify.urlify_b()
print urlify.urlify_o()
