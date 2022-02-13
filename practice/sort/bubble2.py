from typing import List

def bubble(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  index = 0
  while index < len_numbers:
    if index == 0:
      index += 1
    if numbers[index] > numbers[index-1]:
      index += 1
    else:
      numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
      index -= 1
  return numbers

if __name__ == "__main__":
  import random
  num = [random.randint(0, 1000) for i in range(1000)]
  print(bubble(num))