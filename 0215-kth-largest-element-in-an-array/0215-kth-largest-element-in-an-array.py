import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for x in nums:
            heapq.heappush(h,x)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna