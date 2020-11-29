class Some:
    def __init__(self, x):
        self.x = x
    
    def service(self, y):
        print('do service...', self.x + y)

class Other:
    pass

o = Other()
o.x = 100
print(Some.service(o, 200))    # do service... 25
