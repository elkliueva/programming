import unittest

def func(k):
    n = len(k)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]
                flag = True
        if not flag:
            break
    return k

class Tests44(unittest.TestCase):

    def test_1(self):
        with self.assertRaises(TypeError) as e:
            func(['100', '3', '-56', 8])

    def test_2(self):
        with self.assertRaises(NameError) as e:
            func(a)

    def test_3(self):
        with self.assertRaises(Exception) as e:
            func(None, 1)

    def test_4(self):
        with self.assertRaises(IndexError) as e:
            self.assertEqual(func([0])[1], [])

    def test_5(self):
        self.assertEqual(func([100, 3, -56, 8]), [-56, 3, 8, 100])

    def test_6(self):
        self.assertEqual(func([2002, 2.0]), [2.0, 2002])

    def test_7(self):
        self.assertNotEqual(func([1, 2, 3, 4]), True)

    def test_8(self):
        self.assertNotEqual(func([]), 1)

    def test_9(self):
        self.assertIsNotNone(func([5, 1, 6, 2]))

    def test_10(self):
        self.assertIsInstance(func([5, 1, 6, 2]), list)

if __name__ == '__main__':
    unittest.main()