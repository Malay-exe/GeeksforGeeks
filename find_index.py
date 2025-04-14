#find the element by the given key
def find(x,k):
    for i in range(len(x)):
        if x[i] == k:
            return i
    return -1
    
print(find([3,4,5,6],3))