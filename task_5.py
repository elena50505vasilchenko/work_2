my_list = [5, 3, 3, 2, 1]
while True:
    num = int(input('Введите число: '))
    idx = None
    for i, num_1 in enumerate(my_list):
        if num > num_1:
            idx = i
            break
    if idx is None:
        my_list.append(num)
    else:
        my_list.insert(idx, num)
    print(my_list)