class Solution:
    def largest(self, arr):
        # code here
        max = arr[0]
        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
        return max


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna