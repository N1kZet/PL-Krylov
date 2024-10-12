def fill_matrix_spiral(n):
  """Заполняет квадратную матрицу порядка n натуральными числами по спирали."""
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  num = 1
  row_start = 0
  row_end = n - 1
  col_start = 0
  col_end = n - 1

  while row_start <= row_end and col_start <= col_end:
    # Заполняем верхнюю строку
    for i in range(col_start, col_end + 1):
      matrix[row_start][i] = num
      num += 1
    row_start += 1

    # Заполняем правый столбец
    for i in range(row_start, row_end + 1):
      matrix[i][col_end] = num
      num += 1
    col_end -= 1

    # Заполняем нижнюю строку (если она не пустая)
    if row_start <= row_end:
      for i in range(col_end, col_start - 1, -1):
        matrix[row_end][i] = num
        num += 1
      row_end -= 1

    # Заполняем левый столбец (если он не пустой)
    if col_start <= col_end:
      for i in range(row_end, row_start - 1, -1):
        matrix[i][col_start] = num
        num += 1
      col_start += 1

  return matrix

# Ввод порядка матрицы
n = int(input("Введите порядок квадратной матрицы (n): "))

# Заполнение матрицы по спирали
matrix = fill_matrix_spiral(n)

# Вывод матрицы
print("Матрица, заполненная по спирали:")
for row in matrix:
  print(*row)