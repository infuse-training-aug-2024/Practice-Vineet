import re

class ValidatePassword:
    def __init__(self, password_arr):
        self.password_arr = password_arr
        
    def validate(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,12}$"
        if(re.match(pattern, password)):
            return True
        
        return False

    def check_password(self):
        result = []
        for p in self.password_arr:
            if self.validate(p):
                result.append(p)
        
        return result
        


passwords=["ABd1234@1", "aF1#,2w3E*", "2We3345"]

ans = ValidatePassword(passwords)
print(ans.check_password())