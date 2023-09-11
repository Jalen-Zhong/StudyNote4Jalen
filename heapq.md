# 堆

## 堆的性质

> 1. 大顶堆
> 2. 小顶堆
> 3. 堆总是一个完全二叉树

## 堆的应用

> 1. 堆可实现优先队列

## python关于堆的实现：

> 1. 直接调用import heapq API函数（关于heapq 可参考[Python中heapq模块浅析_heapq.heappush_chandelierds的博客-CSDN博客](https://blog.csdn.net/chandelierds/article/details/91357784)）
> 2. 手动构建堆

## 堆排序

#### heapq

```python
import heaqp
# 构造堆
a = [1,3,5,7,3,5,8,89]
	#小顶堆
min_head_heaqp = heapq.heapify(a)
	#大顶堆
max_head_heaqp = heapq.heapify([-x for x in a])
max_head_heaqp = [-x for x in a]

# 堆排
def heapq_sort(a):
	heapq.heapify(a)
	res = []
	while a:
		res.append(heappop(a))
	return res
```

#### 手动

> ```python
> # 构造堆（下沉构造最大堆）
> def heapify(arr, n, i):
>     largest = i
>     left = 2 * i + 1
>     right = 2 * i + 2
>     
>     # 如果左子节点大于根节点，则更新最大值的索引
>     if left < n and arr[left] > arr[largest]:
>         largest = left
>         
>    	# 如果右子节点大于根节点，则更新最大值的索引
>     if right < n and arr[right] > arr[largest]:
>         largest = right
>      
>     # 如果最大值不是父节点，则交换父节点和子节点的最大值
>     if largest != i:
>         arr[largest], arr[i] = arr[i], arr[largest]
>     
>     	#并对交换后的子树进行堆化
>         heapify(arr, n, largest)
> 
> #堆排
> def heap_sort(arr):
>     n = len(arr)
>     
>     # 构建最大堆，从最后一个非叶子节点开始堆化(注意这里是最后一个‘非’叶子节点)
>     for i in range(n//2 - 1, -1, -1)
>     	heapify(arr, n, i)
>         
>     # 逐个将最大值移到数组末尾，并重新堆化剩余的部分
>     for i in range(n - 1, 0, -1):
>         arr[i], arr[0] = arr[0], arr[i]  # 交换根节点和最后一个节点
>         heapify(arr, i, 0)  # 对剩余部分进行堆化(这里是'i')
>     return arr
>         
>     
> ```

