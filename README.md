# 上海交通大学学位论文模板
这是我根据上海交通大学学位论文模板,结合电院微纳电子学系的论文格式要求修改而成的latex硕士论文模板。主要修改如下：
 + 页眉加入双装饰线，页脚也做了相应的修改
 + 页眉上的字居中并改为‘上海交通大学硕士学位论文’
 + 论文的第一页和第二页做了相应的修改


## Makefile 使用

### 编译生成学位论文 PDF 文件

通过以下指令，可以编译生成 thesis.pdf：

```bash
make
```

### 持续编译

编写学位论文往往是一个修改 -> 查看论文 PDF 显示效果 -> 继续修改的过程。因此我们实现了持续编译的支持。在文件被修改后，会自动进行新一轮的编译，产生新的 PDF 文件，在写论文时无需写完重新运行 `make`：

```bash
make pvc
```

### 清除所有生成文件

使用以下指令可以清除之前所有的构建文件：

```bash
make clean
```

### 查看字数统计

通过以下指令，可以查看目前的字数（可只关注词数一项）：

```bash
make wordcount
```

## 反馈问题

如果在使用上有任何问题，建议先阅读[常见问题与建议](https://github.com/sjtug/SJTUThesis/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E4%B8%8E%E5%BB%BA%E8%AE%AE)。如果这些不能解决你的问题，建议以如下的顺序反馈使用过程中的问题：

* [在 GitHub 项目主页开 issue](https://github.com/sjtug/SJTUThesis/issues) (推荐)
* [在水源 BBS TeX_LaTeX 版发帖](https://bbs.sjtu.edu.cn/bbsdoc?board=TeX_LaTeX)

如果你觉得项目的使用体验不好，或者想感谢我们的维护者们等等任何与使用无关的想法，都可以通过我们的[在线聊天频道](https://gitter.im/sjtug/SJTUThesis)告诉我们。

## 如何贡献

SJTUThesis 是一个由诸多感兴趣的同学一起维护的开源项目，我们非常欢迎新的贡献者! 这里有很多贡献的方式:

* 帮助我们解答同学们的[问题](https://github.com/sjtug/SJTUThesis/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Atype%2Fquestion+)，这些问题你也可能遇到过并且知道如何解决
* 与我们一起维护项目的 [Wiki 文档](https://github.com/sjtug/SJTUThesis/wiki)，Wiki 是可以直接编辑的
* 向我们贡献代码，我们有一些对新的贡献者比较友好的问题，你可以从[这些问题](https://github.com/sjtug/SJTUThesis/issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-issue)开始熟悉贡献代码的流程
* 向周围同学安利 SJTUThesis，让更多的同学使用我们维护的模板
* 在我们的[在线聊天频道上](https://gitter.im/sjtug/SJTUThesis)告诉我们你的使用体验，以及吐槽。如果你也想成为项目的长期维护者，也可以通过在线频道告诉我们 :-)

## 后续工作计划

* 分离学位论文的使用文档和示例文档，准备提交到 CTAN [#47](https://github.com/sjtug/SJTUThesis/issues/47)

## 致谢

* 感谢 [CTeX](http://www.ctex.org/HomePage) 提供了 LaTeX 的中文支持
* 感谢那位最先制作出博士学位论文 LaTeX 模板的交大物理系同学
* 感谢 William Wang 同学对模板移植做出的巨大贡献
* 感谢 [@weijianwen](https://github.com/weijianwen) 学长一直以来的开发和维护工作
* 感谢 [@sjtug](https://github.com/sjtug) 以及 [@dyweb](https://github.com/dyweb) 对 0.9.5 之后版本的开发和维护工作
* 感谢所有为模板贡献过代码的[同学们](https://github.com/sjtug/SJTUThesis/graphs/contributors)，以及所有测试和使用模板的各位同学

## 软件许可证

上海交通大学校徽图片(`sjtulogo.pdf` 等)的版权归上海交通大学所有。其他部分使用 [Apache License 2.0](LICENSE) 授权。

[README]: http://sjtug.org/SJTUThesis/README.pdf
[0.9.5]: https://github.com/sjtug/SJTUThesis/releases/tag/0.9.5

