---
layout: post
title: "excerpt from Effective C++"
date: 2013-06-04
comments: false
categories:
- Programming
tags:
- Programming
- C++
---


&nbsp; &nbsp; 
Cpp is like some stubborn old man, who always says "i have lots of obscure habits, dealing with it"......

<b>Lesson 4:</b> the initialization is different from assignment, as well as their representations respectively. It is better to write the constructor as the form of initialization, named "initialization list", rather than just simply give the variables first assignment.

To avoid using objects before they're initialized, then, you need to do only three things. First, manually initialize non-member objects of built-in types. Second, use member initialization lists to initialize all parts of an object. Finally, design around the initialization order uncertainty that afflicts non-local static objects defined in separate translation units.

<b>Lesson 7</b>: declare destructors virtual in polymorphic base classes. C++ specifies that when a derived class object is deleted through a pointer to a base class with a non-virtual destructor, results are undefined. What typically happens at runtime is that the derived part of the object is never destroyed. Eliminating the problem is simple: give the base class a virtual destructor. Then deleting a derived class object will do exactly what you want. It will destroy the entire object, including all its derived class parts.

The purpose of virtual functions is to allow customization of derived class implementations. Any class with virtual functions should almost certainly have a virtual destructor. The implementation of virtual functions requires that objects carry information that can be used at runtime to determine which virtual functions should be invoked on the object. On the other hand, if a class does not contain virtual functions, that often indicates it is not meant to be used as a base class. When a class is not intended to be a base class, making the destructor virtual is usually a bad idea.

<b>Lesson 9</b>: Never call virtual functions during construction or destruction. Because during base class construction of a derived class object, the type of the object is that of the base class. Not only do virtual functions resolve to the base class, but the parts of the language using runtime type information (e.g., dynamic_cast (see Item 27) and typeid) treat the object as a base class type.

The same reasoning applies during destruction. Once a derived class destructor has run, the object's derived class data members assume undefined values, so C++ treats them as if they no longer exist. Upon entry to the base class destructor, the object becomes a base class object, and all parts of C++ treat it that way.

Since you can't use virtual functions to call down from base classes during construction, you can compensate by having derived classes pass necessary construction information up to base class constructors instead.


