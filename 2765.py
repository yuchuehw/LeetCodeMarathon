class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best = 0
        current = 1
        expect = nums[0] + 1
        cycle = -1
        prev = None
        for i in nums[1:]:
            if i == expect:
                current += 1
                expect = i + cycle
                cycle *= -1
            elif prev and i == prev+1:
                best = max(best, current)
                current = 2
                expect = i - 1
                cycle = 1
            else:
                best = max(best, current)
                current = 1
                expect = i + 1
                cycle = -1
            prev = i
        best = max(best, current)
        return best if best > 1 else -1
