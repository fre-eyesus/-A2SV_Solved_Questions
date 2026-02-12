Copy
matrix = []
for i in range(5):
  row = list(map(int, input().split()))
  matrix.append(row)
  if 1 in row:
    r, c = i + 1, row.index(1) + 1
print(abs(r - 3) + abs(c - 3))
