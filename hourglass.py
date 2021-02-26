arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_val = 0

for i in range(0, 4):
    for j in range(0, 4):
        hg_sum = (arr[i][j] + arr[i][j + 1] +arr[i][j + 2]) +\
            (arr[i + 1][j + 1]) +\
            (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

        if hg_sum > max_val:
            max_val = hg_sum

print(max_val)
