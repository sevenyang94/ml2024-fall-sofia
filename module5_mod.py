class inputClass:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def searchNum(self, inp):
        if inp in self.nums:
            return self.nums.index(inp) + 1
        else:
            return -1