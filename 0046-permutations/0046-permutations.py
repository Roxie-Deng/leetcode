class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # all possible paths -> dfs
        # for each path -> 每走到下一节点元素不重复
        n = len(nums)
        ans = []
        path = []
        fresh = [True]*n # 是否用过该元素的flag

        def dfs(j): # path下标
            if j == n:
                ans.append(path.copy())
                return # 找完一条path
            for i in range(n):
                if fresh[i]:
                    path.append(nums[i])
                    fresh[i] = False
                    dfs(j+1)
                    path.pop() # 恢复现场
                    fresh[i] = True # 标记为没用过
        
        dfs(0)
        return ans

        # 路径数:O(n!),每条路径处理复杂度 copy() O(n) -> O(n*n!)
        # O(n)