def interpolSearch(A, elem):
    A = list(map(int, A.split()))
    elem = int(elem)
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[len(A) - 1]:
        return [None]

    # определим верхнюю границу и вызовем рекурсивную функцию
    R = len(A) - 1
    return interpolSearchRec(A, elem, 0, R)


def interpolSearchRec(A, elem, L, R, sp=[]):
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if L> R or elem > A[R] or elem < A[L] :
        return sp
    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if A[L] == A[R]:
        mid = L
    # иначе - вычисляем mid по формуле
    else:
        mid = L + round((elem - A[L]) * (R - L) / (A[R] - A[L]))

    # выполняем сравнение и рекурсивный вызов на одной из частей
    sp.append(A[mid])
    if A[mid] == elem:
        return sp
    elif A[mid] > elem:
        return interpolSearchRec(A, elem, L, mid - 1, sp)
    else:
        return interpolSearchRec(A, elem, mid + 1, R, sp)


elem = '8'
mas = '1 4 7 8 10 17 21 23 26 32 36 40 41 43 44 47 49'
print(*interpolSearch(mas, elem))
