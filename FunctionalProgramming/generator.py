# def fn():
#     yield 1
#     yield 2
#     yield 3
# value = fn()
# # print(value.__next__()) #print only one

# for i in value:
#     print(i)

def sqr():
    n = 1
    while n <= 5:
        s = n ** 2
        yield s
        n += 1

values = sqr()
for i in values:
    print(i)

