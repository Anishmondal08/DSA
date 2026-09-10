class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        count = 0
        vowel = 'aeiou'

        for i in range(k):
            if s[i] in vowel:
                count += 1

        max_count = count
        left = 0

        for right in range(k, len(s)):

            if s[left] in vowel:
                count -= 1

            left += 1

            if s[right] in vowel:
                count += 1

            max_count = max(max_count, count)

        return max_count