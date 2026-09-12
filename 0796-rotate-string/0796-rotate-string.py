class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new = s+s
        if len(s)==len(goal):
            if goal in new:
                return True
            else:
                return False
        else:
            return False            