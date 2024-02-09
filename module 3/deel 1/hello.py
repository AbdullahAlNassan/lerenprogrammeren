def hello(n):
    result = ""
    for i in range(1, n+1):
        result += f"Hello from function town {i}!\n"
    return result

print(hello(3))
print(hello(7))