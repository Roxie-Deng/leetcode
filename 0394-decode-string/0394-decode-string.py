class Solution:
    def decodeString(self, s: str) -> str:
        # nested: decode inner[] first and store it, then decode outer[] and store it
        # 先处理最内层[]，最内层会是在最后匹配到 -> stack
        stack = [] # 记录[]前的str，还要记录[]前的int
        # (repeat_num,cur_str)
        repeat = 0
        cur_str = ""
        for c in s:
            # int
            if c.isdigit():
                repeat = repeat*10 + int(c) # 一次只遍历一个字符，如果是两位数以上需要进行特殊处理
            # [
            elif c == "[":
                stack.append((repeat,cur_str))
                repeat = 0 # 重置
                cur_str = ""
            # ]
            elif c == "]":
                # 弹出最近一组
                repeat_times, prev_str = stack.pop()
                cur_str = prev_str + cur_str * repeat_times
            # str
            else:
                cur_str += c # (3,"") (2,"a") 
        return cur_str
        # O(n);O(n)