
class Tree:
    def __init__(self):
        self.start = Node(0)
        self.nodes = [self.start]
        self.arcs = []

    def __repr__(self):
        return "This is a Decision Tree"

    def finished(self):
        if self.valid():
            print("yippie")
        else:
            print("NOOOOOoOOOOooo")
        self.final_values()
        self.expected_values()

    def id_finder(self, id):
        for i in self.nodes:
            if i.id == id:
                return i
        print("Invalid Entry")
        return None

    def add_arc(self, node_from, node_to, profit=0, chance=None):
        #Creates node to go towards
        node_to = Node(node_to)
        self.nodes.append(node_to)
        #finds the node the arc is coming from
        node_from = self.id_finder(node_from)

        #Creates arc going with node from, node to, profit and chance
        arc = Arc(node_from, node_to, profit, chance)
        self.arcs.append(arc)

        node_to.arcs_in.append(arc)
        node_from.arcs_out.append(arc)

    def valid(self):
        for i in self.nodes:
            current_node = i
            going = True
            past_nodes = []
            while going:
                past_nodes.append(current_node)
                for i in range(0, len(past_nodes)):
                    for j in range(0, len(past_nodes)):
                        if (i != j) and (past_nodes[i] == past_nodes[j]):
                            return False

                if (current_node.arcs_in == []) and (current_node != self.start):
                    return False
                elif current_node.arcs_in == []:
                    going = False
                else:
                    current_node = current_node.arcs_in[0].node_from

        for i in self.nodes:
            length = len(i.arcs_out)
            counter = 0
            sum = 0
            for j in range(0, length):
                for k in self.chance_arcs():
                    if i.arcs_out[j] == k:
                        sum = sum + i.arcs_out[j].chance
                        counter = counter + 1
            if (round(sum, 3) != 1) and (counter == length) and (length != 0):
                print("Chances dont add to 1")
                return False
            if (counter != 0) and (counter != length):
                print("Some nodes aren't all chance or all not chance.")
                return False

        return True

    def end_nodes(self):
        ending_nodes = []
        for i in self.nodes:
            if i.arcs_out == []:
                ending_nodes.append(i)
        return ending_nodes

    def final_values(self):
        ending_nodes = self.end_nodes()
        for i in ending_nodes:
            arcs_to_start = []
            going = True
            current_node = i
            while going:
                arcs_to_start.append(current_node.arcs_in[0])
                current_node = current_node.arcs_in[0].node_from
                if current_node.arcs_in == []:
                    going = False
            sum = 0
            for j in arcs_to_start:
                sum = sum + j.profit
            i.value = round(sum, 2)

    def chance_arcs(self):
        chance_arcs = []
        for i in self.arcs:
            if i.chance != None:
                chance_arcs.append(i)
        return chance_arcs

    def chance_nodes(self):
        chance_nodes = []
        for i in self.nodes:
            added = False
            for j in i.arcs_out:
                if (j.chance != None) and (added == False):
                    added = True
                    chance_nodes.append(i)
        return chance_nodes

    def expected_values(self):
        chance_nodes = self.chance_nodes()
        for i in chance_nodes:
            value = 0
            for j in i.arcs_out:
                value = value + j.chance * j.node_to.value
            i.value = round(value, 3)


class Node:
    def __init__(self, id, arcs_in=None, arcs_out=None):
        self.id = id
        self.arcs_in = arcs_in if arcs_in is not None else []
        self.arcs_out = arcs_out if arcs_out is not None else []
        self.value = 0

    def __repr__(self):
        return "Node:" + str(self.id)


class Arc:
    def __init__(self, node_from, node_to, profit=0, chance=None):
        self.chance = chance
        self.node_from = node_from
        self.node_to = node_to
        self.profit = profit

    def __repr__(self):
        return str(self.node_from) + " --> " + str(self.node_to)