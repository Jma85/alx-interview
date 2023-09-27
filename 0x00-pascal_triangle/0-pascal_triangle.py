#!/usr/bin/python3

def pascal_triangle(n):
  """Returns a list of lists of integers representing the Pascal's triangle of the given height.

  Args:
    height: The height of the Pascal's triangle.

  Returns:
    A list of lists of integers representing the Pascal's triangle of the given height.
  """
  if n <= 0:
    return []

  triangle = [[1]]
  for i in range(1, n):
    prev_row = triangle[-1]
    row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(prev_row[j - 1] + prev_row[j])
    triangle.append(row)
  return triangle
