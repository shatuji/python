class Calculator():
    name = 'this is my calculator'
    price = 10
    def __init__(self,name,price,length,colour):
        self.name = name
        self.price = price
        self.le = length
        self.co = colour
    def add(self,x,y):
        print(self)
        result = x+y
        print(result)
    def minus(self , x ,y):
        result = x - y
        print(result)



