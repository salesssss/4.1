import unittest

def multiply(x,y):

    return x*y

class Mytest(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(4,2),8)

if __name__ == '__main__':
        unittest.main()