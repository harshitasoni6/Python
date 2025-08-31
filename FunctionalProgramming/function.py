# def add(i,j):
#     return i+j 
# a = add # we can initialise variable with fuction name.
# res = a(1,3)
# print(res)

def add(i,j):
    return i+j 

def call(i,j):
    return add(i,j)

def pas(i,j,fn):   # we can pass function as argument
    return fn(i,j)

res = pas(1,2,call)

print(res)
