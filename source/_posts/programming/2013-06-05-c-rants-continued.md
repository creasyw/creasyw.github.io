---
layout: post
title: "C++ rants (continued)"
date: 2013-06-05
comments: false
categories:
- Programming
tags:
- Programming
- C++
---


(<a href="http://www.realworldtech.com/forum/?threadid=104299&amp;curpostid=104196">link</a>)

&gt;Care to write an explicit example of a deep problem? (Except memory management - you already mentioned garbage collection.)

Concurrency, for example.

My point being, that C++ adds absolutely nothing interesting.

&gt;All right. Then why do you think C should have support for structures (struct {...})?

That's just singularly stupid.

C is a good language. It's complete enough (and yes, the ability to handle structured data is very much required for any serious language) to be supremely useful, while at the same time being quite simple.

A language without structured data types would not be a powerful language the way C is. You do need data structures, and you need pointers (to both data and code) to be at all interesting.

But where do you draw the line?

I know that you as a C++ proponent you probably won't really "get" this simple argument, but try:

- read the K&amp;R book on C (the ANSI edition), and be enlightened.

Notice how the language is basically described by one rather thin book. Readably.

So what C does so well is to do that whole "make it as simple as you can, but no simpler". And that is what makes it great. The language is powerful, yet fairly minimal.

There really aren't many features you could remove from the C language without crippling it. Sure, there's
three different looping constructs, and you could make trivial (syntactic) changes to the language, but that's
really not the point. The language is simple, but without being too simple.

Now, that's not what you always want. I understand very well why people want less system-oriented languages with more built-in functionality. As mentioned, support for both garbage collection and concurrency are quite real problems, and they are both things you can do in C, but that you cannot do well with library interfaces, which is how you normally would extend on C.

And garbage collection and concurrency are way more than just syntactic extensions. You can still do them very badly, of course, so it's not a trivial path to go down, and I'm not saying hat a language magically becomes "good" just from supporting one or the other.

But again: C does what it does very well, and with a clarity of thought and design that is entirely and utterly lacking from C++.

And yes, I happen to think that clarity of thought and design is a good thing. It's why I liked UNIX, even though I was initially introduced to other things (VMS - ugh).

C++ is a mess. There's no design. It's just "add crud on top of C". And the crud isn't even meaningful, much less does it have a design. It's totally and utterly random.

It started out random, now it's randomness that gets added to by a committee.

&gt;For example, namespaces and function overloading are *not*
&gt;useless. They *do* solve a real problem that C is incapable
&gt;of solving.

You're full of it.

&gt;For example, if you want in your source code to define a
&gt;function called "connect" and you also want include
&gt;"sys/socket.h", you cannot do that in C.

So to prove how it's not just a syntactic feature, you start talking about syntax?

What drugs are you on?

The name overloading is a total syntactic feature. In C, the way you fix your problem is by a totally trivial syntactic change: you call your function "my_connect()".

Wow. It's like magic. I added three characters, and made your whole reason for the crap that is C++ go away.

The thing is, the above is a really good example of why C++ is horrible, and why C is so simple.

Yes, the C solution is really simple. It's so simple that it looks downright stupid. But it's actually so simple that it is smart because quite frankly, it's a lot easier to get confused in C++ code, when the same function name means totally different due to overloading.

Of course, you're not "supposed" to overload things in confusing ways, but the thing is, just do what C does: just make your function names unique. It's not that hard, and by avoiding the overloading mess, you make it a lot easier to search for (hey look! "grep -w my_connect" just works!), and you avoid ambiguity.

(Same exact thing goes for your other example: just add a module prefix or have some other trivial naming rules for your functional split-up, and be happy)

Linus
<div>

