def seclarg(lst):
    y=set(lst)
    sorted(y)
    y=list(y)
    if len(y)<1:
        return -1
    elif len(y)>1:
        return [y[-2]]
# x=[1,2,3,4,5,6,7,8,9,9,9,9,9]
x=[5,5,5,5,5]
print(seclarg(x))