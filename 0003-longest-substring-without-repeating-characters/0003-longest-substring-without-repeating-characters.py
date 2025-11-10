class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict: {char: occurence}
        showed = defaultdict(int)
        ans = 0
        left = 0

        for right,c in enumerate(s):
            showed[c] += 1
            # shrink the window: value>1
            while showed[c] > 1:
                showed[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        
        return ans