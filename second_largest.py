def find_digit(arr):
    arr.sort()   
    x = arr[-1]   
    for i in range(len(arr)-2,-1,-1):
        print(x)
        if arr[i] != x:
            return arr[i]
        x = arr[i]
    return 0
if __name__ == "__main__":
    print(find_digit([1,2,3,4,5,6,7,8,9,9,9,9,9]))