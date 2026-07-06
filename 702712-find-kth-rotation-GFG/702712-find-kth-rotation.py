class Solution:
    def findKRotation(self, arr):
        # code here
        low = 0
        high = len(arr)-1
        while low<high:
            mid = low+ (high-low)//2
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high = mid
        return low

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna