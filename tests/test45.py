import unittest

def func(h, k):
    n = len(k)
    for i in range(h, n):
        j = i
        while j >= h and k[j] < k[j-h]:
            k[j], k[j-h] = k[j-h], k[j]
            j -= h
    return k

class Tests45(unittest.TestCase):

    def test_1(self):
        with self.assertRaises(TypeError) as e:
            func(3, ['100', '3', '-56', 8])

    def test_2(self):
        with self.assertRaises(NameError) as e:
            func(1, a)

    def test_3(self):
        with self.assertRaises(Exception) as e:
            func(None, 1)

    def test_4(self):
        with self.assertRaises(IndexError) as e:
            self.assertEqual(func(1, [0])[1], [])

    def test_5(self):
        self.assertEqual(func(3, [100, 3, -56, 8]), [8, 3, -56, 100])

    def test_6(self):
        self.assertEqual(func(1, [2002, 2.0]), [2.0, 2002])

    def test_7(self):
        self.assertNotEqual(func(1, [1, 2, 3, 4]), True)

    def test_8(self):
        self.assertNotEqual(func(0, []), 1)

    def test_9(self):
        self.assertIsNotNone(func(3, [5, 1, 6, 2]))

    def test_10(self):
        self.assertIsInstance(func(3, [5, 1, 6, 2]), list)


    def test_9(self):
        with self.assertRaises(NameError) as e:
            func(3, elkliueva)

    def test_10(self):
        with self.assertRaises(Exception) as e:
            func(None, 1)


if __name__ == '__main__':
    unittest.main()