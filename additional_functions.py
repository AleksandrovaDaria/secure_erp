class Random:
    def __init__(self, seed=1):
        self.seed = seed
        
    def randint(self, a, b):
        self.seed = (self.seed * 1103515245 + 12345) % (2**31)
        return self.seed % (b - a + 1) + a
    
    def random(self):
        self.seed = (self.seed * 1103515245 + 12345) % (2**31)
        return self.seed / 2**31
# add class datetime and timedelta
