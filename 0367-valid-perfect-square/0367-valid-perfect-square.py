class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1

        while True:
            if num == i * i:
                return True
            elif i * i > num:
                return False
            else:
                i += 1