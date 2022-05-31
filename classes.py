import random

class Node:
	val = ""
	total_next_nodes = 0

	def __init__(self,val="",next_nodes=[],total_next_nodes=0):
		self.val = val
		self.next_nodes = []
		self.total_next_nodes = total_next_nodes

	def __str__(self):
		return "VALUE: " + self.val

	def __eq__(self,other):
		return self.val == other.val
	def update_node(self,next_node):
		self.next_nodes.append(next_node)

	def rand_node(self):
		return random.choice(self.next_nodes) if len(self.next_nodes) > 0 else None

	def print_data(self):
		print("PRINTING DATA FOR VAL: ", self.val)
		print([str(n.val) for n in self.next_nodes])





