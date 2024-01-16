root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
leaf_node_root1 = []
leaf_node_root2 = []

def recursion(leaf_node, leaf_node_list):
    if leaf_node is None:
        return leaf_node
    
    
    left_last_leaf_node = recursion(leaf_node.left, leaf_node_list)
    right_last_leaf_node = recursion(leaf_node.right, leaf_node_list)
    if left_last_leaf_node.left == None:
        leaf_node_root1.append(left_last_leaf_node.value)
    return leaf_node_root1

recursion(root1, leaf_node_root1)
print(leaf_node_root1)
