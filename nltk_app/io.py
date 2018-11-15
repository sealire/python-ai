FileName = "poem.txt"

with open(FileName, 'r') as file:
    data = file.readlines()
    for i in range(len(data)):
        print(data[i])
