class linkList():
	def __init__(self, value):
		self.val = value
		self.next = None

class Tree():
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None
def get_paths_optimized(node, target, node_chain=[]):
	if (node == None):
		return node_chain
	right_node_chain = -1
	left_node_chain = -1
	if (node.left != None):
		left_node_chain = get_paths_optimized(node.left, target, node_chain)
	if (node.right != None):
		right_node_chain = get_paths_optimized(node.right, target, node_chain)
	if (left_node_chain != -1):
		for i in range(len(left_node_chain)):
			left_node_chain[i].append(node.data)
			printNodes(left_node_chain[i][::-1], target)

	if (right_node_chain != -1):
		for i in range(len(left_node_chain)):
			for j in range(len(right_node_chain)):
				printNodes(left_node_chain[i] + right_node_chain[j][::-1], target)

	if (right_node_chain != -1):
		for i in range(len(right_node_chain)):
			right_node_chain[i].append(node.data)
			printNodes(right_node_chain[i][::-1], target)
	if(left_node_chain == -1 and right_node_chain == -1):
		return [[node.data]]
	if(left_node_chain == -1):
		left_node_chain = []
	if(right_node_chain == -1):
		right_node_chain = []

	return node_chain + left_node_chain + right_node_chain


def printNodes(node_chain, target):
	tempSum = 0
	for i,value in enumerate (node_chain):
		tempSum += value
		if (tempSum == target):
			print node_chain[0:i+1]



T= Tree(3)
T.left = Tree(2)
T.left.right = Tree(1)
T.right = Tree(4)
T.right.left = Tree(1)
T.right.left.left = Tree(3)
T.left.left=Tree(3)
T.left.left.right=Tree(2)
T.left.left.left=Tree(-2)
T.left.left.left.left=Tree(2)
get_paths_optimized(T, 11)

