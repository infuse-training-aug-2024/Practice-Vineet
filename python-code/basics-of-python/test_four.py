import unittest
from four import ValidatePassword
class TestValidatePassword(unittest.TestCase):
    
    def setUp(self):
        self.passwords = ["ABd1234@1", "aF1#,2w3E*", "2We3345"]
        self.validator = ValidatePassword(self.passwords)
        
    def test_validate_password(self):
        self.assertTrue(self.validator.validate("ABd1234@1"))
        self.assertTrue(self.validator.validate("aF1#,2w3E*"))
    
    def test_check_password(self):
        valid_passwords = ["ABd1234@1", "aF1#,2w3E*"]
        self.assertEqual(self.validator.check_password(), valid_passwords)

if __name__ == '__main__':
    unittest.main()

