arr = list(map(int, input().split()))
new_arr = [ i for i in arr if i != 0 and arr != 0]
for i in new_arr:
    if i % 2 == 0:
        i //= 2
    else:
        i += 3
    print(i, end=" ")