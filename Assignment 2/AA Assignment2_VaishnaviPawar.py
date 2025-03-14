def amountPoliceGets(people):
    stack=[]
    money_coll=0

    for dir, fine in people:
        if dir==0:

            for people in stack:
                money_coll=money_coll+people

            stack=[]

        elif dir==1:
            stack.append(fine)
        elif dir==-1:

            while stack and stack[-1]>0:
                money_coll=money_coll+stack[-1]
                stack.pop()
            money_coll=money_coll+fine

            stack.append(0)
    return money_coll



import random
class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.down = None, None  
        
class SkipList:
    def __init__(self):
        self.head = Node(-1)
    
    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next
            if curr.next and curr.next.val == target:
                return True
            curr = curr.down 
        return False

    def insert(self, num: int) -> None:
        pres = self.head
        update = None
        while pres:
            while pres.next and pres.next.val < num:
                pres = pres.next
            if not update:
                update = pres
            if pres.next and pres.next.val == num:
                return
            new = Node(num)
            new.next = pres.next
            pres.next = new
            
            if random.random() < 0.5:
                new_node_down = Node(num)
                new_node_down.down = update.down
                update.down = new_node_down
                
            update = new  
            pres = pres.down 
    
    def __str__(self):
        res = ""
        k = self.head
        while k:
            n_node = k
            while n_node:
                res += str(n_node.val) + " -> "
                n_node = n_node.next
            res = res.rstrip(" -> ") + "\n"
            k = k.down
        return res
    
    
    
    
class Queue:
    DEFAULT_SIZE = 10

    def __init__(self):
        self.queue = [None] * self.DEFAULT_SIZE
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.DEFAULT_SIZE == self.front

    def enque(self, value):
        if self.is_full():
            return False  
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.DEFAULT_SIZE

        self.queue[self.rear] = value
        return True  

    def deque(self):
        if self.is_empty():
            return -1  
        
        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.DEFAULT_SIZE

        return value
    
    

from typing import List

def isItPossible(initial: List[str], final: List[str]) -> bool:
    intr_stack = []
    initialnew=initial.copy()
    initialnew.reverse()
    finalnew=final.copy()
    for i in reversed(finalnew):

        while initialnew and i!=initialnew[-1] and i not in intr_stack:
            intr_stack.append(initialnew.pop())
         
        if len(initialnew)>0 and i == initialnew[-1]:
            initialnew.pop()
            continue
        if len(intr_stack)>=0 and i==intr_stack[-1]:
            intr_stack.pop()
            continue
    return not initialnew and not intr_stack

