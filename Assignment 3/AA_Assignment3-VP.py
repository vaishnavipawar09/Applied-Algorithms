#Q1

def who_wins(n,k):
    if k > n:
        k = k % n
    if k == 0:
        k = n
        
    in_game=0    
    for cnt in range(1, n):
        FrndsInCircle = (cnt + 1)
        ToEliminate = (in_game + k)
        in_game = ToEliminate % FrndsInCircle
       
    return in_game + 1


#Q2

def count_successful_school_commutes(home_coords, school_coords, N):
    
    def possibility(LilyHome_x, LilyHome_y, LilySchool_x, LilySchool_y):
        if LilyHome_x == LilySchool_x and LilyHome_y == LilySchool_y:
            return True
        if LilyHome_x > LilySchool_x or LilyHome_y > LilySchool_y or N == 0:
            return False

        cordinate= (LilyHome_x + LilyHome_y)
        newposition1 = possibility(cordinate, LilyHome_y, LilySchool_x, LilySchool_y)
        newposition2 = possibility(LilyHome_x, cordinate, LilySchool_x, LilySchool_y)

        checkposition = (newposition1 or newposition2)
        return checkposition

    success = 0
    for v in range(N):
        LilyHome_x, LilyHome_y = home_coords[v]
        LilySchool_x, LilySchool_y = school_coords[v]

        if possibility(LilyHome_x,LilyHome_y, LilySchool_x, LilySchool_y):
            success += 1

    return success




#Q3

def zenthar_puzzle(N, K):
    quest_success = []

    def generate_nos_sequence(currentnum, seq_length):
        if seq_length == N:
            quest_success.append(int(currentnum))
            return
        
        while seq_length < N:
            last_num = int(currentnum[-1])
            
            addK = last_num + K
            subK = last_num - K
            
            newlength = seq_length + 1
            if addK <= 9:
                generate_nos_sequence(currentnum + str(addK), newlength)

            if subK >= 0 and K != 0:
                generate_nos_sequence(currentnum + str(subK), newlength)
            return

        quest_success.append(int(currentnum))

    if N == 1:
        quest_success = list(range(1, 10))
    else:
        for i in range(1, 10):
            generate_nos_sequence(str(i), 1)

    return sorted(quest_success)


#Q4

def decompress(s):
    newstack = [] 

    for detail in s:
        if detail == ')':
            inside = ''
            while newstack[-1] != '(':
                inside = newstack.pop() + inside
            newstack.pop()  
            
            ctr = ''   
            while  newstack and newstack[-1].isdigit():
                ctr = newstack.pop() + ctr
            newstack.append(int(ctr) * inside)
        else :
            newstack.append(detail)
        
            
    original_text = ''.join(newstack)
    
    return original_text 

#Q5

from typing import List

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def create_bt_count_oracles_extract(values: List[int], k: int) -> bool:
    RootOfTree = TreeNode(values[0])
    CountTheOracles = 1

    def build_a_tree(pres_node, PresIndex):
        nonlocal CountTheOracles
        IndexLeftNode = 2 * PresIndex + 1
        IndexRightNode = 2 * PresIndex + 2

        if IndexLeftNode < len(values):
            pres_node.left = TreeNode(values[IndexLeftNode])
            if values[IndexLeftNode] > pres_node.value: 
                CountTheOracles += 1
            build_a_tree(pres_node.left, IndexLeftNode)

        if IndexRightNode < len(values):
            pres_node.right = TreeNode(values[IndexRightNode])
            if values[IndexRightNode] > pres_node.value: 
                CountTheOracles += 1
            build_a_tree(pres_node.right, IndexRightNode)

    build_a_tree(RootOfTree, 0)

    ExtractsPresent = (CountTheOracles >= k)
    
    return ExtractsPresent



#Q6

def solve_puzzle(root):
    if not root:
        return 0

    Level_MaxProduct = 0
    MaxProduct = 0
    productlist = [1] 

    def using__dfs(curr_node, pres_level):
        nonlocal MaxProduct, Level_MaxProduct

        if not curr_node:
            return

        if pres_level == len(productlist):
            productlist.append(1)
        
        productlist[pres_level] *= curr_node.val

        if productlist[pres_level] > MaxProduct:
            MaxProduct = productlist[pres_level]
            print(MaxProduct)
            Level_MaxProduct = pres_level
            print(Level_MaxProduct)

        using__dfs(curr_node.left, pres_level + 1)
        using__dfs(curr_node.right, pres_level + 1)

     
    using__dfs(root, 0)

    return Level_MaxProduct + 1 

#Q7

def TreeOfNumbers(root) -> int:
    def using_dfs(presentnode, current_no):
        if not presentnode:
            return 0
        
        current_no = current_no * 10 + presentnode.data
        
        if not presentnode.left and not presentnode.right:  # Leaf node
            return current_no
        
        SumLeftNode = using_dfs(presentnode.left, current_no)
        SumRightNode = using_dfs(presentnode.right, current_no)
        TotalSum = SumLeftNode + SumRightNode
        return TotalSum

    if not root:
        return 0
    
    return using_dfs(root, 0)

#Q8
class amor_dict():
    def __init__(self, num_list=[]):
        self.dictdata = {}
        for var in num_list:
            self.insert(var)

    def insert(self, num):
        presentlevel = 1
        while presentlevel in self.dictdata and len(self.dictdata[presentlevel]) == 2**presentlevel:
            presentlevel += 1
        if presentlevel not in self.dictdata:
            self.dictdata[presentlevel] = []
        
       
        self.dictdata[presentlevel].append(num)
        self.dictdata[presentlevel].sort()
               
        while presentlevel in self.dictdata and len(self.dictdata[presentlevel]) == 2**presentlevel:
            if presentlevel + 1 not in self.dictdata:
                self.dictdata[presentlevel + 1] = []
            self.dictdata[presentlevel + 1].extend(self.dictdata[presentlevel])
            if presentlevel in self.dictdata:
                self.dictdata[presentlevel] = []
            self.dictdata[presentlevel + 1].sort()
            presentlevel += 1

    def search(self, num):
        for levelinDict, searchvalue in self.dictdata.items():
            if num in searchvalue:
                return levelinDict - 1
        return -1

    def print(self):
        listofelements = []
        Toplevel = max(self.dictdata.keys(), default=-1)  
        if Toplevel == -1:
            return [[]]
        for ctr in range(1, Toplevel + 1):
            listofelements+=[self.dictdata[ctr][:]]
            
        return listofelements