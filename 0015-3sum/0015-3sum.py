class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pick One Num + solve 2Sum on remaining array
        # if sorted: two pointers moving toward each other
        nums.sort()
        n = len(nums)
        ans =[]

        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]: #skip duplicates
                continue # move onto the next iteration
            if x + nums[i+1] + nums[i+2] > 0: # x is too big
                break 
            if x + nums[-2] + nums[-1] < 0: # x is too small
                continue

            # 2sum
            l = i+1
            r = n-1

            while l<r:
                s = nums[l]+nums[r]+x
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    # record solution
                    # move l & r to find the next solution while skiping duplicates
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1 # next candidate
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
        
        return ans
# Time: O(n^2)
# Space: O(1)
        