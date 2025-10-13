class Parent:
    # 1. Global variables
    num1 = 100
    counter =1

    # 2. Defining Constructors, summing and printing 2 numbers
    def __init__(self, a, b):
        print(f"Executing Default constructor of obj{Parent.counter} ..")  # 1st statement to get execute after object creation
        self.firstNum = a
        self.secondNum = b
        print(f"Sum of 2 nos : {self.firstNum}+{self.secondNum} = {self.firstNum+self.secondNum}")

    # 3. print method
    def methodPrint(self):
        print(f"Print method is executed using Obj{Parent.counter}")

    # 4. Summation using 2 instance variable of constructor and 1 global variable
    def summation(self, a, b, c):
            return a+b+c

    # 5. Object creation, Passing argument to the constructor    ---> There is no need to pass self for constructor
obj1 = Parent(99, 99)
Parent.counter+=1
obj2 = Parent(20,20)
Parent.counter = 1
    # 6. Printing global variable
print(f"Global variable of Parent - num1 : {obj1.num1}")

    # 7. Calling Print method using 2 objects
obj1.methodPrint()
Parent.counter+=1
obj2.methodPrint()

    # 8. Summation method    ---> Need to pass self for Non-constructor Argument passing methods as first argument
print(f"Sum of {10, 20,30} using obj1 = {obj1.summation(10, 20, 30)}")
print(f"Sum of {33, 33,33} using obj2 = {obj2.summation(33, 33, 33)}")