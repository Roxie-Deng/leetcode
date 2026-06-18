class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 简单看分为两批：众数和非众数
        # 相同阵营+1，不同阵营-1 
        # 众数freq > n/2, 一定不会被非众数抵消完
        # Boyer-Moore 投票：候选元素计数器
        ans = hp = 0

        for x in nums:
            if hp == 0: # 更换候选元素
                ans = x
                hp = 1
            elif x == ans:
                hp += 1
            else:
                hp -= 1
        
        # 血条还在的
        return ans