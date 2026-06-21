# 存单词+共同前缀 -> 最直观的想法是指针类，树结构，把每个字母作为一个节点，这样 'ap' 和 'app' 就能共用 'a' 和 'p'
# key: 字母 val: 下一个节点
class TrieNode: # 内部节点类
    def __init__(self):
        self.children = {}
        self.is_end = False # 结尾标记：标记单词是否结束

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # 如果树中还没有该字母新建一个节点挂上去
                cur.children[c] = TrieNode()
            cur = cur.children[c] # 移动指针
        cur.is_end = True # 遍历到最后一个节点，结尾标记为True

    def search(self, word: str) -> bool:
        # 需要遍历到end
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False # 路断了直接否定
            cur = cur.children[c]
        return cur.is_end # 检验结尾标记:是不是最后一个字母

    def startsWith(self, prefix: str) -> bool:
        # 不一定遍历到end
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False # 路断了直接否定
            cur = cur.children[c]
        return True # 不用检查是不是最后一个字母
    # O(L)
    # O(N*L) 单词个数*单词长度
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)