# l = [i for i in range(1,11)]
# iteration = iter(l)
# for i in l:
#     print(iteration.__next__()) # Only print one element at once.


l = [i for i in range(1,11)]
iteration = iter(l)
for i in l:
    print(next(iteration)) # Only print one element at once.