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
    
#Class for Queue
class Queue:

  #function to initialise an instance of queue, taking no input
  def __init__(self):
    #set queue instance variable, head, to None
    self.head_node = None
    #set queue instance variable, tail, to None
    self.tail_node = None
    
  #function to enqueue (add a node to the queue's tail), taking value as input
  def enqueue(self, value):
    #assign a temporary variable (new tail) to a Node instance with data set to value input
    new_tail = Node(value)
    #if queue head instance variable is None
    if self.head_node == None:
      #set queue head instance variable to new tail
      self.head_node = new_tail
      #set queue tail instance variable to new tail
      self.tail_node = new_tail
    #else
    else:
      #set next node instance variable of the tail of this queue to new tail
      self.tail_node.set_next_node(new_tail)
      #set the tail node of this instance of queue to new tail
      self.tail_node = new_tail
  
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
  
  #function to dequeue (remove and return the queue's head), taking no input
  def dequeue(self):
    #assign a temporary variable (current head) to head of this instance of queue 
    current_head = self.head_node
    #if current head is None
    if current_head == None:
      #return None
      return None
    #else
    else:
      #if next node instance variable of current head is None
      if current_head.next_node == None:
        #set the tail node of this instance of queue to None
        self.tail_node = None
        #set the head node of this instance of queue to None
        self.head_node = None
        #return current head
        return current_head
      #else
      else:
        #assign a temporary variable (next head) to the next node instance variable of current head
        next_head = current_head.next_node
        #set the head node of this instance of queue to next head
        self.head_node = next_head
        #return current head
        return current_head
