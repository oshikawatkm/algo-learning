from typing import List

def partition(numbers: List[int], high: int, low: int) -> int:
  i -= 1
  pivot = numbers[high]
  for j in range(low, high):
    if number[j] <= pivot:
      i += 1
      numbers[i], numbers[j] = numbers[j], numbers[i]
  numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
  return i

def quick_sort(numbers: List[int]) -> List[int]:
  def _quick_sort(number, low, high) -> None:
    if low < high:
      partition_index = partition()
      _quick_sort(numbers, low, partition_index-1)
      _quick_sort(numbers, partition_index+1, high)

  _quick_sort(numbers, 0, len(numbers)-1)
  return numbers

if __name__ == "__main__":
  import random
  nums = [random.randint(0,1000) for i in range(10)]
  print(quick_sort(nums)) 