class Solution:
    def maxArea(self, height: List[int]) -> int:
        # width*height
        # width = right-left
        # height = min(height[left],height[right])
        # left,right move towards from two edges
        # width decreases; try to find higher height
        n = len(height)
        l,r = 0, n-1
        cur_max=0
        while l<r:
            if height[l]<height[r]:
                cur_max = max(cur_max,(r-l)*height[l])
                l += 1
            else:
                cur_max = max(cur_max,(r-l)*height[r])
                r -= 1
        return cur_max
        # O(n);O(1)