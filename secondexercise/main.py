import pktutils


def bubblesort(mlist):
    m = len(mlist)
    for x in range(m):
        for y in range(0, m - x - 1):
            if mlist[y] > mlist[y + 1]:
                mlist[y], mlist[y + 1] = mlist[y + 1], mlist[y]
    return mlist

def insertionsort(mlist):
    for i in range(1, len(mlist)):
        key = mlist[i]
        j = i - 1
        while j >= 0 and key <= mlist[j]:
            mlist[j + 1] = mlist[j]
            j -= 1
            mlist[j + 1] = key
    return mlist

def selectionsort(mlist):
    for i in range(len(mlist)):
        min_index = i
        for j in range(i + 1, len(mlist)):
            if mlist[min_index] > mlist[j]:
                min_index = j
        mlist[i], mlist[min_index] = mlist[min_index], mlist[i]
    return mlist

if __name__ == "__main__":
    nlist = [1, 2, 5, 6, 3, 9, 7, 8, 8, 4]
    bsortlist = bubblesort(nlist)
    isortlist = insertionsort(nlist)
    ssortlist = selectionsort(nlist)
    print(bsortlist)
    print(isortlist)
    print(ssortlist)
