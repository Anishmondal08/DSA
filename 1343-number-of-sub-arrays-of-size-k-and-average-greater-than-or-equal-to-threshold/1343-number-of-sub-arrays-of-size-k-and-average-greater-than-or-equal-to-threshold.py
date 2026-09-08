class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window_sum = 0
        count = 0

       
        for i in range(k):
            window_sum += arr[i]

        if window_sum >= k * threshold:
            count += 1

    
        left = 0

        for right in range(k, len(arr)):
            window_sum -= arr[left]
            left += 1

            window_sum += arr[right]

            if window_sum >= k * threshold:
                count += 1

        return count