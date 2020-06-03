#leetcode easy list stock profit finder
# prices = list(map(int,input().strip().split()))

# sub = 0
# c = []
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#             if (prices[j]>prices[i]):
#                 sub = prices[j] - prices[i]
#                 print(sub)
#                 break
#             else:
                
#                 break   


# HACKERRANK PROBLEM # find the Runner up score


# T = int(input())

# N = list(map(int,input().split()))

# c = []
# d = []
# N.sort()

# for i in N:
#     if i not in c:
#         c.append(int(i))


# for l in c:
#     if l not in d:
#         d.append(l)

# for j in range(len(d)) :
#     for k in range(j + 1, len(d)):

#         if (d[k] > d[j]):

#             l = d[k-1]

# print(l)
