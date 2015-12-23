---
layout: post
title: "Install opencv in mac osx"
date: 2012-10-04
comments: false
categories:
- Programming
tags:
- Programming
- OpenCV
- setup
---


The most straightforward way is via homebrew.

{% highlight bash %}
brew update 
sudo brew install opencv
{% endhighlight %}

Then, all of the dependencies will be install with opencv. The reason to use `sodu` is because there will be twice `brew link` used in the process which could not link certain libraries without permission.

Finally, the brew gave a wrong file to update. Instead of updating `.profile`, the correct destination should be `.bash_profile`. And add the line: `export PYTHONPATH=/usr/local/lib/python2.7/site-packages/:$PYTHONPATH`

That is it.


cheers,
