# 回溯算法

> 回溯算法的的代码框架：
>
> ```python
> def backtracking(parameters):
> 	if (终止条件)：
>     	存放结果
>         return
>     
>     for (选择：本节点所连接的其他节点)：
>     	处理节点
>         backtracking(路径，选择列表)# 递归
>         回溯，撤销处理结果
> ```
>
> 