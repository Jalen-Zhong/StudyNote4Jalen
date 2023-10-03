# 回溯算法

> **for循环横向遍历，递归纵向遍历，回溯不断调整结果集**
>
> **回溯是递归的副产品，只要有递归就会有回溯**。

> 回溯算法的的代码框架：
>
> ```python
> def backtracking(parameters):
> 	if (终止条件)：
>     		存放结果
>         	return
>     
>     	for (选择：本节点所连接的其他节点)：
>     		处理节点
>        	backtracking(路径，选择列表)# 递归
>        	回溯，撤销处理结果
> ```

# 组合问题

> N个数里面按一定规则找出k个数的集合

## 组合

```python
'''
回溯在递归之后，因为递归满足返回条件后，会return退出顶层递归函数，然后再pop()进行回溯

剪枝：
剪枝的地方在于循环不需要遍历的地方

假设n=4,k=4，那么第一层的循环就不需要取2了，因为从取2一定不能凑出k=4，同理第一层2，3，4都不取
第二层3，4都不取

解释：
因为[x, n]的数组长度起码应该是:

k-len(path)

才有继续搜索的可能， 那么就有:

n-x+1 = k-len(path)

解方程得:

x = n+1 - (k-len(path))

而且这个x是可以作为起点往下搜的 也就是:

for i in range(startidx, x+1)

这里的x是可以取到的
'''
```

## 组合总和Ⅲ

```python
'''
与"组合"相比多一个条件

剪枝：
两个剪枝
1.当sum(path) > n时，无意义，剪掉
2.当len(path) > k时，无意义，剪掉
'''
```

## 电话号码的字母组合

```python
'''
与"组合"和"组合总和Ⅲ"的地方不同在于，这里的遍历是遍历字符

注意遍历的对象

这里不需要用到startidx
'''
```

## ==组合总和Ⅱ==

> 一次过
>
> ==**重要**==
>
> **去重**
>
> **树层去重的话，需要对数组排序**

```python
'''
因为是组合且可以重复选择，所以startidx = i而不是i+1

如果是排列：startidx = 0

剪枝：
# 放在遍历里
if sum(path) + candidates[i] > target:
    continu 
    
or

# 放在判断条件里
if sum(path) > target:
	return
'''

'''
去重：
if i > startidx and nums[i] == nums[i-1] and used[i-1] == Flase:
	continue

注意这里一定要加上used[i-1] == Flase来表示树层的逻辑
比如：[1,1,2]
当used = [0,1,0]时，去重，因为第二个1不需要再组合了，因为第一个1已经与2组合成了[1,2]
而当used = [1,0,0]时，不能去重，因为去重后则[1,1,2]这个组合将会被去掉
'''
```

## 总结

**如果是一个集合来求组合的话，就需要startIndex，如"组合、组合Ⅲ"**

**如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，如“电话号码的字母组合”**



# 切割问题

> 一个字符串按一定规则有几种切割方式

### 分割回文串

> **其实切割问题类似组合问题**。
>
> 例如对于字符串abcdef：
>
> - 组合问题：选取一个a之后，在bcdef中再去选取第二个，选取b之后在cdef中再选取第三个.....。
> - 切割问题：切割一个a之后，在bcdef中再去切割第二段，切割b之后在cdef中再切割第三段.....。

```python
'''
与组合问题不同的是，切割问题的终止条件是判断分割线是否在字符串最后

path.append(s[startidx:i+1])也要判断是否满足s[startidx:i+1]是回文串

分割问题的精髓在于思考分割线，而不是类似于组合问题思考元素个体
'''
```



# 子集问题

> 一个N个数的集合里有多少符合条件的子集
>
> **组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点**

### 子集

```python
'''
与“组合”问题一样，只不过子集不需要终止条件，也不能剪枝，因为要找到树的所有节点，而不只是叶子节点
'''
```

# 排列问题

> N个数按一定规则全排列，有几种排列方式

## 全排列

> 不包含重复元素的全排列

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        self.backtracking(nums, path, res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(0, len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.backtracking(nums, path, res)
                path.pop()

'''
一次过
因为是排列，所以没有startidx,每次遍历都从0开始
因为每个元素只能取一次，所以要判断元素是否被选取：
if nums[i] not in path
'''
```

## ==全排列Ⅱ==

> 包含重复元素的全排列
>
> ==**重要**==
>
> **去重**
>
> **去重一定要对元素进行排序，这样我们才方便通过相邻的节点来判断是否重复使用了**

```python
# 重要！！！！！！！！！！！！！！！！！！！！！！
# 点后两个数相等，且后一个数没被取用（避免相同的数被二次取用）；或者当前数被取用（避免同一个数被二次取用），则跳过当前遍历（去重）
if i > startIndex(0) and candidates[i] == candidates[i - 1] and not used[i - 1] or used[i]:
	continue

'''
去重问题：
全排列：i > 0
组合：i > startidx
'''
```

# 棋盘问题

> N皇后解数独等等

### N皇后

```python
'''
主要难点是注意约束条件和定义棋盘判断约束条件
'''
```

# 总结

## 算法复杂度

![image-20231003152811944](C:\Users\iMAN\AppData\Roaming\Typora\typora-user-images\image-20231003152811944.png)