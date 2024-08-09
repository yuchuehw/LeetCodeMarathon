from typing import List
class Solution:
  def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
    lm = [0]*m
    ln = [0]*n
    for i,j in indices:
      lm[i] += 1
      ln[j] += 1
    return sum(1 for i in lm for j in ln if (i+j)%2)

  def oddCells2(self, m: int, n: int, indices: List[List[int]]) -> int:
    lm = [0]*m
    ln = [0]*n
    for i,j in indices:
      lm[i] ^= 1
      ln[j] ^= 1
    om = lm.count(1)
    on = ln.count(1)
    return (n-on) * om + (m-om) * on
