class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in str(key):
            h += ord(char)
        return h%self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                break
        self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                return element[1]
            
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    

t = HashTable()
t['march 1']= 654
t['march 2']= 124
t['march 3']= 800
t['march 4']= 541
t['march 5']= 879
t['march 6']= 435
t['march 17']= 900
print(t['march 17'])