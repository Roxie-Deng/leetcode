class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x1+x2 = target, return[i1,i2]
        seen = {}

        for i,x in enumerate(nums):
            complement = target-x 
            if complement in seen: # 若存在，肯定在x左边
                return [seen[complement],i]
            seen[x] = i 
        
        # O(n);O(n)