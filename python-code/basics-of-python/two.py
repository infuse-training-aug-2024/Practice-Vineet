class ArrayClass:
    def __init__(self, arr):
        self.arr = arr
        
        
    def element_at(self, index):
        return self.arr[index]

    def inclusive_range(self, start_pos, end_pos):
        return self.arr[start_pos:end_pos+1]

    def non_inclusive_range(self, start_pos, end_pos):
        return self.arr[start_pos: end_pos]

    def start_and_length(self, start_pos, length):
        l = length
        from_start_pos = self.arr[start_pos:]
        l = len(from_start_pos)
        return l
    
arr = ArrayClass([9, 5, 1, 2, 3, 4, 0, -1])
print(arr.element_at(2))
print(arr.inclusive_range(1, 5))
print(arr.non_inclusive_range(1, 5))
print(arr.start_and_length(2, 0)) # length=0 -- initially