class Solution:
    def maxArea(self, height: List[int]) -> int:
         # find maximum of: min(height[l],height[r])*(r-l)
        cur_max = a = h = 0
        n = len(height)

        # left, right pointers move towards each other to decrease (r-l)
        l = 0
        r = n-1

        while l<r:
            h = min(height[l],height[r])
            a = (r-l)*h
            cur_max = max(cur_max,a)

            if height[l] < height[r]: # left move
                l += 1
            else: 
                r -= 1

        return cur_max
            
