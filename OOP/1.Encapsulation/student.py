# # Method 1
# class student:
#     def __init__(self,name = None,rollNo = None,marks = None):
#         self.name = name
#         self.rollNo = rollNo
#         self.marks = marks

# s1 = student()
# s1.name = "Mayank"
# s1.rollNo = 34
# s1.marks = 60

# print("Details of s1: ",s1.name,s1.rollNo,s1.marks)


# Method 2 
# in this we have to pass arguments 
# if we don't pass while creating object 
# write None in argument so that it would not through error.

class student:
    __noOfStudent = 0
    __schoolName = "APS"
    def __init__(self,name ,rollNo ,marks):
        self.name = name
        self.rollNo = rollNo
        self.__marks = marks   #private variable
        student.__noOfStudent += 1

    @classmethod
    def __auth(cls):
        return "0000"
    #getter
    def getMarks(self):
        return self.__marks
    # #setter
    # def setMarks(self,newMarks):
    #     self.__marks = newMarks
    # if we modify above setter method
    # to make it more secure so that no can change data until 
    # he/she don't have password like insta,facebook acoount
    #setter with sercurity
    def setMarks(self,newMarks,password):
        if password == self.__auth():
            self.__marks = newMarks
            return "Information Updated."
        else:
            return "Not a valid user or incorrect password."
       
    #we can access with both class name and also with object 
    # otherwise we have define two get one with no argument 
    # and another one with self.
    # logically think schools is name for all student 
    # if we don't have object we should we able to see school name.
    @staticmethod 
    def getTotalStudent():
        return  student.__noOfStudent
    
    @staticmethod
    def getSchoolName():
        return  student.__schoolName
    
    @classmethod
    def setSchoolName(cls,newSchoolName,password):
        if password == cls.__auth():
            student.__schoolName = newSchoolName
            return "Information Updated."
        else:
            return "Not a valid user or incorrect password."
    
    # Methods
    def study(self):
        print("This is study time for " + self.name)
    def play(self):
        print("Don't play it's study time!" + self.name)


s1 = student("mayank",34,90)
s2 = student("shivay",35,80)
s3 = student("shiv",36,100)
s4 = student("ayan",37,40)
s5 = student("vinay",38,90)
print("Details of s2: ",s2.name,s2.rollNo,s2.getMarks())
print(s2.setMarks(85,'0001'))
print("Details of s2: ",s2.name,s2.rollNo,s2.getMarks())
print(s4.getTotalStudent())
print(student.getSchoolName())
print(student.setSchoolName("NSIT","0000"))
# student.__schoolName = "BKD" #we are not able to access.k
print(student.getSchoolName())
s2.study()
s2.play()
