# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2
# Find the first order in the list of valid strings

# The first letter of the string must be A
# Each letter in the i-th block must be
# - Later in the alphabet than its preceding letter in the string if i is odd (ASC for odd)
# - And earlier in the alphabet than its preceding letter if i is even (DESC for even)
# For the first letter of a block, its preceding letter exists, even though it is not in the block

# Example
# Has 2 blocks L1 = 2, L2 = 3
# String must 1 + L1 + L2 = 1 + 2 + 3 = 6 letters, (1 = initial A)
# Not valid string: XYZYBA, AZYCBA and AYZYBB
# Valid string: AYZYBA, ABDCBA

# Input
# Get number of test case (T)
# Get the number of blocks in test case (N)
# Get L1, L2, ..., Ln the number of letter each block must have (L)

# Output
# Case #x: y >> x = number of test case, y = the first valid string in alphabetical order

T = int(input())
for i in range(T):
  N = int(input())
  L = input().split(' ')
  L = [1] + L

  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  letterMap = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
  }
  
  data = []
  for j in range(N + 1):
    length = int(L[j])
    if (j == 0):
      data.append(['A'])
    else:
      tmp = []
      if (j % 2 == 0):
        index = length - 1
        for k in range(length):
          tmp.append(letters[index])
          index -= 1
        
        lastBlock = data[j - 1]
        if (letterMap[lastBlock[len(lastBlock) - 1]] <= length - 1):
          lastBlock[len(lastBlock) - 1] = letters[length]
      else:
        index = 0
        lastBlock = data[j - 1]
        if (letterMap[lastBlock[len(lastBlock) - 1]] >= index):
          index += 1

        for k in range(length):
          tmp.append(letters[index])
          index += 1
      data.append(tmp)

  ans = ''
  for p in data:
    str = ''.join(p)
    ans += str

  print('Case #{0}: {1}'.format(i+1, ans))
