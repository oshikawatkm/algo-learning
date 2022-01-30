from typing import List


def gnome_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    if numbers[i] > numbers[i+1]:
      numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
      i = i - 1

  return numbers


if __name__ == "__main__":
  import random
  nums = [random.randint(0, 1000) for i in range(10)]
  print(gnome_sort(nums))