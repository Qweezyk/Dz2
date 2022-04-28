def num_translate(x):
    if x.istitle():
        number_upper = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три',
                        'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'семь',
                        'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
        result = f'"{number_upper[x]}"'
    else:
        number = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
                  'four': 'четыре','five': 'пять', 'six': 'шесть', 'seven': 'семь',
                  'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
        result = f'"{number[x]}"'
    return result


print(num_translate('Seven'))
print(num_translate('ten'))
x = input()
print(num_translate(x))