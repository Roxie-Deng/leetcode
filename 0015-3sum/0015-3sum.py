class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pick out ONE NUM(for loop), solve 2Sum
        # if hash 2Sum, hard to delete duplicates(we want value instead of index here)
        # To skip duplicate items and move pointers, we sort first

        # 2Sum + 2SumII(sorted)
        # 固定一个数+双指针
        # 外层循环：固定第一个数
        # 内层循环：从剩余数组的最小值和最大值开始，左指针i+1，右指针n-1向中间移动
        nums.sort() # O(nlogn);O(n)
        n = len(nums)
        ans = []

        for i in range(n-2): # loop through i, NOW PROBLEM: nums[j]+nums[k] = -nums[i], just like 2SumII
            if i>0 and nums[i-1] == nums[i]: # skip duplicates
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0: # add two smallest
                break # non-decreasing;往后走不可能再找到满足题目的i
            if nums[i]+nums[n-2]+nums[n-1]<0: # add two biggest
                continue # nums[i] is too small; i should be bigger
            
            # i is likely to generate triplets we want
            # begin to move 2 pointers
            left,right = i+1,n-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    # skip the duplicates of nums[left] or nums[right]
                    left += 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif s<0:
                    left += 1
                else:
                    right -= 1
        return ans

        # O(n^2);O(n)