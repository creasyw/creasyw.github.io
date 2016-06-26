---
layout: post
title: "Emacs Progression Path"
date: 2016-06-26 16:37
comments: true
summary: The progression path of learning to enjoy the Emacs envrionment by a Vim user
categories:
- Programming
tags:
- Programming
- Emacs
- Haskell

---

[_Update_] This is a post I wrote two years ago. Since then, I have
gradually moved most of my _personal_ developing environment from Vim
to Emacs. So, it is the time to rewrite part of the post and add the updates.

I was hoping to find something like [Python Progression Path](http://stackoverflow.com/questions/2573135/python-progression-path-from-apprentice-to-guru) or sort of "best practice" for Emacs, because the difference between Vim and Emacs was much larger than I thought. But what I found were either teaching about basic operations such as saving and quiting the editor for people who had access to comupter for the 1st time, or talking about tricks of using Emacs Lisp for the high-end hard-core players... It seemed like I was stuck in the middle, and would stay there for a very long time...

I will sort the contents here as incremental records simulating my Emacs learning process, as well as keeping track of nontrivial materials and thoughts.

### References:

* These two great post are the starting point to enter the
  world of Emacs [1](http://sachachua.com/blog/2013/05/how-to-learn-emacs-a-hand-drawn-one-pager-for-beginners/), [2](http://sachachua.com/p/26006).
* To play with Emacs, I still need to open quite a few cheat sheets...
    - Emacs: ([compact version](http://refcards.com/docs/gildeas/gnu-emacs/emacs-refcard-a4.pdf), and [a more user friendly verion](http://cs.iupui.edu/~kweimer/EmacsCheatSheet.pdf)).
    - [Magit](https://magit.vc/manual/magit-refcard.pdf)
    - [Geiser](http://www.nongnu.org/geiser/geiser_5.html) with the
      Haskell mode
    - [Prelude](http://g-design.net/textmate.pdf)
* Steve Yegge's suggestion for [improving productivity with Emacs](https://sites.google.com/site/steveyegge2/effective-emacs)
* My previous [post](http://wqiong.com/blog/2013/07/01/setup-emacs-in-mac-os/) to setup Emacs in Mac OS.
* GNU [Emacs Manual](http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html) and [Emacs LISP Manual](http://www.gnu.org/software/emacs/manual/html_node/elisp/)
* [Guidelines](http://batsov.com/articles/2012/02/19/package-management-in-emacs-the-good-the-bad-and-the-ugly/) for package management in Emacs.
* [Emacs Wiki](http://www.emacswiki.org/emacs/)
* [Mastering Emacs](http://www.masteringemacs.org/)
* [From Vim to Emacs+Evil chaotic migration guide](http://juanjoalvarez.net/es/detail/2014/sep/19/vim-emacsevil-chaotic-migration-guide/)


### Packages:

- [Prelude](http://batsov.com/prelude/) -- very easy to setup, and
  add/disable modules and/or modes, which are defined at
  [`init.el`](https://github.com/creasyw/dot_file/blob/master/init.el)
  and [prelude-modules.el](https://github.com/creasyw/dot_file/blob/master/prelude-modules.el).
- [Evil](https://www.emacswiki.org/emacs/Evil), the Vim mode. This
  would make the live much easier, maybe just because it provides a decent editor inside of
  the emacs OS =P. And there is a trick to
  [copy and paste large chunks of text in OSX](http://stackoverflow.com/questions/3960034/pasting-text-into-emacs-on-macintosh).
- [Oh-my-emacs](https://github.com/xiaohanyu/oh-my-emacs) is an
  alternative of Prelude to start with, but I met quite a few incompatible issues for the mac os. [Emacs24 Starter Kit](https://github.com/eschulte/emacs24-starter-kit) is also well-known but relatively inactive recently.
- [Magit](https://github.com/magit/magit). "Magit is the most popular interface to git. If you are new to git and do not need support for other vcs this is likely the package you should try first" -- quoted from [EmacsWiki](http://www.emacswiki.org/emacs/Git). The detail explanation can be found from [Mastering Emacs](http://www.masteringemacs.org/articles/2013/12/06/introduction-magit-emacs-mode-git/).
- Auto-completion is `M-/`, or
  [Company](http://company-mode.github.io/) for fancier scenarios.
- [HighlightSymbol](http://www.emacswiki.org/emacs/HighlightSymbol)
    with self-explanatory name, but currently it does not work well within
    Prelude.
- [Haskell mode](http://haskell.github.io/haskell-mode/)

### Misc

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

- Multiple windows:
    - `C-x 0`  delete this window
    - `C-x 1`  delete all other windows
    - `C-x 2`  vertically split window
    - `C-x 3`  split window side by side
- Scoll down the page
    - `C-v`: page down
    - `C-u 8 C-v`: scoll down 8 lines
    - `C-l`: move the current line to the middle of the window
    - `C-u 0 C-l`: move the current line to the head of the window
- Getting help
    - `C-h c \<Command sequence\>`:   a very brief description of the command.
    - `C-h k \<Command sequence\>`   displays the documentation of the function, as well as its name
    - `C-h t` evoke the tutorial of Emacs within the editor.
    - `C-h a topics RET` searches for commands whose names match the
    argument topics. The argument can be a keyword, a list of keywords,
    or a regular expression.
        - `C-h i d m emacs RET i topic RET` searches for topic in the
        indices of the Emacs Info manual
        - `C-h i d m emacs RET s topic RET` searches the text of the
        manual.
- Shell History (also Useful for Haskell REPL)
    - `M-p (or) C-\<UP\>`: Fetch the next earlier old shell command.
    - `M-n (or) C-\<DOWN\>`: Fetch the next later old shell command.
    - `M-r`: Begin an incremental regexp search of old shell commands.
    - `C-c C-x`: Fetch the next subsequent command from the history.
    - `C-c .`: Fetch one argument from an old shell command.
    - `C-c C-l`: Display the buffer's history of shell commands in another window (comint-dynamic-list-input-ring).
