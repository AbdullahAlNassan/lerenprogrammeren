a = str(input('Geef een woord'))
b = str(input('Geef nog een woord'))

if a < b:     
    print(f'Woord {a} heeft meer letters dan woord {b}')
elif a > b:   
    print(f'Woord {a} heeft minder letters dan woord {b}')
else:                   
    print(f'Woord {a} en woord {b} hebben evenveel letters')