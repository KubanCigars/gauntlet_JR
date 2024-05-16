"""

Task 1: My "Hello World"
Description: Ask the user to input two numbers
            Return the sum of the numbers IF the former > the latter

"""



num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1 > num2:
    sum_numbers=num1+num2
    print(sum_numbers)




"""

Task 2: Fruit Loops
Description: Write a function that takes any number of number imputs, meaning integer and float types,
            return the max value of these numbers
            the code must exit the loop if the number input is 0


"""
input_num = input("Enter the number")
max_list = []

while input_num != "0":
    max_list.append(round(float(input_num)))
    input_num = input("Enter the number")
print(max_list)


"""

Task 3
Description: Introduction to functions
            Create a function that takes two integer inputs
            return the power of each so x**y and y**x

"""

def power(x,y):
    num1= x**y
    num2= y**x
    return(num1,num2)

x = int(input("Enter number: "))
y = int(input("Enter number: "))

power1,power2 = power(x,y)
print(power1,power2)

"""

Task 4: File Handling
Description: Learn how to:
            Create a file
            Write to a file
            Read a file
            Append to a file


"""

files = open("text.txt","wt")
files.write("Hello World")
files.close()
files = open("text.txt","a")
"""
.write method is used for both appending and writing a new file :)
also remember to close the file if its going to perform a new operation on it

"""

files.write("Goodbye World")
files.close()
files = open("text.txt","rt")
print(files.read())

"""

Task 5: Classes
Description: Make a class named "Person"
            This person will have a name and age variable
            Case Sensitive
            Add a function for setting the age of the person
            Add a function for getting the name of the person

"""
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return(print("The person's name is" + self._name))
    
    def get_age(self):
        return (print("The person's age is" + str(self._age)))

person_1 = Person("Harry", 15)
person_1.get_name()
person_1.get_age()

"""

Task 999: Calculator

"""