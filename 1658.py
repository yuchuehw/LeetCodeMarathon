class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        elif target == 0:
            return len(nums)
        left = 0
        right = 0
        best = float('inf')
        sum_ = 0
        while True:
            
            if sum_ == target:
                best = min(best, len(nums) - right + left)
            if sum_ < target:
                right += 1
                if right > len(nums):
                    return best if best != float('inf') else -1
                sum_ += nums[right-1]
            elif sum_ >= target:
                sum_ -= nums[left]
                left += 1
