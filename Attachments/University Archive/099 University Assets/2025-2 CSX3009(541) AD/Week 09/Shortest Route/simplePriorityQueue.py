'''
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the priority queue instantiation
'''

class Simple_Priority_Queue:
    def compare(x, y):  # a default compare function for min heap
        return x < y
    
    def __init__(self, cmp=compare):
        self.a = []
        self.cmp = cmp
        
    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < len(self.a) and self.cmp(self.a[l],self.a[i]):
            largest = l
        else:
            largest = i
        if r < len(self.a) and self.cmp(self.a[r],self.a[largest]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
        
    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a)-1
        j = (i-1)//2
        while i > 0 and self.cmp(self.a[i],self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)//2

    def dequeue(self):
        x = self.a[0]
        last = len(self.a)-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        del self.a[last]
        self.heapify(0)
        return x



