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
	
