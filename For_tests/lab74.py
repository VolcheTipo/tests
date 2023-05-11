def insert2Mas(A, n, i, elem):
    A = list(map(int, A.split()))
    # если вставлять уже некуда, пишем full
    if len(A) == n:
        print("full")
        return
        # в цикле печатаем переносы элементов
    s = ''
    for y in range(n, i, -1):
        s = s + 'A[{}] = A[{}]'.format(y, y - 1) + '\n'
    # печатаем копирование элемента elem в нужное место

    return s + 'A[{}] = {}'.format(i, elem)


n, i, elem = map(int, '6 2 3'.split())
A = '3 6 2 1 6 4 0 0 0 0'
print(insert2Mas(A, n, i, elem))