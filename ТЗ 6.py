a = float(input('Сколько денег собрал первый ребёнок?'))
s = float(input('Сколько денег собрал второй ребёнок?'))
d = float(input('Сколько денег собрал третий ребёнок?'))
f = float(input('Сколько стоит мороженое?'))
if float(f) - float(a) >= 0:
    print('У первого ребёнка осталось', float(f) - float(a), 'рублей.')
if float(f) - float(a) <= -1:
    print('Первому ребёнку не хватило', float(f) - float(a), 'рублей.')
    
if float(f) - float(s) >= 0:
    print('У второго ребёнка осталось', float(f) - float(s), 'рублей.')
if float(f) - float(s) <= -1:
    print('Второму ребёнку не хватило', float(f) - float(s), 'рублей.')

if float(f) - float(d) >= 0:
    print('У третьего ребёнка осталось', float(f) - float(d), 'рублей.')
if float(f) - float(d) <= -1:
    print('Третьему ребёнку не хватило', float(f) - float(d), 'рублей.')
