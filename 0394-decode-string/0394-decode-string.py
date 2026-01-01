class Solution:
    def decodeString(self, s: str) -> str:
        # nested; full completion relies on the inner scope; temporarily store inner, restore outer later -> stack
        # sub-problem -> recursion
        k = 0 # repeat count on current bracket level
        ans = '' # built_string on current bracket level
        stack = [] # each element: (ans,k) tuple; "LIFO", the most inner barcket will be processed first, outer last; outer = outer_str + k* inner_str

        for c in s:
            if c.isalpha():
                ans += c
            elif c.isdigit():
                k = k*10 + int(c) # accumulate consecutive digit characters to form k
            elif c == "[": # recursion
                stack.append((ans,k))
                k = 0
                ans = ''
            else: # ']'
                pre_ans, pre_k = stack.pop()
                ans = pre_ans + pre_k*ans
            
        return ans
        # O(n^depth);O(depth+n)