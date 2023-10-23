a = input('Geef een woord: ')
b = input('Geef nog een woord: ')

if len(a) < len(b):
    print(f'Woord {a} heeft minder letters dan woord {b}')
elif len(a) > len(b):
    print(f'Woord {a} heeft meer letters dan woord {b}')
else:
    print(f'Woord {a} en woord {b} hebben evenveel letters')
