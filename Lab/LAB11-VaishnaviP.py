def minCostConnectPoints(points):
    def calculatemanhattan(p1, p2):
        cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # calculates the cost
        return cost

    NumOfPts = len(points)
    inMST = [False] * NumOfPts   # check if present in MST
    inMST[0] = True  # Starting with the first point
    totalCost = 0

    for _ in range(NumOfPts - 1):  # connect all points except 1st
        min_dist = float('inf')
        for ctr1 in range(NumOfPts):  # check closest pt anywhere
            if inMST[ctr1]:
                for ctr2 in range(NumOfPts):
                    if not inMST[ctr2]:
                        dist = calculatemanhattan(points[ctr1], points[ctr2])
                        if dist < min_dist:  # update mindist and nextpt
                            min_dist = dist
                            next_point = ctr2

        inMST[next_point] = True  # marked to be in the MST
        totalCost += min_dist  # Total cost calcultion

    return totalCost
