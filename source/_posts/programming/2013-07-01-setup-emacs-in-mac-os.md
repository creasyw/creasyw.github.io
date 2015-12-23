---
layout: post
title: "Setup emacs in Mac OS"
date: 2013-07-01
comments: false
categories:
- Programming
tags:
- Programming
- LISP
- Emacs
- setup
- Mac OS
---

The setup is much harder than I thought...

1. using homebrew installs the emacs and guile. Then, I also need to add path in the .bash_profile to launch the up-to-date emacs rather than the original version 22.1 shipped with the os.
<code>export PATH=/usr/local/Cellar/emacs/24.3/bin:$PATH</code>
2. Enable the <a href="http://stackoverflow.com/questions/162896/emacs-on-mac-os-x-leopard-key-bindings">Meta key in terminal</a>, or similar position for iterm2.

3. I accidentally found this "<a href="https://github.com/technomancy/emacs-starter-kit">emacs-starter-kit</a>", which had 2300+ stared and really saved my day. Just follow the instruction and everything will be fine.

In current state, I feel emacs kind of like vim+tmux. Anyway, learning new knowledge is always a pleasure, especially about this kind of "legacy" stuff.


cheers,

[UPDATE: after changed the loading sequence of bash in <code>/etc/paths/</code> the first step seems unnecessary... actually, that was something I should do as soon as I used <a href="http://bit.ly/IUVl9a">homebrew</a> to port packages.
