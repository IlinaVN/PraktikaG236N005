import functools


@functools.lru_cache(maxsize=4)
def trib(n):
    if n in (1, 2):
        return 0
    if n in (3,):
        return 1
    return trib(n - 1) + trib(n - 2) + trib(n - 3)


print('Введите число элементов массива:')
n = int(input())
a = [0] * n
b = [0] * n
for i in range(0, n):
    print('a[', i, ']=')
    a[i] = int(input())
print(a)
for i in range(0, n):
    b[i] = trib(a[i])
print('Числа трибоначчи:', b)
