#Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.
def merg(a,b,k):
    x=a+b
    x.sort()
    return x[k-1]
print(merg([2 ,3, 6, 7, 9],[1,4,8,10],5))