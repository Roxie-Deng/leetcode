class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n);O(1)
        # 自己和自己异或=0; 任何数和0异或=它自己
        # 所有数字异或操作最后的结果就是single number
        flag = 0

        for n in nums:
            flag ^= n
        return flag