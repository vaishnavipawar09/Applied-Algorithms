# Que1

import copy


def MaximumDeafPeople(PeopleShout):
    def caldistance(pt1, pt2):
        EuclideanDist = ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

        return EuclideanDist

    def useDFS(personIdx, shoutreached):
        shoutreached[personIdx] = True
        deafcnt = 1
        xcord1, ycord1, rcord1 = PeopleShout[personIdx]

        indx = 0
        while indx < len(PeopleShout):
            if not shoutreached[indx]:
                xcord2, ycord2, _ = PeopleShout[indx]
                newdist = caldistance((xcord1, ycord1), (xcord2, ycord2))
                if newdist <= rcord1:
                    deafcnt += useDFS(indx, shoutreached)
            indx += 1

        return deafcnt

    maxPeopledeaf = 0
    for ctr in range(len(PeopleShout)):
        shoutreached = [False] * len(PeopleShout)
        maxPeopledeaf = max(maxPeopledeaf, useDFS(ctr, shoutreached))

    return maxPeopledeaf


# Que2

def cheapest_path(n, costs, start):

    costofcity = [float('inf')] * n
    costofcity[start] = 0
    selected = set()

    while len(selected) < n:
        CityCostMin = None
        for CityIdx in range(n):
            NotSelected = CityIdx not in selected
            NewCityCostMin = CityCostMin is None or costofcity[CityIdx] < costofcity[CityCostMin]
            if NotSelected and NewCityCostMin:
                CityCostMin = CityIdx

        selected.add(CityCostMin)

        CityIdx = 0
        while CityIdx < n:
            pathexists = costs[CityCostMin][CityIdx] != 0
            NotSelected = CityIdx not in selected
            if pathexists and NotSelected:
                new_cost = costofcity[CityCostMin] + \
                    costs[CityCostMin][CityIdx]
                if new_cost < costofcity[CityIdx]:
                    costofcity[CityIdx] = new_cost
            CityIdx += 1

    return costofcity

# Que3


def generate_password(words):

    def CalMaxOverlap(chksuffix, chkprefix):

        if chksuffix in chkprefix:
            return len(chksuffix)

        if chkprefix in chksuffix:
            return len(chkprefix)

        highestoverlap = 0
        idx = 1
        minlen = min(len(chksuffix), len(chkprefix)) + 1
        while idx < minlen:
            if chksuffix.endswith(chkprefix[:idx]):
                highestoverlap = idx
            idx += 1
        return highestoverlap

    words.sort(key=len, reverse=True)

    while len(words) > 1:
        maximumlen = -1
        MergeThePair = (0, 0)

        wordidx = 0
        while wordidx < len(words):
            overlapidx = 0
            while overlapidx < len(words):
                if wordidx != overlapidx:
                    common = CalMaxOverlap(words[wordidx], words[overlapidx])

                    if common > maximumlen:
                        maximumlen = common
                        MergeThePair = (wordidx, overlapidx)

                overlapidx += 1
            wordidx += 1

        wordidx, overlapidx = MergeThePair

        words[wordidx] += words[overlapidx][maximumlen:]
        del words[overlapidx]

    puzzlesolved = words[0]

    return puzzlesolved


# Que4

def maximumPeople(personHeight, roomHeight):
    MaxPeople = 0
    personHeight.sort()

    numRoomParts = len(roomHeight)

    PersonIdx = 0
    roomoccupied = -500

    while PersonIdx < (len(personHeight)):
        if PersonIdx > numRoomParts - 1:
            return MaxPeople

        RoomIdx = 0

        while RoomIdx < numRoomParts:
            if roomHeight[RoomIdx] == roomoccupied:
                break
            if personHeight[PersonIdx] <= roomHeight[RoomIdx]:
                RoomIdx += 1
            else:
                break

        RoomIdx -= 1
        if RoomIdx != -1:
            MaxPeople += 1
            roomHeight[RoomIdx] = roomoccupied

        PersonIdx += 1
    return MaxPeople


# Que5

def smallestString(encoded: str) -> str:

    mysterylist = list(encoded)
    listlen = len(mysterylist)

    ctr = 0
    while ctr < (listlen // 2):
        if mysterylist[ctr] != 'a':
            mysterylist[ctr] = 'a'
            return ''.join(mysterylist)
        ctr += 1

    mysterylist[-1] = 'b'
    successfullydecoded = ''.join(mysterylist)

    return successfullydecoded


# Que6

def SafeVertex(nxtvertex, graphmatrix, visitorder, pathIdx):

    if graphmatrix[visitorder[pathIdx - 1]][nxtvertex] == 0:
        return False

    for vertex in visitorder:
        if vertex == nxtvertex:
            return False

    return True


def FindHamCycle(adjmatrix, visitorder, VertexIdx):

    if VertexIdx == len(adjmatrix):
        PresentInGraph = (
            adjmatrix[visitorder[VertexIdx - 1]][visitorder[0]] == 1)
        return PresentInGraph

    nxtvertex = 1
    while nxtvertex < len(adjmatrix):
        if SafeVertex(nxtvertex, adjmatrix, visitorder, VertexIdx):
            visitorder[VertexIdx] = nxtvertex
            if FindHamCycle(adjmatrix, visitorder, VertexIdx + 1):
                return True
            visitorder[VertexIdx] = -1

        nxtvertex += 1
    return False


def grandTour(checkpoints):
    numchkpts = len(checkpoints)
    visitorder = [-1] * numchkpts

    visitorder[0] = 0

    if not FindHamCycle(checkpoints, visitorder, 1):
        return False

    return True
