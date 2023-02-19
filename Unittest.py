import unittest
class MyTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True,True) # add assertion here

    def test_failed(self):
        self.assertNotEqual(False,'Failure Message')

    def testEqual(self):
        self.assertEqual(8, 13 - 5)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
