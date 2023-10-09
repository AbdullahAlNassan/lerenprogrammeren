a = int(input('voer a in'))
b = int(input('voer b in'))

if a > b :
    maximum = a
    print(f"a is het grootste getal, {maximum}")
    minimum = b
    print(f"Het maximum getal is {maximum}")
    print(f"Het minimum getal is {minimum}")

elif a < b :
    minimum = a
    print(f'a is het kleinste getal, {minimum}')
    maximum = b
    print(f"Het grootste getal is {maximum}")
    print(f"het kleinste getal is {minimum}")

else:
    print('a en b zijn even groot')
    print(a)
    print(b)   
