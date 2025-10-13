# Goal of program:
# 1. Read all lines as list
# 2. Reverse the list
# 3. Print the reversed data into file

# NOTE: Here with open is used as it used to open files and automatically closes the file
# and we can mention the read or write mode (Optional) 

with open("SampleText.txt", "r") as reader:
    content = reader.readlines() #[ABC, BCD, CDE, DEF]
with open("SampleText.txt", "w") as writer:
    for line in reversed(content):
        writer.write(line)