class Solution:
  def isThree(self, n: int) -> bool:
    if n < 4:
      return False
    a = int(n**0.5+0.1)
    if a**2 != n:
      return False
    return a in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101}
