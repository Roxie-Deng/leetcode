# 查找O(1)，删除O(1) -> Hash and 双向链表
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict() # 实例化。有序字典：不仅存键值对还保存键插入的顺序
        self.capacity = capacity # 属性赋值

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # 只要访问了就挪到末尾
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) # 把key挪到末尾

        self.cache[key] = value # 无论在不在都要更新值

        # 删掉最久没用的
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # last默认值为True,弹出最后的；last为False时弹出最前面的
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)