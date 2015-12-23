---
layout: post
title: "Tail recusive function in Python"
date: 2013-02-14
comments: false
categories:
 - Programming

tags:
- Python
- SML
- Programming
---


&nbsp; &nbsp; 
The issue came from <a href="http://stackoverflow.com/questions/14828945/python-several-callings-of-function-containing-recursions-cause-runtimeerror">my question in stackoverflow</a>. Basically, it was a misplaced question, because the reason why my program would hit the "<span class="typ" style="border: 0px; color: #2b91af; font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; font-size: 14px; line-height: 18px; margin: 0px; padding: 0px; vertical-align: baseline;">RuntimeError</span><span class="pun" style="border: 0px; font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; font-size: 14px; line-height: 18px; margin: 0px; padding: 0px; vertical-align: baseline;">:</span><span class="pln" style="border: 0px; font-family: Consolas, Menlo, Monaco, 'Lucida Console', 'Liberation Mono', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Courier New', monospace, serif; font-size: 14px; line-height: 18px; margin: 0px; padding: 0px; vertical-align: baseline;"> maximum recursion depth exceeded</span>" was that I just passed the sorted array by the first scenario to the second scenario. This caused the second one hit the "worse case" and exceed the "maximum recursion depth". Well... it was embarrassing to admit that I forgot dereferencing the variable...

Anyway, the question concerning recursion in Python has been in my head for a while, even since I started learning Scheme. This time, the kind answer below my question shed lights on how to solve this kind of problem. Then I dug a little deeper and find more about tail recursion in Python.

The following is an example with problematic way to implement a recursive function:

{% highlight python %}
def fac(n):
    return 1 if n < 2 else n * fac(n - 1)

> fac(3000)
> RuntimeError: maximum recursion depth exceeded
{% endhighlight %}

The right way to do this is to make a local helper function "tail recursive" with the help from anonymous function.

{% highlight python %}
def fac(n):
    def f(n, acc):
        return acc if n < 2 else lambda: f(n - 1, acc * n)

    t = f(n, 1)
    while callable(t):
        t = t()
    return t
{% endhighlight %}

And an even elegant&nbsp;way is to use built-in function "reduce":

{% highlight python %}
def fac3(n):
    return reduce(lambda x,y:x*y, xrange(1,n))
{% endhighlight %}

The latter two could deal with any input number. Tada~

Extended references:

- <a href="http://python-history.blogspot.com/2009/04/origins-of-pythons-functional-features.html">Origins of Python's "Functional" Features</a>
- <a href="http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html">Tail Recursion Elimination</a>
- <a href="http://metapython.blogspot.com/2010/11/tail-recursion-elimination-in-python.html">Tail Recursion Elimination in Python</a>

Besides, studying Standard ML does give me much much more insights into both programming itself and programming in Python. Except the attractive tail recursion, Python has quite a few amazing features of functional programming. &nbsp;In retrospect, now I appreciate more about what was listed in the "<a href="http://stackoverflow.com/questions/2573135/python-progression-path-from-apprentice-to-guru">progression path</a>", and of course, cannot wait to progress to Haskell.

cheers,
