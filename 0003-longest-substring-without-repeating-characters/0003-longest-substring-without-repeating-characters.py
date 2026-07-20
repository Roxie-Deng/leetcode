class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brutal: for i in range(n) 里面套 for j in range(i,n), 枚举所有子串，筛选是否有重复字符，记录长度
        # 去重: hash
        # 避免嵌套循环: 使用双指针
        n = len(s)
        cur_max = 0
        left = right = 0
        char_freq = defaultdict(int) # 哈希表 char: freq

        for right in range(n):
            char_freq[s[right]] += 1
            while char_freq[s[right]] > 1:
                # 删除记录，缩小窗口
                char_freq[s[left]] -= 1
                left += 1
            # 记录长度
            cur_max = max(cur_max,right-left+1)
        return cur_max
        # O(n) 每个char被访问一次；O(26)
