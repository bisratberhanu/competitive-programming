class Bitset:

    def __init__(self, size: int):
		
        self.bit = [False for i in range(size)]
		
        self.bitinv = [True for i in range(size)]
		
        self.ones = 0
		
        self.zeros = size
		
        self.size = size

    def fix(self, idx: int) -> None:
		
        if not self.bit[idx]:
            self.zeros -= 1
            self.ones += 1
        self.bit[idx] = True
        self.bitinv[idx] = False

    def unfix(self, idx: int) -> None:
		
        if self.bit[idx]:
            self.zeros += 1
            self.ones -= 1
        self.bit[idx] = False
        self.bitinv[idx] = True

    def flip(self) -> None:
		
        self.ones,self.zeros = self.zeros,self.ones
		
        self.bit,self.bitinv = self.bitinv,self.bit

    def all(self) -> bool:
		# return True if ones counter equal to size otherwise False.
        return self.ones == self.size

    def one(self) -> bool:
		# returns True if ones counter greater than zeros
        return self.ones > 0

    def count(self) -> int:
		# returns the number of ones
        return self.ones

    def toString(self) -> str:
		# appending 1 to string if it's True in self.bit otherwise 0
        ans = ''
        for bit in self.bit:
            if bit:
                ans += '1'
            else:
                ans += '0'
        return ans