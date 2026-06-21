class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 去重 -> hash
        # Counter or 字符串排序（考虑到key的创建选后者）
        
        group = defaultdict(list) # 只要key不存在自动创建空列表

        for s in strs:
            sorted_s = ''.join(sorted(s)) # eat -> aet
            group[sorted_s].append(s) # {'eat':['eat','ate','tea']}
        
        ans = list(group.values())

        return ans

        # O(n*k*logk); O(n*k)
        # 实际处理的总字符数 O(n*k)
            