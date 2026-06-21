class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n): 不能排序；不能嵌套
        # for遍历O(n) -> 操作每个元素的复杂度必须为O(1) -> Hash
        unique = set(nums)
        longest = 0

        for x in unique:
            # 只有当 x 是序列的起点时开始计数
            if x-1 not in unique:
                cur_num = x
                cur_len = 1
                while cur_num + 1 in unique:
                    cur_num += 1
                    cur_len += 1
                longest = max(longest,cur_len)
        return longest
        # O(n):O(n)