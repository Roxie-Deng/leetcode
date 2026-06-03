class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0]) # 按左端点升序原地排序intervals

        ans = []
        for interval in intervals: # 遍历待排序/合并区间
            if ans and interval[0] <= ans[-1][1]: # ans不为空，且，待排序区间的左端点小于等于最后一个合并区间的右端点->合并
                # 更新合并区间的右端点
                ans[-1][1] = max(interval[1],ans[-1][1])
            else:
                ans.append(interval)
        return ans