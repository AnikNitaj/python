import os

lines = ("hello world\n"","Welcome to python\n")

with open("example2.txt","w")as file:
    #file.write("Hhgsswg")
    file.writelines(lines)

if os.path.exists("example2.txt"):
    print("example2.txt exists")