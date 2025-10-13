# ParentClassFile.py is 8th file
# ChildClassFile.py is 10th file
  
str1 = "Focus on Goal"
str2 = "and Success will follow"
str3 = "Focus"

# 1. Finding length of string
len = len(str1)

# 2. Iterating through string using for loop (But on each line)
for i in range(0, len):
    print(str1[i])

    # or
print(str1[0:5]) # If you want to print substring - prints "Focus" (in single line)

# 3. Concatenation
print(str1,str2) # prints "Focus on Goal and Success will follow" 

# 4. Comparing 2 strings - 

print(str1 == str3) # prints False - Compares full string
print(str3 in str1) # prints True - Substring check

# 5. split()
splitStr = str1.split(" ")
print(splitStr) # prints list of strings - ['Focus on Goal', 'and Success will follow']
print(splitStr[0])

# 6. strip() - removes leading and trailing spaces (similar to trim() in other languages)
str4 = "   Hello World   "
print(str4.strip()) # prints "Hello World"
print(str4.lstrip()) # prints "Hello World   "
print(str4.rstrip()) # prints "   Hello World"