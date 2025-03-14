def minimum_balls(c1, c2, c3, c4, c5, p):
      
    i = 0
    for k in [c1, c2, c3, c4, c5]:
        count = min(k, p - 1)
        i += count
    i += 1
    return i




from typing import List

def longestBlues(tiles : List[int] , k) -> int:
    number_of_tiles = 0  
    L = 0  
    
    for R in range(len(tiles) ):
        if tiles[R] == "pink":
            k -= 1  
        
            while k < 0:
                if tiles[L] == "pink":
                    k += 1 
                L += 1

        number_of_tiles = max(number_of_tiles, R - L + 1)

    return number_of_tiles





import re

def CandiesLog(s):

    candies = re.findall(r'([a-z])(\d+)', s)
    
    kids = len(candies)
    count_of_candy = {}
    total_candy = 0   
   
    
    for flavors, str_count in candies:
        count = int(str_count)
        count_of_candy[flavors] = count_of_candy.get(flavors, 0) + count
        total_candy += count
        
    sort_candies = sorted(count_of_candy.items())
    
    candy_str = ''.join(f"{flavors}{count}" for flavors, count in sort_candies)
    
    res = F"K{kids}T{total_candy}{candy_str}"
       
    return res



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HeimdallQuest:
    def reverse_k_steps(self, head, k):
        if not head or k <= 1:
            return head
        
      
        def reverse_list(head, k):
            n = head
            prev = None
            for _ in range(k):
                nxt = n.next
                n.next = prev
                prev = n
                n = nxt
            return prev
               
        ctr = 0              
        node = head
               
        x = head
        while x:
            ctr += 1
            x = x.next
        
        if ctr < k:
            return head
        
        p_tail, new = None, None
        
        while ctr >= k:
            node = head
            for _ in range(k):
                node = node.next
                       
            reverse = reverse_list(head, k)
            
            if p_tail:
                p_tail.next = reverse
            else:
                new = reverse
            
            head.next = node
            
            p_tail = head
            head = node
            ctr -= k
        
        return new

    def get_linked_list(self, head):
        res = []
        i = head
        while i:
            res.append(i.value)
            i = i.next
        return res

    def create_linked_list(self, lst):
        if not lst:
            return None
        head = Node(lst[0])
        j = head
        for x in lst[1:]:
            j.next = Node(x)
            j= j.next
        return head
    
