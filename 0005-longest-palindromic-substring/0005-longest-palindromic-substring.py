class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        start = 0
        # 回文：从中心往两边看，左右对称相等
        for i in range(n): # 枚举中心
            # 当回文串长度为奇数
            l = r = i
            while l>=0 and r<n and s[l] == s[r]: 
                l -= 1
                r += 1
                if r-l-1 > max_len: # r,l已发生变化
                    max_len = r-l-1
                    start = l+1
            # 当回文串长度为偶数，中心为两个字符
            l,r = i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
                if r-l-1 > max_len: # r,l已发生变化
                    max_len = r-l-1
                    start = l+1
        return s[start:start+max_len]
        # O(n*n/2);O(1)
        