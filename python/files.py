f = open("file.txt")

lines = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()