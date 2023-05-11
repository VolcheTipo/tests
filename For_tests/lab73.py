def Fib(n):
    a = 1
    if n > 2:
        a = Fib(n - 2) + Fib(n - 1)
    return a


def fibSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    A = list(map(int, A.split()))
    elem = int(elem)
    l = len(A)
    # вычисляем нужное число Фибоначчи
    if elem > A[l - 1] or elem < A[0]:
        return [None]

    # вызываем рекурсивную функцию
    for i in range(l + 2):
        fk = Fib(i)
        if fk >= l:
            f_num = i
            break
    spisik = []
    return fibSearchRec(A, elem, 0, Fib(f_num - 1), fk, l, spisik)


def fibSearchRec(A, elem, lo, fk_1, fk, l, sp=[]):
    # если подмассив пустой ИЛИ из одного элемента, который не равен elem, то делать нечего
    if fk == 0 or (fk == 1 and A[lo] != elem):
        sp.append(A[lo])
        return sp

    # если подмассив из одного элемента, который равен elem, то выводим ответ и завершаемся
    if A[lo] == elem and fk == 1:
        sp.append(A[lo])
        return sp

    # вычисляем (k-2)-е число Фибоначчи
    fk2 = fk - fk_1

    # вычисляем mid - правый элемент первого подмассива (смотрим, чтобы он не выпал за границы)
    # не забываем выводить ответ
    mid = min(lo + fk2 - 1, l - 1)
    sp.append(A[mid])
    if A[mid] == elem:
        return sp


    # выполняем сравнение и рекурсивный вызов на одной из частей
    elif A[mid] > elem:
        return fibSearchRec(A, elem, lo, fk_1 - fk2, fk2, l, sp)
    elif A[mid] < elem:
        return fibSearchRec(A, elem, lo + fk2, fk2, fk_1, l, sp)


elem = '8'
mas = '3 4 7 10 13 16 18 19'
print(*fibSearch(mas, elem))