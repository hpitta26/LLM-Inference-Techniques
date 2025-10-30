import json
from graphviz import Digraph
import sys
import os
# Run --> python _tree_plot.py path_to_tree.json

def plot_tree_from_json(tree, graph=None, node_id=0):
    if graph is None:
        graph = Digraph(format='svg')
        graph.attr('node', shape='box', style='filled', fillcolor='lightblue', fontname='Helvetica')

    label = f"{tree.get('action', 'None')}\n{tree.get('summary', '')}"
    current_id = str(node_id)
    graph.node(current_id, label)

    children = tree.get('children', [])  # Expecting a list of children
    for i, child in enumerate(children):
        child_id = f"{node_id}-{i}"  # Unique ID for each child
        graph.edge(current_id, child_id)
        plot_tree_from_json(child, graph, child_id)

    return graph

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python _tree_plot.py path_to_tree.json")
        sys.exit(1)

    json_path = sys.argv[1]

    with open(json_path, 'r') as f:
        tree_data = json.load(f)

    graph = plot_tree_from_json(tree_data)
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    output_file = f"outputs/{base_name}_output"

    # Render the graph to the dynamically named output file
    output_path = graph.render(output_file, format='svg', cleanup=True)

    print(f"Tree saved as {output_path}")
