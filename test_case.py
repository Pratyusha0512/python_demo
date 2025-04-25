import unittest

class TestMain(unittest.TestCase):
    def test_example(self):
        self.assertEqual("Hello, World!".lower(), "hello, world!")

if __name__ == '__main__':
    unittest.main()
