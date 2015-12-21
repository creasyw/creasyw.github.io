---
layout: post
title: "Reading note of SICP (5)"
date: 2014-05-15 00:55
comments: true
summary: some digest of SICP while I was reading it
categories: 
- Programming
tags:
- LISP
- Racket
---

* The ability to visualize the consequences of the actions under consideration is crucial to becoming an expert programmer.
* Procedures that manipulate procedures, including accept them as arguments or return them as values, are called *higher-order procedures*. (The *sigma* summation and the derivative operation are all good/simple examples for the latter case.) This is one of the basic characteristics of *factional programming languages*.
* The significance of higher-order procedures is that they enable us to represent these abstractions explicitly as elements in our programming language, so that they can be handled just like other computational elements......As programmers, we should be alert to opportunities to identify the underlying abstractions in our programs and to build upon them and generalize them to create more powerful abstractions......It poses challenges for efficient implementation, but the resulting gain in expressive power is enormous.
* As with compound procedures, the main issue is to be addressed is that of abstraction as a technique for coping with complexity, while the data abstraction enables us to erect suitable *abstraction barriers* between different parts of a program.
* In general, the underlying idea of data abstraction is to identify for each type of data object a basic set of operations in terms of which all manipulations of data objects of that type will be expressed, and then to use only those operations in manipulating the data.
* The approach of *stratified design* is the notion that a complex system should be structured as a sequence of levels that are described using a sequence of languages. Each level is constructed by combining parts that are regarded as primitive at that level, and the parts constructed at each level are used as primitives at the next level. The language used at each level of a stratified design has primitives, means of combinations, and means of abstraction appropriate to that level of detail.
* (Thoughts) I thought local binding with "let/let\*/letrec" are similar to what I did in the imperative programming in a sense that I was telling the program what to do. However, this is not the essence. The local binding is the part of paper which contains the "where..." after a complicated formula. It is the way for data abstract.
