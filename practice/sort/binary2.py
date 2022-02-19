from typing import List, NewType

IndexNum = NewType('IndexNum', int)


def binary_search(numbers: List[int], value: int) -> int:
  def _binary_search(numbers: List[int], value: int, left: IndexNum, right: IndexNum) -> IndexNum:
    if left > right:
      return -1
    
    mid = (left + right) // 2
    if numbers[mid] == value:
      return mid
    elif numbers[mid] < value:
      return _binary_search(numbers, value, mid + 1, right)
    else:
      return _binary_search(numbers, value, 0, len(numbers)-1)

  return _binary_search(numbers, value, 0, len(numbers)-1)

if __name__ == "__main__":
  nums = [2,14,16,27,31,37,45,62,68,88,93]
  print(binary_search(nums, 89))