# Given a number N, write a program to check whether given number is Adam Number or not.
# Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other.
def checkAdamOrNot(N):
        # code here 
        x=1
        x=N**2
        y=''
        for i in f"{N}":
            y=i+y
        a=int(y)
        b=a**2
        # print(x,b)
        r=''
        for j in f"{b}":
              r=j+r
        # print(r)
        ri=int(r)
        return 'YES' if x==ri else 'NO'
g=12
print(checkAdamOrNot(g))
