> python中的hash结构
>
> dict
>
> set
>
> frozenset:不可变的set
>
> 

# 有效的字母异味词

```python
'''
设置一个hash保存t的字母出现次数
遍历s的时候逐次递减
如果hash表全为0则返回True
'''
```

# 查找共用字符

```python
'''
一个hash表来更新每个字符字母出现次数
一个hash表来更新最小次数频次
'''
```

# 四数相加Ⅱ

```python
'''
分组+HASH
将O（n^4）降到O（N^2）
'''
```

# 三数之和

> ==重要==

```python
'''
HASH：两层for循环就可以确定 a 和b 的数值了，可以使用哈希法来确定 0-(a+b) 是否在 数组里出现过

问题：因为不能包含重复的三元组，去重困难

方法：双指针

先排序，保证数组有序
遍历数组，设置left = i+1, right = len(nums)-1
如果nums[i] + nums[left] + nums[right] > 0,则right向左移
如果nums[i] + nums[left] + nums[right] < 0,则left向右移
直到right = left

要注意重复元素的判断：
continue if i > 0 and nums[i] == nums[i-1]
right -= 1 while right > left and nums[right] == nums[right-1]
left += 1 while right > left and nums[left] == nums[left+1]

剪枝：
return res if nums[i] > 0
'''
```

# 四数之和

```python
'''
思路与“三数之和”一样
'''
```

