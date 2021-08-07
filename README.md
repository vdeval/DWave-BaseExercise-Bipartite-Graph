# DWave-BaseExercise-Bipartite-Graph
D-Wave project. Base Exercise: Bipartite Graph
## Project Name
Bipartite Graph
## Description
Test program for checking if a graph is bipartite

Problem: 

A graph is bipartite if and only if it is possible to assign one of two different colors to each vertex of the graph so that no two adjacent vertices are assigned the same color.

Given: G = {V={Vi}, E={Ei}}

Goal: find, if exists, a partition of V in two subset corresponding to the bipartite graph

Implementation principles:
1. Build a QUBO graph with variables "x" corresponding to vertices of the graph.
1. Connected vertices of the graph corresponding to connected vertex in the QUBO (quadratic terms).
1. For each variable "x", value 0 corresponds to one color, value 1 corresponds to the other.
1. The constraint for two adjacent vertices (x1 and x2) having different colors is implemented by: - x1 - x2 + 2x1x2 + 1
1. Apply the constraint to all the pairs of connected vertices and sum up all the values forlinear terms. (Note: As the constant "-1" is not added to the QUBO, the minimum energy will not be zero, but "-n" where n is the numebr of edges {Ei})
1. Input the graph to a sampler. If the graph is bipartite there are at least two solutions (symmetric between them) with energy "-n", and the values of the "x" define how to assign colors to each vertex.