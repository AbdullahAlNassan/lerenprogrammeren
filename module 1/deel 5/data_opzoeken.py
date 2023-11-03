def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)
    print(splitted_strings)
    # if 0 <= position < len(splitted_strings):
    if position >= 0 and position < len(splitted_strings):
        value = splitted_strings[position]
    else:
        value = None
    return value


toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position = 4

result = get_value(toets_data, separator, position)
print(result)
data = 'bmw/audi/ferari/tesla'
result = get_value (data,'/', 2)
print (result)