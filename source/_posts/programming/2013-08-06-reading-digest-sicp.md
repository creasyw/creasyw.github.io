---
layout: post
title: "Reading note of SICP"
date: 2013-08-06
comments: false
categories:
- Programming
tags:
- Programming
- LISP
---


P59. I still don't think it is necessary to use "square" instead of (* x x) everywhere we perform this operation, but I appreciate the idea of "abstraction". It is really a good idea (and practice) to abstract concepts in different levels and use them accordingly.

Most of the examples I read are in a top-down design manner: firstly use the abstract concepts, and then implement it in a lower level. The concerns for specific lower-level modules is similar to the way I did using unit test. But I am a little bit confuse how to perform the unit test in this manner. Especially for the closure using in LISP--implementing local helper functions right after building major function-- how can I make sure the helper functions are right before I run the program as a whole? If I separate a helper function as an independent one, it seems that quite a little redundant work has to perform when I move it back to the major function.

Anyway, SICP just makes me love Racket even more =D

cheers,
