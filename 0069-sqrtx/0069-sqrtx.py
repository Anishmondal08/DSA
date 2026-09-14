class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        i = 1

        while True:
            if i * i <= x:
                i += 1
            else:
                return i - 1