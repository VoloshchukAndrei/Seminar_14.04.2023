#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#1 2 3 4 5
#6 -> 5

N = int(input("Укажите размер массива: ")) 
print("Введите элементы массива:")
mas = [int(input()) for i in range(N)] 
x = int(input("Задайте число X: "))
i = 0 
y = mas[0]
z = mas[i]
for i in mas:
    if z < y:
        y = z
    i += 1
print(y)