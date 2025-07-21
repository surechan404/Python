# 1. if-else
#indentation is important

a = 4
if a >3:
    print("\n{} {}".format("Value of a is", a))
    print("{} {}".format(a,"> 3"))
    print("If's Second line")
else:
    print("a < 3")
    print("Else's second line..")


# 2. Else-if

numb = 10
if numb == 0:
    print("Number is Zero \n")
elif 1 <= numb <= 5:
    print("Number is between 1 to 5 \n")
elif 6 <= numb <= 10:
    print("Number is between 6 to 10 \n")
else:
    print("Invalid Number \n")

# 3. Nested if
numb2 = 71
if numb2 > 10:
    print("Number is greater than 10")
    if numb2 > 50:
        print("Number is greater than 50\n")

# 4. Ternary operator

x =8
print("Even" if x%2==0 else "Odd")

age = int(input("Enter Age.."))
print("Eligible to Vote" if age>=18 else "Not eligible to Vote")
print("")



















