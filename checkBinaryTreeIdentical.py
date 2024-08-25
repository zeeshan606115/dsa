class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def is_identical(root1, root2):
	if (root1 == None and root2 == None):
		return True
	if(root1 !=None and root2 != None and root1.data == root2.data):
		left_data = is_identical(root1.left, root2.left)
		right_data = is_identical(root1.right, root2.right)

		if (left_data and right_data):
			return True
		return False

	return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.right = Node(6)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.right = Node(6)
root2.right.right.right = Node(6)

if (is_identical(root1, root2)):
	print("Trees are identical")

else:
	print("trees are not identical")