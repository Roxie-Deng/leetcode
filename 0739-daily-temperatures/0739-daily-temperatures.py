class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n # output，初始值均为0
        st = [] # 单调栈，存储下标

        for i in range(n-1,-1,-1): # 从右向左遍历temperatures
            t = temperatures[i] # 第i天温度
            while st and t >= temperatures[st[-1]]: # st存储下标,对应的温度为从栈底到栈顶递减
                st.pop() # 栈顶那天不可能成为左边任何一天的第一个更高温度，弹出
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

        # O(n): 每个元素操作次数。虽有while，单个元素最多做两次操作，pop()次数<=n
        # O(n)：额外内存