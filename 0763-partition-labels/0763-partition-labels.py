# 【什么是贪心】 每步都选择当前的局部最优解，且局部最优解不损害全局最优解，且不回头
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 题目是什么意思：将s划分为不同区间，每个区间中的字母不会出现在其他区间
        # brutal: 尝试所有切分点
        # 做hash: 帮助确认每个字母在序列中出现的最后一个位置
        # 找区间end: 这个区间内的所有字母出现的最后一个位置不能在end右边
        # if i == end，当前索引已到达这个区间内的所有字母出现的最后一个位置的最大值，可以切分
        last = {}
        for i,c in enumerate(s):
            last[c] = i # O(n);O(26)
        
        ans = []
        start = end = 0 # 当前正在处理的区间

        for i,c in enumerate(s):
            end = max(end,last[c]) 

            if i==end:
                ans.append(end-start+1)
                start = end+1
        return ans
        # O(n);O(26)
