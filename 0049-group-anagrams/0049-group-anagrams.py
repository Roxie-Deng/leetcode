class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 本质上是去重
        # hash str: Counter or 字符串排序（后者明显更简单）
        ans = defaultdict(list) # sorted_s:s1,s2 # O(n*k) space

        for s in strs: # O(n) time
            sorted_s_list = sorted(s) # 不改变原有的s # O(klogk) time; O(k) space
            sorted_s = "".join(sorted_s_list) # O(k) time; O(k) space
            ans[sorted_s].append(s)
        ans = list(ans.values())
        return ans

        # O(n*klogk);O(n*k)