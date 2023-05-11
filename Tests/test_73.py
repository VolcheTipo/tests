from unittest import TestCase, main
from For_tests.lab73 import fibSearch


class TestOnMassiv(TestCase):
    def setUp(self):
        self.y = '8 800 555 35 35'
        self.x = [777, 585, 925]
    def test_for_alone(self):
        #self.assertEqual(fibSearch('2 4 7 9 15 16 20 21 22 28 29', '13' ), '16 7 9 15', 'Что-то неправильно работает') #!!!
        self.assertNotEqual(fibSearch('2 3 23 13 45 67', '13' ), [None], 'Что-то неправильно работает') #!!!

    def test_for_emptiness(self):
        self.assertEqual(fibSearch('10 2 34 57 42 12 7 9', '42'), [None], 'Что-то неправильно работает' )
    def test_different(self):
        for i in range(len(self.x)):
            self.assertIsInstance(self.x[i], type(self.x[0]), 'Шо ты мне тут даешь, тут вообще-то разные типы' )


if __name__ == '__main__':
    main()



from For_tests.lab73 import fibSearchRec
class TestInWork(TestCase):
    def test_special_conditions_1(self): #дубликаты
        a = fibSearchRec(list(map(int, '3 4 7 10 13 16 18 19'.split())), 8, 0, 8, 5, len(list(map(int, '2 4 7 9 15 16 20 21 22 28 29'.split())))-1)
        self.assertFalse(a == a[0]*len(a), 'Зачем мне один и тот же элемент')

    def test_special_conditions_2(self):  # дубликаты
        a = fibSearchRec(list(map(int, '2 4 7 9 15 16 20 21 22 28 29'.split())), 4, 0, len(list(map(int, '2 4 7 9 15 16 20 21 22 28 29'.split()))) - 1)
        for i in range(len(a)):
            self.assertFalse(a.count(a[i]) > len(a)/2)


if __name__ == '__main__':
    main()