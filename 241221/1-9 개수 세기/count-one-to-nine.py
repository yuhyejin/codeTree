count_arr = [0] * 10

n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    count_arr[i] += 1

for i in range(1, 10):
    print(f"{count_arr[i]}")