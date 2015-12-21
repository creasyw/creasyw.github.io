---
layout: post
title: "Solving Sudoku"
date: 2015-01-06 16:37
comments: false
tags:
- Programming
- code snippet
- Algorithm
---

Sudoku is one of my long-time favorite game for killing time in a flight or idly waiting something. It tests memory and deduction. More importantly, it is fun to play.

The original thought of solving it comes from the [Algorithm Design Manual](http://www.algorist.com) and its [wiki page](http://en.wikipedia.org/wiki/Sudoku_solving_algorithms). However, the backtracking algorithm provided in both places are somewhat obscure. Specifically for the backtracking solution, the algorithm is:

{% highlight python lineanchors %}
def backtracking(board, x, y):
    if finished(x, y):
        return board
    elif board(x, y) is not empty:
        return backtracking(board, x+1, y)

    temp = local_copy(board)
    for i in every possible value:
        temp[x, y] = i
        backtracking(temp, x+1, y)
        temp[x, y] reset to empty
{% endhighlight %}

By exploring every possible solution, it actually performs a depth-first search. But as a typical backtracking implementation, a proper pruning has a greater impact on search time than any other factor. Specifically, a pruning strategy requires carefully ordering the evaluations of the pieces. In this implementation, it means that the algorithm needs to decide evaluating which empty slot. Obviously, in a given stage, evaluating a slot with only three candidates takes only 1/3 search spacing comparing with a slot with nine candidates.

I use the basic rules of Sudoku to eliminate candidates:

1. If a square has only one possible value, then eliminate that value from the square's peers (same line, same column, and same zone).
2. If a unit has only one possible place for a value, then put the value there.

Each iteration of backtracking possesses its own information of both board and the available candidates for each currently empty slot. The algorithm only explore the slot with lest candidates, and whenever an empty slot is assigned a value, both information will be updated. This process is called _variables ordering_ by [Constraint Propagation](http://norvig.com/sudoku.html).

Concerning the data types, it is tempting to use heap for the empty slots since the program is only interest in the slot with lest candidates. But since the constraints also needs to update in every iteration, and there are only 60+ empty slots at most. It is good enough to use a dictionary with coordinates as key and the candidates as values.

The two major functions are the Constraint Propagation:
{% highlight python lineanchors %}
def eliminate(choices, val, i, j):
    result = {}
    # deep copy
    for item in choices:
        result[item] = list(choices[item])
    del result[(i,j)]
    for m in range(9):
        # propagate in the same row
        if (i,m) in result and val in result[(i,m)]:
            result[(i,m)].remove(val)
        # propagate in the same col
        if (m,j) in result and val in result[(m, j)]:
            result[(m, j)].remove(val)
    # propagate in the same zone
    for m in range(i/3*3, i/3*3+3):
        for n in range(j/3*3, j/3*3+3):
            if (m,n) in result and val in result[(m,n)]:
                result[(m,n)].remove(val)
    return result
{% endhighlight %}
, and the optimized main function:
{% highlight python lineanchors %}
def solve_opt(board, choices):
    if len(choices) == 0:
        return board

    temp = np.array(board)
    x, y = min(choices, key=(lambda k: len(choices[k])))
    if len(choices[(x, y)]) == 0:
        return None
    for i in choices[(x, y)]:
        temp[x, y] = i
        temp_choices = eliminate(choices, i, x, y)
        result = solve_opt(temp, temp_choices)
        if result is not None:
            return result
        temp[x, y] = 0
{% endhighlight %}

The complete program can be found [here](https://gist.github.com/creasyw/79648574056bdc881c2f).

It is nice to see the hardest puzzle solved in a second:) And how simple the original algorithm is for a seemly complicated problem.


cheers:)
