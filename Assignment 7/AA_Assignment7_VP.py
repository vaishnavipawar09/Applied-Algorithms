# Que1
from heapq import heappush, heappop
from typing import List
import heapq


def specialHub(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    graph = {i: [] for i in range(n)}
    for edge1, edge2, weight in edges:
        graph[edge1].append((edge2, weight))
        graph[edge2].append((edge1, weight))

    def usingdijkstra(startingcity):
        citydistances = [float('inf')] * n
        citydistances[startingcity] = 0
        priorityqueue = [(0, startingcity)]

        while priorityqueue:
            current_minDist, currentvertex = heapq.heappop(priorityqueue)

            if current_minDist > citydistances[currentvertex]:
                continue

            for neighborcity, currweight in graph[currentvertex]:
                totaldistance = current_minDist + currweight
                if totaldistance < citydistances[neighborcity]:
                    citydistances[neighborcity] = totaldistance
                    heapq.heappush(
                        priorityqueue, (totaldistance, neighborcity))

        return citydistances

    leastConnected = float('inf')
    chosenCity = -1

    for city in range(n):
        nearbyCities = sum(1 for dist in usingdijkstra(
            city) if dist <= distanceThreshold and dist != 0)

        if nearbyCities < leastConnected:
            leastConnected = nearbyCities
            chosenCity = city
        elif nearbyCities == leastConnected and city > chosenCity:
            chosenCity = city

    return chosenCity


# Que2

def challenge(n: int, connections: List[List[int]]) -> int:
    rootArray = list(range(n + 1))

    def findRoot(cityStart):
        if rootArray[cityStart] != cityStart:
            rootArray[cityStart] = findRoot(rootArray[cityStart])
        return rootArray[cityStart]

    def linkCities(cityStart, adjCity):
        rootArray[findRoot(cityStart)] = findRoot(adjCity)

    connections.sort(key=lambda cityStart: cityStart[2])

    linkingcost, linkCount, idx = 0, 0, 0

    while idx < len(connections) and linkCount < n - 1:
        cityStart, adjCity, edgecost = connections[idx]
        if findRoot(cityStart) != findRoot(adjCity):
            linkCities(cityStart, adjCity)
            linkingcost += edgecost
            linkCount += 1
        idx += 1

    if linkCount == n - 1:
        return linkingcost
    else:
        return -1

# Que3


def min_cost_to_supply_water(n, wells, pipes):
    watersystem = [[] for _ in range(n + 1)]

    for house_idx, houseWellCost in enumerate(wells, 1):
        watersystem[0].append((houseWellCost, house_idx))

    for house1, house2, supplycost in pipes:
        watersystem[house1].append((supplycost, house2))
        watersystem[house2].append((supplycost, house1))

    def usingPrim_WaterCost():
        minWatercost = 0
        visitednode = [False] * (n + 1)
        min_heapQueue = [(0, 0)]

        while min_heapQueue:
            supplycost, villagehouse = heapq.heappop(min_heapQueue)
            if visitednode[villagehouse]:
                continue

            minWatercost += supplycost
            visitednode[villagehouse] = True

            for edgecost, nxthouse in watersystem[villagehouse]:
                if not visitednode[nxthouse]:
                    heapq.heappush(min_heapQueue, (edgecost, nxthouse))

        return minWatercost

    return usingPrim_WaterCost()


# Que4

def cheapestRoutes(s, prices):
    priceslen = len(prices)
    min_prices = [float('inf')] * priceslen
    min_prices[s] = 0

    pqueue = [(0, s)]

    while pqueue:
        flightfare, currcity = heapq.heappop(pqueue)

        if flightfare > min_prices[currcity]:
            continue

        for adjcity in range(priceslen):
            if prices[currcity][adjcity] != -1:
                newflightfare = flightfare + prices[currcity][adjcity]
                if newflightfare < min_prices[adjcity]:
                    min_prices[adjcity] = newflightfare
                    heapq.heappush(pqueue, (newflightfare, adjcity))

    newPrices = []
    for flightfare in min_prices:
        if flightfare == float('inf'):
            newPrices.append(-1)
        else:
            newPrices.append(flightfare)

    min_prices = newPrices

    return min_prices


# Que5

def isDividePossible(n, connected_houses):
    Houseconnection = [[] for _ in range(n)]
    for houseA, houseB in connected_houses:
        Houseconnection[houseA].append(houseB)
        Houseconnection[houseB].append(houseA)

    housecolors = [-1] * n

    def usingdfs(currHouse, colorofhouse):
        housecolors[currHouse] = colorofhouse
        for adjacentHouse in Houseconnection[currHouse]:
            if housecolors[adjacentHouse] == -1:
                if not usingdfs(adjacentHouse, 1 - colorofhouse):
                    return False
            elif housecolors[adjacentHouse] == housecolors[currHouse]:
                return False
        return True

    for ctr in range(n):
        if housecolors[ctr] == -1:
            if not usingdfs(ctr, 0):
                return False

    return True

# Que6


def minCostToConnectHubs(hubs):
    def calManhattanDist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def using_mst():
        numOfHubs = len(hubs)
        minCost = [float('inf')] * numOfHubs
        minCost[0] = 0
        hubInMST = [False] * numOfHubs

        connectionCost = 0
        priorityQueue = [(0, 0)]

        while priorityQueue:
            edgeCost, currHub = heapq.heappop(priorityQueue)

            if hubInMST[currHub]:
                continue

            hubInMST[currHub] = True
            connectionCost += edgeCost

            for nxtHub in range(numOfHubs):
                if not hubInMST[nxtHub]:
                    hubDistance = calManhattanDist(hubs[currHub], hubs[nxtHub])
                    if hubDistance < minCost[nxtHub]:
                        minCost[nxtHub] = hubDistance
                        heapq.heappush(priorityQueue, (hubDistance, nxtHub))

        return connectionCost

    return using_mst()


# Que7


def findMaxSuccessPath(n, edges, prob, start_node, end_node):
    satelliteNetwork = {i: [] for i in range(n)}
    for edgeidx, (a, b) in enumerate(edges):
        satelliteNetwork[a].append((b, prob[edgeidx]))
        satelliteNetwork[b].append((a, prob[edgeidx]))

    PriorityQueue = [(-1, start_node)]

    HighestSuccess = [0] * n
    HighestSuccess[start_node] = 1

    while PriorityQueue:
        prob, station = heapq.heappop(PriorityQueue)
        prob = -prob

        if station == end_node:
            return prob

        for nxtsatellite, linkProb in satelliteNetwork[station]:
            newProb = prob * linkProb
            if newProb > HighestSuccess[nxtsatellite]:
                HighestSuccess[nxtsatellite] = newProb
                heapq.heappush(PriorityQueue, (-newProb, nxtsatellite))

    return 0.0


# Que8


def minimumTimeToVisit(grid):
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    rowCount, colCount = len(grid), len(grid[0])
    visitQueue = [(0, 0, 0)]
    visitedCells = set()

    while visitQueue:
        traveltime, gridRow, gridCol = heappop(visitQueue)

        if (gridRow, gridCol) in visitedCells:
            continue
        visitedCells.add((gridRow, gridCol))

        if (gridRow, gridCol) == (rowCount - 1, colCount - 1):
            return traveltime

        if gridRow + 1 < rowCount and (gridRow + 1, gridCol) not in visitedCells:
            if (grid[gridRow + 1][gridCol] - traveltime) % 2 == 0:
                waitTime = 1
            else:
                waitTime = 0

            heappush(
                visitQueue, (max(traveltime + 1, grid[gridRow + 1][gridCol] + waitTime), gridRow + 1, gridCol))

        if gridRow - 1 >= 0 and (gridRow - 1, gridCol) not in visitedCells:
            if (grid[gridRow - 1][gridCol] - traveltime) % 2 == 0:
                waitTime = 1
            else:
                waitTime = 0

            heappush(
                visitQueue, (max(traveltime + 1, grid[gridRow - 1][gridCol] + waitTime), gridRow - 1, gridCol))

        if gridCol + 1 < colCount and (gridRow, gridCol + 1) not in visitedCells:
            if (grid[gridRow][gridCol + 1] - traveltime) % 2 == 0:
                waitTime = 1
            else:
                waitTime = 0

            heappush(
                visitQueue, (max(traveltime + 1, grid[gridRow][gridCol + 1] + waitTime), gridRow, gridCol + 1))

        if gridCol - 1 >= 0 and (gridRow, gridCol - 1) not in visitedCells:
            if (grid[gridRow][gridCol - 1] - traveltime) % 2 == 0:
                waitTime = 1
            else:
                waitTime = 0

            heappush(
                visitQueue, (max(traveltime + 1, grid[gridRow][gridCol - 1] + waitTime), gridRow, gridCol - 1))

    return -1


# Que9

def WeightLimitedPathsExist(n, edgelist, querylist):
    bridgeConnections = {ctr: [] for ctr in range(n)}
    for edgeA, edgeB, edgewt in edgelist:
        bridgeConnections[edgeA].append((edgeB, edgewt))
        bridgeConnections[edgeB].append((edgeA, edgewt))

    def usingdfs(currentIsland, targetIsland, maxweight, visitedIslands):
        if currentIsland == targetIsland:
            return True
        visitedIslands.add(currentIsland)
        for nxtIsland, bridgeCapacity in bridgeConnections[currentIsland]:
            if nxtIsland not in visitedIslands and maxweight <= bridgeCapacity:
                if usingdfs(nxtIsland, targetIsland, maxweight, visitedIslands):
                    return True
        return False

    journeypossible = []
    for startpt, endpt, weightcapacity in querylist:
        visitedIslands = set()
        resultobtained = usingdfs(
            startpt, endpt, weightcapacity, visitedIslands)
        journeypossible.append(resultobtained)

    return journeypossible


# Que10

def shortestFareRoute(start, target, specialRoads):
    def calculatemanhattandist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    CityMap = {}

    for bridge in specialRoads:
        startX, startY, endX, endY, bridgeCost = bridge
        CityMap[(startX, startY)] = CityMap.get(
            (startX, startY), []) + [(endX, endY, bridgeCost)]
        CityMap[(endX, endY)] = CityMap.get(
            (endX, endY), []) + [(startX, startY, bridgeCost)]

    def usingdijkstra(startpos, endpos):
        minHeap = [(0, startpos)]
        visitednode = set()
        while minHeap:
            totalfare, currentpos = heapq.heappop(minHeap)
            if currentpos in visitednode:
                continue
            visitednode.add(currentpos)
            if currentpos == endpos:
                return totalfare
            for neighbor in CityMap.get(currentpos, []):
                if neighbor not in visitednode:
                    nxtCost = totalfare + neighbor[2]
                    heapq.heappush(
                        minHeap, (nxtCost, (neighbor[0], neighbor[1])))

            for changeX, changeY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                adjposition = (currentpos[0] + changeX,
                               currentpos[1] + changeY)
                if 0 <= adjposition[0] and 0 <= adjposition[1] and adjposition not in visitednode:
                    nxtCost = totalfare + \
                        calculatemanhattandist(
                            currentpos[0], currentpos[1], adjposition[0], adjposition[1])
                    heapq.heappush(minHeap, (nxtCost, adjposition))
        return float("inf")

    minSpendTargetReached = usingdijkstra(tuple(start), tuple(target))
    return minSpendTargetReached
