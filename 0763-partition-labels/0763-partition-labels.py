class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 将s划分为不同区间，每个区间中的字母不会出现在其他区间
        # 区间贪心
        last = {}
        for i, c in enumerate(s):
            last[c] = i # 记录每个字符最后出现的下标

        ans = []
        start = end = 0 # 正在被处理的区间

        for i,c in enumerate(s):
            end = max(end,last[c]) # 动态更新当前区间的最远位置
            if end == i: 
                ans.append(end-start+1)
                start = end+1
        return ans
        # O(n);O(26)