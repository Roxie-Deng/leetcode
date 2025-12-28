class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    # 双向链表：向前、向后都可以实现O(1)时间
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = None # 业务规则：切断当前节点之后的所有节点，防止历史分叉

        # 将new node接到current node之后
        new_node.prev = self.current
        self.current.next = new_node

        # 更新当前页面为new node
        self.current = new_node
        # O(1)

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            # 指针回退
            self.current = self.current.prev
            steps -= 1
        return self.current.url
        # O(steps)
        
    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            # 指针前移
            self.current = self.current.next
            steps -= 1
        return self.current.url
        # O(steps)

     #space: O(n)      
     
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)