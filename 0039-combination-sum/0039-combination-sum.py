class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # all possible unique paths -> dfs。决策树对于每一个item: 选或不选
        path = []
        ans = []

        def dfs(i,left):
            if left == 0:
                ans.append(path.copy()) # 找到一个合法组合,path全局唯一要进行拷贝
                return
            
            # 没有可选的数字或背包超重->剪枝
            if i == len(candidates) or left<0:
                return

            # 不选
            dfs(i+1,left)

            # 选
            path.append(candidates[i])
            dfs(i,left-candidates[i])
            path.pop() # 恢复现场

        dfs(0,target)
        return ans

        # 对于tree: O(time) = 分支数^深度,O(space)=深度
        # 每一层节点数: N，递归深度: target/min
        # O(N^(traget/min))
        # O(target/min)
