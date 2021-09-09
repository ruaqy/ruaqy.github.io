# RuaBlog 轻量化且开源的静态博客系统

版本:*v1.0.0.1* 日期:*2021年9月9日* 维护:*RQY*

[![RQY/RuaBlog](https://gitee.com/muronglengjing/rua-blog/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/rua-blog)

<a href='https://gitee.com/muronglengjing/rua-blog/stargazers'><img src='https://gitee.com/muronglengjing/rua-blog/badge/star.svg?theme=dark' alt='star'></img></a>  [![fork](https://gitee.com/muronglengjing/rua-blog/badge/fork.svg?theme=dark)](https://gitee.com/muronglengjing/rua-blog/members)

界面预览[Rua小屋](https://ruaqy.github.io)

## 使用说明

### 下载安装

拷贝整个仓库后可以自行进行修改(LICENSE:[Mulan PSL v2](http://license.coscl.org.cn/MulanPSL2))。

### 技术说明

所有页面靠markdown编译器实现，依赖客户端完成编译。

markdown分析器采用[Christopher Jeffrey](https://github.com/markedjs/marked)(MIT Licensed)的markdown parser。

使用python作为后端，进行静态编译markdown文件。

### 使用说明

#### 打开后端

文件目录下，在控制台输入```python manager.py```可以看到所有命令，常见的操作有

##### 添加项目

```
python manager.py -a "待添加的项目"
```

##### 移除项目

```
python manager.py -r
```

##### 生成数据库文件

```
python manager.py -p
```

##### 生成markdown文件

```
python manager.py -b
```

##### 生成数据库文件并生成markdown文件

```
python manager.py -g
```



### 文件系统

|文件夹			|含义								|
|--------------|-----------------------------------|
|ccs			|存放ccs文件							|
|img			|存放运行时所需要的图片				|
|js			|存放运行所用的js文件					|
|data	|存放编译所需要的数据	|
|pages			|存放一些界面文稿						|
|pages/post	|存放能被显示的文稿(会被git记录)		|
|pages/draft	|存放不会被显示的草稿(不会被git记录)	|




## 更新记录

### 2021年9月9日

 1. 修复了多次项目多次添加的问题
 2. 增加了静态编译器的功能，现在可以添加项目、生成数据库以及编译文件了
 3. 这是第一个正式版本，近期项目会搁置一段时间，如果有进展，会第一时间在网站上发布

### 2021年9月8日

 1. 使用python作为后端，增加了编译文件的功能

### 2021年9月7日

 1. 增加了markdown阅读器，取代了原有的html界面
 2. 删除了冗余文件
 3. 修正了一些错误，删除了大量无用的网页，转为markdown实现