#compile polymorphism
#method 1

# class sum:
#     def add(self,a,b=0,c=0,d=0):
#         return a + b + c + d
    
# obj1 = sum()
# obj2 = sum()
# obj3 = sum()

# print(obj1.add(2,3,4))
# print(obj2.add(2,3,4,1))
# print(obj3.add(2,2,2))

#method2

class sum:
    def add(self,*args):
        s = 0
        for i in args:
            s += i

        return s
    
obj1 = sum()
obj2 = sum()
obj3 = sum()

print(obj1.add(2,3,4))
print(obj2.add(2,3,4,1))
print(obj3.add(2,2,2))
