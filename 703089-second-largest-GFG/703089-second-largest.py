class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n<2:
            return -1
        large = float('-inf')
        s_large = float('-inf')
        for i in range(n):
            
            if arr[i]> large:
                s_large = large
                large = arr[i]
            elif arr[i]>s_large and arr[i]!=large:
                s_large = arr[i]
            
            
        return s_large if s_large!= float('-inf') else -1

    
        # code here
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna