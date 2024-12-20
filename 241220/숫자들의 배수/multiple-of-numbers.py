n = int(input())
cnt = 0; k = n; i = 2
arr = []
while True:
    print(k, end=" ")
    if k % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
    k = n * i
    i += 1
    arr.append(k)