class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area=min(height[l],height[r])*(r-l)
        # r-l 必然会逐渐缩小
        # 高尽量取更大
        l,r = 0, len(height)-1
        cur_max = 0

        while l<r:
            width = r-l
            if height[l]<height[r]:
                # 现在以左为高，算完面积收缩左边
                cur_max = max(cur_max,height[l]*width)
                l += 1
            else:
                cur_max = max(cur_max,height[r]*width)
                r -= 1
        return cur_max
        # O(n);O(1)