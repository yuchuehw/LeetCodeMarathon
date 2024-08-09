from itertools import combinations

class CombinationIterator:
  def __init__(self, characters: str, combinationLength: int):
    self.hold = None
    self.c = combinations(characters,combinationLength)
  def next(self) -> str:
    if self.hold:
      temp = self.hold
      self.hold = None
      return "".join(temp)
    return "".join(next(self.c))
  def hasNext(self) -> bool:
    try:
      self.hold = next(self.c)
      return True
    except:
      self.hold = None
      return False