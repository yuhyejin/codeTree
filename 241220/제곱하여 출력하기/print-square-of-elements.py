n = int(input())
arr = list(map(int, input().split()))
new_arr = [elem ** 2 for elem in arr]
for j in new_arr:
    print(f"{j}", end=" ")