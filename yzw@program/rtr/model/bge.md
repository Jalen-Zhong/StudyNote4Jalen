# 引言

​	`rtr`中使用了`bge-small-zh-v1.5`权重，下面将深入介绍`BGE`。

# BGE

## 概述

​	Foundation Model有两个代表，一个是Large Language Model，另一个是Embedding Model。

​	前者聚焦**文本空间**，其形式化功能为text -> text；后者聚焦**向量空间**，其功能为text -> embedding。转为向量能做些什么呢？比较常见的使用场景包括`retrieval`（如检索知识库、检索Tool）、`clustering`（聚类）、`classification`（分类，通常需再接一层分类layer）等。

​	`BGE`由北京智源人工智能研究院开源，属于Embedding Model。Embedding Model是将自然形式的数据样本（如语言、代码、图片、音视频）转化为向量（即连续的数字序列），并用向量间的“距离”衡量数据样本之间的“相关性”。

## 方法论

​	`BGE`面向中文世界通用embedding模型。

### 数据方面

​	兼顾`scale`、`diversity`、`quality`这三个维度，这是通用embedding模型能训练出来的**前提**

​	数据分为无标签数据集和标注数据集。标注数据集来自于下游任务，关注各种具体场景业务。

### 训练方面

​	使用3阶段训练策略，从`pre-training` 到 `general-purpose fine-tuning` 再到 `task-specific fine-tuning`；前两个阶段是保证通用性的**基石，**最后一个阶段则在**保持通用**的基础上，进一步**精进**下游任务的效果。

## 训练细节

### pre-training

​	采取**RetroMAE**训练策略

### general-purpose-fine-tuning

​	1.采用in-batch negative sample方法

​	2.使用大batch_size（论文使用的size为19200）

### task-specific fine-tuning

​	1.**instruction-based fine-tuning**。核心思路是将衡量`sim（x1，x2）`，转化为衡量`sim（instruction+x1，instruction+x2）`，这个instruction就是一段text prompt，用以说明domain、task等内容。例如在retrieval任务中，query侧加入的instruction为`为这个句子生成表示以用于检索相关文章：`；

​	2.**hard negative sampling**。在训练过程中，采取**ANN-style sampling strategy[8]**，从该任务的corpus中**全局性**地采样出一个**embedding表征最接近的hard negative sample**。

# 其他

## 权重用法

[BAAI/bge-small-zh · Hugging Face](https://huggingface.co/BAAI/bge-small-zh)

## 效果

[MTEB Leaderboard - a Hugging Face Space by mteb](https://huggingface.co/spaces/mteb/leaderboard)

## 项目地址

[[FlagEmbedding/FlagEmbedding/BGE_M3 at master · FlagOpen/FlagEmbedding (github.com)](https://github.com/FlagOpen/FlagEmbedding/tree/master/FlagEmbedding/BGE_M3)](https://github.com/FlagOpen/FlagEmbedding)

## 论文地址

[[2402.03216\] BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation (arxiv.org)](https://arxiv.org/abs/2402.03216)

# 参考

[BGE论文解读：如何炼成中文世界的通用Embedding Model - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/669596130)

[大模型知识“外挂”，智源开源最强语义向量模型BGE - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/649145407)

[[2402.03216\] BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation (arxiv.org)](https://arxiv.org/abs/2402.03216)