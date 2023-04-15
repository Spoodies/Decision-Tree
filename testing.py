from decision_tree import *
from graphviz import Digraph

# Update the standalone visualization function
def visualize_tree(tree):
    g = Digraph('DecisionTree', format='png')
    g.attr(rankdir='LR', size='10,5')

    for node in tree.nodes:
        g.node(str(node.id), label=str(node.id), shape='circle', color='skyblue', style='filled')

    for arc in tree.arcs:
        g.edge(str(arc.node_from.id), str(arc.node_to.id),
               label=f'{arc.profit:.1f}, {arc.chance * 100:.0f}%' if arc.chance is not None else f'{arc.profit:.1f}',
               fontsize='12', color='gray')

    g.view()

budget = Tree()
# Arcs: From Node, To Node, profit(0), chance
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
for i in range(2, 5):
    print(budget.nodes[i-1].value)

# visualize_tree(budget)