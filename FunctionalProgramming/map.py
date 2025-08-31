# # Method 1

# def sqr(a):
#     return a * a
# numbers = [1,2,3,4,5,6,7]
# ans = list(map(sqr,numbers))
# print(ans)


# # Method 2

# numbers = [1,2,3,4,5,6,7]
# ans = list(map(lambda a : a ** 2,numbers))
# print(ans)


# # Method 3
# ans = list(map(lambda a : a ** 2,range(1,11)))
# print(ans)

# Method 4
# difference between map and filter, 
# if we try to check even no.,
# filter will return element which are even 
# whereas map will give true false in output
ans = list(map(lambda a : a % 2 == 0,range(1,11)))
print(ans)