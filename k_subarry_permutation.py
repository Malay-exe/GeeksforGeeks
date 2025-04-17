#Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.
def sliding_maximum(x, k):
    c = []
    for i in range(len(x) - k + 1):  
        c.append(max(x[i:i + k]))
    return c
print(sliding_maximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))


# another method

def sliding_maximum(arr, k):
    return [max(arr[i:i + k]) for i in range(len(arr) - k + 1)]
print(sliding_maximum([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))