# 序言

> 数组是存放在==连续内存空间==上的==相同类型数据==的集合。
>
> - **数组下标都是从0开始的。**
> - **数组内存空间的地址是连续的**
> - **数组的元素是不能删的，只能覆盖**

# 二分插查找

> **二分查找法有以下几个前提：**
>
> - 1、数组为有序数组
> - 2、数组中不存在重复元素
>
> 所以，如果题目中包含以上两个条件，那么就可以思考能否使用二分查找法；相反，如果想使用二分查找法，就得去构造以上这两个条件。
>
> 
>
> **边界条件**
>
> - [left, right]\:
>
>   ```python
>   left = 0
>   right = len(nums) - 1
>   
>   while (left <= right) # 满足合法的边界条件
>   	middle = left + (right - left) / 2
>   	if nums[middle] > target:
>           # 因为范围为右闭，且nums[middle]已经大于target，
>           # 如果right = middle，则将nums[middle]又再次包含进去了，
>           # 那么没有任何意义，所以是right = middle - 1
>   		right = middle - 1 
>       # 同理
>       elif nums[middle] < target:
>           left = middle + 1
>       # nums[middle] == target
>   	else:
>       	return middle
>   ```
>
> - [left, right):
>
>   ```python
>   left = 0
>   right = len(nums)
>   
>   while (left < right) # 满足合法的边界条件
>   	middle = left + (right - left) / 2
>   	if nums[middle] > target:
>           # 因为范围为右开
>   		right = middle 
>       # 同理
>       elif nums[middle] < target:
>           left = middle + 1
>       # nums[middle] == target
>   	else:
>       	return middle
>   ```
>
>   ==根据区间的定义来确定边界条件==

# 334.递增的三元子序列

> **贪心**
>
> **双向遍历**

```python
'''
双向遍历：
定义两个数组min = max = [0] * n
一共遍历三次：
1.min[i]表示nums[:i]中最小值
2.max[i]表示nums[i:]中最大值
3.return True if min[i-1] < nums[i] < max[i+1]

时间复杂度：O(n)
空间复杂度：O(n)
'''

'''
贪心：
维护one和two两个变量，one表示最小值，two为第二小的值，只要出现nums[i] > two则返回True
'''
```

