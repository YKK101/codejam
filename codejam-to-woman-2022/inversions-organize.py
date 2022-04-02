# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870

T = int(input())
for i in range(T):
  N = int(input())

  totalTopLeft = 0
  totalTopRight = 0
  for j in range(N):
    row = input()
    for l in range(len(row)):
      if (row[l] == 'I' and l < N):
        totalTopLeft += 1
      elif (row[l] == 'I'):
        totalTopRight += 1
  
  totalBottomLeft = 0
  totalBottomRight = 0
  for k in range(N):
    row = input()
    for m in range(len(row)):
      if (row[m] == 'I' and m < N):
        totalBottomLeft += 1
      elif (row[m] == 'I'):
        totalBottomRight += 1

  a = abs(totalTopLeft - totalBottomRight)
  b = abs(totalTopRight - totalBottomLeft)

  print('Case #{0}: {1}'.format(i+1, a + b))