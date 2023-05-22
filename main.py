from random import shuffle
spisok = ['соль, перец, хлеб, картофель']

trix = input('Введите ингридиент (хватит - стоп):')
while trix != 'хватит':
    if trix in spisok:
        print('этот ингридиент уде есть')
    else:
        spisok.append(trix)

    trix = input('Введите ингридиент (хватит - стоп):')

blender = []
nums = int(input('Сколько требуется ингридиентов: '))
for i in range(nums):
    shuffle(spisok) 
    blender.append(spisok[0])
    spisok.remove(spisok[0])


print('Приготовь что нибудь из:')
for i in range(nums):
    print(blender[i])