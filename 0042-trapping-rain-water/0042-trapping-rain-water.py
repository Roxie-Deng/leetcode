class Solution:
    def trap(self, height: List[int]) -> int:
        # 能够接水是因为能形成凹槽：左柱，右柱，底
        # 对于一根柱子i, 找到一根右柱j使得j比i+1...j-1都高（也就是说在[i,j]范围内，i眼中j最高，j眼中i最高）
        # 装水范围[i+1,j-1],so i,j如果紧密相邻也是不行的
        # 木桶原理高度min(height[i],height[j])

        # 维护一个数组结构：记录j前见过的柱子，同时能够最快拿到i -> 栈
        # 入栈前，把比当前柱子矮的全部弹出，结算水量，再入栈
        
        stack = []
        n = len(height)
        cur_sum = 0

        for right in range(n):
            while stack and height[right]>height[stack[-1]]:# 可能形成凹槽
                # 开始出栈：1. 栈空掉
                bottom = stack.pop()

                if not stack: # 没有左柱
                    break # 去找下一个右柱
                
                # 2. 栈没空，有底也有左柱
                left = stack[-1]

                cur_sum += (right-left-1)*(min(height[left],height[right])-height[bottom])
            stack.append(right) # 矮柱，直接入栈
        return cur_sum
        # O(n);O(n)
