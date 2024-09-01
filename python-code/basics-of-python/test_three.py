import unittest
from three import Sports

class TestSports(unittest.TestCase):

    def setUp(self):
        self.sports_list = ["Cricket", "TT", "Football", "Hockey"]
        self.sports = Sports(self.sports_list, 2)
    
    def test_skip_sports_default(self):
        expected_result = ["2:Football", "3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)

    def test_skip_sports_with_skip_num_1(self):
        self.sports.skip_num = 1
        expected_result = ["1:TT", "2:Football", "3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)

    def test_skip_sports_with_skip_num_3(self):
        self.sports.skip_num = 3
        expected_result = ["3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)

    def test_skip_sports_with_skip_num_0(self):
        self.sports.skip_num = 0
        expected_result = ["0:Cricket", "1:TT", "2:Football", "3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)

    def test_skip_sports_with_skip_num_greater_than_list(self):
        self.sports.skip_num = 5
        expected_result = []
        self.assertEqual(self.sports.skip_sports(), expected_result)

if __name__ == '__main__':
    unittest.main()
