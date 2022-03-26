# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2
# Same size = Same amount of treats

# Example
# sizes = [10, 20, 10, 25]
# treats = [1, 2, 1, 3]

# Input
# Get number of testcases (T)
# Get number of pets in next day (N)
# Get S1, S2, ..., Sn size of each pet (S)

# Output
# Case #x: y >> x = number of test case, y = minimum number of treats

from typing import OrderedDict

T = int(input())
for i in range(T):
  N = int(input())
  S = input().split(' ')
  
  data = {}
  for j in S:
    key = int(j)
    if data.get(key):
      data[key] = data[key] + 1
    else:
      data[key] = 1

  totalCount = 0
  treatCount = 1
  sortedKeys = sorted(data)
  for k in sortedKeys:
    totalCount += treatCount * data[k]
    treatCount += 1
  
  print('Case #{0}: {1}'.format(i+1, totalCount))