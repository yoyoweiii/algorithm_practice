#basic algorithm practice part2
random_list=[6,8,6,5,531,5,2,8,89,54,23,15,5,6,8654,5,56,45,5,54,65,2,654,23,1]
def merge(L,R):
    temp=[]
    i=j=0
    while len(temp)<(len(L)+len(R)):
        if L[i]<R[j]:
            temp.append(L[i])
            i+=1
        else: 
            temp.append(R[j])
            j+=1
        if i == len(L) or j == len(R):
            temp.extend(L[i:] or R[j:])
            break
    return temp
def mergesort(a):
    if len(a) < 2:
        return a
    mid=int(len(a)/2)
    left=mergesort(a[:mid])
    right=mergesort(a[mid:])
    return merge(left,right)
print(mergesort(random_list))
