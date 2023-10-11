> ```python
> A = 'aaa'
> print(A.join('bbb'))
> > baaabaaab
> print(A.replace('a', 'b'))
> > bbb
> A = '  aa b '
> print(A.strip())
> > aa b
> print(A.split())
> > ['aa','b']
> print(''.join(reversed(A))) # reversed(A)是一个生成对象
> > ' b aa  '
> 
> '''
> python语言常用字符串处理语法
> '''
> ```

# 反转字符串Ⅱ

```python
s = s[:i] + s[i:i+k][::-1] + s[i+k:]
```

# 反转字符串中的单词

```
'''
这种题目对于python语言相对来说更容易
但问题解决的思维方式与其他语言一致

用双指针解法严格的时间复杂度为O(n/2)
'''
```

# KMP

> ==重要==
>
> **作用：**字符串匹配问题
>
> **思想：**当出现字符串不匹配时，查找已经匹配过的字符，并跳过他们，避免重复匹配
>
> **做法：**先将被匹配字符s1的最长公共前后缀保存到数组next中，next[i]表示前i个字符的最长公共前后缀长度
>
> 利用next进行查表，若s1[j]与S[i]不匹配，则j = next[j-1]（找到该不匹配字符的前一个字符的长公共前后缀长度），一直找到s1[j] = S[i]或j=0（s1第一个字符）停止。如果字符串匹配，则指针j向前移动一位继续匹配。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = [0] * len(needle)
        # 先将被匹配字符needle的最长公共前后缀保存到数组next中，
        # next[i]表示前i个字符的最长公共前后缀长度
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            # 如果字符不匹配，查表退回
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            # 匹配则下一个
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    def getNext(self, next, s):
        # 初始化
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            # 当字符串不匹配时，查表
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            # 当字符串匹配时，则j指向neddle下一个字符
            if s[i] == s[j]:
                j += 1
            # 保存结果
            next[i] = j

```



> 