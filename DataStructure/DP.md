# 动态规划

## 步骤

> 1. 确定dp数组（dp table）以及下标的含义
> 2. 确定递推公式
> 3. dp数组如何初始化
> 4. 确定遍历顺序
> 5. 举例推导dp数组

## 背包问题

### 推导公式

```python
dp[i] = max(dp[i], dp[i - weight[i]] + value[i])

'''
物品有重量和价值两个纬度
'''
```

```python
dp[i] += dp[i - weight[i]]

'''
物品只有一个纬度
'''
```

```python
dp[i] = dp[i] or dp[i - weight[i]]
```

```
dp[i] = min(dp[i], dp[i - weight[i]])
```



### 0-1背包

#### 二维dp

> 要先遍历物品，再遍历背包

```python
def knapsack_01(weight, value, bagweight):
    # 二维数组
    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品个数
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(bagweight + 1):  # 遍历背包容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[len(weight) - 1][bagweight]
```

#### 一维dp

> 要先遍历物品，再遍历背包，背包遍历要从大到小遍历，保证物品只放一次

```python
def knapsack_01(weight, value, bagWeight):
    # 初始化
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(bagWeight, weight[i] - 1, -1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[bagWeight]
```

#### 总结

> 在做0-1背包题目时，需要注意题意的转换！
>
> **0-1背包一定要先遍历物品再遍历背包，因为要保证物品只取一次。**
>
> **0-1背包的一维dp写法需要从大到小遍历物品，保证物品只取一次**

### 完全背包

#### 外物内包

```python
def test_CompletePack(weight, value, bagWeight):
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(weight[i], bagWeight + 1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]
```

#### 外包内物

```python
def test_CompletePack(weight, value, bagWeight):
    dp = [0] * (bagWeight + 1)
    for j in range(bagWeight + 1):  # 遍历背包容量
        for i in range(len(weight)):  # 遍历物品
            if j - weight[i] >= 0:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]
```

#### 总结

> **如果求组合数就是外层for循环遍历物品，内层for遍历背包**。
>
> **如果求排列数就是外层for遍历背包，内层for循环遍历物品；强调顺序就是排列**
>
> 举一个例子：计算dp[i]的时候，结果集只有 {A,B} 这样的集合，不会有{B,A}这样的集合，因为staffs = {A，B，C}遍历放在外层，B只能出现在A后面！
>
> **如果是求最小，则遍历顺序没有关系，因为并不强调集合是组合还是排列**
>
> 如果求最小值，初始化为：dp = [inf] * (nums + 1)
>
> 如果求最大值，初始化为：dp = [0] * (nums + 1)

## 打家劫舍

### 普通打家劫舍

```python
# 确定下标，i个房屋以内能偷的最大价值
dp = [0] * len(nums)
#初始化
dp[0],dp[1] = nums[0], max(nums[0], nums[1])
#递推公式
dp[i] = max(dp[i-1],dp[i-2] + nums[i])
```

### 环形打家劫舍

```python
# 不考虑偷第一家
no_head_rob = rob(nums[1:len(nums)])
# 不考虑偷最后一家
no_tail_tob = rob(num[0:len(nums)-1])
```

### 树形打家劫舍

```python
'''
需要后续遍历，因为要先处理两个子节点
把偷与不偷的情况都存储到dp = [偷，不偷]中，最后输出max(dp)即可
'''
```

## 买卖股票

### 只能买卖一次

```python
# 持有股票的状态下手中利润的最大值dp[i][0]应该等于买（-prices[i]）或不买(dp[i-1][0])的最大值：
dp[i][0] = max(-prices[i], dp[i-1][0])

# 不持有股票的状态下手中利润最大值dp[i][1]应该等于卖（dp[i][0] + prices[i]）或不卖(dp[i][1])的最大值
dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])

# 初始化
dp[0][0] = -prices[0]

'''
1.第i天的利润情况有两种 —— 持/不持股票的利润
2.第i天的利润情况与第i-1天有关
3.只要保持第i天前的每一天持/不持股票的最大利润，则第i的最大利润便可求解出来
4.买卖只是一个状态变化的条件，而不是状态本身，状态本身仍然是手中持/不持股票情况下的最大利润
'''
```

### 买卖多次

```python
# 持有股票的状态下手中利润的最大值dp[i][0]应该等于买（dp[i-1][1]-prices[i]）或不买(dp[i-1][0])的最大值：
dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])

# 不持有股票的状态下手中利润最大值dp[i][1]应该等于卖（dp[i][0] + prices[i]）或不卖(dp[i][1])的最大值
dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])

# 初始化
dp[0][0] = -prices[0]

'''
1.第i天的利润情况有两种 —— 持/不持股票的利润
2.第i天的利润情况与第i-1天有关
3.买卖只是一个状态变化的条件，而不是状态本身，状态本身仍然是手中持/不持股票情况下的最大利润
'''
```

### 至多2次买卖

```python
'''        
一天一共就有五个状态:
没有操作 （其实我们也可以不设置这个状态）:dp[i][0] = 0
第一次持有股票:dp[i][1] = max(dp[i-1][1], dp[i][0] - prices[i])
第一次不持有股票:dp[i][2] = max(dp[i-1][2], dp[i][1] + prices[i])
第二次持有股票:dp[i][3] = max(dp[i-1][3], dp[i][2] - prices[i])
第二次不持有股票:dp[i][4] = max(dp[i-1][4], dp[i][3] + prices[i])

初始化：
dp[0][1], dp[0][3] = -prices[0], -prices[0]
因为第二次持有股票（第二次买入）是依赖于第一次卖出状态，其实相当于第0天第一次买入了，第一次卖出了，然后再买入一次（第二次买入），那么现在手头上没有现金，只要买入，现金就做相应的减少。
'''
```

### 至多k次买卖

```python
'''
与至多2次买卖思路一样，一天有2*k+1个状态

初始化：
for kk in range(k):
	dp[0][2*kk + 1] = -prices[0]
'''
```

### 多次买卖含冷冻期

```python
'''
持有股票 dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i]):要么不买，要买也是只能在'持/不冷'状态下买
不持有股票,并在冷冻期 dp[i][1] = dp[i-1][0] + prices[i]：只能是当天卖股票
不持有股票，不在冷冻期 dp[i][2] = max(dp[i-1][2], dp[i-1][1])：'不持/冷' or '不持/不冷' 

初始化：
dp[0][0] = -prices[0]
'''
```

### 多次买卖含手续费

```python
'''
持有股票：dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
不持有股票： dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

初始化：
dp[0][0] = -prices[0]
'''
```

## 子序列问题

### 最长递增子序列

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)

'''
dp[i]表示第i个位置最长递增子序列的长度
nums[i]需要和nums[0:i]（nums[j]）前所有值比较，如果nums[i]大于nums[j]啊，
则dp[i] = dp[j]+1
初始化：因为每个元素其本身的最长递增子序列为其本身，即1
'''
```



### 最长连续递增子序列

> 子序列连续

```python
'''
dp[i] = dp[i-1]+1 if nums[i] > nums[i-1]
'''
```

### 最长重复子序列

> 子序列连续

```python
if nums1[i-1] == nums2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
'''
这是典型的体现DP底层HASH表逻辑的题目，仔细体会
若序列递增，则在上一层的基础上+1,即：dp[i][j] = dp[i-1][j-1] + 1
'''
```

### 最大子序和

> 子序列连续

```python
dp[i] = max(dp[i-1] + nums[i], nums[i])

'''
要么是nums[i]，要么是前i最大加nums[i]
'''
```



### 最长公共子序列

> 子序列不连续

```python
if nums1[i-1] == nums2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
'''
与"最长重复子序列"不同的地方在于这里需要考虑到无序的情况

即ABC与ACE考虑ABC与AC的情况和考虑AB和ACE的情况，即dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
'''
```

### 不相交的线

> 子序列不连续

```
'''
同上
'''
```

### 判断子序列

> 编辑距离

```python
if s2[j-1] == s1[i-1]:
    dp[i][j] = dp[i-1][j-1]

'''
当s1[i] == s2[j]时，dp[i][j]的状态取决于dp[i-1][j-1],即s2[:j-1]的字符是否是s1[:i-1]的子序列,如果是，则s2[:j]也是s1[:i]的子序列
'''
```



### 不同子序列

> 编辑距离
>
> ==与'判断子序列'不同的地方在于，一个是是否存在，一个是存在几个==
>
> =='判断子序列'的当前状态也就只与s2[:j-1]和21[:i-1]的情况有关==
>
> ==’不同子序列‘的当前状态需要多考虑s2[:j]是否已经是s1[i-1]的子序列情况，也就是dp[i-1] [j]的情况==

```python
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
else:
    dp[i][j] = dp[i-1][j]
    
'''
下标定义：
dp[i][j]表示s2[:j]在s1[:i]子序列的个数

与"判断子序列"不同的地方在于，当s1[i] == s2[j]时，dp[i][j]的状态来源于选和不选s1[i]这个字符。
选：s2[:j-1]之前有n1个属于s1[:i]的子序列，那么选就有s2[:j]就在s1[:i]有n1个子序列
不选：s2[:j]之前有n2个属于s1[:i]的子序列，那么不选仍有n2个s2[:j]是s1[:i]的子序列
'''
```

### 两个字符串的删除操作

> 编辑距离

```python
if word1[j-1] == word2[i-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1)
    
'''
如果第word1第i个字符等于word2第2个字符，则最小删除步数应该等于dp[i-1][j-1]
如果不是，则删除步数应该为min(dp[i][j-1], dp[i-1][j]) + 1，因为word1和word2都能删，要选择最小的步数
'''
```

### 编辑距离

> 编辑距离

```python
 if word1[j-1] == word2[i-1]:
       dp[i][j] = dp[i-1][j-1]
 else:
       dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
       
'''
对于递推公式我的理解：
如果word1[j-1] == word2[i-1]，则当前状态（dp[i][j]）继承上一个状态（dp[i-1][j-1]）
如果word1[j-1] ！= word2[i-1]，则当前状态为三种状态转移而来，分别是：
dp[i][j-1] + 1:表示增加一个字符
dp[i-1][j-1] + 1:表示修改一个字符
dp[i-1][j] + 1: 表示删除一个字符
取最小操作数，即min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1即可
'''
```

## 回文

### 回文子串

```python
'''
状态转移方程：
dp[i][j] = dp[i+1][j-1]，表示从下标i到j是不是回文子串，取决于从下标i+1到j-1是不是回文子串

转移条件：
1.j - i < 2 and s[i] == s[j]：表示一个字符和两个字符的情况，这一定是回文子串
2.j - i > 2 and s[i] == s[j]：表示三个以上的字符的情况，这种情况是不是回文子串取决于中间字符是不是回文子串
3.s[i] != s[j]：一定不是回文子串

遍历顺序：
for i in range(len(s)-1, -1, -1):
	for j in range(i, len(s)):
	
会用到没有计算过的dp[i + 1][j - 1]来判断了[i,j]是不是回文。
所以一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。
且i不能大于j

总结：
状态转移方程和遍历顺序不容易想，可以开阔思路
'''
```

### 最长回文子串

```python
'''
ij含义：dp[i][j]表示从下标i到j最长的回文子序列长度

状态转移： 
dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j]
dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if s[i] != s[j]

解释：
如果s[i]与s[j]不相同，说明s[i]和s[j]的同时加入 并不能增加[i,j]区间回文子序列的长度，那么分别加入s[i]、s[j]看看哪一个可以组成最长的回文子序列。
加入s[j]的回文子序列长度为dp[i + 1][j]。
加入s[i]的回文子序列长度为dp[i][j - 1]。
'''
```

## 总结

> 做了一系列的动规题目下来，我对动规的理解：
>
> 1.DP的本质是用HASH MAP保存遍历时中间结果变量，牺牲空间换取时间
>
> 2.如果当前状态取决于前状态，那么就可以使用DP，其本质也是状态机
>
> 3.当一个问题可以不断分成无数个子问题，且子问题还可再分，且问题逻辑一样，那么就可以使用DP（DP与递归有相似之处）==（回文、背包）==
>
> 4.特别的要注意分析当前状态情况，有哪些状态？选或不选？这些状态由前面哪些状态推到而来？==（股票、打劫）==， 
>
> 5.在手推DP map的时候，注意用箭头画出当前状态的转移方向来源
