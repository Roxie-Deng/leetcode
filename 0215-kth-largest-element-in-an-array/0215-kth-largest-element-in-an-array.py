class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brutal:排序
        # heap: 小根堆，维护一个size为k的heap，遍历完arr后根就是arr中第k大的数
        min_heap = []

        for num in nums:
            if len(min_heap)<k: # heap没满，num直接加入
                heapq.heappush(min_heap,num)
            else:
                # 当有比小根堆root更大的数字时，num加入heap
                if min_heap[0]<num:
                    heapq.heapreplace(min_heap,num) # heapq复杂度logk
        return min_heap[0]
        # O(nlogk);O(k)