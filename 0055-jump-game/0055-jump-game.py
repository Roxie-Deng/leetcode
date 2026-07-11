class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # new_idx = i+[0,nums[i]]
        # target_idx = n-1
        # brutal: all possible paths, until true -> inefficient
        # 我们只需要知道能不能走出去,final_idx>=target_idx
        # 所以找到能走的最远位置就可以了
        # 从左往右遍历，维护一个变量furthest表示到目前为止全局能到的最远索引，如果当前索引i>furthest，说明不可能到达i更别提n-1；否则，更新furthest = max(furthest,i+nums[i])

        n = len(nums)
        furthest = 0
        
        for i in range(n):
            if furthest>=n-1:
                return True

            if furthest>=i:
                furthest = max(furthest,i+nums[i])
            else:
                return False
        # O(n);O(1)
            