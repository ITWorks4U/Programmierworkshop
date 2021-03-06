#!/usr/bin/python3

class Node:
	data = None
	next = None

	def __init__(self, data):
		self.data = data
		self.next = None
	# end constructor
# end class

class LinkedList:
	head = None

	def __init__(self):
		self.head = None
	# end constructor

	def printList(self):
		current = self.head

		while current is not None:
			print(" - node: {0}\n - content: {1}\n - next node at: {2}\n".format(current, current.data, current.next))
			current = current.next
		# end while

		print()
	# end method

	def addToList(self, newData):
		newNode = Node(newData)

		if self.head is None:
			self.head = newNode
		else:
			current = self.head

			while current.next is not None:
				current = current.next
			# end while

			current.next = newNode
		# end if
	# end method

	def removeFromList(self, removeKey):
		headVal = self.head

		if headVal is not None:
			if headVal.data == removeKey:
				self.head = headVal.next
				headVal = None
			else:
				previousNode = None

				while headVal is not None:
					if headVal.data == removeKey:
						break
					# end if

					previousNode = headVal
					headVal = headVal.next
				# end while

				if headVal is not None:
					previousNode.next = headVal.next
					headVal = None
				# end if
			# end if
		# end if
	# end method

	def reverseList(self):
		previousNode = None
		tmp = None
		currentNode = self.head

		while currentNode is not None:
			tmp = currentNode.next
			currentNode.next = previousNode
			previousNode = currentNode
			currentNode = tmp
		# end while

		self.head = previousNode
	# end method

	def clearList(self):
		current = self.head

		while current is not None:
			current = current.next
			del self.head
			self.head = current
		# end while
	# end method
# end class