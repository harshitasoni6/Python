class user:
    def __init__(self,name,id,age,password):
        self.name = name
        self.id = id
        self.age = age
        self.__password = password

    def login(self,passkey):
        if passkey == self.__password:
            print("Login Successful")
        else:
            print("Invalid user or incorrect password.")

    def logout(self):
        print("logout")


class student(user):
    def __init__(self,name,id,rollNo,password,mark,age):
        super().__init__(name,id,age,password)
        self.rollNo = rollNo
        self.mark = mark
    def login(self,passkey):
        print("OTP sent!")
        super().login(passkey)


s1 = student("Harshita",1,6,6666,100,25)
s1.login(6666)
s1.password = 9999
print(s1.password)
