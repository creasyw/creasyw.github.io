---
layout: post
title: "General posts about Lisp"
date: 2012-06-04
comments: false
summary: Lots of people talking about LISP
categories:
- Digest
tags:
- Programming
- LISP
---

- <a href="http://lib.store.yahoo.net/lib/paulgraham/jmc.ps">The Roots of Lisp (ps)</a>
- <a href="http://www.paulgraham.com/diff.html">What Made Lisp Different</a> (<a href="http://www.ruanyifeng.com/blog/2010/10/why_lisp_is_superior.html">Chinese translation</a>)
- <a href="http://www.paulgraham.com/lisp.html">Paul Graham's collection</a>
- <a href="http://www.winestockwebdesign.com/Essays/Lisp_Curse.html">The Lisp Curse</a> by Rudolf Winestock 
- <a href="http://lists.warhead.org.uk/pipermail/iwe/2005-July/000130.html">Why Lisp macros are cool, a Perl perspective </a>
- <a href="http://www.defmacro.org/ramblings/lisp.html">The Nature of Lisp</a>
- <a href="http://www.dreamsongs.com/Files/LispGoodNewsBadNews.pdf">Lisp: Good News, Bad News, How to Win Big (pdf)</a>
- <a href="http://www.lambdassociates.org/blog/bipolar.htm%20">The Bipolar Lisp Programmer</a>
- <a href="http://www.informatics.sussex.ac.uk/research/groups/nlp/gazdar/nlp-in-lisp/index.html%20">Natural Language Processing in Lisp (book)</a>
- <a href="http://www.cs.rpi.edu/academics/courses/fall05/ai/scheme/tips.html">Tips for using Scheme and debugging your code</a>
- <a href="http://coolshell.cn/articles/7526.html">Lisp的永恒之道</a> (Chinese)


A <a href="http://itasoftware.com/careers/work-at-ita/ita-engineering.html?catid=#">great explanation</a> from ITA Software about why and how to use different languages, including Lisp (CL), Python, Java, and C/C++. 

>Lisp is a programmable programming language, and one of the few languages that can be used for a wide range of applications. At ITA we have projects with vastly different focus, and it's precisely Lisp's versatility that makes it so useful to us. Lisp allows us to define a wide variety of abstractions to manage the complexity, and at the same time we get the speed we want - and our customers demand.
>
>While most of ITA's algorithm-intensive code is implemented in high-level languages like Lisp, we use C/C++ to provide system support to our Lisp-based applications where the Common Lisp runtime support is inadequate. For instance, we represent large static datasets as densely packed arrays stored in files. We use C++ to make the mmap() calls and fetch pointers into these mappings for Lisp to access.
>
>Once in a while, we have had a hard time fooling the Lisp compiler into generating sufficiently fast machine code for a given function. When that happens, we can usually just rewrite the function in C++ and call it from Lisp.

and... <a href="http://www.paulgraham.com/carl.html">quote from an email</a> of Carl de Marcken from Paul: 

>A lot of our Lisp is designed to compile into very efficient assembly. We make a lot of use of Lisp's macro capabilities, but shy away from many other Lisp features like closures, generic functions, complex sequence functions and garbage collection. We're doing an incredible amount of computation - getting 10 seconds on a modern machine is an incredible gift - but if we're sloppy at all 10 seconds can turn into ten minutes, not adequate for a travel agent or web site. We disassemble most every Lisp function looking for inefficiencies and have had both CMUCL and Franz enhanced to compile our code better.
>
>We've had very little trouble getting non-Lisp programmers to read and understand and extend our Lisp code. The only real problem is that the training most programmers have in Lisp has taught them to code very inefficiently, without paying any attention to the compiler. Of course, with things like STL and Java, I think programmers of other languages are also becoming pretty ignorant.
