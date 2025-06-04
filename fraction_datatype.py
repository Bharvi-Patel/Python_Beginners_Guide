# creating our own function datatype

class Fraction:
    def __init__(self,n,d):
        self.n = n
        self.d = d

    def __str__(self):
        return "{}/{}".format(self.n,self.d)
        #  __str__ = automatically call hota hai jab bhi apne class ke object ko print function ke andar daalta hai

    def __add__(self,other):
        tem_n = self.n * other.d + other.n * self.d
        tem_d = self.d * other.d
        return "{}/{}".format(tem_n,tem_d)
    
    def __sub__(self,other):
        tem_n = self.n * other.d - other.n * self.d
        tem_d = self.d * other.d
        return "{}/{}".format(tem_n,tem_d)

    def __mul__(self,other):
        tem_n = self.n * other.n
        tem_d = self.d * other.d
        return "{}/{}".format(tem_n,tem_d)

    def __truediv__(self,other):
        tem_n = self.n * other.d
        tem_d = self.d * other.n
        return "{}/{}".format(tem_n,tem_d)



s=Fraction(5,6)
t=Fraction(7,5)
print(s)
print(t)
print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(type(s))