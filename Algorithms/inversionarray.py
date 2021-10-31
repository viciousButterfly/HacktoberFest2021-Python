def merge(A, aux, low, mid, high):

    k = i = low
    j = mid + 1
    inversionCount = 0

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (mid - i + 1)  # NOTE

        k = k + 1

    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
    

    for i in range(low, high + 1):
        A[i] = aux[i]
    return inversionCount


def mergeSort(A, aux, low, high):

    # Base case
    if high == low:  # if run size == 1
        return 0

    mid = low + ((high - low) >> 1)
    inversionCount = 0

    
    inversionCount += mergeSort(A, aux, low, mid)        # split / merge left half
    inversionCount += mergeSort(A, aux, mid + 1, high)   # split / merge right half
    inversionCount += merge(A, aux, low, mid, high)      # merge the two half runs

    return inversionCount


if __name__ == '__main__':

    n=int(input())
    A=list(map(int,input().split()))
    aux=A.copy()
    print(mergeSort(A, aux, 0, len(A) - 1)) 