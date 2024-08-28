import unittest
from one import SerialAverage
class TestSerialAverage(unittest.TestCase):

    def test_check_input_string(self):
        sa = SerialAverage('002-10.00-20.00')
        self.assertTrue(sa.check_input_string())

        sa = SerialAverage('02-10.00-20.0')
        self.assertFalse(sa.check_input_string())

    def test_serial_average(self):
        sa = SerialAverage('002-10.00-20.00')
        self.assertEqual(sa.serial_average(), '002-15.00')

        sa = SerialAverage('123-25.50-30.75')
        self.assertEqual(sa.serial_average(), '123-28.12')


if __name__ == '__main__':
    unittest.main()
