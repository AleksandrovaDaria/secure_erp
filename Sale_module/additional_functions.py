class Random:
    def __init__(self, seed=1):
        self.seed = seed
        
    def randint(self, a, b):
        self.seed = (self.seed * 1103515245 + 12345) % (2**31)
        return self.seed % (b - a + 1) + a
    
    def random(self):
        self.seed = (self.seed * 1103515245 + 12345) % (2**31)
        return self.seed / 2**31

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
    
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    
class DateTime:
    def __init__(self, year, month, day, hour, minute, second):
        self.date = Date(year, month, day)
        self.time = Time(hour, minute, second)
        
    def __str__(self):
        return f"{self.date} {self.time}"
    
class TimeDelta:
    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        self.total_seconds = ((days * 24 * 60 * 60) + (seconds + (microseconds / 1000000) + (milliseconds / 1000)) + (minutes * 60) + (hours * 60 * 60) + (weeks * 7 * 24 * 60 * 60))
        
    def __str__(self):
        hours, remainder = divmod(self.total_seconds, 60 * 60)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes}:{seconds}"
