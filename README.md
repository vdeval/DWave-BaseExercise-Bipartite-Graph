# DWave-BaseExercise-Bipartite-Graph
D-Wave project. Base Exercise: **Bipartite Graph**
## Description
A graph is bipartite if and only if it is possible to assign one of two different colors to each vertex of the graph so that no two adjacent vertices are assigned the same color.
* **Given**: G = {V={Vi}, E={Ei}}
* **Goal**: find, if exists, a partition of V in two subset corresponding to the bipartite graph
## Solution:
It is straigthforward to map the graph to be analyzed to a graph representation of a QUBO problem:
* Each vertex corresponds to a QUBO variable.
* Each edge is translated in a constraint between the two vertices (QUBO variables) of type "different values".

Processing all the edges and summing the constraint values for all of them in the QUBO Dictionary will create the overall constraint for the graph.

## Implementation:
1. Build a QUBO graph with variables "x" corresponding to vertices of the graph.
1. Connected vertices of the graph correspond to connected vertices in the QUBO (quadratic terms).
1. For each variable "x", value 0 corresponds to one color, value 1 corresponds to the other.
1. The constraint for two adjacent vertices (x1 and x2) having different colors is implemented by:  
 `- x1 - x2 + 2x1x2 + 1`
1. Apply the constraint to all the pairs of connected vertices and sum up all the values for linear terms. (Note: As the constant "-1" is not added to the QUBO, the minimum energy will not be zero, but "-n" where n is the numebr of edges {Ei})
1. Input the graph to a sampler. If the graph is bipartite there are at least two solutions (symmetric between them) with energy "-n", and the values of the "x" define how to assign colors to each vertex.