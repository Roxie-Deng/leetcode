class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 拓扑排序。入度法（开锁）：二维数组（邻接表）+计数器数组（记锁的数量）+队列（待处理的门） +计数器（已处理的数组）    
        # course:要上的课，pre:先修的课
        graph = [[] for _ in range(numCourses)] # 准备一个二维数组用于保存pre可解锁的course  e.g. [[1,0],[0,1]]-> [[1],[0]]
        # in-degree: 指向一个节点的箭头数量 (out-degree: 从一个节点出发的箭头数量)
        indegree = [0]*numCourses # 用于保存course需要的pre数量

        # 把依赖关系填入
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # 将所有没有pre的course放入队列
        q = deque(i for i in range(len(indegree)) if indegree[i]==0)

        # BFS
        studied = 0 # 记录已经学了多少门课程

        while q: 
            cur_c = q.popleft()
            studied += 1 # 学了一门课

            # 看学的这门课是哪些课的pre，也就是说看学的这门课能解锁哪些进阶课
            for higher_c in graph[cur_c]:
                indegree[higher_c] -= 1 

                # 当这门进阶课的先修课都学完了，进阶课也入队
                if indegree[higher_c] == 0:
                    q.append(higher_c)
        
        return studied == numCourses
        # N(nodes), E(edges)
        # 状态数（N+E），出队/入队复杂度O(1) -> 时间O(N+E)
        # 空间O(N+E)