#62. Intro to Tutorial Challenges
def introTutorial(V, arr):
    return arr.index(V)
	
#63. Insertion Sort - Part 1
def insertionSort1(n, arr):
    v = arr[-1]
    idx = n-2
    
    while (v < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1
        
    arr[idx+1] = v
    print(' '.join(map(str, arr)))
	
#64. Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = key

        print(' '.join(map(str, arr)))
		
#65. Correctness and the Loop Invariant
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
		
#66. Running Time of Algorithms
def runningTime(arr):
    shift = 0
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            shift += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return shift
	
#67. Quicksort 1 - Partition
def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    return left + right

#68. Quicksort 2 - Sorting
def quickSort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    l, r = [], []
    for i in arr:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
            
    sub = quickSort(l) + [p] + quickSort(r)
    print(' '.join(map(str, sub)))
    return sub

n = int(input())
arr = list(map(int, input().split()))

quickSort(arr)

#69. Quicksort In-Place
def partition(st, en):
    global arr
    if en - st > 0:        
        pivot, border = arr[en], st
        for i in range(st, en):
            if arr[i] < pivot:
                arr[i], arr[border] = arr[border], arr[i]
                border +=1         
        arr[en], arr[border] = arr[border], arr[en]
        print (' '.join(map(str,arr)))
        partition(st, border-1) #Sort Left
        partition(border+1, en) #Sort Right
        
n = int(input())
arr = list(map(int, input().split()))

partition(0, n-1)

#70. Running Time of Quicksort
class Insertion:
    def __init__(self):
        self.count=0
        
    def insertionsort(self,a):
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while j>=0 and a[j]>key:
                self.count+=1
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
        return self.count
    
class QuickSort:
    def __init__(self):
        self.count=0
        
    def swap(self,b,c,d):
        temp=b[c]
        b[c]=b[d]
        b[d]=temp
        return b
    
    def partition(self,a,s,e):
        pivot=e
        pindex=s
        for i in range(s,e):
            if a[i]<=a[pivot]:
                self.swap(a,i,pindex)
                self.count+=1
                pindex+=1
        self.count+=1
        self.swap(a,pindex,pivot)
        return pindex
    
    def quicksort(self,a,s,e):
        if s<e:
            pIndex=self.partition(a,s,e)
            self.quicksort(a, s, pIndex-1)
            self.quicksort(a, pIndex+1, e)
        return self.count
        
n=int(input())
br=[]
ar=[int(temp) for temp in input().strip().split(' ')]
for i in ar:
    br.append(i)

start=0
end=len(ar)-1
quicksort=QuickSort()
insertion=Insertion()
print(insertion.insertionsort(br)-quicksort.quicksort(ar, start, end))

#71. Counting Sort 1
def countingSort(arr):
    ar = [0 for i in range(100)]
    
    for i in arr:
        ar[i] += 1
        
    return ar
	
#72. Counting Sort 2
def countingSort(arr):
    ar = [0 for i in range(100)]
    
    for i in arr:
        ar[i] += 1
        
    return [i for i in range(100) for _ in range(ar[i])]
	
#73. Counting Sort 3
n = int(input())
ar = []

for i in range(n):
    ar.append(input().split())
    
a = [0 for i in range(100)]
for i in ar:
    a[int(i[0])] += 1
    
count = 0
for i in range(len(a)):
    count += a[i]
    a[i] = count
    
print(*a)

