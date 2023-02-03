#Class for node
class Node:
  
  #function to initialise an instance of node, taking data and next node (default as None) as input
  def __init__(self, data, next_node = None):
    #set node instance variable, data, to data input
    self.data = data
    #set node instance variable, next node, to next node input
    self.next_node = next_node

  #function to set a node's instance variable, next node, taking next node as an input
  def set_next_node(self, next_node):
    #set node instance variable, next node, to next node input
    self.next_node = next_node

#Class for linked list
class LinkedList:
  
  #function to initialise an instance of linked list, taking head node (default as None) as input
  def __init__(self, head_node = None):
    #set linked list instance variable, head node, to an instance of node with value of head node input
    if head_node == None:
      self.head_node = head_node
    else:
      self.head_node = Node(head_node)
    
  #function to add node to the head of an instance of linked list, taking value as input
  def add_to_head(self, value):
    #if linked list, head instance variable is None
    if self.head_node == None:  
      #set linked list, head instance variable to a Node instance with data set to value input
      self.head_node = Node(value)
    #else
    else:
      #assign a temporary variable (new head) to a Node instance with data set to value input
      new_head = Node(value)
      #set new head next node instance variable to the head node of this instance of linked list
      new_head.set_next_node(self.head_node)
      #set the head node of this instance of linked list to new head
      self.head_node = new_head
    #return Success, node added
    return (f"Success, added node with value: {value}")
    
  #function to remove a node from linked list, taking value as input
  def remove_value(self, value):
    #assign a temporary variable (current) to the head node of this instance of linked list
    current = self.head_node
    #if current's data instance variable is value
    if current.data == value:
      #set the head node of this instance of linked list to the next node instance variable of current
      self.head_node = current.next_node
    #while current's next node instance variable is not None
    while current.next_node != None:
      #if current's next node instance variable value is input value
      if current.next_node == value:
        #assign a temporary variable (target) to the next node instance variable of current
        target = current.next_node
        #set current's next node instance variable to target's next node instance variable
        current.set_next_node(target.next_node)
        #return Success, node removed
        return (f"Success, node with value: {value} removed")
      #set current to current's next node instance variable
      current = current.next_node
    #return Error, node not present
    return (f"Error, node with value: {value} not in linked list")
    
  #function to return linked list as list
  def as_list(self):
    #initialise a temporary variable (result) to list
    result = []
    #assign a temporary variable (current) to the head node of this instance of linked list
    current = self.head_node
    #while current is not None
    while current is not None:
      #append current's data instance variable to result
      result.append(current.data)
      #assign result to result's next node instance variable
      result = result.next_node
    #return result
    return result
