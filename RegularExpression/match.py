import re
pattern = "apple"
if re.match(pattern,"appleball") :
    print("True")
else:
    print("False")
if re.match(pattern,"ballapple") :
    print("True")
else:
    print("False")

#only match first starting character
