arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr[1], arr[2] = list(map(int, input().split()))
for i in range(3, 11):
    arr[i] = arr[i-1] + arr[i-2]
    if arr[i] >= 10:
        arr[i] = arr[i]%10
for i in arr[1:]:
    print(f"{i}", end=" ")