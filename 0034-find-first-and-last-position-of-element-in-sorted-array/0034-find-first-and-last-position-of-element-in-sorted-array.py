class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst():
            left,right = 0, len(nums) - 1
            ans = -1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    ans = mid
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid - 1
            return ans
        def findlast():
            left,right = 0, len(nums) - 1
            ans = -1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    ans = mid
                    left = mid+1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return ans
            
        return [findfirst(),findlast()]

            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna