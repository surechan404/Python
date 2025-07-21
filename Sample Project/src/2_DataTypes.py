# Basic dataTypes
# 1. Numeric
    # int - Integers of non-limited length  => a = 100
    # long - Long integers (deprecated in Python 3.x)
    # float - Decimal digits upto 15 => b = 3.14159453297
    # complex - Complex numbers => c = 100+3j
num = 100
passMark = 35.0
sciNum = 10e3
print (num, passMark, sciNum)  # => 100 35.0 10000.0

# 2. String
a = 'String inside single quotes'  #adds a blankspace between 2 strings
b = "String inside double quotes"  #adds No blankspace between 2 strings
print(a,b)
print(a+b)

# 3. List
    # a. Ordered sequence of multiple values wih different types of data
    # mutable
c = [1, "AB", 3.15, "A+", 7e5]
print(c)  # => [1, 'AB', 3.15, 'A+', (100+3j)]
print (c[0])  # => 1
print (c[1])  # => AB
print (c[-1]) # -1 refers to last index of list => 700000.0
print (c[0:5]) # prints first element to last (0:last+1)
print (c[1:4]) # prints second element to penultimate element

    # b. insert a value between elements [First value is target index
c.insert(2, "C")
print(c)

    # c. append a new value at last
c.append( "Last value")
print(c)

    # d. Updating a value
c[1] = 6
print(c)

    # e. Deleting a value
del c[1]
print(c)

# 4. Tuple
    # Immutable, same as like list

d = (1, "BCA", 99.9999, "SC", 4e5)
print(d)
print(d[2]) #index of 2 => 3rd element
# d[1] = 2   Cannot override/Update

# 5. Dictionary
    # Unordered sequence of data with key-value pair (Like Objects)

e = {"firstName":"Suresh", "secondName":"Chander", "Initials": "R", "age": 27, 1:"0123456789", "empty":""}
print(e["firstName"])
print(e["secondName"])
print(e["age"])
print(e[1])
print("Null"+e["empty"])
print(e)

    # Creating a dictionary in Runtime
dict = {}

    # Adding data to created dictionary
dict["firstName"] = "Suresh"
dict["lastName"] = "Chander"
dict["dept"] = "IT"
print(dict)

    # print(dict["age"])  => KeyError: 'age' as age is not an existing key
dict["age"] = 27
print(dict["age"])