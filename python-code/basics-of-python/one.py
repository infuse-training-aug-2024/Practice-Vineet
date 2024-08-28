import re
class SerialAverage:
    def __init__(self, s):
        self.s = s
    
    def check_input_string(self):
        pattern = r"^\d{3}-\d{2}\.\d{2}-\d{2}\.\d{2}$"
        ss = self.s
        if re.match(pattern,ss):
            return True
        
        return False
        
        
    def serial_average(self):
        if self.check_input_string():
            serial_number_sss = self.s[0:3]
            
            xx_xx = float(self.s[4:9])
            yy_yy = float(self.s[10:])

            zz_zz = round((xx_xx+yy_yy)/2, 2)
            return f"{serial_number_sss}-{zz_zz:.2f}"
        else:
            print("Please, check the input string")


sa = SerialAverage('002-10.00-20.00')
print(sa.serial_average())