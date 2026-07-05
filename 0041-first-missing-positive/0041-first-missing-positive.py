class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brutal: 放入一个哈希集合，从1开始往上数，第一个缺失的就是答案 O(n) and O(n)
        # 优化：数组本身能否哈希
        # 对于一个长度为n的数组，答案只可能在[1,n+1]产生
        # 只关心值为[1,n]的数字，把他们一一对应放在[0,n-1]的位置，比1小比n大的都当作垃圾
        # 遍历新数组，找到第一个不在正确位置的数字
        n = len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i] !=nums[nums[i]-1]:# num挪到索引num-1的位置 + 避免重复数字死循环
            # 为什么用while:换到i来的新数字当然还需要检查
                idx = nums[i]-1
                nums[i],nums[idx] = nums[idx],nums[i]
                # 必须先通过 x 固定原始值，再用 idx = x-1 锁定目标索引
                # 因为如果在交换语句中直接写 nums[nums[i] - 1]，
                # 当 nums[i] 先被赋值改变后，这个索引就会错位，导致数据被放到错误的位置。
        
        # 正数都去了正确的索引位置 nums[i] == i+1
        # 找到第一个nums[i] != i+1 ,里的值 i+1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # 如果1-n全部在位，答案就是n+1
        return n+1
        # O(n);O(1)