Status: #

Class: [[CSX3003]]

Subject/Topics: #Graphs

Date: 2024-09-02

Teacher: [[KWANKAMOL NONGPONG]]
___
Name - Puran Paodensakul
ID - 6611140
Sec - 542

Fundamental review questions:  
  
1) What are the components of a graph? 
   - The Vertices and Edges are the components of a graph.
  
2) Give a real-life example of a graph that is directed.  
   - A map from city to city.
  
3) Give a real-life example of a graph that is undirected. 
   -  facebook friend request system
  
4) What does it mean when a graph is called “connected”?  
   -  A graph is called connected if there is a path between any two vertices in the graph.

1) What does it mean when a graph is called “fully connected”?  
  -  A fully connected  graph means that every pair of vertices is connected by a unique edge.
  
6) Is a tree connected graph?  
   - Yes
  
7) A tree is a specific type of graph. What makes a tree distinguished from graph?  
   
  
8) What is rooted tree? 
   - A rooted tree is a tree where one vertex is designated as the root, and all other vertices are connected via directed paths emanating from the root. 
  
9) What is a leaf?  
   - A tree with no children.
  
10) How many edges are there in a tree having n nodes?  
  -  A tree with n nodes has n−1 edges.
  
11) How many simple path(s) is(are) there between a pair of tree nodes?  
  -  One
  
12) What is a “weighted” graph?
 - A weighted graph is one where each edge has an associated numerical value , often representing cost, distance, or time.

13) 13) For each of the graph below, give its representation as an edge list, a collection of  
adjacency lists, and an adjacency matrix.

## a) 

### Edge list:
```
(1,3), (1,2), (1,0)
```

### Adjacency lists:
```
0: [1]
1: [0, 2, 3]
2: [1]
3: [1]
```

### Adjacency matrix:
```
  0 1 2 3
0 0 1 0 0
1 1 0 1 1
2 0 1 0 0
3 0 1 0 0
```

## b)

### Edge list:
```
(1,2), (1,3), (2,3), (3,2), (3,4), (4,3)
```

### Adjacency lists:
```
1: [2, 3]
2: [3]
3: [2, 4]
4: [3]
```

### Adjacency matrix:
```
  1 2 3 4
1 0 1 1 0
2 0 0 1 0
3 0 1 0 1
4 0 0 1 0
```

## c) 

### Edge list:
```
(v1,v2,5), (v1,v3,6), (v2,v3,8), (v2,v4,3), (v2,v5,4), (v3,v5,6), (v4,v5,3), (v4,v6,7), (v5,v6,7)
```

### Adjacency lists:
```
v1: [(v2,5), (v3,6)]
v2: [(v1,5), (v3,8), (v4,3), (v5,4)]
v3: [(v1,6), (v2,8), (v5,6)]
v4: [(v2,3), (v5,3), (v6,7)]
v5: [(v2,4), (v3,6), (v4,3), (v6,7)]
v6: [(v4,7), (v5,7)]
```

### Adjacency matrix:
```
   v1  v2  v3  v4  v5  v6
v1  0   5   6   0   0   0
v2  5   0   8   3   4   0
v3  6   8   0   0   6   0
v4  0   3   0   0   3   7
v5  0   4   6   3   0   7
v6  0   0   0   7   7   0
```

## d)

### Edge list:
```
(F,B,13), (F,N,11), (A,F,43), (A,B,14), (B,D,23), (D,A,5), (N,B,22)
```

### Adjacency lists:
```
F: [(B,13), (N,11)]
A: [(F,43), (B,14)]
B: [(D,23)]
D: [(A,5)]
N: [(B,22)]
```

### Adjacency matrix:
```
  F  A  B  D  N
F 0  0  13 0  11
A 43 0  14 0  0
B 0  0  0  23 0
D 0  5  0  0  0
N 0  0  22 0  0
```
