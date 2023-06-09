# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))