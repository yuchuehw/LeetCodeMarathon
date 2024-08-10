class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        prev = None
        cons = 0
        best = 0
        ones = 0
        for c in s:
            if c == "0":
                if prev == "1":
                    print(ones, cons)
                    if ones*2 <= cons:
                        best = max(best, ones*2)
                    else:
                        best = max(best, (cons-ones)*2)
                        
                    ones = 0
                    cons = 1
                else:
                    cons+=1
                prev = "0"
            if c == "1":
                if prev == None:
                    pass
                else:
                    prev = "1"
                    cons += 1
                    ones += 1
        
        if ones*2 <= cons:
            best = max(best, ones*2)
        else:
            best = max(best, (cons-ones)*2)
        return best
            
