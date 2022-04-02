# FIXME: WRONG ANSWER!
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870

def myFunc(data):
  return data[1][0]

T = int(input())
for i in range(T):
  tmp = input().split(' ')
  D = int(tmp[0]) # no. of delivery
  N = int(tmp[1]) # no. of order
  U = int(tmp[2]) # no. of leaves / order

  delivers = []
  expires = []
  for j in range(D):
    tmp2 = input().split(' ')
    M = int(tmp2[0]) # delivery time in minute since opening
    L = int(tmp2[1]) # no. of delivered leaves
    E = int(tmp2[2]) # store life in minute
    delivers.append([M, L, E])
    expires.append([M + E, L])
  
  orders = []
  tmp3 = input().split(' ')
  for data in tmp3:
    orders.append(int(data))

  timeline = list(map(lambda e: ['D', e], delivers)) + list(map(lambda e: ['E', e], expires)) + list(map(lambda e: ['O', [e]], orders))
  timeline.sort(key=myFunc)

  stock = 0
  orderCount = 0
  for event in timeline:
    if (event[0] == 'O'):
      if (stock >= U):
        orderCount += 1
        stock -= U
      else:
        break
    elif (event[0] == 'D'):
      stock += event[1][1]
    elif (event[0] == 'E'):
      stock = max(0, stock - event[1][1])

  print('Case #{0}: {1}'.format(i+1, orderCount))