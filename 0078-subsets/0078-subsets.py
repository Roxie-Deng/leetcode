class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        # 递归参数: i: 下一步允许开始选择的位置
        # 当前问题：选择当前递归层要加入path的数字，引入循环变量j遍历nums，表示当前层正在尝试选的元素
        # 子问题：如果选了nums[j],下一递归层从哪里继续选
        # 递归参数变化：i-> j+1 (防止回头选)

        def dfs(i):
            ans.append(path.copy()) # 安全记录当前正在构造的path

            if i == n: return

            for j in range(i,n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
            # 结尾自动return
        
        dfs(0)
        return ans

        # time: copy:O(n), visit:O(branching options^depth)=O(2^n) -> O(n*2^n)
        # space: O(n)