
# que1

def translate_message(arr):
    hashtable = set(arr)
    maxseqlen = 0

    for seqstart in arr:
        seqlength = 0
        currentelement = seqstart

        while currentelement in hashtable:
            seqlength += 1
            currentelement += 7
        maxseqlen = max(maxseqlen, seqlength)

    return maxseqlen

# que2


def find_order_size(orders):

    orderTracker = set()
    symPairs = 0

    for orderlist in orders:
        [v, w] = orderlist
        if (w, v) in orderTracker:
            orderTracker.remove((w, v))
            orderTracker.add((v, w))
            symPairs += 1
        else:
            orderTracker.add((v, w))

    ResultSize = len(orders) - symPairs

    return ResultSize


# que3

def findCircusStrings(circusString):
    def calHashStr(substr):
        currHash = 0
        for char in substr:
            currHash = ord(char) + currHash * 31
        return currHash

    uniqueHashes = set()
    resultList = []
    for startidx in range(len(circusString) - 9):
        presSubstr = circusString[startidx:startidx + 10]
        substringHash = calHashStr(presSubstr)
        if substringHash in uniqueHashes and presSubstr not in resultList:
            resultList.append(presSubstr)
        else:
            uniqueHashes.add(substringHash)

    return sorted(list(resultList))


# que4

def aliveOrDead(trees, tigersWish):

    trees = [int(tree) for tree in trees if tree != 'X']
    ValuesOfTree = set(trees)

    lenofTree = len(trees)
    for idx1 in range(lenofTree):
        for idx2 in range(idx1 + 1, lenofTree):
            for idx3 in range(idx2 + 1, lenofTree):
                currtotal = trees[idx1] + trees[idx2] + trees[idx3]

                requiredtree = tigersWish - currtotal
                if requiredtree in ValuesOfTree:
                    if trees[idx1] != requiredtree:
                        if trees[idx2] != requiredtree:
                            if trees[idx3] != requiredtree:
                                return 'Alive'
    return 'Dead'
