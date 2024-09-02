import unittest
from one import SerialAverage

class TestSerialAverage(unittest.TestCase):

    def test_check_input_string_valid(self):
        sa = SerialAverage('002-10.00-20.00')
        self.assertTrue(sa.check_input_string())

    def test_check_input_string_invalid_length(self):
        sa = SerialAverage('02-10.00-20.0')
        self.assertFalse(sa.check_input_string())

    def test_check_input_string_invalid_format(self):
        sa = SerialAverage('ABC-10.0-20.00')
        self.assertFalse(sa.check_input_string())

    def test_serial_average_valid(self):
        sa = SerialAverage('002-10.00-20.00')
        self.assertEqual(sa.serial_average(), '002-15.00')

    def test_serial_average_valid_large_numbers(self):
        sa = SerialAverage('123-25.50-30.75')
        self.assertEqual(sa.serial_average(), '123-28.12')

    def test_serial_average_with_zero(self):
        sa = SerialAverage('456-0.00-20.00')
        self.assertEqual(sa.serial_average(), '456-10.00')

    def test_serial_average_with_same_values(self):
        sa = SerialAverage('789-15.00-15.00')
        self.assertEqual(sa.serial_average(), '789-15.00')

    def test_serial_average_negative_values(self):
        sa = SerialAverage('999--10.00-20.00')
        self.assertEqual(sa.serial_average(), '999-5.00')

    def test_serial_average_decimal_rounding(self):
        sa = SerialAverage('111-15.678-20.123')
        self.assertEqual(sa.serial_average(), '111-17.90')


if __name__ == '__main__':
    unittest.main()
