import re

class SerialAverage:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def check_input_string(self):
        # Adjust pattern to handle optional negative signs and ensure proper format
        pattern = r"^\d{3}-\-?\d{2}\.\d{2}-\-?\d{2}\.\d{2}$"
        return bool(re.match(pattern, self.input_string))
        
    def serial_average(self):
        if self.check_input_string():
            serial_number_sss = self.input_string[0:3]
            xx_xx = float(self.input_string[4:9])
            yy_yy = float(self.input_string[10:])
            
            zz_zz = round((xx_xx + yy_yy) / 2, 2)
            
            return f"{serial_number_sss}-{zz_zz:.2f}".replace('--', '-')
        else:
            return "Invalid input string"

