# n1
"""
class Person:

    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    def showinfo(self):
        print(f"name: {self.name}, surname: {self.surname}, age: {self.age}")

userName = input("Enter your name:\t")
userSurname= input("Enter your surname:\t")
userAge = int(input("Enter your age:\t"))
user=Person(userName,userSurname,userAge)
user.showinfo()
"""

# n2
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def showinfo(self):
        P=self.width+self.width+self.height+self.height
        S=self.width*self.height
        print(f"P:{P},S:{S}")

userWid = int(input("Enter rectangle width:\t"))
userHei = int(input("Enter rectangle height:\t"))
obj=Rectangle(userWid,userHei)
obj.showinfo()

