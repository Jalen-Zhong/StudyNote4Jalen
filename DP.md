# 动态规划

## 背包问题

### 推到公式

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

#### 其他

> 在做0-1背包题目时，需要注意题意的转换！

### 完全背包

#### 先物后包

```python
def test_CompletePack(weight, value, bagWeight):
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(weight[i], bagWeight + 1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]
```

#### 先包后物

```python
def test_CompletePack(weight, value, bagWeight):
    dp = [0] * (bagWeight + 1)
    for j in range(bagWeight + 1):  # 遍历背包容量
        for i in range(len(weight)):  # 遍历物品
            if j - weight[i] >= 0:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]
```