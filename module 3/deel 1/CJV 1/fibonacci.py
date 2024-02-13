def fibonacci(n):
    eerste_getal, tweede_getal = 0, 1
    for _ in range(n):
        eerste_getal, tweede_getal = tweede_getal, eerste_getal + tweede_getal
    return eerste_getal

for i in range(10):
    print(fibonacci(i))