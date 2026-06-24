class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 保证在子串中，不同的字母出现次数为k
        # 涉及统计次数 -> hash
        # longest -> 遍历右枚举左
        left = 0
        ans = 0 # 有效窗口长度
        seen = defaultdict(int)
        max_count = 0 # seen字典中最大的val

        for right, c in enumerate(s):
            seen[c] += 1 
            max_count =  max(max_count,seen[c])
            # 破坏窗口 L-max_count > k 
            if right-left+1 - max_count > k:
                seen[s[left]] -= 1
                left+=1 
            ans = max(ans,right-left+1)
        return ans
        # O(n);O(1)


