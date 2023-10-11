## NanoGPT

## 搭建GPT

### 词索引的encoder与decoder

我们需要创建一个encoder和decoder字典，以便于获得词索引和解析词索引得到输出

```python
# here are all the unique characters that occur in this text
chars = sorted(list(set(text)))
vocab_size = len(chars)

# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print(encode("hii there")) # [46, 47, 47, 1, 58, 46, 43, 56, 43]
print(decode(encode("hii there"))) # hii there
```

### 词向量

我们用nn.Embedding创建索引列表到词向量映射的哈希表，输入是索引列表，输出是相应的词嵌入

```python
class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
		# 定义词表，模块的输入是索引列表，输出是相应的词嵌入，vocab_size=65
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size) 

    def forward(self, idx, targets=None):
        # idx and targets are both (B,T) tensor of integers
        logits = self.token_embedding_table(idx) # (B,T,C)
        print(logits.shape) # [4,8,65]
```

### 预测

NLP为一个顺序结果预测，当前位置的预测结果只与前面所有预测结果有关

```python
block_size = 8
train_data[:block_size+1]
>
tensor([18, 47, 56, 57, 58,  1, 15, 47, 58])


x = train_data[:block_size]
y = train_data[1:block_size+1]
for t in range(block_size):
    context = x[:t+1]
    target = y[t]
    print(f"when input is {context} the target: {target}")
    
>
when input is tensor([18]) the target: 47
when input is tensor([18, 47]) the target: 56
when input is tensor([18, 47, 56]) the target: 57
when input is tensor([18, 47, 56, 57]) the target: 58
when input is tensor([18, 47, 56, 57, 58]) the target: 1
when input is tensor([18, 47, 56, 57, 58,  1]) the target: 15
when input is tensor([18, 47, 56, 57, 58,  1, 15]) the target: 47
when input is tensor([18, 47, 56, 57, 58,  1, 15, 47]) the target: 58
```

### 优化器

```python
# create a PyTorch optimizer
optimizer = torch.optim.AdamW(m.parameters(), lr=1e-3)

batch_size = 32
for steps in range(100): # increase number of steps for good results... 
    
    # sample a batch of data
    xb, yb = get_batch('train')

    # evaluate the loss
    logits, loss = m(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
```

