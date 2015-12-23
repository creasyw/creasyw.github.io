---
layout: post
title: "All-pairs shortest path"
date: 2013-09-30 23:49
comments: true
summary: An algorithmic analysis for the problem of all-pairs shortest path
categories:
- Programming
tags:
- Python
- Algorithm
- code snippet
---

The question comes from the online course *Algorithm Design and Analysis (Part II)* in coursera. It is an [all-pairs shortest path problem](http://en.wikipedia.org/wiki/Shortest_path_problem#All-pairs_shortest_paths). As mentioned in the wikipedia, a more straightforward solution with Floyd–Warshall algorithm takes \\(O(N^3)\\) complexity, and the more computational efficient approach is to use a combination of Dijkstra's algorithm, Bellman-Ford algorithm, and Johnson's algorithm, which chould decrease the complexity to \\(O(N^2logN)\\). I implement the latter one for more interesting and challenging. There are several obstacles make the implementation a little bit trickier than I thought.

I have tried two or three different versions of Dijkstra's algorithm while solving other math puzzles, and this time I use the built-in heapq function in Python. Keeping the "about-to explore" nodes in order and extracting the smallest/largest cost one in every iteration are the essense of this algorithm. But the cost to every node has to be updated when a node moves from "about-to explore" to "fully explored" category. At first, I just remove the original value and push the updated one into the heap. Because the heapq has no updated or remove methods, I can only use the remove mehtod of the list. This works fine for small amount of nodes (200) but the heap cannot keep right struture when the data becomes just a little bigger (500). Then I have to *heapify* it every time I update a "about-to explore" node.

{% highlight python %}
def dijkstras(graph, start):
    # keep a record of the distance of the nodes from the start vertex
    distance = defaultdict()
    # keep track of the candidates for the next move
    index = defaultdict()
    # store the cost and node into heap using cost as the key
    heap = []
    heapq.heapify(heap)
    #will be used to trace the path of the sjortest distance to each node
    distance[start] = 0
    if start in graph and type(graph[start])==dict:
        for (node, cost) in graph[start].items():
            heap_update(heap, index, node, cost)
    else:
        return distance
    #initially all nodes are yet to be explored
    while len(index) > 0:
        # need to extract the node with the minimum path
        node, cost = heap_pop(heap, index)
        # store the node into known graph
        distance[node] = cost
        # update the knowledge according to existing node
        if node in graph and type(graph[node])==dict:
            for (node, localcost) in graph[node].items():
                if node not in distance:
                    heap_update(heap, index, node, localcost+cost)
    return distance
{% endhighlight %}

The Bellman-Ford algorithm is more expensive compared with Dijkstra's algirhtm if the graph is densily connected, but it deals with negative edge cost. This is also the one that helps me fully appreciate the dynamic programming.The implementation is intuitive and straightforward. For every vertex, the brutal force search performs to find the current optimal solution based on the previous knowledge. The optimization for space complexity is to only store the most recent result--keep an 2\*N array and use a pointer filp-flop in every iteration is more effecient than keeping two 1\*N array, discarding the older one and reclaiming a new one in every iteration. Aother optimization I make is to store the "about-to explore" nodes in a bucket, just as what Dijkstra's does, which eliminates plenty of unnecessary calculation. But its tricky aspect is that because this algorithm is computing "distributed", different from the "centralized" spanning of Dijkstra's, if several "exploring" vertices point to a same "about-to explore" vertex, only the optimal cost should be kept.


{% highlight python %}
def bellman_ford (arr, start, size):
    """ The input arr stores all info of the graph in a dictionary.
        The basic element in the arr are three-columns data -- 
        [start_point, end_point, cost]"""
    count = 1
    data = np.zeros((2, size+1))
    # initialization
    data.fill(float("inf"))
    data[0, start] = 0
    bucket = {}
    for i in arr[start]:
        bucket[i] = {start:arr[start][i]}
    
    for i in range(1, size):
        # use set() to make sure start points in the next round are unique
        candidate = set()
        previous = count ^ 1
        data[count] = data[previous]
        for v in bucket:
            data[count, v] = min(data[previous, v], \
		data[previous, bucket[v].keys()[0]] \
	        +bucket[v].values()[0])
            candidate.add(v)
        # stop early if there is no place to span
        if (data[count]==data[previous]).all():
            break
        # update the bucket
        bucket = {}
        for j in candidate:
            for k in arr[j]:
                if (k in bucket and data[count,j]+arr[j][k] < \
		      data[count, bucket[k].keys()[0]] + \
		      bucket[k].values()[0]) or k not in bucket:
                    bucket[k] = {}
                    bucket[k][j] = arr[j][k]
        if not bucket:
            break
        count = previous
    
    # check cycle with negative sum
    previous = count ^ 1
    data[count] = data[previous]
    for v in bucket:
        data[count, v] = min(data[previous,v], \
		data[previous, bucket[v].keys()[0]]+bucket[v].values()[0])
    if (data[count]== data[previous]).all():
        return data[count]
    else:
        return float("inf")
{% endhighlight %}

Finally, the two algorithms above are connected by the Johnson's algorithm. Dijkstra's algorithm cannot deal with negative edge costs, but much more fast than Bellman-Ford especially in the case of "all-pairs". Furthermore, the negative costs cannot be got rid of by adding uniformly for every edge. Johnson's algorithm neatly solves it by adding pseudo-node to find weights of vertices and changing values of edges concerning their connected vertices. There is no hidden obstacle in the implementation. Only the special care should be taken for manipulating the nodes. It reminds me coding in C...

{% highlight python %}
def johonsons(data, vertex):
    d1 = data.copy()
    # make psedu node pointing to all other nodes with zero cost
    plus1 = vertex+1
    d1[plus1] = {}
    for i in range(1, plus1):
        d1[plus1][i] = 0
    # calculate the reweight vector
    reweight = bellman_ford(d1, plus1, plus1)
    # reweight all cost to make it nonnegative
    if type(reweight) == float:
        # stop if there is any negative cycle in the graph
        return None
    else:
        for i in data:
            for k in data[i]:
                data[i][k] = data[i][k]+reweight[i]-reweight[k]
    
    return [min(reconvert(reweight,vertex,dijkstras(data,i),i))\
            for i in range(1,vertex+1)]
{% endhighlight %}

The overall algorithm solves the question and runs kind of standard. Still, I do not satisfy with the update procedure of heap. I will write a new version of this data structure in the near future and see if it can provide significant boost for the performance.

p.s. The vistualization of code block is optimized from the original Octopress style to Github-style based on the [tutorial](http://blog.codebykat.com/2013/05/23/gorgeous-octopress-codeblocks-with-coderay/).  
p.p.s. The inline latex-style formula comes with Kramdown, MathJax and [this tutorial](http://yoyzhou.github.io/blog/2012/08/05/add-latex-support-for-octopress/). Besides, there is [another minor bug to deal with](http://brianbuccola.github.io/blog/2012-11-28-latex-math-in-octopress.html).
