class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def height_tree(root_node):
	if(root_node == None):
		return 0
	else:
		left_depth = height_tree(root_node.left)
		right_depth = height_tree(root_node.right)

		if(left_depth > right_depth):
			return (1+ left_depth)
		else:
			return (1+ right_depth)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)

print(height_tree(root))