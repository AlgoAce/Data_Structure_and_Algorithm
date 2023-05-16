# Graph

## Application

### Traveling Salesperson Problem
<img src="./img/00.png" />

### Propositional Satisfiability

Given a propositional formula, is there a way to assign truth values to the variables to make the formula true?

$$
((((a \wedge b) \vee c) \wedge d) \vee (\neg e))
$$

### Hua rong Pass Puzzle

<img src="./img/01.png" />

### 8 Puzzle

<img src="./img/02.png" />

---

# Graph Search

<img src="./img/03.png" />

### Formally a Graph Search

A search Problem is defined by:

-  A set of states
-  A start state
-  Goal State
-  A succeror (neighbour) function
-  (opt) A cost associated with each action

### Example

<img src="./img/04.png" />

Question: How to formulating 8-puzzle as a Search Problem

Question: Which of the following is a successor of 530, 976, 241?

- 350, 876, 241
- 536, 870, 241
- 537, 806, 241
- 538, 076, 241

### Generate a Search Tree
<img src="./img/05.png" />

```Python
# G => The Graph
# s => start state
# goal(n) => Goal test
def generalSearchProblem(G, s, goal(n)):
    frontier = {[s]}

    while frontier is not empty:
        select and remove path <n0, ..., nk> from frontier

        if (goal(nk)):
            return <n0, ..., nk> 
        
        for every neighbour n of nk:
            add <n0, ..., nk> to frontier
        
    return no solution
```


# Uniformed Search Algroithms

### Deap-First Search

- Treat the frontier as a stack (Last in first out)
- Expand the last recent node added to forntier

#### Trace DFS on the search tree

<img src="./img/06.png" />

#### Properties of DFS
- Space complexity?
- Time complexity?
- Guaranteed to find a solution if on exists?

#### Try DFS on this grid search problem
- Expand the succerrors in the order: up, left, right and down
- Number the nodes as they are removed from the frontier
- Use cycle pruning
<img src="./img/07.png" />

### Breadth-first Search

- Treat the frontier as a queue (First in first out)
- Expand the oldest node added to forntier

#### Trace BFS on the search tree

<img src="./img/06.png" />

#### Properties of BFS
- Space complexity?
- Time complexity?
- Guaranteed to find a solution if on exists?

#### Try BFS on this grid search problem
- Expand the succerrors in the order: up, left, right and down
- Number the nodes as they are removed from the frontier
- Use cycle pruning
<img src="./img/07.png" />

## Compareing BFS and DFS

Which of BFS and DFS would you choose? Why?
1. Memory is limited.
2. All solutions are deep in the tree.
3. The search graph contains cycles.
4. The branching factor is large/infinite.
5. We must find the shallowest goal node.
6. Some solutions are very shallow.

## Exercise:

- Suppose that mempry is very limited. Which of BFS and DFS would you choose?
  - BFS
  - DFS
  - Both
  - Neither

- Suppose that all solutions are deep in the search tree. Which of BFS and DFS would you choose?
  - BFS
  - DFS
  - Both
  - Neither

- Suppose that we must find the shallowest goal node. Which of BFS and DFS would you choose?
  - BFS
  - DFS
  - Both
  - Neither

- Suppose that all solutions are shallow in the search tree. Which of BFS and DFS would you choose?
  - BFS
  - DFS
  - Both
  - Neither

## Lowest-cost first search
What if arcs have different costs?

We want an algorithm to find the optimal solution.

The frontier is a priority queue ordered by path cost. Expand the neighbour with the lpwesrt total cost.

