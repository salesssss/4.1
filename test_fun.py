import unittest

def fun (x):
    
        return x-1

class Mytest(unittest.TestCase):
        
        def test(self):
            self.assertEqual(fun(6),5)
    
if __name__ == '__main__':
        unittest.main()
        