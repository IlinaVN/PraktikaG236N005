def maxsum(arr):
    maximum = max(arr)
    if maximum < 0:
        return maximum
    summa = 0
    ending = 0
    for i in arr:
        ending = ending + i
        ending = max(ending, 0)
        summa = max(summa, ending)
    return summa


print('Введите число элементов массива:')
n = int(input())
a = [0] * n
for i in range(0, n):
    print('a[', i, ']=')
    a[i] = int(input())
print(a)
print('Максимальная последовательная сумма чисел:', maxsum(a))
