# 1. for loop
obj = [1,2,3,5,6,9,7,0,6,76]
for i in obj:
    print(i)
print()

    # Example 1: Multiplying numbers in list with 2
obj = [1,2,3,5,6,9,7,0,6,76]
for i in obj:
    print(i*2)
print()

    # Example 2: Summing first 7 natural nos
sum = 0
for i in range(1,8): #Range from 1 to 8-1 => 1 to 7
    sum +=i
print(sum)
print()

    # Example 3: Incrementing the range by count 2 Eg. for(int i=0;i<8;i+2)
counter = 0
for i in range(1,100,2):
    counter +=1
    print(i)
print("{} {}".format("Total odd nos until 100 is", counter))
print(f"Total odd nos until 100 is {counter}")
    # Example 4: Skipping First index of range()

for j in range(10):
        print(j)  # prints from 0 to 9
print()


# 2. while loop

num =15
while num > 1:
    print(num)
    num -= 1
print("End of while loop..\n")


    # Example 1: If no. is 3, then don't print it
num1 = 9
while num1 > 1:
    if num1 != 3:
        print(num1)
    num1 -= 1
print("End of while loop..\n")

# 3. else in "for" and "while" loops
# USed to indicate loops that are not ended by not using break

for i in range(1,6):
    print(i)
    if i ==4:
        break # comment this line to undersrtand the fslow
else:
    print("Loop finished without break")






# 4. Loop control statements:  while loop with "break" and "continue"

# num2 = 15
# while num2 > 1:
#     if num2 == 7:
#         num2 -= 1
#         continue  # skips this iteration of whole loop
#     if num2 == 4:
#         break # Totally moves out of the loop and executes next set of codes
#     print(num2)
#     num2 -= 1
# print("While loop ends..\n")





















