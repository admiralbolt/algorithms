

def generate_sierpinski_triangle(n):
  if n <= 0:
    return []
  if n == 1:
    return [[1]]
  if n == 2:
    return [[1], [1, 1]]
  triangle = [[1], [1, 1]]
  for i in range(1, n):
    new_row = [1]
    for j in range(len(triangle[i]) - 1):
      new_row.append(triangle[i][j] + triangle[i][j + 1])
    new_row.append(1)
    triangle.append(new_row)
  return triangle

total = 0
for row in generate_sierpinski_triangle(100):
  for item in row:
    if item > 1000000:
      total += 1
print(total)
