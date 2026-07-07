class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # {")":"("}
        if not s:
            return 0

        stack = [] # 用于存左括号的下标,同时检查valid parentheses
        # 当遇到(时入栈opening_idx, 当遇到)时，先弹出栈顶，计算closing_idx和opening_idx的距离，维护一个全局变量更新当前最大值
        # 放入-1当作基准起点，避免空栈
        stack.append(-1)
        # 如果)前面没有对应的有效(就会把-1弹出来，就会空栈，说明)是个无效)，此时把它的索引入栈当作新的地基
        n = len(s)
        cur_max = 0

        for i in range(n):
            if s[i] == ")":
                # 先弹出栈顶
                idx = stack.pop()
                # 1.栈没空，有效()
                if stack:
                    length = i-stack[-1] # 新的栈顶索引就是这段有效substring的前一位
                    cur_max = max(cur_max,length)
                # 2.栈空了，无效)
                else:
                    stack.append(i)
            else: #"("
                stack.append(i)
        return cur_max
        # O(n);O(n)