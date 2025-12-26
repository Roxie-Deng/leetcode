class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # bisect: 在有序列表中快速找到某个元素应插入的位置
        n = len(arr)
        span =n//4 +1
        for i in range(0,n,span):
            l = bisect.bisect_left(arr,arr[i])
            r = bisect.bisect_right(arr,arr[i])
            if r-l >= span: # 满足题目条件
                return arr[i]
        return -1

    # O(logn); O(1)