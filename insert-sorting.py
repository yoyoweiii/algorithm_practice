#basic algorithm practice part1
randomlist=[6,8,6,5,531,5,2,8,89,54,23,15,5,6,8654,5,56,45,5,54,65,2,654,23,1]
randomlist2=[10,9,8,7,6,5,4,3,2,1]
def insertion_sort(randomlist):
    print("before: ",randomlist)
    for i in range(1,len(randomlist)):
        key = randomlist[i]
        j=i-1
        while j >= 0 and key < randomlist[j]:
            randomlist[j+1]=randomlist[j]
            j-=1
        randomlist[j + 1] = key
    print("after: ",randomlist)
insertion_sort(randomlist)
insertion_sort(randomlist2)
