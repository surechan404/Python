# 1. classes are user defined blueprint or prototype
# 2. sum, multiplication, addition, constant
# 3. methods, class variabls, instance variables, constructor etc


class Main:
    num1 = 100

# 4. Default constructor - Instead Classname, in python __init__(self) is used.
# 5. Default constructor will be called automatically when an object is created
    def __init__(self, a, b):
        # In above, Object is passed within self and other parameters with next params respectively
        print(f"Statement of Default constructor of ..")  # 1st statement to get execute
        self.firstNum = a
        self.secondNum = b
        print(self.firstNum+self.secondNum)


    def method(self):
        print("Method within the class is executed..")

    def summation(self, a, b, c):
            return a+b+c

    #def summation(self)
         # return self.firstNum + self.secondNum + Main.num

# 6. Object creation
obj = Main(15,15)
obj1 = Main(20,20)

print(f"Sum of 2 nos {obj.num1}")
obj.method()
obj1.method()


print(f"3 params sum = {obj.summation(10, 10, 30)}")


# 7. Variables -> Class variable, local variable
# 8. Values passed within the function/constructor are called as Instance variables
# 9. Always use self.instVariable to call
# 10. While passing instVariable the value goes to constructor and add it next to the self E.g. __init__(self, a, b):
# 11. To access the Class variable, use Classname.variable E.g. Calculator.num
# 12. Constructor always readds the class variables and stores within the self
# 13. self keyword is mandatory to call variable name in methods
# 14.





