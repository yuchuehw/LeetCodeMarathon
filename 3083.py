class Solution:
  def isSubstringPresent(self, s: str) -> bool:
    rs = s[::-1]
    data = {s[i:i + 2]: 1 for i in range(len(s) - 1)}
    return any([rs[i:i + 2] in data for i in range(len(s) - 1)])
