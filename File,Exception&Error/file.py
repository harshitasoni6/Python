# import os

# # Get the folder where file.py is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)

# import os
# print(os.getcwd())  # Shows current working directory

# f = open(r'C:\\Users\\sonih\\OneDrive\\Documents\\Python\\TuteDude\\Python\\File,Exception&Error\\File.txt','r') 
# f = open('file.txt', 'r')
# read_f = f.read()
# read_f = f.read(6)  #we can also specify no. of character in f.read(no_of_character) output will be the that no of character from file.txt 
#print(read_f)

# read_l = f.readline()
# print(read_l)

# read_ls = f.readlines()
# print(read_ls)


# f.close()

with open('file.txt','r') as f:
    read_l = f.read()
    print(read_l)
