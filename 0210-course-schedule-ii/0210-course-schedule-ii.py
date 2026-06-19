class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 拓扑排序
        # 依赖关系数组
        graph = [[] for _ in range(numCourses)]
        # 计数器数组,每门course需要的pre数量
        indegree = [0]*numCourses

        # 填充graph 和indegree
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 待处理队列：无先修课程的课程
        # 出队入队O(1),
        q = deque(i for i in range(numCourses) if indegree[i] == 0)

        # 答案容器
        ans = []

        while q:
            cur_c = q.popleft()
            ans.append(cur_c)

            for higher_c in graph[cur_c]:
                indegree[higher_c] -= 1

                if indegree[higher_c] == 0:
                    q.append(higher_c)
        
        return ans if len(ans) == numCourses else []

# O(N+E); O(N+E)