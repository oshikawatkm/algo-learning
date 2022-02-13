from typing import List

def merge_sort(numbers: List[int]) -> List[int]:
  if len(numbers)





if __name__ == '__main__':
  import random
  nums = [random.randint(1,1000) for _ in range(10)]
  print(merge_sort(nums))