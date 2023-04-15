import tkinter as tk
from tkinter import ttk
from decision_tree import *
from graphviz import Digraph

# Update the standalone visualization function
def visualize_tree(tree):
    g = Digraph('DecisionTree', format='png')
    g.attr(rankdir='LR', size='20,10')

    for node in tree.nodes:
        label = str(node.id) + "\n" + f'{node.value:.2f}'
        g.node(str(node.id), label=label, shape='circle', color='skyblue', style='filled')

    for arc in tree.arcs:
        g.edge(str(arc.node_from.id), str(arc.node_to.id),
               label=f'{arc.profit:.1f}, {arc.chance * 100:.0f}%' if arc.chance is not None else f'{arc.profit:.1f}',
               fontsize='12', color='gray')

    g.view()

# Create a window
root = tk.Tk()
root.title("Decision Tree Builder")

# Create a Tree object
budget = Tree()

# Function to add arc
def add_arc(event=None):
    node_from = int(entry_node_from.get())
    node_to = int(entry_node_to.get())
    profit = float(entry_profit.get())
    chance = float(entry_chance.get()) if entry_chance.get() != '' else None
    tree_view.insert('', 'end', values=(node_from, node_to, profit, chance))

    # Clear the entry fields
    entry_node_from.delete(0, tk.END)
    entry_node_to.delete(0, tk.END)
    entry_profit.delete(0, tk.END)
    entry_chance.delete(0, tk.END)


# Function to edit arc
def edit_arc():
    selected_item = tree_view.selection()[0]
    values = tree_view.item(selected_item)['values']

    entry_node_from.insert(0, values[0])
    entry_node_to.insert(0, values[1])
    entry_profit.insert(0, values[2])
    entry_chance.insert(0, values[3] if values[3] is not None else '')

    tree_view.delete(selected_item)


def update_arc(event=None):
    add_arc()
    edit_button.config(state=tk.DISABLED)

def drag_and_drop(event):
    if tree_view.identify_region(event.x, event.y) == "separator":
        return

    selected_item = tree_view.selection()[0]
    x, y, widget = event.x, event.y, event.widget
    drop_index = widget.index(widget.identify_row(y))

    tree_view.move(selected_item, '', drop_index)

# Function to finish and visualize tree
def finish():
    for row in tree_view.get_children():
        values = tree_view.item(row)['values']
        budget.add_arc(*values)
    budget.finished()
    visualize_tree(budget)
    root.quit()

# Entry fields
entry_node_from = tk.Entry(root)
entry_node_to = tk.Entry(root)
entry_profit = tk.Entry(root)
entry_chance = tk.Entry(root)
entry_chance.insert(0, '')

# Labels
label_node_from = tk.Label(root, text="Node from ID:")
label_node_to = tk.Label(root, text="Node to ID:")
label_profit = tk.Label(root, text="Profit:")
label_chance = tk.Label(root, text="Chance:")

# Treeview
tree_view = ttk.Treeview(root, columns=("Node From", "Node To", "Profit", "Chance"), show="headings")
tree_view.heading("Node From", text="Node From")
tree_view.heading("Node To", text="Node To")
tree_view.heading("Profit", text="Profit")
tree_view.heading("Chance", text="Chance")

# Function to handle tree_view selection
def on_treeview_select(event):
    if tree_view.selection():
        edit_button.config(state=tk.NORMAL)

# Bind the selection event
tree_view.bind("<<TreeviewSelect>>", on_treeview_select)

# Bind Enter key to the add_arc function
root.bind('<Return>', add_arc)
root.bind('<Return>', update_arc)
tree_view.bind('<B1-Motion>', drag_and_drop)

# Buttons
add_arc_button = tk.Button(root, text="Add Arc", command=add_arc)
edit_button = tk.Button(root, text="Edit Arc", command=edit_arc, state=tk.DISABLED)
finish_button = tk.Button(root, text="Finish", command=finish)

# Grid layout
label_node_from.grid(row=0, column=0)
entry_node_from.grid(row=0, column=1)

label_node_to.grid(row=1, column=0)
entry_node_to.grid(row=1, column=1)

label_profit.grid(row=2, column=0)
entry_profit.grid(row=2, column=1)

label_chance.grid(row=3, column=0)
entry_chance.grid(row=3, column=1)

add_arc_button.grid(row=4, column=0, pady=10)
edit_button.grid(row=4, column=1, pady=10)
finish_button.grid(row=4, column=2, pady=10)

tree_view.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()

# Arcs: From Node, To Node, profit(0), chance
# budget.add_arc(0, 2, -7.1)
# budget.add_arc(0, 3, -2.8)
# budget.add_arc(0, 4, -1.2)
#
# i = 0
# budget.add_arc(2+i, i*3+5, 15.4, 0.15)
# budget.add_arc(2+i, i*3+6, 5.2, 0.65)
# budget.add_arc(2+i, i*3+7, 3.1, 0.2)
#
# i = 1
# budget.add_arc(2+i, i*3+5, 10.2, 0.15)
# budget.add_arc(2+i, i*3+6, 4.6, 0.65)
# budget.add_arc(2+i, i*3+7, 1.9, 0.2)
#
# i = 2
# budget.add_arc(2+i, i*3+5, 5.3, 0.15)
# budget.add_arc(2+i, i*3+6, 2.8, 0.65)
# budget.add_arc(2+i, i*3+7, 0.9, 0.2)
