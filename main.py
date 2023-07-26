class Calculate:
    
#     def add(self,a,b): 
#         return a +b ,"adding two numbers"
#     def add(self,a,b,c):
#         return a * b *c  ,"multiplying three numbers"
    
    def add(self,a,b,c=0):
        if c ==0:
            return a+b , "adding two numbers, you given c =0"
        else:
            return a * b * c , "mutiplying three numbers , got three values"
        

### Example of method overriding

class Animal:
    def walk(self):
        print("this is  parent class and walk method")
        
class Dog(Animal):
    def walk(self):
        print("this is child class")


class MyVsCode:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def vscodemethod(self):
        print("my first vs code testing")

    def method2(self):
        print("method2" , self.a, self.b)


def myfirstmodule(x,y):
    if x == 1:
        print(x + y)
    else:
        print("please provide number")