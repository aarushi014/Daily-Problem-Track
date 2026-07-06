from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need= Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, ch in enumerate(s):
            if need[ch]>0:
                missing-=1
            need[ch] -= 1
            while missing == 0:
                if end == 0 or right-left+1<end-start:
                    start,end = left, right+1
                need[s[left]]+=1
                if need[s[left]]>0:
                    missing+=1
                left+=1
        return s[start:end]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna