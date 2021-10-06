import pktutils

def bubblesort(mlist):
    m = len(mlist)
    for x in range(m):
        for y in range(m-x-1):
            if mlist[y] > mlist[y+1]:
                mlist[y], mlist[y+1] = mlist[y+1], mlist[y]

def insertionsort(mlist):
    for i in range(1, len(mlist)):
        key = mlist[i]
        j = i-1
        while j >= 0 and key <= mlist[j]:
            mlist[j+1] = mlist[j]
            j -= 1
            mlist[j+1] = key
def selectionsort(mlist):
    for i in range(len(mlist)):
        min_index = i
        for j in range(i + 1, len(mlist)):
            if mlist[min_index] > min_index[j]:
                min_index = j
        mlist[i], mlist[min_index] = mlist[min_index], mlist[i]

if __name__ == "__main__":
    nlist = [1,2,5,6,3,9,7,8,8,4]
    print(bsortlist = bubblesort(nlist))
    print(isortlist = insertionsort(nlist))
    print(ssortlist = selectionsort(nlist))

