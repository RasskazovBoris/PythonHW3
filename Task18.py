a = int(input("Введите длину списка: "))
array = []
for i in range(a):
    b = int(input ("Введите значение №" + str(i + 1) + ": "))
    array.append(b)
print (array)
x = int(input("Введите число: "))
diff = x - array[0]
answer = int()
for i in range(len(array)):
    if abs(x - array[i]) < diff:
        diff = x - array[i]
        answer = i
print (array[answer])
