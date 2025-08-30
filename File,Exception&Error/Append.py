f = open('Append.txt','a')
a_f = f.write("\nHello! will print the above text.")
print(a_f)
f.close()

f = open('Append.txt','r')
r = f.read()
print(r)
f.close()