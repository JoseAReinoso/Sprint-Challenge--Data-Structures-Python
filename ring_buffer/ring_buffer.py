class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.present = 0

    def append(self, item):
        if len(self.cache) < self.capacity:
            self.cache.append(item)
            
        else:
            
            self.cache[self.present] = item
            self.present += 1

             
        #this will reset the index back to 0 after code on top runs
        if self.present == self.capacity:
            self.present = 0
    


    def get(self):
        return self.cache