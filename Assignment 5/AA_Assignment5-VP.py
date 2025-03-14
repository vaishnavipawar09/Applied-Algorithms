#Oues1

def busRemaining(busStation):
    
    if not busStation:
        return 0

    busroute = [busStation[0]]
    idx = 1  

    while idx < len(busStation):
        busStart, busEnd = busStation[idx]
        LastStationstart, LastStationend = busroute[-1]

        if busStart <= LastStationend:
            busroute[-1] = [LastStationstart, max(LastStationend, busEnd)]
        else:
            busroute.append([busStart, busEnd])

        idx += 1 

    busRunning = len(busroute)
    
    return busRunning

#Ques2

import heapq

def solvePuzzle(numbers):
    lengthofnum = len(numbers)
    visitedList = [False] * lengthofnum
    PuzzleAnswer = 0

    priorityQueue = []  
    for ctn, val in enumerate(numbers):
        
        heapq.heappush(priorityQueue, (val, ctn))

    while priorityQueue:
        val, presIndex = heapq.heappop(priorityQueue)
        
        if not visitedList[presIndex]:
            PuzzleAnswer += val
            visitedList[presIndex] = True

            
            if presIndex - 1 >= 0:
                visitedList[presIndex - 1] = True
            if presIndex < lengthofnum - 1:
                visitedList[presIndex + 1] = True

    return PuzzleAnswer

#Ques3

import heapq

def findMedianPrice(prices, k):
    if not prices or k <= 0:
        return []

    def insertNumber(Currentnum, minimumHeap, maximumHeap):
        if not maximumHeap or Currentnum <= -maximumHeap[0]:
            heapq.heappush(maximumHeap, -Currentnum)
        else:
            heapq.heappush(minimumHeap, Currentnum)
        balanceTheHeaps(minimumHeap, maximumHeap)

    def removeTheNumber(Currentnum, minimumHeap, maximumHeap):
        if Currentnum <= -maximumHeap[0]:
            maximumHeap.remove(-Currentnum)
            heapq.heapify(maximumHeap)
        else:
            minimumHeap.remove(Currentnum)
            heapq.heapify(minimumHeap)
        balanceTheHeaps(minimumHeap, maximumHeap)

    def balanceTheHeaps(minimumHeap, maximumHeap):
        while len(minimumHeap) > len(maximumHeap):
            heapq.heappush(maximumHeap, -heapq.heappop(minimumHeap))
        while len(maximumHeap) > len(minimumHeap) + 1:
            heapq.heappush(minimumHeap, -heapq.heappop(maximumHeap))

    def findTheMedian(minimumHeap, maximumHeap, k):
        if k % 2 == 0:
            return (-maximumHeap[0] + minimumHeap[0]) / 2.0
        return -maximumHeap[0]

    minimumHeap, maximumHeap = [], []
    medianofPrices = []

    for indx in range(len(prices)):
        insertNumber(prices[indx], minimumHeap, maximumHeap)
        if indx >= k - 1:
            medianofPrices.append(findTheMedian(minimumHeap, maximumHeap, k))
            removeTheNumber(prices[indx - k + 1], minimumHeap, maximumHeap)
    
    return medianofPrices


#Ques4
def mergeAndCal(buildings, workspace, LStart, middle, REnd, res_counts):
    LIndex, RIndex, mergeIndex = LStart, middle, LStart
    shortercount = 0

    
    while LIndex < middle and RIndex < REnd:
        if buildings[LIndex][0] <= buildings[RIndex][0]:
            workspace[mergeIndex] = buildings[LIndex]
            res_counts[buildings[LIndex][1]] += shortercount
            LIndex += 1
        else:
            workspace[mergeIndex] = buildings[RIndex]
            shortercount += 1
            RIndex += 1
        mergeIndex += 1

    
    while LIndex < middle:
        workspace[mergeIndex] = buildings[LIndex]
        res_counts[buildings[LIndex][1]] += shortercount
        LIndex += 1
        mergeIndex += 1
    
    while RIndex < REnd:
        workspace[mergeIndex] = buildings[RIndex]
        RIndex += 1
        mergeIndex += 1
    
    for idx in range(LStart, REnd):
        buildings[idx] = workspace[idx]

def usingMergeSort(buildings, workspace, LIndex, RIndex, res_counts):
    if RIndex - LIndex > 1:
        midIndex = (LIndex + RIndex) // 2
        usingMergeSort(buildings, workspace, LIndex, midIndex, res_counts)
        usingMergeSort(buildings, workspace, midIndex, RIndex, res_counts)
        mergeAndCal(buildings, workspace, LIndex, midIndex, RIndex, res_counts)

def shorterBuildings(heights):
    NumberOfBuildings = len(heights)
    HeightIndexed = [(hgt, idx) for idx, hgt in enumerate(heights)]
    templist = [0] * NumberOfBuildings
    resultlist = [0] * NumberOfBuildings

    usingMergeSort(HeightIndexed, templist, 0, NumberOfBuildings, resultlist)
    
    return resultlist



#Ques5
import bisect

def findNearestHeater(positionOfhouse, heaters):
    insertionIdx = bisect.bisect_right(heaters, positionOfhouse)
    if insertionIdx == 0:
        return heaters[0]
    if insertionIdx == len(heaters):
        return heaters[-1]
    Rightiscloser = heaters[insertionIdx] - positionOfhouse
    Leftiscloser = positionOfhouse - heaters[insertionIdx - 1]
    if Rightiscloser < Leftiscloser:
        return heaters[insertionIdx]
    return heaters[insertionIdx - 1]


def determineStandardRadius(houses, heaters):
    houses.sort()
    heaters.sort()

    maxRadius = 0

    for house in houses:
        nearestHeater = findNearestHeater(house, heaters)
        maxRadius = max(maxRadius, abs(nearestHeater - house))

    return maxRadius

#Ques6

def isRearrangePossible(s, k):
    if k == 0:
        return True
    
    countFreq = {}
    for letter in s:
        countFreq[letter] = countFreq.get(letter, 0) + 1

    maxHeap = [(-freq, letter) for letter, freq in countFreq.items()]

    def createheapify(hArray, hsize, rootIdx):
        largest = rootIdx
        Lchild = 2 * rootIdx + 1
        Rchild = 2 * rootIdx + 2

        if Lchild < hsize and hArray[Lchild][0] < hArray[largest][0]:
            largest = Lchild
        if Rchild < hsize and hArray[Rchild][0] < hArray[largest][0]:
            largest = Rchild
        if largest != rootIdx:
            hArray[rootIdx], hArray[largest] = hArray[largest], hArray[rootIdx]
            createheapify(hArray, hsize, largest)

    def buildMaxHeap(hArray):
        arrlen = len(hArray)
        for i in range(arrlen, -1, -1):
            createheapify(hArray, arrlen, i)

    buildMaxHeap(maxHeap)

   
    def popMax():
        maxHeap[0], maxHeap[-1] = maxHeap[-1], maxHeap[0]
        maxItem = maxHeap.pop()
        createheapify(maxHeap, len(maxHeap), 0)
        return maxItem

    
    cooldownQueue = []
    arrangedMagicals = []

    while maxHeap:
        freq, letter = popMax()
        arrangedMagicals.append(letter)
        
        cooldownQueue.append((freq + 1, letter))
        if len(cooldownQueue) >= k:
            freq, letter = cooldownQueue.pop(0)
            if -freq > 0:
                maxHeap.append((freq, letter))
                buildMaxHeap(maxHeap)
                
                
    RearrangePossible = (len(arrangedMagicals) == len(s))
    
    return RearrangePossible



#Ques7
from heapq import heappush, heappop

class Huffman():
    def _init_(self):
        self.huffman_codes = {}
        self.source_string = ""

    def set_source_string(self, src_str):
        self.source_string = src_str

    def generate_codes(self):
        charFrequency = dict()
        for char in self.source_string:
            if char in charFrequency:
                charFrequency[char] += 1
            else:
                charFrequency[char] = 1
      
        createpq = []
        for presChar, freq in charFrequency.items():
            heappush(createpq, (freq, presChar))
            
        huffman_codes = {}
        while len(createpq) > 1:
            merged_nodes = ""
            Lfreq, LNode = heappop(createpq)
            
            for presChar in LNode:
                if presChar in huffman_codes:
                    huffman_codes[presChar] = huffman_codes[presChar] + '0'
                else:
                    huffman_codes[presChar] = '0'

                merged_nodes += presChar

            
            Rfreq, RNode = heappop(createpq)
            for presChar in RNode:
                if presChar in huffman_codes:
                    huffman_codes[presChar] = huffman_codes[presChar] + '1'
                else:
                    huffman_codes[presChar] = '1' 

                merged_nodes += presChar
            
            heappush(createpq,(Lfreq + Rfreq, merged_nodes))

        for key, val in huffman_codes.items():
            huffman_codes[key] = val[::-1]
    
        self.huffman_codes = huffman_codes

    def encode_message(self, message_to_encode):
        encoded_msg = ""
        for flg in message_to_encode:
            encoded_msg += self.huffman_codes[flg]

        return encoded_msg
    
    def decode_message(self, encoded_msg):
        decoded_msg = ""
        while encoded_msg:
            for sym, currcode in self.huffman_codes.items():
                if encoded_msg.startswith(currcode):
                    decoded_msg += sym
                    encoded_msg = encoded_msg[len(currcode):]

        return decoded_msg
    

#Ques8
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Wavelet_Tree:
    def __init__(self, A):
        Minimumval = min(A)
        Maximumval = max(A)
        self.root = self.buildTree(A, Minimumval, Maximumval)
        
    def buildTree(self, A, lowval, highval):
        if lowval == highval:
            return Node('X' * A.count(lowval))
        
        midval = (lowval + highval) // 2
        LSequence, RSequence = [], []
        datainBits = ''

        for ctn in A:
            if ctn <= midval:
                datainBits += '0'
                LSequence.append(ctn)
            else:
                datainBits += '1'
                RSequence.append(ctn)

        Lchild = 0 
        if LSequence:
            Lchild = self.buildTree(LSequence, lowval, midval)
        else:
            None
            
        Rchild = 0
        if RSequence: 
            Rchild = self.buildTree(RSequence, midval + 1, highval) 
        else: 
            None
            
        return Node(datainBits, Lchild, Rchild)

    def get_wavelet_level_order(self):
        allLevels = []
        CurrentLevelnode = [self.root]
        while CurrentLevelnode:
            levelData = []
            nextLevelNode = []
            for presNode in CurrentLevelnode:
                levelData.append(presNode.data)
                if presNode.left:
                    nextLevelNode.append(presNode.left)
                if presNode.right:
                    nextLevelNode.append(presNode.right)
            allLevels.append(levelData)
            CurrentLevelnode = nextLevelNode
        return allLevels

    def rank(self, character, position):
        if "X" in self.root.data:
            return len(self.root.data[:position])
        return self.recursiveRank(self.root, 0, 9, character, position)

    def recursiveRank(self, currnode, lowpt, highpt, character, position):
        if not currnode:
            return 0

        if lowpt == highpt:
            return min(position, len(currnode.data))

        midpt = (lowpt + highpt) // 2
        LeftCharCount = currnode.data[:position].count('0')

        if character <= midpt:
            return self.recursiveRank(currnode.left, lowpt, midpt, character, LeftCharCount)
        else:
            return self.recursiveRank(currnode.right, midpt + 1, highpt, character, position - LeftCharCount)


