import unittest
from two import ArrayClass
class TestArrayClass(unittest.TestCase):
    
    def setUp(self):
        self.array = [9, 5, 1, 2, 3, 4, 0, -1]
        self.arr_class = ArrayClass(self.array)
    
    def test_element_at(self):
        self.assertEqual(self.arr_class.element_at(0), 9)
        

    def test_inclusive_range(self):
        self.assertEqual(self.arr_class.inclusive_range(1, 5), [5, 1, 2, 3, 4])
        self.assertEqual(self.arr_class.inclusive_range(0, 7), [9, 5, 1, 2, 3, 4, 0, -1])
            

    def test_non_inclusive_range(self):
        self.assertEqual(self.arr_class.non_inclusive_range(1, 5), [5, 1, 2, 3])
        self.assertEqual(self.arr_class.non_inclusive_range(0, 7), [9, 5, 1, 2, 3, 4, 0])


    def test_start_and_length(self):
        self.assertEqual(self.arr_class.start_and_length(2, 0), 6)
        self.assertEqual(self.arr_class.start_and_length(0, 0), 8)


if __name__ == '__main__':
    unittest.main()
