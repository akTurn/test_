#Creating class Employee
class Employee:

    #defining constructor
    def __int__(self,emp_no,emp_name,emp_basic):
        self.emp_no = empt_no
        self.emp_name = emp_name
        self.emp_phone = emp_phone

#Asking user to input details
emp_no = input("Enter the number ")
emp_name = input("Enter your name ")
emp_basic = input("Enter Basic description ")

e = Employee()

#store details in emp.txt file
fo = open("emp.txt", "w")
fo.write("No {}\nName {}\nBasic {}\n ".format(emp_no,emp_name,emp_basic))
fo.close()


#Reading details from emp.txt file and displaying
fo = open("emp.txt", "r+")
str = fo.read()
print(str)
