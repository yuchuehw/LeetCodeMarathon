class Solution:
  def orArray(self, nums: List[int]) -> List[int]:
    return [i|j for i,j in zip(nums, nums[1:])]
    return [nums[i]|nums[i+1] for i in range(len(nums)-1)]