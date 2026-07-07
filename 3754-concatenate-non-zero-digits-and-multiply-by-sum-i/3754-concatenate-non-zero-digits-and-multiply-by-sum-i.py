class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""

        for ch in str(n):
            if ch != '0':
                s += ch

        if s == "":
            return 0

        x = int(s)
        digit_sum = 0

        for ch in s:
            digit_sum += int(ch)

        return x * digit_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna