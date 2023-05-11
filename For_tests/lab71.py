elem = '13'
mas = '2 4 7 9 15 16 20 21 22 28 29'


def binSearch(A, elem):
    elem = int(elem)
    A =  list(map(int, A.split()))
    # если искомый элемент за границами диапазона,то делать нечего
    if not A:
        return [None]
    if elem < A[0] or elem > A[len(A) - 1]:
        # print(None)
        return [None]
    # определим верхнюю границу и вызовем рекурсивную функцию
    hi = len(A) - 1
    return binSearchRec(A, elem, 0, hi)

spisok = []
def binSearchRec(A, elem, lo, hi):
    global spisok
    # если подмассив пустой, то делать нечего
    if not A:
        return
        # определяем (и печатаем) средний элемент
    mid = (lo + hi) // 2
    if elem > A[0] and elem < A[len(A) - 1]:
        spisok.append(A[mid])
    if A[mid] == elem:
        if A[mid] not in spisok:
            spisok.append(A[mid])
        #print(" ".join(map(str, spisok)))
        #return " ".join(map(str, spisok))
        return spisok
        # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] > elem >= A[lo]:
        return binSearchRec(A, elem, lo, mid - 1)
    elif A[mid] < elem <= A[hi]:
        return binSearchRec(A, elem, mid + 1, hi)
    if elem > A[0] and elem < A[len(A) - 1]:
        #print(" ".join(map(str, spisok)))
        return spisok
print(*binSearch(mas, elem))




