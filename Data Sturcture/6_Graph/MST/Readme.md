# Minimum Spanning Tree

## Background

A Minimum Spanning Tree (MST) algorithm is a method used in graph theory to find a subset of edges in a connected, edge-weighted graph. This subset forms a tree that includes every vertex of the graph, and the total weight of all the edges in the tree is minimized. The concept of a minimum spanning tree is significant in various fields, such as network design, where it can be used to minimize the cost of connecting all points in a network.


Here are some of the key applications of MST:
1. **Urban and Transportation Planning**: MSTs can assist in optimizing road layouts, ensuring that all necessary areas are connected with the shortest possible total road length, reducing construction and maintenance costs.
2. **Computer Network Routing Protocols**: Some routing protocols used in computer networks, like the Link-State Routing Protocol, use MSTs to determine the most efficient routing path.
3. **Forestry Management**: In forestry, MSTs can help in planning roads to access various forest locations with minimal environmental impact.

## Algroithm

There are several algorithms to find a minimum spanning tree, but two of the most well-known are Kruskal's Algorithm and Prim's Algorithm. Here's a general description of how MST algorithms typically work:

**Initialize**: Start with a graph consisting of vertices and weighted edges. In the beginning, the MST contains no edges.

**Edge Selection**: At each step, select an edge that has the lowest weight and does not form a cycle is added to the MST.

**Adding the Edge**: If the edge is safe to add (i.e., it doesn't form a cycle), include it in the MST.

**Repeat**: Continue the process until the MST has  V − 1 edges, where V is the number of vertices in the graph.

<center>
    <img src = './img/01.png' width = 600px>
</center>   


<center>
    <img src = './img/02.png' width = 600px>
</center>   
<center>
    <img src = './img/03.png' width = 600px>
</center>   

<center>
    <img src = './img/04.png' width = 600px>
</center>   

## Implementation

The hard point here is how to detect cycle and how to find the minimum weight.

Assume we have graph has structed like below:

```python
N = 10  # number of vertex in graph
M = 20
graph = []

for i in range (M):
    a, b, weight = map(int, input().split())
    edge = list(map(int, input().split()))
    graph.append(edge)
```

```python

def root(parent, i):
    if parent[i] == i:
        return i
    return root(parent, parent[i])

def union(parent, rank, x, y):
    # Find the roots of the sets that x and y belong to.
    xroot = root(parent, x)
    yroot = root(parent, y)

    # Attach the smaller tree under the root of the bigger tree.
    # This is the "union by rank" optimization.
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def MST(N, graph, d):
    # Sort the edges by weight
    sorted_graph = sorted(graph, key=lambda x: x[2])

    parent = {}
    rank = {}

    for edge in sorted_graph:
        v1, v2, _ = edge
        if v1 not in parent:
            parent[v1], rank[v1] = v1, 0
        if v2 not in parent:
            parent[v2], rank[v2] = v2, 0

    for edge in sorted_graph:
        v1, v2, _ = pipe
        v1_root = root(parent, v1)
        v2_root = root(parent, v2)

        if v1_root != v2_root:
            union(parent, rank, v1_root, v2_root)
            # we need this edge 
        else:
            # we do not need this edge (there is a cycle)
```

## Exercise


**Problem Description**

The city of Waterloo has buildings numbered 1, 2, . . . , N. The city has M pipes that connect
pairs of buildings. Due to urban planning oversights, building 1 is the only sewage treatment plant
in the city. Each pipe can be either active or inactive. The set of active pipes forms a valid plan
if building 1 is directly or indirectly connected to each other building using active pipes. (Pipes
directly connect pairs of buildings. Buildings X and Z are indirectly connected if X is directly or
indirectly connected to Y , and Y is directly or indirectly connected to Z.)

The municipal government of Watermoo is currently operating a valid plan of N −1 pipes today,
but they think it is too expensive! Each pipe has a monthly maintenance fee that the city must pay
when it is active, and the total cost of a valid plan is the sum of the maintenance fees of its active
pipes. (Inactive pipes cost nothing.)

The city wants you to minimize the cost of the plan, and they want you to do it quickly. Every
day, the city will allow you to activate one pipe, and deactivate another pipe. How many days do
you need to make the set of active pipes form a valid plan, whose cost is minimum among all valid
plans

Note that it is possible that the plan becomes invalid while you are working, but by the end it
should be a valid plan.


**Input Specification**

The first line will contain the integers N, M, and D (1 ≤N ≤100 000, N −1 ≤M ≤
200 000). Each of the next M lines contain three integers A<sub>i</sub>, B<sub>i</sub>, and C<sub>i</sub>, which
means that there is a pipe from building A<sub>i</sub> to building B<sub>i</sub> that costs C<sub>i</sub> per month when activated
(1 ≤A<sub>i</sub>, B<sub>i</sub> ≤N, 1 ≤C<sub>i</sub> ≤10<sup>9</sup>). The first N − 1 of these lines represent the valid plan the city is currently using.

It is guaranteed that there is at most one pipe connecting any two buildings and no pipe connects a
building to itself.

**Output Specification**

Output one integer on a single line, the minimum number of days to complete this task. If the
initial valid plan is already an optimal plan, then output 0.

**Sample Input 1**
```
4 4 0
1 2 1
2 3 2
3 4 1
4 1 1
```
**Output for Sample Input 1**

```
1
```


