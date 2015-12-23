---
layout: post
title: "Python/Numpy version collisions"
date: 2013-07-23
comments: false
categories:
- Programming
tags:
- Programming
- Python
- Mac OS
- setup
---

Before this accident, I did not even know there were so many places relevant with a single program... I opened the pandora's box beginning with using <code>brew doctor</code> &nbsp;which told me to move directory /usr/local/bin/ prior to /usr/bin/ so that all the homebrewed packages could be found automatically. After I did this, if I executed matplotlib, I would have this runtime error <code>RuntimeError: module compiled against API version 8 but this version of numpy is 6</code>&nbsp;which was somewhat correct by the way. Because I used superpack installed the latest version of numpy(1.8), scipy(0.13), and matplotlib(1.4), but if I printed out the "numpy.__version__" in a script, it showed 1.6.1.

1. delete all of the outdated versions of numpy
2. make sure I explicitly add PYTHONPATH in the bash_profile.
3. I even uninstalled and reinstalled the numpy

But the problem was still there.

After an exhausted search, I found that numpy-1.6.1 in "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/" WTF! I still don't know why it search into 2.6 given there is another 2.7 in the same level of directory. Deleting both 2.6 and 2.7 directories (only delete the 2.6 could not work either...) finally solved the problem. ahooooo....
