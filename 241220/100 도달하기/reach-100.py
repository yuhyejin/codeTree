n = int(input())
arr = [1, n]
for i in range(3, 20):
    arr.append(arr[-1] + arr[-2])
for i in arr:
    print(i, end=" ")
    if i > 100:
        break
