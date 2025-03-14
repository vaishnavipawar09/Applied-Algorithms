# Ques1

def MinimumExpenditure(AppleTreePrice):
    NumberOfFarms = len(AppleTreePrice)

    if NumberOfFarms == 1:
        OneFarm = min(AppleTreePrice[0])
        return OneFarm

    farm_mincost1, farm_mincost2, farm_mincost3 = 0, 0, 0

    for ctr in range(NumberOfFarms):
        MinCost1, MinCost2, MinCost3 = farm_mincost1, farm_mincost2, farm_mincost3
        farm_mincost1 = AppleTreePrice[ctr][0] + min(MinCost2, MinCost3)
        farm_mincost2 = AppleTreePrice[ctr][1] + min(MinCost1, MinCost3)
        farm_mincost3 = AppleTreePrice[ctr][2] + min(MinCost1, MinCost2)

    minexpenditure = min(farm_mincost1, farm_mincost2, farm_mincost3)

    return minexpenditure


# Ques2

def alignments(A, B):

    dp_2dlist = [[0] * (B + 1) for _ in range(A + 1)]
    dp_2dlist[0][0] = 1

    rowindex = 1
    while rowindex <= A:
        dp_2dlist[rowindex][0] = 1
        rowindex += 1

    columnindex = 1
    while columnindex <= B:
        dp_2dlist[0][columnindex] = 1
        columnindex += 1

    rowindex = 1
    while rowindex <= A:
        columnindex = 1
        while columnindex <= B:
            diagonalvalue = dp_2dlist[rowindex-1][columnindex-1]
            abovevalue = dp_2dlist[rowindex-1][columnindex]
            leftvalue = dp_2dlist[rowindex][columnindex-1]
            dp_2dlist[rowindex][columnindex] = (
                diagonalvalue + abovevalue + leftvalue)
            columnindex += 1
        rowindex += 1

    return dp_2dlist[A][B]


# Ques3

def smallestMissingNumber(streetNumbers):

    RightIndex = len(streetNumbers) - 1
    missingnum = using_dac(streetNumbers, 0, RightIndex)
    if missingnum in streetNumbers:
        return missingnum + 1
    return missingnum


def using_dac(streetNumbers, LIndex, RIndex):
    if LIndex > RIndex:
        return LIndex

    MidIndex = LIndex + (RIndex - LIndex) // 2

    if streetNumbers[MidIndex] == MidIndex:
        MoveRight = MidIndex + 1
        return using_dac(streetNumbers, MoveRight, RIndex)
    else:
        MoveLeft = MidIndex - 1
        return using_dac(streetNumbers, LIndex, MoveLeft)


# Ques4

def solution_inheritance(num_items, num_boxes, children):
    if num_boxes < children or children <= 0:
        less = -1
        return less

    def distributionsuccess(MaxPartitionSum):
        SumOfItems = 0
        DivisonCount = 0
        IndexPosition = 0

        while IndexPosition < len(num_items):
            SumOfItems += num_items[IndexPosition]
            if SumOfItems > MaxPartitionSum:
                DivisonCount += 1
                SumOfItems = num_items[IndexPosition]
            IndexPosition += 1

        DivisonCount += 1

        return DivisonCount <= children

    LSide = max(num_items)
    RSide = sum(num_items)

    while LSide < RSide:
        MidPt = (LSide + RSide) // 2

        if distributionsuccess(MidPt):
            RSide = MidPt
        else:
            LSide = MidPt + 1

    return LSide


# Ques5

def place_max_speedbump(len_road, bump_int1, bump_int2, bump_int3):

    if len_road <= 0:
        return 0

    minspeedbump = [float('-inf')] * (len_road + 1)
    minspeedbump[0] = 0

    SpeedBumpIntervals = {bump_int1, bump_int2, bump_int3}

    flg = 1
    while flg <= len_road:
        for bumpinterval in SpeedBumpIntervals:
            Checkposition = flg - bumpinterval
            if Checkposition >= 0:
                minspeedbump[flg] = max(
                    minspeedbump[flg], minspeedbump[Checkposition] + 1)
        flg += 1

    if minspeedbump[len_road] > 0:
        possible = minspeedbump[len_road]
        return possible
    else:
        notpossible = 0
        return notpossible


# Ques6

def find_path(stone_inscription_list):

    NumberOfStones = len(stone_inscription_list)
    if NumberOfStones == 0:
        return 0

    MinStoneReq = [float('inf')] * NumberOfStones
    MinStoneReq[0] = 0

    CurrStone = 0
    while CurrStone < NumberOfStones:
        upperlimit = CurrStone + stone_inscription_list[CurrStone] + 1
        upperlimit = min(upperlimit, NumberOfStones)

        OtherStone = CurrStone + 1
        while OtherStone < upperlimit:
            MinStoneReq[OtherStone] = min(
                MinStoneReq[OtherStone], MinStoneReq[CurrStone] + 1)
            OtherStone += 1

        CurrStone += 1

    LastStone = MinStoneReq[-1]
    return LastStone


# Ques7


def decode_cryptic_message(lists):

    def mergebothlists(scroll1, scroll2):

        LIndex = RIndex = 0
        resultOfMerge = []

        while LIndex < len(scroll1) and RIndex < len(scroll2):
            if scroll1[LIndex] < scroll2[RIndex]:
                resultOfMerge.append(scroll1[LIndex])
                LIndex += 1
            else:
                resultOfMerge.append(scroll2[RIndex])
                RIndex += 1

        while LIndex < len(scroll1):
            resultOfMerge.append(scroll1[LIndex])
            LIndex += 1

        while RIndex < len(scroll2):
            resultOfMerge.append(scroll2[RIndex])
            RIndex += 1

        return resultOfMerge

    while len(lists) > 1:
        mergedpairs = []
        scrollindex = 0

        while scrollindex < len(lists) - 1:
            mergedpairs.append(mergebothlists(
                lists[scrollindex], lists[scrollindex + 1]))
            scrollindex += 2

        if scrollindex < len(lists):
            mergedpairs.append(lists[scrollindex])

        lists = mergedpairs

    if lists:
        return lists[0]
    else:
        return []
