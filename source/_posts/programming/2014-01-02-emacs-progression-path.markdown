---
layout: post
title: "Emacs Progression Path"
date: 2014-01-02 16:37
comments: true
summary: I was hoping to find something like Python Progression Path or sort of "best practice" for Emacs. But what I found were either teaching about basic operations or talking about tricks of using Emacs Lisp. So I am trying to make a path by myself, so that I would not be stuck in the middle (like forever..).
categories:
- Programming
tags:
- Programming
- Emacs
---

I was hoping to find something like [Python Progression Path](http://stackoverflow.com/questions/2573135/python-progression-path-from-apprentice-to-guru) or sort of "best practice" for Emacs, because the difference between Vim and Emacs was much larger than I thought. But what I found were either teaching about basic operations such as saving and quiting the editor for people who had access to comupter for the 1st time, or talking about tricks of using Emacs Lisp for the high-end hard-core players... It seemed like I was stuck in the middle, and would stay there for a very long time...

I will sort the contents here as incremental records simulating my Emacs learning process, as well as keeping track of nontrivial materials and thoughts.

### References:

* [Tow](http://sachachua.com/blog/2013/05/how-to-learn-emacs-a-hand-drawn-one-pager-for-beginners/) [pics](http://sachachua.com/p/26006) served as the very beginning of entering the world of Emacs.
* Cheat Sheet ([compact version](http://refcards.com/docs/gildeas/gnu-emacs/emacs-refcard-a4.pdf), and [a more user friendly verion](http://cs.iupui.edu/~kweimer/EmacsCheatSheet.pdf)).
* C-h t. Tutorial of Emacs within the editor. It should be the first doc to read.
* My previous [post](http://wqiong.com/blog/2013/07/01/setup-emacs-in-mac-os/) to setup Emacs in Mac OS.
* Steve Yegge's suggestion for [improving productivity with Emacs](https://sites.google.com/site/steveyegge2/effective-emacs)
* [Prelude](http://batsov.com/prelude/) -- very easy to setup, and add/disable modules.
* [Oh-my-emacs](https://github.com/xiaohanyu/oh-my-emacs) is another option to start with, but I met quite a few incompatible issues for the mac os. [Emacs24 Starter Kit](https://github.com/eschulte/emacs24-starter-kit) is also well-known but relatively inactive recently.
* GNU [Emacs Manual](http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html) and [Emacs LISP Manual](http://www.gnu.org/software/emacs/manual/html_node/elisp/)
* [Guidelines](http://batsov.com/articles/2012/02/19/package-management-in-emacs-the-good-the-bad-and-the-ugly/) for package management in Emacs.
* [Emacs Wiki](http://www.emacswiki.org/emacs/)
* [Mastering Emacs](http://www.masteringemacs.org/)
* [From Vim to Emacs+Evil chaotic migration guide](http://juanjoalvarez.net/es/detail/2014/sep/19/vim-emacsevil-chaotic-migration-guide/)

--Well, it is really a road that will never end...

### Packages:

* [Magit](https://github.com/magit/magit). "Magit is the most popular interface to git. If you are new to git and do not need support for other vcs this is likely the package you should try first" -- quoted from [EmacsWiki](http://www.emacswiki.org/emacs/Git). The detail explanation can be found from [Mastering Emacs](http://www.masteringemacs.org/articles/2013/12/06/introduction-magit-emacs-mode-git/).
* [Company](http://company-mode.github.io/) for auto-completion.

### Random Thoughts
* One of the most fundamental change from Vim to Emacs is that Vim is the most powerful editor in this planet while Emacs is kind of ["operating system" with a lousy editor](http://c2.com/cgi/wiki?EmacsAsOperatingSystem). It might be a rant to the right place, but anyway, the other side of the story is that emacs can be regarded as an OS which means that it might be much more powerful when the configuration is right. I should be able to do things that are used to complete via the combination of vim, shell, REPL, and compiler, and I SHOULD NOT launch and exit it very often as what I am doing with vim.
* Everything looks a little bit more decent within the emacs,
  including the shell.


### Useful Key Combinings:

Kill a line:
C-a C-k (move the cursor to the begining of the line, thenkill from the cursor to the end of the line)

Kill 2 lines: C-a C-u 2 C-k

Kill a specific region
C-\<SPC\> C-w (move around to highlight region, then kill contents within highlight region)

Yank the killed contents C-y

Retrieve yanking history
M-y (right after the 1st yanking. -- this is intersting)

The difference between "killing" and "deleting" is that "killed" text
can be reinserted (at any position), whereas "deleted" things cannot
be reinserted in this way (you can, however, undo a deletion--see below).
Reinsertion of killed text is called "yanking".  Generally, the
commands that can remove a lot of text kill the text (they are set up so
that you can yank the text), while the commands that remove just one
character, or only remove blank lines and spaces, do deletion (so you
cannot yank that text).  \<DEL\> and C-d do deletion in the simplest
case, with no argument.  When given an argument, they kill instead.
-- This is valid for both vim and emacs.

Multiple windows:
- C-x 0  delete this window
- C-x 1  delete all other windows
- C-x 2  vertically split window
- C-x 3  split window side by side

Scoll down the page
- C-v (page down)
- C-u 8 C-v (scoll down 8 lines)
- C-l (move the current line to the middle of the window)
- C-u 0 C-l (move the current line to the head of the window)

Getting help
- C-h c \<Command sequence\>   (a very brief description of the command.)
- C-h k \<Command sequence\>   (displays the documentation of the function, as well as its name)

Auto-completion
- M-/
- [Company](http://company-mode.github.io/) is good complementory plug-in

Shell History (also Useful for Haskell REPL)
- M-p (or) C-\<UP\>: Fetch the next earlier old shell command.
- M-n (or) C-\<DOWN\>: Fetch the next later old shell command.
- M-r: Begin an incremental regexp search of old shell commands.
- C-c C-x: Fetch the next subsequent command from the history.
- C-c . : Fetch one argument from an old shell command.
- C-c C-l: Display the buffer's history of shell commands in another window (comint-dynamic-list-input-ring).

### Missing Features:

This is a list for what I should expand the functionalities of my Emacs.

* Highlight symbol at the point. There is [a package](http://www.emacswiki.org/emacs/HighlightSymbol) for this purpose, but currently it does not work well within Prelude.
* Interactive input for M-x.
