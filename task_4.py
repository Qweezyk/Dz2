from random import randrange, choice

def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    while n >= 1:
        joke = (f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        jokes.append(joke)
        n -= 1
    return jokes

n = int(input('Введите кол-во шуток: '))
print(get_jokes(n))