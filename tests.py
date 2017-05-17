import unittest

from foobarqix import foobarqix

class FooBarQixTests(unittest.TestCase):

    def test_should_return_number_when_input_is_not_divisble_by_3_5_7(self):
        self.assertEqual("1", foobarqix(1))
        self.assertEqual("4", foobarqix(4))

    def test_should_return_Foo_when_input_is_divisible_by_3(self):
        self.assertEqual("Foo", foobarqix(6))
        self.assertEqual("Foo", foobarqix(12))

    def test_should_return_Bar_when_input_is_divisible_by_5(self):
        self.assertEqual("Bar", foobarqix(10))
        self.assertEqual("Bar", foobarqix(20))

    def test_should_return_Qix_when_input_is_divisible_by_7(self):
        self.assertEqual("Qix", foobarqix(14))
        self.assertEqual("Qix", foobarqix(28))

    def test_should_return_a_combination_of_FooBarQix(self):
        self.assertEqual("FooQix", foobarqix(3*7))
        self.assertEqual("BarQix", foobarqix(5*7*4))
        self.assertEqual("FooBar", foobarqix(3*5*4))
        self.assertEqual("FooBarQix", foobarqix(3*5*7*4))
    
    def test_should_replace_3_by_Foo(self):
        self.assertEqual("Foo", foobarqix(13))

    def test_should_replace_5_by_Bar(self):
        self.assertEqual("Bar", foobarqix(52))

    def test_should_replace_7_by_Qix(self):
        self.assertEqual("Qix", foobarqix(17))
