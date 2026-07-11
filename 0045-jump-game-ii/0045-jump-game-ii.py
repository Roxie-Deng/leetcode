class Solution:
    def jump(self, nums: List[int]) -> int:
        # new_idx = i + [0,nums[i]]
        # min_jump 
        # brutal: all paths -> inefficient
        # 借用BFS的思想: I am on某一节点(i,nums[i])到一堆叶子节点 表示 我能去的所有范围 -> 找层数最少的
        # 想办法不必去访问所有叶子节点，我们只需要关心层数
        # 维护变量: cur_end表示当前这一跳能去的最远的idx，farthest表示cur_end范围内下一跳能去的最远的idx,当走到cur_end时，steps+1， 新的cur_end即之前的farthest

        steps = cur_end = furthest = 0
        n = len(nums)

        for i in range(n):
            if cur_end >= n-1:
                break

            furthest = max(furthest,i+nums[i])

            if i == cur_end:
                steps += 1
                cur_end = furthest
        return steps
        # O(n);O(1)