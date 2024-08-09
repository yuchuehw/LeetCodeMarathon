from collections import Counter
class Solution:
  def countKDifference(self, nums: List[int], k: int) -> int:
    return sum(abs(nums[i]-nums[j]) == k for i in range(len(nums)) for j in range(i+1,len(nums)))
  def countKDifference2(self, nums: List[int], k: int) -> int:
    c = Counter(nums)
    result = 0
    for el in c:
      result += c[el] * c.get(el+k,0)
    return result