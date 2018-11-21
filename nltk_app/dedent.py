import textwrap3

FileName = ("poem.txt")

print("**Before Formatting**")
print(" ")

with open(FileName, 'r') as file:
    data = file.readlines()
    for i in range(len(data)):
        print(data[i])

print(" ")
print("**After Formatting**")
print(" ")
with open(FileName, 'r') as file:
    data = file.readlines()
    for i in range(len(data)):
        dedented_text = textwrap3.dedent(data[i]).strip()
        print(dedented_text)
