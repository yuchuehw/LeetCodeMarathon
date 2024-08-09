class Solution:
  def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    def avg(l: List):
      return sum(l)//len(l)
    output = []
    for i in range(len(img)):
      new_row = []
      output.append(new_row)
      for j in range(len(img[0])):
        temp = []
        for x in range(i-1,i+2):
          for y in range(j-1,j+2):
            if 0<=x<len(img) and 0<=y<len(img[0]):
              temp.append(img[x][y])
        new_row.append(avg(temp))
    return output