class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # width*height
        # (r-l+1)*height
        # 一条柱子所能形成的最大矩形一定是往两边扩展，直到遇到比它更矮的,遍历每根柱子找到所有可能
        n = len(heights)
        '''
        max_area = area = 0
        for i in range(n):
            h = heights[i]
            left = i
            while left>=0 and heights[left]>=h:
                left -= 1
            right = i
            while right<n and heights[right]>=h:
                right += 1
            # 跳出循环的left,right是比h矮的柱子的坐标，不是求面积的坐标 r-l+1-2
            area = (right-left-1)*h
            max_area = max(max_area,area)
        return max_area
        # O(n^2);O(1)
        '''
        # 优化思路：维护一个数据结构来存储“候选柱子”
    # 核心观察：从左到右遍历时，如果当前柱子 i 比前面某根柱子 j 矮，
    # 那么 i 就成了 j 的右边界（因为 j 无法再向右扩展），此时可以立即结算 j 的面积，并从候选集合中移除 j。
    # 由于 j 被移除后，i 左边剩下的柱子都比 i 高（否则会继续被弹出），
    # 因此这个数据结构中，从栈底到栈顶，柱子的高度是严格递增的 —— 这就是单调栈。
    # i就是右边界
    # 栈中存储的是柱子的下标，栈顶是当前最靠右的候选柱子，
    # 当弹出栈顶柱子 j 时，它的左边界就是新的栈顶（即左边第一个比它矮的柱子），若栈为空则左边界为 -1。
        stack = [] # 栈顶是最右边的候选柱子
        max_area = 0
        for right in range(n+1):
            # 最后一根柱子也是候选柱子，在它右边造一根虚拟柱
            h = heights[right] if right<n else 0
            while stack and h<heights[stack[-1]]:
                j = stack.pop()
                height = heights[j]
                left = stack[-1] if stack else -1 # 左边界是左边第一个严格小于当前高度的柱子,如果左边没有柱子就应该为-1 
                max_area = max(max_area,height*(right-left-1))
            stack.append(right)
        return max_area
        # O(n);O(n)