import re
pattern = "apple"
if re.search(pattern,"appleball") :
    print("True")
else:
    print("False")
if re.search(pattern,"ballapple") :
    print("True")
else:
    print("False")

#search character in the string