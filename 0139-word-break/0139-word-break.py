class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # any word for w in wordDict in s, s = s-word, word for w in wordDict in s...
        # any word for w in wordDict == s

        @cache
        def dfs(remaining):
            if remaining == "":
                return True
            for word in wordDict:
                if remaining.startswith(word):
                    if dfs(remaining[len(word):]):
                        return True
            return False
        return dfs(s)
        # 状态数=参数的不同取值个数, n
        # 每个状态的工作量, for, m
        # Time: O(状态数*每个状态的工作量)=O(n*m)
        # Space: O(缓存大小+递归深度)=O(2n) O(n)