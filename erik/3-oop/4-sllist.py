# class Node(object):
#  def __init__(self,value,next=None):
#   self.value = value
#   self.next = next
#
# class SLList(object):
#  def __init__(self):
#      self.head = None
#      self.tail =  None

class Node(object):
 def __init__(self, value):
  self.value = value
  self.next = None

class SinglyLinkedList(object):
 def __init__(self):
  self.head = None
  self.tail = None

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
print list.head.value
