import unittest

def dummy_function(x):
    return x

class TestDummyFunction(unittest.TestCase):

    def test_returns_input(self):
        self.assertEqual(dummy_function(42), 42)

    def test_returns_string(self):
        self.assertEqual(dummy_function("hello"), "hello")

    def test_returns_none(self):
        self.assertIsNone(dummy_function(None))

if __name__ == '__main__':
    unittest.main()
