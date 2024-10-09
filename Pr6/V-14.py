#1
arr = [10,11,12,13,14,15,16,17,18,19]
max = arr.index(max(arr))
min = arr.index(min(arr))
arr[max], arr[min] = arr[min], arr[max]
print(arr)
#2
numbers = []
for i in range(10):
  number = int(input(f"Введите число {i + 1}: "))
  numbers.append(number)
average = sum(numbers) / len(numbers)
for i in range(len(numbers)):
  if numbers[i] > average:
    numbers[i] = 1
print("Массив:", numbers)
print("Среднее арифметическое:", average)