class MedianFinder:
    # 不停地收到数字，随时输出当前列表的中位数
    # len is odd,就是中间那个数；even, 是中间两个数的平均值
    # 暴力：每次排序
    # 优化：把数字分成两堆（小堆，大堆），能够快速heappop得到小堆最大值和大堆最小值 -> 小堆用大根堆，大堆用小根堆
    def __init__(self):
        # 外部值 self.属性 = 参数
        # 内部属性 self.属性 = 新建对象
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        # 先加左，最大值推右，后平衡

        # heapq默认实现小根堆（根节点小于子节点）。我们通过取负数实现大根堆
        heapq.heappush(self.left, -num) 
        # 把左堆最大值放入右堆，确保右堆都比左堆大
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # 如果数量不平衡，把右堆最小的还给左堆（记得取反）
        if len(self.left)<len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
    # O(logn);O(n)
    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0] # 只能取值，不能pop
        else:
            return (-self.left[0]+self.right[0])/2.0
    # O(1);O(n)

    # heappush,heapop O(logn); heapify O(n) 所有下层步数总和是收敛到n的

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()