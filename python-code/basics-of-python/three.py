class Sports:
    def __init__(self, sports_arr, skip_num):
        self.sports_arr = sports_arr
        self.skip_num = skip_num
    
    def skip_sports(self):
        result = []
        for i in range(self.skip_num, len(self.sports_arr)):
            result.append(f"{i}:{self.sports_arr[i]}")
        
        return result
    

sp = Sports(["Cricket", "TT", "Football", "Hockey"], 2)
print(sp.skip_sports())