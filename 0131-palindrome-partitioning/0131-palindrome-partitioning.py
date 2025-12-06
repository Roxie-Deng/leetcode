class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        # imagine there is a separator after each char
        # current question: which separator to choose
        # sub question: next separator to choose (cannot revisit)
        # param: i -> the starting point of next decision; j -> loop variable to iterate str/separators
        def dfs(i):
            if i == n: # s cannot be divided anymore
                ans.append(path.copy())
                return
            for j in range(i,n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return ans

        # time: copy O(n), visit O(2^n) -> O(n*2^n)
        # sapce: O(n)