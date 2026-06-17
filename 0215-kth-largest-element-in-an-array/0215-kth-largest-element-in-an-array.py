class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 构建size为k的小根堆（根最小）装nums中最大的k个数，那么根就是nums中第k大的数
        min_heap = []

        for num in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,num) # 堆未满直接加入,堆维持min_heap[0]最小 # heapq模块,(堆列表,item)参数原地修改
            else:
                if num>min_heap[0]:
                    heapq.heapreplace(min_heap,num) #等价于pop(heap)+push(heap,item)
        
        return min_heap[0]
        # 遍历n,二叉树操作log k -> O(nlogk)
        # O(k)