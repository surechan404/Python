file = open("SampleText.txt")

# 1. Read the entire file
# content = file.read()
# print(content)

# 2. Read a certain number of characters
# print(file.read(3))  # This will print from the 3rd letter in the file but as of now nothing will print as the cursor is at the end of the file           

#  3. Read a single line from current cursor position
# print(file.readline())  

# 4. Printing line by line using readline()
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

# 5. Printing line by line using readlines()
for lines in file.readlines():
    print(lines)



file.close() 