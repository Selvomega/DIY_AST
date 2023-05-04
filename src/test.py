from syntax_tree import SyntaxTree
from node_type import NodeType

with open("build_tree_test","r") as handle:
    data = handle.read()

tree = SyntaxTree()
tree.build_tree(data)
tree.print_tree()