# Method 1
'''
def even(a):
    return a % 2 == 0
numbers = [1,2,3,4,5,6,7]
ans = list(filter(even,numbers))
print(ans)
'''


# Method 2
'''
numbers = [1,2,3,4,5,6,7]
ans = list(filter(lambda a : a % 2 == 0,numbers))
print(ans)
'''

# Method 3
ans = list(filter(lambda a : a % 2 == 0,range(1,11)))
print(ans)