#Class for node
class Node:
  
  #function to initialise an instance of node, taking data, next node (default as None), and previous node (default as None) as input
  def __init__(self, data, next_node = None, prev_node = None):
    #set node instance variable, data, to data input
    self.data = data
    #set node instance variable, next node, to next node input
    self.next_node = next_node
    #set instance variable, previous node, to previous node input
    self.prev_node = prev_node
   
  #function to set a node's instance variable, next node, taking next node as input
  def set_next_node(self, next_node):
    #set node instance variable, next node, to next node input
    self.next_node = next_node
  
  #function to set a node's instance variable, previous node, taking previous node as input
  def set_prev_node(self, prev_node):
    #set node instance variable, previous node, to previous node input
    self.prev_node = prev_node

#Class for doubly linked list
class DoublyLinkedList:

  #function to initialise an instance of doubly linked list, taking no input
  def __init__(self):
    #set doubly linked list instance variable, head node, to None
    self.head_node = None
    #set doubly linked list instance variable, tail node, to None
    self.tail_node = None
  
  #function to add to the head of this instance of doubly linked list, taking value as input
  def add_to_head(self, value):
    #assign a temporary variable (new head) to a node instance with data set to value input
    new_head = Node(value)
    #if doubly linked list head instance variable is not None
    if self.head_node != None:
      #set previous node instance variable of doubly linked list head node, to new head
      self.head_node.set_prev_node(new_head)
      #set next node instance variable of new head to head node of doubly linked list
      new_head.set_next_node(self.head_node)
    #set the head node of this instance of doubly linked list to new head
    self.head_node = new_head
    #if doubly linked list tail node instance variable is None
    if self.tail_node == None:
      #set the tail node of this instance of doubly linked list to new head
      self.tail_node = new_head
      
  #function to add to the tail of this instance of doubly linked list, taking value as input
  def add_to_tail(self, value):
    #assign a temporary variable (new tail) to a node instance with data set to value input
    new_tail = Node(value)
    #if doubly linked list tail node instance variable is not None
    if self.tail_node != None:
      #set next node instance variable of doubly linked list tail node, to new tail
      self.tail_node.set_next_node(new_tail)
      #set previous node instance variable of new tail to tail node of doubly linked list
      new_tail.set_previous_node(self.tail_node)
    #set the tail node of this instance of doubly linked list to new tail
    self.tail_node = new_tail
    #if doubly linked list head node instance variable is None
    if self.head_node == None:
      #set the head node of this instance of doubly linked list to new tail
      self.head_node = new_tail
  
  #function to remove the head of this instance of doubly linked list, taking no input
  def remove_head(self):
    #assign a temporary variable (current head) to the head node of this instance of doubly linked list
    current_head = self.head_node
    #if doubly linked list head node instance variable is None
    if current_head == None:
      #return None
      return None
    #assign a temporary variable (new head) to the next node instance variable of doubly linked list head node instance variable
    new_head = current_head.next_node
    #set doubly linked list head node instance variable to new head
    self.head_node = new_head
    #if new head is not None
    if new_head != None:
      #set previous node instance variable of new head to None
      new_head.set_prev_node = None
    #if current head is the tail node of this instance of doubly linked list
    if current_head == self.tail_node:
      #call remove tail function on this instance of doubly linked list
      self.remove_tail()
  
  #function to remove the tail of this instance of doubly linked list, taking no input
  def remove_tail(self):
    #assign a temporary variable (current tail) to the tail node of this instance of doubly linked list
    current_tail = self.tail_node
    #if doubly linked list tail node instance variable is None
    if current_tail == None:
      #return None
      return None
    #assign a temporary variable (new tail) to the previous node instance variable of doubly linked list tail node instance variable
    new_tail = current_tail.next_node
    #set doubly linked list tail node instance variable to new tail
    self.tail_node = new_tail
    #if new tail is not None
    if new_tail != None:
      #set next node instance variable of new tail to None
      new_tail.set_next_node(None)
    #if current tail is the head node of this instance of doubly linked list
    if current_tail == self.head_node:
      #call remove head function on this instance of doubly linked list
      self.remove_head()
      
  #function to remove a node from doubly linked list, taking value as input
  def remove_by_value(self, value):
    #assign a temporary variable (node to remove) to None
    node_to_remove = None
    #assign a temporary variable (current node) to the head node of this instance of linked list
    current_node = self.head_node
    #while current node next node instance variable is not None
    while current_node.next_node != None:
      #if value instance variable of current node is value
      if current_node.data == value:
        #set node to remove to current node
        node_to_remove = current_node
        #break
        break
      #set current node to next node instance variable of current node
      curremt_node = current_node.next_node
    #if node to remove is None
    if node_to_remove == None:
      #return None
      return None
    #if node to remove is the head node of this instance of doubly linked list
    if node_to_remove == self.head_node:
      #call remove head function on this instance of doubly linked list
      self.remove_head()
    #if node to remove is the tail node of this instance of doubly linke list
    if node_to_remove == self.tail_node:
      #call remove tail function on this instance of doubly linked list
      self.remove_tail()
    #else
    else:
      #assign a temporary variable (next node) to the next node instance variable of node to remove
      next_node = node_to_remove.next_node
      #assign a temporary variable (previous node) to the previous node instance variable of node to remove
      previous_node = node_to_remove.prev_node
      #set the next node instance variable of previous node to next node
      previous_node.set_next_node(next_node)
      #set the previous node instance variable of next node to previous node
      next_node.set_prev_node(previous_node)
    #return node to remove
    return node_to_remove
    
