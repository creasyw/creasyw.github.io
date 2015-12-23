---
layout: post
title: "Progress at Humming Identification and SICP"
date: 2012-05-16
comments: false
categories:
- Programming
tags:
- Programming
- LISP
- Blahblah
- Working progress
---


Humming Identification. 

已然经历了两次较大的重建，现在的中段程序应该算是稳定了，前段程序接近黔驴技穷了，后段程序最后一次大修改后还在服务器里面跑着。出结果之后再用一两天时间整理，然后再看看清唱部分的阈值应该如何处理。不出意外的话，这就接近世界先进水平了:)

现在回头看来，其实真正值得研究的部分还是在最初的参数提取。SIFT里面对于图像的各种锥形不变、边框加深、棱角过滤，对于音频信号都是不适用的。而语音信号的频谱重复或者音乐信号的长时重复在哼唱识别中又是不适用的。所以现在只能使用较为原始的 local maximum cascade filtering。若是频谱图能如图像般的直观，有些经验总结的东西在里面，就好了。


SICP

思考过一段时间的结果，<a href="http://coolshell.cn/articles/6639.html">因为有了电据就少用到电钻</a>，于是熟练了Py也就先放放ruby了。转过身来硬着头皮读这本书。而第一天读过前言，我就知道这决不会是个令我后悔的决定。无数人的推荐，自然是有其中道理的。而把读过的几本经典书籍横向比较，会发现它们都会刻意避开很多fancy的概念，着力强调着那些在设计程序过程中永恒不变的东西。K&amp;R把C的很多基本库函数都重建了一遍，而SICP更是从加减乘除开始重构。

开始读书之前，我也刻意找了一下CL和Scheme的对比。记得有个人说，如果想用Lisp做项目，CL更合适；想体会编程的乐趣，Scheme更合适，只是，它的核实在是太简单了。几个月看下来，其对于Scheme的评价当真实字字珠玑。这是一个无比强大的语言，data abstraction &amp; procedure abstraction，之后再抹去两者的差别，都只是当作object处理。看到这里，我会有错觉，认为自己都可以来设计Clojure了，这简直就是顺理成章的事情！tail recursion，比循环更加直观易懂，而更牛逼的是这竟然不会按照stack的模式迭代后增加内存的占用。至于enclosure和lambda calculus，在Python里面也有借鉴，但是我是直到这里才真正学会了如何使用它们⋯⋯当然，我很清楚这些词汇推砌起来的仍然仅仅是些皮毛。里面很多在程序设计时的考虑，才是更需要我好好体会的。


BTW, 今天的时间累计到2800了~

cheers, 
