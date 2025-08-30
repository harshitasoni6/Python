f = open('Write.txt','w')
w = f.write('Using this write mode,\nyou can write in the file.\nIf there is some existing it will over write the content.')
print(w) # no of character
f.close()

f = open('Write.txt','r')
r = f.read()
print(r)
f.close()