###################################################################################################
# Custom library for basic graph functions
#
# 1 - DrawG: Print a graph on a file, with node labels and [optional] colors for nodes and edges
#     Input:  G: graph (NetworkX)
#             filename: file to be created (png format)
#             [n_col]: node color
#             [e_col]: edge color
#
#
###################################################################################################

# ------- Import -------

# Python library import section
import matplotlib.pyplot as plt
import networkx as nx


#  ------- Print a graph -------
def DrawG(G, filename, n_col='#1f78b4',e_col='k'):
    node_pos = nx.get_node_attributes(G,'pos')
    if node_pos: nx.draw(G,node_size=200, edgelist=list(G.edges), nodelist=list(G.nodes), pos=node_pos, 
                         node_color=n_col, edge_color=e_col, with_labels = True)
    else:        nx.draw(G,node_size=200, edgelist=list(G.edges), nodelist=list(G.nodes),
                         node_color=n_col, edge_color=e_col, with_labels = True)
    plt.savefig(filename, facecolor='white', dpi=100)
    plt.clf()


#  ------- Test Area -------

# Print a graph
#G01 = nx.Graph([(1,2), (2,3), (3,4), (3,5), (4,5), (4,6), (6,7), (7,8), (3,8)])
#DrawG(G01, "MyGraph_01")
#DrawG(G01, "MyGraph_02","red")
#DrawG(G01, "MyGraph_03","red","green")
#DrawG(G01, "MyGraph_04",["red","black","red","black","red","black","red","black"],
#      ["green","yellow","green","yellow","green","yellow","green","yellow","green"])

# Print a graph with positions
#G02=nx.Graph()
#G02.add_node("R1", pos=(1,2))
#G02.add_node("R2", pos=(2,2))
#G02.add_node("R3", pos=(3,2))
#G02.add_node("R4", pos=(4,2))
#G02.add_node("R5", pos=(5,2))
#G02.add_node("A1", pos=(1,0))
#G02.add_node("A2", pos=(2,0))
#G02.add_node("A3", pos=(3,0))
#G02.add_node("A4", pos=(4,0))
#G02.add_node("A5", pos=(5,0))
#G02.add_edges_from([("R1","A1"),("R1","A2"),
#                    ("R2","A1"),("R2","A5"),
#                    ("R3","A1"),
#                    ("R4","A2"),("R4","A4"),("R4","A5"),
#                    ("R5","A3"),("R5","A5")])
#DrawG(G02, "MyGraph_11")
#DrawG(G02, "MyGraph_12",["red","red","red","red","red","blue","blue","blue","blue","blue"],
#      ["green","green","yellow","yellow","green","yellow","yellow","yellow","green","green"])