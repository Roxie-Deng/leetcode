class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 先merge再sort O((m+n)log(m+n))
        # 题目要求log(m+n) -> 二分查找
        # 中位数的本质：1.左半个数 = 右半个数 （或者左边多一个） 2.左边所有元素<=右边所有元素
        # 我们可以分别在两个数组中间画一条分界线i,j，使得两个分界线的左边刚好包含左半部分所有元素
        # 0...i-1  and  0...j-1 左半
        # i...,j... 右半
        # 根据以上规律1，i确定时,j也确定.再来判断规律2，满足时即找到median
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1 # 确保nums1是较短数组(why: 二分范围更小，效率更高，边界处理更简单)
        
        m,n = len(nums1),len(nums2)
        # 左半个数
        left_half = (m+n+1)//2 # 如果m+n为偶数，左半个数:(m+n)//2;为奇数，左半个数:(m+n)//2+1

        left,right = 0,m # 注意右边界不是m-1，因为i可以取0和m

        while left<=right:
            # 划分左半，两个数组各需要贡献:
            i = (left+right)//2 # 在nums1上做二分
            j = left_half - i

            # 获取nums1左/右半，nums2左/右半边界值
            # 我们要找的分界线要满足：
            # nums1左边最大值<=nums2右边最小值
            # nums2左边最大值<=nums1右边最小值
            # i = 0 说明nums1左半没有元素，当然是可能的，为满足以上不等式用负无穷替代
            # i = m 说明nums1右半没有元素，用正无穷替代
            left1 = nums1[i-1] if i>0 else float('-inf')
            right1 = nums1[i] if i<m else float('inf')
            # nums2同理
            left2 = nums2[j-1] if j>0 else float('-inf')
            right2 = nums2[j] if j<n else float('inf')

            # 情况1:满足条件
            if left1<=right2 and left2<=right1:
                # m+n为奇数，median为左半部分最大值
                if (m+n)%2 == 1:
                    return max(left1,left2)
                # m+n为偶数，median为(左半部分最大值+右半部分最小值)//2
                else:
                    return (max(left1,left2)+min(right1,right2))/2.0
            # 情况2: i太大。nums1为合体的左半贡献太多个。那么比i大的切分点也统统不可能了
            elif left1>right2:
                right = i-1
            # 情况3: i太小
            else:
                left = i+1
    # O(log(m+n));O(1)