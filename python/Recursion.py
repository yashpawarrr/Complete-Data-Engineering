def goodDay(name):
    if name == "Alice":
        return "Good day, Alice!"
    else:
        return "Good day, stranger!"
    
print(goodDay("Alice"))

# // Recursion example

def recur(n):
    if (n <= 1):
        return 1
    return n*recur(n-1)

print(recur(5))