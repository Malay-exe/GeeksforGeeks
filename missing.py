#print the missing number
def miss(lst):
    lst.sort()
    for i in range(lst[0], lst[-1] + 1):
        if i not in lst:
            return i
    # return lst[0] - 1 
    return lst[-1] +1
# x=[0]
x=[1,2,3]
# x=[1,3,4,5]
print(miss(x))