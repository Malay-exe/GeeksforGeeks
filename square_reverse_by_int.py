def rev_n(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

def adam(N):
    rev_N = rev_n(N)
    
    square_N = N * N
    square_rev_N = rev_N * rev_N
    
    rev_square_N = rev_n(square_N)
    
    return 'YES' if rev_square_N == square_rev_N else 'NO'
        

N = 12
print(adam(N))
