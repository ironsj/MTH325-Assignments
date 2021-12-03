def greedy(graph, order):
    colors = {}  # creates dictionary to be returned
    colorlist = []  # empty list that will hold all colors used
    for vertex in order:  # goes through each vertex in order given
        for key in graph:  # goes through each vertex in graph
            if vertex == key:  # makes it so vertices are done in order
                neighborColor = []  # empty list that will hold colors of the neighbors
                for neighbor in graph[key]:  # goes through each neighbor for vertex
                    if neighbor in colors:  # if a neighbor is already colored
                        neighborColor.append(colors[neighbor])  # adds neighbor color to list
                    else:  # if neigbor is not colored
                        colors[key] = 1  # if no neighbors are colored make it the first color
                        if 1 not in colorlist:
                            colorlist.append(1)  # adds 1 to the list of colors if not used yet
                unique = [i for i in colorlist if i not in neighborColor]  # colors in used colors but not in neighbors
                if (len(unique) == 0):  # if the new list is empty
                    largest = max(neighborColor)  # takes the largest neighborColor
                    colors[key] = largest + 1  # makes vertex a new color
                    colorlist.append(largest + 1)  # adds new color to used colors
                else:  # if the new list is not empty
                    colors[key] = unique[0]  # makes the vertex the smallest available color
    return colors  # returns dictionary of vertices with colors


a = {'a': ['b', 'c', 'e'], 'b': ['a'], 'c': ['a', 'd'], 'd': ['c'], 'e': ['a', 'f', 'h'], 'f': ['e', 'g'], 'g': ['f'],
     'h': ['e']}
b = ['b', 'd', 'c', 'h', 'g', 'f', 'e', 'a']
c = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}
d = ["A", "D", "B", "C"]
print(greedy(a, b))
print(greedy(c, d))
