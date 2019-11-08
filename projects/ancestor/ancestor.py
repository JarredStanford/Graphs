from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for ancestor in ancestors:
        if ancestor[0] not in g.vertices:
            g.add_vertex(ancestor[0])
        if ancestor[1] not in g.vertices:
            g.add_vertex(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])
    
    return g.last_ancestor(starting_node)
    