class Solution:
  def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
    result = []
    for i,val in enumerate(variables):
      a,b,c,d = val
      if (a**b%10)**c%d==target:
        result.append(i)
    return result