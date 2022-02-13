from typing import List


def gnome(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    if numbers[i] > numbers[i+1]:
      numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
      i = i - 1

  print(numbers)

if __name__ == "__main__":
  import random
  num = [random.randint(0,1000) for i in range(10)]
  print(gnome(num))