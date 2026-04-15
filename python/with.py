# f = open("file.txt")

# print(f.read())

# f.close()


# # But with ( WITH ) statement, we don't have to worry about closing the file

# with open("file.txt") as f:
#     print(f.read())


# f = open("poeam.txt")

# content = f.read()

# if( "twinkle" in content):
#     print("yeah")
# else:
#     print("no")

# f.close()




# Object and Class Attribute !!!!

class Emp:
    lang = "PY"
    salary = 1200000

hari = Emp()

hari.name = "Hari"    # HIGHER PRIORITY & Adding an attribute to an object
print(hari.lang)

hari.getInfo()  # means > Emp.getInfo(harry); >>> It require an argument ! (provide self while defining function)

# ex inside ** Emp ** class

def getInfo(self):
    print(f"Name is {self.name} and salary is {self.salary}")

# OR if it's not taking anything soo mark it as @ Static mathod

@staticmethod     ##### DECORATOR !
def getInfo():
    print("This is a static method")