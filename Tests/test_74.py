from unittest import TestCase, main
from For_tests.lab74 import insert2Mas


class TestOnMassiv(TestCase):
    def setUp(self):
        self.y = '8 800 555 35 35'
        self.x = [777, 585, 925]
        self.z = '1 2 3 4 5 6'
        #self.u = '1 7 7 4 9 8 2 2 3 4 5 8 8 9 88 7 0 1'
        self.u = '23 11 24 13'
    def test_positive1(self):
        A= '3 6 2 1 6 4 0 0 0 0'
        n = 6
        i = 2
        elem =  3

        self.assertEqual(insert2Mas(A, n, i, elem), '''A[6] = A[5]
A[5] = A[4]
A[4] = A[3]
A[3] = A[2]
A[2] = 3''' , 'Что-то неправильно работает') #!!!
    def test_positive2(self):
        A = '3 8 1 6 7 0 0 0 0'
        n =5
        i = 1
        elem = 1
        self.assertEqual(insert2Mas(A, n, i, elem), '''A[5] = A[4]
A[4] = A[3]
A[3] = A[2]
A[2] = A[1]
A[1] = 1''', 'Что-то неправильно работает')

######################################################################
    def test_for_alone(self):
        #M = '1'
        M = '1 2 3 4 5 6 7 8 9 0'
        n = 1
        i = 0
        elem = 1
        f = insert2Mas(M, n, i, elem)
        a= str(f)
        self.assertFalse(a.count('\n') ==0, 'Массив из одного элемента не пропущу')
############################################################################################
    def test_for_emptiness(self):
        M = ''
        n = 0
        i = 0
        elem = 0
        f = insert2Mas(M, n, i, elem)
        a = str(f)
        self.assertFalse(len(a.split())==0, 'Массив из ничего не пропущу')
    def test_different(self):
        for i in range(len(self.x)):
            self.assertIsInstance(self.x[i], type(self.x[0]), 'Шо ты мне тут даешь, тут вообще-то разные типы' )

    def test_special_conditions_1(self): #дубликаты
        self.assertFalse(self.z == (len(self.z.split()) * (self.z.split()[0]+ ' ')).rstrip(), 'Зачем мне один и тот же элемент')


if __name__ == '__main__':
    main()


