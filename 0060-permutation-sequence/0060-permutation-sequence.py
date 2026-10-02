class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []

        for i in range(1, n + 1):
            nums.append(i)

        k = k - 1
        result = ""

        for i in range(n, 0, -1):
            fact = 1

            for j in range(1, i):
                fact = fact * j

            index = k // fact

            result = result + str(nums[index])

            nums.pop(index)

            k = k % fact

        return result