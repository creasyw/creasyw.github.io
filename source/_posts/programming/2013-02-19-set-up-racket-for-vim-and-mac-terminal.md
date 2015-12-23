---
layout: post
title: "Set up Racket for Vim and mac Terminal"
date: 2013-02-19
comments: false
categories:
- Programming
tags:
- Programming
- setup
- Racket
- Vim
- Mac OS
---

Racket is fairly great:), though the setting up procedure is kind of twisted. There is a .dmg installation file in the official website, which makes it quite straightforward to install in the Application folder. And, of course, the DrRacket app is awesome when I accidentally put mouse in one of the variables in the code, and then all its dependencies reveal via arrows.

But I am still used to writing code in vim and testing it in a parallel split window of iterm. I googled the solution, but cannot find a comprehensive one. So, I just list my solution here, which come from either stackoverflow or other persons' blogs.

1. vim syntax and highlight are <a href="https://github.com/wlangstroth/vim-racket">out there</a> ready for use.
2. Adding one command line to ~/.vimrc. `au BufRead,BufNewFile *.rkt set filetype=racket`
3. Adding the path of executable racket to `~/.bach_profile`. `export PATH=$PATH:/Applications/Racket\ v5.3.3/bin/`
4. If using the existing file, one should delete the first line of code "#lang racket" if existed.
5. Optional. Installing rlwrap to make the repl more user friendly.

That is much of it.


cheers,
