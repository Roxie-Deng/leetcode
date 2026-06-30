class Solution:
    def trap(self, height: List[int]) -> int:
        # 求和（遍历i，找i左边/右边最高，取最小，减去i）-> O(n^2)
        # 使用双指针，从两侧出发向中间走，动态更新左边最高和右边最高，每次只处理较矮的一侧，求和 (矮侧highest - height[矮侧下标])

        left = 0
        right = len(height)-1

        l_peak = r_peak = 0
        total = 0

        while left<right:
            if height[left]<height[right]: # 左侧更矮,左侧决定蓄水量
                if height[left] >= l_peak:
                    l_peak = height[left]
                else: # l_peak更高，水不会从左侧流出
                    total += l_peak-height[left]
                left += 1
            else: # 右侧更矮
                if height[right]>=r_peak:
                    r_peak = height[right]
                else:
                    total += r_peak-height[right]
                right -= 1
        
        return total
        # O(n);O(1)