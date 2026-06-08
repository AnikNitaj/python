with open("example.txt","r")as file:
    file1 = file.readline()

print(file1)


with open("example.txt","r")as file:
    lines = file.readline()
    print(lines)