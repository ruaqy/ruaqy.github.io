# matlab神经网络工具箱

matlab拥有着很多实用的工科计算工具，其中就包含了神经网络工具箱。利用matlab，可以很容易地搭建一个实用的神经网络。

### 启动神经网络工具箱

```matlab
nnstart
```

输入后，会出现窗体，点击对应的窗体即可启动相关的训练程序。

其中包含

- nftool(Neural network fitting tool，神经网络拟合工具) 常用于线性拟合
- nprtool(Neural network pattern recognition tool，神经网络模式识别工具) 常用于分类问题（有标签）
- nctool(Neural network classification or clustering tool，神经网络分类与聚类工具) 用于聚类问题（无标签）
- ntstool(Neural network time series tool，神经网络时序拟合工具) 带有记忆功能的拟合工具

启动后按照指引，可以执行对应的功能。

## 神经网络拟合数据

据证明，简单的神经网络可以拟合任何实际的函数。

LM算法(Levenberg-Marquardt)适合于大多数的问题，但对于有小噪声干扰的数据，贝叶斯正则化算法(Bayesian Regularization)可以通过长时间的运算以获得更好的拟合效果。对于大规模的问题，量化共轭梯度法(Scaled Conjugate Gradient)更推荐适用，因为其梯度计算比实用雅各比行列式能节约更多的内存。

## 神经网络模式分类

神经网络在分类问题上也很实用。

对于分类问题来说，其数据格式应该是这样的：

- 二分类

```matlab
inputs  = [0 1 0 1; 0 0 1 1];
targets = [1 0 0 1; 0 1 1 0];
```

- 三分类

```matlab
inputs  = [0 0 0 0 5 5 5 5; 0 0 5 5 0 0 5 5; 0 5 0 5 0 5 0 5];
targets = [1 0 0 0 0 0 0 0; 0 1 1 1 1 1 1 0; 0 0 0 0 0 0 0 1];
```

输入为MxN维矩阵，对于K分类问题，输入应该为MxK维矩阵。对输出来说，每个分类的列都应该只包含一个1，其余为0。

## 自组织映射聚类

聚类问题是神经网络的一个出色的应用，通过相似性对数据进行分组。

## 动态时序神经网络

动态神经网络适用于时序预测。

## 网络参数

为了验证网络效果，我们需要对生成的网络参数进行分析。

### Performance(误差函数)

- mse(Mean squared normalized error performance function，归一化均方误差函数) 表现数据与预测值直接的距离和，越小越好。

### Regression(相关性)

表现为系统输出与数据之间的关联性，越接近于1表现越好。

### Training State(训练状态)

- Gradient梯度
- Mu学习率
- Validation Checks失败检验次数

### Error Histogram(误差直方图)

横坐标为目标值-输出值，纵坐标为出现的次数。

### Confusion(混乱型)

表现不同数据集中的分类的精确性，横坐标为目标分类，纵坐标为系统训练的输出分类。

红色表示错误分类，绿色表示正确分类。高亮块表示当前训练得到的精确度，右下角表示总体精确度。

### Receiver Operating Characteristic(认知工作特性)

表现不同数据集中的ROC特性，对于完美的测试结果，应该贴合在左上边框，表现为全敏感性和全特异性。

## 参考文献

本文首载自[RuaBlog](ruaqy.github.io)。

> [Matlab训练神经网络实操 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/67383423)

> matlab官方文档