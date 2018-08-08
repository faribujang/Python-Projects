class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        
        multiples_2_count = 0
        multiples_3_count = 0
        
        for n in range(2, 58):
            n = (multiples_2_count*2)+(multiples_3_count*3)
            while n%2 == 0:
                return n/2
                multiples_2_count += 1
            while n%3 == 0:
                return n/3
                multiples_3_count += 1
        return (multiples_2_count*2)*(multiples_3_count*3)

intbreak = Solution()

print(intbreak.integerBreak(15))

