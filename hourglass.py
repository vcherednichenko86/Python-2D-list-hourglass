arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sum_list = []

for i in range(0, 4):
    for j in range(0, 4):
        hg_sum = (arr[i][j] + arr[i][j + 1] +arr[i][j + 2]) +\
            (arr[i + 1][j + 1]) +\
            (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

        sum_list.append(hg_sum)

print(max(sum_list))
