def miss(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
x=[1]
# x=[1,2,3]
# x=[1,3,4,5]
print(miss(x))