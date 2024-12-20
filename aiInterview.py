import treeswift
tree = treeswift.read_tree_newick(my_newick_string)
for node in tree.traverse_postorder():
    print(node)