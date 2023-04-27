from decision_tree import *
import pydot
from PIL import Image
import io

def visualize_tree(tree):
    graph = pydot.Dot(graph_type='digraph', rankdir='LR')

    # Add nodes
    for node in tree.nodes:
        label = f'{node.id}\n{node.value}'
        graph.add_node(pydot.Node(node.id, label=label, shape='circle', style='filled', fillcolor='lightblue'))

    # Add edges
    for arc in tree.arcs:
        label = f'{arc.profit} ({arc.chance})' if arc.chance is not None else f'{arc.profit}'
        graph.add_edge(pydot.Edge(arc.node_from.id, arc.node_to.id, label=label, fontsize="10"))

    # Display the graph using PIL.Image
    png_data = graph.create_png()
    image = Image.open(io.BytesIO(png_data))
    image.show()

# Arcs: From Node, To Node, profit(0), chance
budget = Tree()

budget.add_arc(0, 2, -7.1)
budget.add_arc(0, 3, -2.8)
budget.add_arc(0, 4, -1.2)

i = 0
budget.add_arc(2+i, i*3+5, 15.4, 0.15)
budget.add_arc(2+i, i*3+6, 5.2, 0.65)
budget.add_arc(2+i, i*3+7, 3.1, 0.2)

i = 1
budget.add_arc(2+i, i*3+5, 10.2, 0.15)
budget.add_arc(2+i, i*3+6, 4.6, 0.65)
budget.add_arc(2+i, i*3+7, 1.9, 0.2)

i = 2
budget.add_arc(2+i, i*3+5, 5.3, 0.15)
budget.add_arc(2+i, i*3+6, 2.8, 0.65)
budget.add_arc(2+i, i*3+7, 0.9, 0.2)

budget.finished()

# Add this line at the end of your running file
visualize_tree(budget)