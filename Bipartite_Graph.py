###################################################################################################
# Test program for checking if a graph is bipartite
#
# Problem: 
# A graph is bipartite if and only if it is possible to assign one of two different colors
# to each vertex of the graph so that no two adjacent vertices are assigned the same color.
#
# Given: G = {V={Vi}, E={Ei}}
#
# Goal: find, if exists, a partition of V in two subset corresponding to the bipartite graph
#
# Implementation principles:
# 1 - Build a QUBO graph with variables "x" corresponding to vertices of the graph.
# 2 - Connected vertices of the graph corresponding to connected vertex in the QUBO (quadratic terms).
# 3 - For each variable "x", value 0 corresponds to one color, value 1 corresponds to the other.
# 4 - The constraint for two adjacent vetices (x1 and x2) having different colors is implemented by:
#         - x1 - x2 + 2x1x2 + 1
# 5 - Apply the constraint to all the pairs of connected vertices and sum up all the values for
#     linear terms.
#     Note: As the constant "-1" is not added to the QUBO, the minimum energy will not be zero
#           but "-n" where n is the numebr of edges {Ei}
# 6 - Input the graph to a sampler. If the graph is bipartite there are at least two solutions
#     (symmetric between them) with energy "-n", and the values of the "x" define how to assign
#     colors to each vertex.
###################################################################################################

# ------- Import Section -------

# Python library import section
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

# D-Wave library import section
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave_networkx as dnx

# Custom Library for Graph Drawing
import MyGraph as mg

# ------- Code section -------

# ------- Main function to test for bipartite graph -------
def TestBipartite (G, label):
    # Print the original graph
    mg.DrawG(G, (label + ": Original Graph"))
    # ------- Create the QUBO -------
    # Initialize the Q matrix
    Q = defaultdict(int)
    # Fill in Q matrix:
    # For each edge (u,v):
    #    Add "-1" to both the "u" diagonal term and the "v" diagonal term
    #    Add "+2" to the "(u,v)" quadratic term
    for u, v in G.edges:
        Q[(u,u)] += -1
        Q[(v,v)] += -1
        Q[(u,v)] += 2
    # ------- Run our QUBO on the QPU -------
    # Run the QUBO on the solver from your config file
    sampler = EmbeddingComposite(DWaveSampler())
    response = sampler.sample_qubo(Q,
                                chain_strength=10,   # Arbitrary choice...
                                num_reads=100,
                                label=label1)
    print(response)
    # ------- Check if the graph is bipartite -------
    energy = response.first.energy
    e_len = len(G.edges)
    print("Energy: ", energy, " - Edges: ", e_len )
    if energy == -e_len:
        print ("Graph is bipartite")
    else:
        print ("Graph is not bipartite")
    # ------- Print the graph -------
    # Select first response
    #sample = response.record.sample[0]
    sample = response.first.sample
    # Select the color for each node
    def nodeColor(s):
#        if sample[s-1]==0 : return 'green'
        if sample[s]==0 :   return 'green'
        else:               return 'red'
    node_color = [nodeColor(x) for x in G.nodes]
    # Print with node color
    mg.DrawG(G, (label + ": Bipartite Graph"), node_color)


# ------- Main -------

# ------- Graph 01: Bipartite -------
label1 = "Graph 01"
print("Analysing graph - ", label1)
# Create graph with NetworkX
G1=nx.Graph()
G1.add_node(1, pos=(1,2) )
G1.add_node(2, pos=(3,2) )
G1.add_node(3, pos=(0,0) )
G1.add_node(4, pos=(4,0) )
G1.add_node(5, pos=(2,-1) )
G1.add_edges_from([(1,3),(1,4),(2,3),(2,4),(5,3),(5,4)])
# Call the function
TestBipartite (G1, label1)

# ------- Graph 02: Bipartite -------
label2 = "Graph 02"
print("Analysing graph - ", label2)
# Create graph with NetworkX
G2=nx.Graph()
G2.add_node('a', pos=(1,3) )
G2.add_node('b', pos=(2,3) )
G2.add_node('c', pos=(3,2) )
G2.add_node('d', pos=(2,0) )
G2.add_node('e', pos=(1,0) )
G2.add_node('f', pos=(0,1) )
G2.add_node('g', pos=(0,2) )
G2.add_edges_from([('a','c'),('a','e'),('a','g'),
                   ('b','c'),('b','e'),('b','f'),
                   ('c','d'),
                   ('d','e'),('d','f'),('d','g')])
# Call the function
TestBipartite (G2, label2)

# ------- Graph 03: NOT Bipartite -------
label3 = "Graph 03"
print("Analysing graph - ", label3)
# Create graph with NetworkX
G3=nx.Graph()
G3.add_node('a', pos=(1,2) )
G3.add_node('b', pos=(2,2) )
G3.add_node('c', pos=(3,1) )
G3.add_node('d', pos=(2,0) )
G3.add_node('e', pos=(1,0) )
G3.add_node('f', pos=(0,1) )
G3.add_edges_from([('a','b'),('a','e'),('a','f'),
                   ('b','c'),('b','d'),('b','e'),('b','f'),
                   ('c','d'),('c','f'),
                   ('d','e'),('d','f'),
                   ('e','f')])
# Call the function
TestBipartite (G3, label3)