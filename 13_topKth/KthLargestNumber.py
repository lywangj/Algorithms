# Kth Largest Number in a Stream
from heapq import *

class KthLargestNumberInStream:
  def __init__(self, nums, k):
    # TODO: Write your code here
    self.minHeap = []
    for num in nums:
      heappush(self.minHeap, num)
      if len(self.minHeap) > k:
        heappop(self.minHeap)
    self.k = k

  def add(self, num):
    # TODO: Write your code here
    heappush(self.minHeap, num)
    heappop(self.minHeap)
    return self.minHeap[0]

def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))  # 5
  print("4th largest number is: " + str(kthLargestNumber.add(13)))  # 6
  print("4th largest number is: " + str(kthLargestNumber.add(4)))  # 6


main()
