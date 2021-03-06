import os
import sys
import unittest

sys.path.append(os.getcwd())
print("current working directory:", os.getcwd())
from recipe_TDD import *


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_integer(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEqual(nitro_salt("1000"), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEqual(nitro_salt("text"), 0)


if __name__ == '__main__':
    unittest.main()
