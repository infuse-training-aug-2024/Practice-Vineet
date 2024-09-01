import unittest
from four import ValidatePassword

class TestValidatePassword(unittest.TestCase):
    
    def setUp(self):
        self.passwords = ["ABd1234@1", "aF1#,2w3E*", "2We3345", "abcdEF12", "AB12@", "abc123", "ABC@1"]
        self.validator = ValidatePassword(self.passwords)
        
    def test_validate_password_valid(self):
        self.assertTrue(self.validator.validate("ABd1234@1"))

    def test_validate_password_valid_complex(self):
        self.assertTrue(self.validator.validate("aF1#,2w3E*"))

    def test_validate_password_no_special_character(self):
        self.assertFalse(self.validator.validate("abcdEF12"))

    def test_validate_password_too_short(self):
        self.assertFalse(self.validator.validate("AB12@"))

    def test_validate_password_no_uppercase(self):
        self.assertFalse(self.validator.validate("abc123"))

    def test_validate_password_no_digit(self):
        self.assertFalse(self.validator.validate("ABC@1"))

    def test_check_password(self):
        valid_passwords = ["ABd1234@1", "aF1#,2w3E*"]
        self.assertEqual(self.validator.check_password(), valid_passwords)

    def test_check_password_no_valid_passwords(self):
        self.validator = ValidatePassword(["abcdEF12", "AB12@", "abc123", "ABC@1"])
        valid_passwords = []
        self.assertEqual(self.validator.check_password(), valid_passwords)

if __name__ == '__main__':
    unittest.main()
