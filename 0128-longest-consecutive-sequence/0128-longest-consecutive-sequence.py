class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        # O(n) time: NO sorting
        # 一边遍历一边查找, 操作还得是O(1) -> hash -> set的成员检查

        # 只需要unique nums
        set_nums = set(nums) # O(n);O(n)
        longest = 0

        for x in set_nums:
            if x-1 not in set_nums: # 只有当x是起点时开始计数 # 因为有这层过滤，即便是for套while，每个x也只被访问一次
                cur_len = 1
                cur_num = x+1
                while cur_num in set_nums:
                    cur_len += 1
                    cur_num += 1
                longest = max(longest,cur_len)
        return longest
        # O(n);O(n)

        