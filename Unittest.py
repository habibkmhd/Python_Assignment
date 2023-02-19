import unittest
class MyTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True,'Success Message') # add assertion here

    def test_failed(self):
        self.assertEqual(False,'Failure Message')
        
    def testEqual(self):
        self.assertEqual(8, 13 - 5)


if __name__ == '__main__':
    unittest.main()
