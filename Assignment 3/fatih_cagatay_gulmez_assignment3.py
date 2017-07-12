def bestRoute(mountain):
#### initialization
    decisionMatrix = []
    rowNum = len(mountain)
    for i in range(rowNum):
        decisionMatrix.append([])
        for j in range(rowNum):
            decisionMatrix[i].append((0, None, None))
#### numOfNodes = mountainHeight*(mountainHeight+1)/2
#### complexity = numOfNodes = O(n)
#### Beginning of Algorithm
    for level in range(rowNum):
        route = 0
        bestRoute = 0
        while route<rowNum:
            try:
                if level == 0:
                    decisionMatrix[level][route] = mountain[level][route], (0, 0)
                else:
                    if route == 0:
                        decisionMatrix[level][route]= decisionMatrix[level-1][route][0]+mountain[level][route], (level-1, route)
                    else:
                        probableParentOneValue = decisionMatrix[level - 1][route - 1][0] + mountain[level][route]
                        probableParentOne = (level - 1, route - 1)
                        probableParentTwoValue = decisionMatrix[level - 1][route][0] + mountain[level][route]
                        probableParentTwo = (level - 1, route)
                        parent = max(probableParentOneValue, probableParentTwoValue)
                        if parent == probableParentOneValue:
                            decisionMatrix[level][route]= parent, probableParentOne
                        else:
                            decisionMatrix[level][route] = parent, probableParentTwo
                        if level == rowNum-1:
                            if bestRoute < decisionMatrix[level][route][0]:
                                bestRoute = decisionMatrix[level][route][0]
                                bestRouteEnd = level, route
                route += 1
            except IndexError:
                break
#### End of algorithm
    node = bestRouteEnd
    route = str(node)
    while node != (0,0):
        node = decisionMatrix[node[0]][node[1]][1]
        route = str(node)+", " + route

    return "Route: " + route + "\nScore: " + str(decisionMatrix[bestRouteEnd[0]][bestRouteEnd[1]][0])


def bestSelection(conferences):
    size = len(conferences)
    conference = [] # Conference names.
    begin = [] # Begin times
    end = [] #End times
    count = [] # Participant numbers
    total = [] # Total number of participants for each column.
    decisionMatrix = []
    temp = 0
    for con in conferences:
        decisionMatrix.append([])
        for con_ in range(size):
            decisionMatrix[temp].append(0)
        temp += 1
        [b, e, c] = conferences[con]
        conference.append(con)
        begin.append(b)
        end.append(e)
        count.append(c)
        total.append(0)
###End of initialization.
###Algorithm starts here.
    for row in range(size):
        for col in range(row+1):
            if decisionMatrix[row][col] != 0:
                pass
            else:
                if (begin[row] > end[col] or end[row] < begin[col]):
                    decisionMatrix[row][col] += count[row]
                    total[col] += count[row]
                elif row == col:
                    decisionMatrix[row][col] = count[row]
                    total[col] += count[row]
                elif begin[row] == end[col] or end[row] == begin[col] and count[row]>count[col]:
                    decisionMatrix[col][col] = 0
                    total[col] -= count[col]
                    decisionMatrix[row][col] += count[row]
                    total[col] += count[row]
### Algorithm ends here.
    maxCount = 0, None
    for totalParticipant in range(len(total)):
        if total[totalParticipant] > maxCount[0]:
            maxCount = total[totalParticipant], totalParticipant

    out = "Selected Conferences: "
    for counter in range(size):
        if decisionMatrix[counter][maxCount[1]] != 0:
            out = out + conference[counter] + " "

    return out+"\nTotal number of participants: " + str(maxCount[0])


def possibleCombinations(number):
    result = [[()], [(1,)]]
    if number== 1:
        return [1]
    elif number<1:
        return None
    else:
        num = 2
        while num <= number:
            temp = []
            for i in range(num):
                for decision in result[i]:
                    a = tuple(sorted((num - i,) + decision))
                    if len(a)>1 and a not in temp:
                        temp.append(a)
            result.append(temp)
            num += 1
        return result[number]

for i in range(1,6):
    print possibleCombinations(i)