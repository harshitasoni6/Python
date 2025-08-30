f = open('ReadWriteMode.txt','r+')
w = f.write("Now this is r+ mode which will read - write both.")
f.close()

f = open('ReadWriteMode.txt','r+')
r = f.read()
print(r)
f.close()