N = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 20) for i in range(N)]
print(list)
x = int(input("Введите искомое число "))
index_element = 0
min_element = abs(x - list[0])
for i in range(1, N):
    buffer_element = abs(x -list[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")