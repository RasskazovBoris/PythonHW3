a = int(input("Введите длину списка: "))
array = []
for i in range(a):
    b = int(input ("Введите значение №" + str(i + 1) + ": "))
    array.append(b)
print (array)
x = int(input("Сколько раз в массиве встречается число "))
acc = 0
for i in array:
    if x == i:
        acc = acc + 1

print (acc)