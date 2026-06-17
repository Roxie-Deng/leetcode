class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 维护一个大小为 k 的最小堆，堆中存储 (频率, 元素) 元组（Python 的堆默认按元组第一个元素排序）
        counts = Counter(nums) # dict {num:cnt}

        min_heap = []

        for num,cnt in counts.items():
            if len(min_heap)<k:
                heapq.heappush(min_heap,(cnt,num))
            else:
                if cnt>min_heap[0][0]:
                    heapq.heapreplace(min_heap,(cnt,num))
        return [num for cnt,num in min_heap]

        # 遍历O(n)*2,二叉树O(logk) -> O(nlogk)
        # hash:O(n),heap:O(k) -> O(n)