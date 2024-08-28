import unittest
from three import Sports
class TestSports(unittest.TestCase):

    def setUp(self):
        self.sports_list = ["Cricket", "TT", "Football", "Hockey"]
        self.sports = Sports(self.sports_list, 2)
    
    def test_skip_sports(self):
        
        expected_result = ["2:Football", "3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)

        self.sports.skip_num = 1
        expected_result = ["1:TT", "2:Football", "3:Hockey"]
        self.assertEqual(self.sports.skip_sports(), expected_result)


if __name__ == '__main__':
    unittest.main()
