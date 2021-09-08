# RuaBlog 开源的静态博客系统


[![RQY/RuaBlog](https://gitee.com/muronglengjing/rua-blog/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/muronglengjing/rua-blog)

<a href='https://gitee.com/muronglengjing/rua-blog/stargazers'><img src='https://gitee.com/muronglengjing/rua-blog/badge/star.svg?theme=dark' alt='star'></img></a>  [![fork](https://gitee.com/muronglengjing/rua-blog/badge/fork.svg?theme=dark)](https://gitee.com/muronglengjing/rua-blog/members)

界面预览[Rua小屋](https://ruaqy.github.io)

## 使用说明

### 下载安装

拷贝整个仓库后可以自行进行修改(LICENSE:[Mulan PSL v2](http://license.coscl.org.cn/MulanPSL2))。

### 技术说明

markdown分析器采用[Christopher Jeffrey](https://github.com/markedjs/marked)(MIT Licensed)的markdown parser。

### 文件系统

 |文件夹			|含义								|
 |--------------|-----------------------------------|
 |ccs			|存放ccs文件							|
 |img			|存放运行时所需要的图片				|
 |js			|存放运行所用的js文件					|
 |pages			|存放一些界面文稿						|
 |pages/post	|存放能被显示的文稿(会被git记录)		|
 |pages/draft	|存放不会被显示的草稿(不会被git记录)	|


## 更新记录

### 2021年9月7日

 1. 增加了markdown阅读器，取代了原有的html界面
 2. 删除了冗余文件