class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        cnt = 0

        for i in range(1,n):
            if s[i].lower() != s[i-1].lower():
                cnt += 1
        return cnt

    # O(n); O(1)