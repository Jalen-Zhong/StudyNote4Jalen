# 图

## 深搜（DFS）

回溯算法，其实就是dfs的过程，这里给出dfs的代码框架：

```python
def dfs(parameters):
	if (终止条件)：
    	存放结果
        return
    
    for (选择：本节点所连接的其他节点)：
    	处理节点
        dfs(图，选择节点)# 递归
        回溯，撤销处理结果
```

## LeetCode

### [200. 岛屿数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-islands/description/)

#### DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directs = [[-1,0],[1,0],[0,-1],[0,1]]
        res = 0
        
        def dfs(x,y):
            if visited[x][y] == True or grid[x][y] == '0':# 深搜终止条件
                return
            visited[x][y] = True
            for direct in directs:
                directX = x + direct[0]
                directY = y + direct[1]
                
                if directX >= m or directX < 0 or directY >= n or directY < 0:# 方向终止条件
                    continue
                dfs(directX, directY)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    res += 1
                    dfs(i,j)
        return res
                
        
'''
用一个HASH MAP来存储图节点的访问情况
设置一个HASP MAP来模拟图上下左右方向
深搜终止条件为：图节点被访问过或图节点为水域
方向终止条件为：下一个需要访问的图节点越界
遍历所有图节点，每一次深搜的返回，都说明有唯一的岛屿存在，则岛屿数量+1
思考：
深搜的主要关注点在于终止条件
'''
```

#### BFS（没看任何解析手撕半小时做出来：）了）

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directs = [[-1,0],[1,0],[0,-1],[0,1]]
        res = 0

        def bfs(que):
            if not que: # 广搜终止条件
                return
            x, y = que.popleft()
            for direct in directs:
                directX = x + direct[0]
                directY = y + direct[1]
                if directX >= m or directX < 0 or directY >= n or directY < 0: # 入队条件
                    continue
                if visited[directX][directY] == False and grid[directX][directY] == '1': # 入队条件
                    visited[directX][directY] = True
                    que.append((directX, directY))
            bfs(que)

        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    visited[i][j] = True
                    que = collections.deque()
                    que.append((i,j))
                    res += 1
                    bfs(que)
        return res

'''
思路：用队列来保存图节点四周的节点，并标记被保存的节点
入队条件：1.节点未被标记且节点为陆地；2.节点不越界
广搜终止条件：队列为空，则初始化队列，岛屿数量+1（节点为空时则说明找到唯一岛屿）
遍历方式及条件：满足节点未被访问，且为陆地（遍历所有节点）
'''
```

