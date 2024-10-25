#Для правильной работы кода создайте текстовый документ с названием dara.txt, в который запишите название первого продукта
q = int(input('Есть ещё товар, который надо купить, 1)да, 2)нет'))
if q == 1:
    a = input('Введите название второго продукта.')
    
    file = open('dara.txt', 'r', encoding='utf-8')
    s = file.read()


    f_file = open('dara.txt', 'w', encoding='utf-8')
    f_file.write(s+' и '+a)

    #file.write(s+' и '+a)

    file.close()
    f_file.close()
if a == 2:
    print('Тогда у вас только 1 товар.')