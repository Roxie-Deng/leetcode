class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # start_i<=start_j<=end_i, [start_i,max(end_i,end,j)]
        # 先升序排序，这样我们可以确保当前处理的区间要么与前面的合并，要么放在后面
        # 维护一个结果列表merged，比较merged[-1].end 和 正在遍历的interval.start

        intervals.sort() # 默认按第一个元素排序 O(nlogn)

        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else: # interval.start <= merged[-1].end 有重叠，合并，更新merged[-1].end 
                end = max(merged[-1][1],interval[1])
                merged[-1][1] = end
        return merged
        # O(nlogn);O(n)
