# 二叉树

## 二叉树的定义

1. 数组
2. 链表

```python
class TreeNode:
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right
```

## 二叉树的遍历

> 前中后序遍历的逻辑其实都是可以借助**栈使用递归的方式**来实现的，而广度优先遍历的实现一般使用队列来实现。**用栈来实现递归的写法，也就是所谓的迭代法**
>
> **递归的实现就是：每一次递归调用都会把函数的局部变量、参数值和返回地址等压入调用栈中**，然后递归返回的时候，从栈顶弹出上一次递归的各项参数，所以这就是递归为什么可以返回上一层位置的原因。
>
> ==**在分析遍历的时候（链表的时候）注意要一个一个节点去分析，不然很容易混淆**==

1. 前序遍历（深度优先遍历） 

   > 递归法

   ```python
   class TreeNode:
   	def __init__(self,val=0,left=None,right=None):
           self.val = val
           self.left = left
           self.right = right
   class Solution:
       def preorderTraversal(self, root):
           if not root:return []
       
       	left = self.preorderTraversal(root.left)
           right = self.preorderTraversal(root.right)
           
           return [root.val] + left + right
       
   if __name__=='__main__':
       root = TreeNode(3, TreeNode(9), TreeNode(1, TreeNode(2), TreeNode(7)))
       print(Solution().preorderTraversal(root))
   	
   ```

   > 迭代法
   >
   > ```python
   > class Solution:
   >     def preorderTraversal(self, root):
   >         if not root: return []
   > 
   >         stack = [root]
   >         res = []
   >         while stack:
   >             node = stack.pop()
   >             res.append(node.val) # 先处理中节点
   >             if node.right:
   >                 stack.append(node.right) # 右节点先入栈
   >             if node.left:
   >                 stack.append(node.left) # 左节点后入栈
   > 
   >         return res
   > '''
   > 先处理根节点
   > 再分别处理右 左节点
   > 因为栈推出时顺序为左 右
   > 最后的遍历顺序为中→左→右
   > '''
   > ```
   >
   > 

2. 中序遍历（深度优先遍历）

   > 递归法

   ```python
   class Solution:
       def inorderTraversal(self, root):
           if not root:return []
       
       	left = self.preorderTraversal(root.left)
           right = self.preorderTraversal(root.right)
           
           return left + [root.val] + right
   ```

   > 迭代法（**中序遍历的迭代法与前后遍历思路不一致**）
   >
   > ```python
   > class Solution:
   >     def inorderTraversal(self, root):
   >         if not root:return
   >     	
   >         stack = []
   >         res = []
   >         cur = root
   >         while cur or stack:
   >             if cur:
   >                 # 找到最左的叶子节点，该过程中不断将父节点压入栈中
   >                 stack.append(cur)
   >                 cur = cur.left # 这里最后的cur.left可以理解为指向None
   >             else:
   >                 # 到达最后节点后处理栈顶元素
   >                 cur = stack.pop()
   >                 res.append(cur.val)
   >                 cur = cur.right
   > 		return res
   > 
   >  '''
   >  出栈的顺序即使遍历顺序，主要关注入栈的元素和顺序
   >  '''
   > ```
   >
   > 

3. 后序遍历（深度优先遍历）

   > 递归法

   ```python
   class Solution:
       def postorderTraversal(self, root):
           if not root:return []
       
       	left = self.preorderTraversal(root.left)
           right = self.preorderTraversal(root.right)
           
           return left + right + [root.val] 
   ```

   > 迭代法
   >
   > ```python
   > class Solution:
   >     def preorderTraversal(self, root):
   >         if not root: return []
   > 
   >         stack = [root]
   >         res = []
   >         while stack:
   >             node = stack.pop()
   >             res.append(node.val) # 先处理中节点
   >             if node.left:
   >                 stack.append(node.left) # 左节点先入栈
   >             if node.right:
   >                 stack.append(node.right) # 右节点后入栈
   > 
   >         return res[::-1]
   > 
   > '''
   > 后序遍历顺序为：左右中
   > 入栈顺序为：中左右
   > res的遍历顺序（出栈顺序）为：中右左
   > res[::-1]的遍历顺序为：左右中
   > '''
   > ```
   >
   > 

4. 层序遍历（广度优先遍历）

```python
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return []

        que = deque([root])
        res = []
        while que:
            level = []
            for _ in range(len(que)):
                out = que.popleft()
                level.append(out.val)
                if out.left:
                    que.append(out.left)
                if out.right:
                    que.append(out.right)
            res.append(level)
        return res
    

```



> **[可视化](https://pythontutor.com/visualize.html#mode=edit)**： [Python Tutor code visualizer: Visualize code in Python

## 二叉搜索树

#### 定义

> 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
> 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
> 它的左、右子树也分别为二叉搜索树

#### 性质

> 在进行中序遍历时，节点的val总是递增的

## 二叉树的公共祖先

#### 二叉树的最近公共祖先

> [236. 二叉树的最近公共祖先 - 力扣（LeetCode）](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/)
>
> ```python
> class Solution:
>     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
>         if root is None or root == q or root == p:
>             return root
>         
>         left = self.lowestCommonAncestor(root.left, p, q)
>         right = self.lowestCommonAncestor(root.right, p, q)
> 
>         if left and right:
>             return root # 这里的root就是公共祖先的原因是因为是从该节点（root）向下遍历递归的
>         if not left and right:
>             return right
>         if left and not right:
>             return left
>         else:
>             return None
>         
> '''
> 后序遍历
> '''
> ```
>
> 

#### 搜索二叉树的最近公共祖先

## LeetCode

### 二叉树的属性

#### [257. 二叉树的所有路径 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-paths/description/)

```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 1.特殊情况
        # 2.递归
            # 2.1 遇到叶子节点时就将path路径保存
            # 2.2 保存后回溯到上一个节点（这里用栈来实现回溯的逻辑）
        if not root:return []
        path = []
        res = []
        self.dfs(root, path, res)

        return res
        
    def dfs(self, root, path, res):
        path.append(root.val)
        if not root.left and not root.right:
            res.append('->'.join(map(str, path)))
        if root.left:
            self.dfs(root.left, path, res)
            path.pop() # 回溯在这里！！！！！！！！！！
        if root.right:
            self.dfs(root.right, path, res)
            path.pop()
           
'''
注意理解递归的时候，要理解递归的底层逻辑是用栈来实现的，其本质是将函数帧压入栈
这里的pop()这是在栈为空的时候进行，其逻辑是函数帧栈为空，则执行path的回溯（这里的回溯
底层逻辑也是栈）
'''
```

