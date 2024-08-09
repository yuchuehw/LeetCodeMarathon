class Solution:
  def balancedStringSplit(self, s: str) -> int:
    count = 0
    r_count = 0
    l_count = 0
    for ss in s:
      r_count += (ss == "R")
      l_count += (ss == "L")
      if r_count == l_count:
        count += 1
        r_count = 0
        l_count = 0
    return count