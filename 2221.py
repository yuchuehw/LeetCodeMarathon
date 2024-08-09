class Solution:
  def triangularSum(self, nums: List[int]) -> int:
    for j in range(len(nums),1,-1):
      for i in range(j-1):
        nums[i] = (nums[i]+nums[i+1])%10
    return nums[0]

