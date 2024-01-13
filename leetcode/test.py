class abc:
    def __init__(self):
        
        self.d = 5

    def a(self, l):
        def x(z):
            print(self.d)
            return z
        print(l)

s = abc()
print(s.x(5))
    