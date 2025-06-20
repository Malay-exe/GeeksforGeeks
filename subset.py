#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
def sub(a, b):
    for i in b:  
        if i not in a:  
            print("b[] is not a subset of a[]")
            return 
    print("b[] is a subset of a[]")  

a = [1, 2, 3, 4, 5]
b = [1,2,8]
sub(a,b)