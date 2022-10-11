def main():
    listNumOne = getWrit()
    listCount = getTotalNum(listNumOne)
    #print(listNumOne)
    #print(listCount)
    # print(getMax(listCount))
    getListRange(listCount, listNumOne)


def getWrit():
    listNumOne = []
    listNum = []
    with open('pbnumbers_v1.txt', 'r') as file:

        descr = file.readlines()
        for ch in descr:
            h = ch.split()
            listNum.append(h)

        for num in range(len(listNum)):
            for i in range(len(listNum[num])):
                topNum = listNum[num][i]
                listNumOne.append(topNum)
        return listNumOne


def getTotalNum(listNumOne):
    """Подсчет повторений"""
    index = 1
    listCount = [0] * len(listNumOne)

    for ch in range(len(listNumOne)):
        index = index + 1
        count = 1
        for i in range(index, len(listNumOne)):
            if listNumOne[ch] == listNumOne[i]:
                count = count + 1
                listCount[ch] = count

    return listCount


def getMax(listCount):
    count = 0
    listMax = []
    totalVal = []
    resList = set(listCount)

    while count != 10:

        for i in resList:
            listMax.append(i)

        second_largest = listMax[0]
        largest_val = listMax[0]
        for i in range(len(listMax)):
            if listMax[i] > largest_val:
                largest_val = listMax[i]

        for i in range(len(listMax)):
            if listMax[i] > second_largest:
                second_largest = listMax[i]

        count = count + 1
        resList.remove(max(resList))
        listMax = []
        totalVal.append(second_largest)

    return totalVal


def getListRange(listCount, listNumOne):
    index = 0
    count = 0
    listMax = []
    totalVal = []
    resList = set(listCount)
    print(resList)
    for i in resList:
        totalVal.append(i)

    for n in listCount:
        if n == totalVal[0]:
            top = listNumOne[index]
            print(top, listCount[n])

        index = index + 1

        # print(indexList)

        count = count + 1

    # totalSum = getMin(list_index, listNumOne)

    # print('Value:', totalSum,'totalSum:',totalVal[0])


def getMin(list_index, listNumOne):
    totalSum = listNumOne[list_index]
    return totalSum


if __name__ == "__main__":
    main()