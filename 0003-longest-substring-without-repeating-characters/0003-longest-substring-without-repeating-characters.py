class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash+双指针
        seen = defaultdict(int)
        longest = 0
        left = 0

        for right,c in enumerate(s):
            seen[c] += 1
            while seen[c] > 1:
                seen[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)
        return longest
        # O(n)每个c最多被左右指针各访问一次;O(256)