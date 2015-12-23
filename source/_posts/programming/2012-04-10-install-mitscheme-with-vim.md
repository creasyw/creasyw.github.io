---
layout: post
title: "Install MIT/Scheme with Vim"
date: 2012-04-10
comments: false
categories:
- Programming
tags:
- Programming
- Vim
- Scheme
- setup
---

After wondering around for a while, I finally found this was quite foolproof... 

It could be divided into five steps:

-  `$ brew install mit-scheme`. (Its version is usually a little bit older than the latest <a href="http://www.gnu.org/software/mit-scheme/">MIT/GNU Scheme</a>)
- Install <a href="http://www.gnu.org/software/screen/">GNU screen</a> if it was not installed before.
- Install <a href="http://www.vim.org/scripts/script.php?script_id=2711">Screen Vim plug-in</a> according the steps in that webpage.
- Add the following into `~/.vimrc`
{% highlight Vim Script %}
"For screen.vim send block
"to SendScreen function
"(eg Scheme interpreter)
vmap <C-c><C-c> :ScreenSend<CR>
nmap <C-c><C-c> vip<C-c><C-c>
{% endhighlight %}
- launch Vim and write `:ScreenShell mit-scheme`.

It is all set for the fun:)

References: <a href="http://www.ktaylor.name/vim/">[1]</a>, <a href="http://www.uponmyshoulder.com/blog/2011/so-you-want-to-do-the-sicp/">[2]</a>

cheers,
