from typing import List
from collections import Counter

class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    c = Counter(nums)
    m = max(c.values())
    return list(c.values()).count(m) * m

