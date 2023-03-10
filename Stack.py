#Class for Node
class Node:

  #function to initialise an instance of node, taking data as input
  def __init__(self,data):
    #set node instance variable, data, to data input
    self.data = data
    #set node instance variable, next node, to None
    self.next_node = None
    
  #function to set a node's instance variable, next node, taking next node as an input
  def set_next_node(self, next_node):
    #set node instance variable, next node, to next node input
    self.next_node = next_node
    
#Class for Stack
class Stack:

  #function to initialise an instance of stack, taking no input
  def __init__(self):
    #set stack instance variable, head, to None
    self.head_node = None
    
  #function to push (add a new node to stack head), taking value as input
  def push(self, value):
    #assign a temporary variable (new head) to a Node instance with data set to value input
    new_head = Node(value)
    #if stack head instance variable is None
    if self.head_node == None:
      #set stack head instance variable to new head
      self.head_node = new_head
    #else
    else:
      #set the next node instance variable of new head to the head node of this stack
      new_head.set_next_node(self.head_node)
      #set stack head instance variable to new head
      self.head_node = new_head
  
  #function to pop (take a node from the stack head), taking no input
  def pop(self):
    #if head of this instance of stack is not None
    if self.head:
      #assign a temporary variable (current head) to the head instance variable of this stack
      current_head = self.head_node
      #set stack head instance variable to the next node instance variable of current head
      self.head_node = current_head.next_node
      #return current head
      return current_head
    #return None
    return None
  
  #function to peek (view head without modifying the state of the queue), taking no input
  def peek(self):
    #if head of this instance of queue is None
    if self.head_node == None:
      #return None
      return None
    #else
    else:
      #return head instance variable, data
      return self.head_node.data
  
  
