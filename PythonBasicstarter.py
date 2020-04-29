#section school #Basic #GFG

# problem 1
# a,b,c = input().split()
# print(a)
# print(b)
# print(c)


# problem 2
# a = int(input("total number of input"))

# for i in range(a):
#     b = int(input())
#     c = b*(b - 3) // 2
#     print(c)

# problem 3

# a = int(input("Enter the number of times"))
# b = []
# for i in range(a):
#     c = int(input("enter the side number"))
#     b.append(b)
# if (5 in b):
#     print("6");
# if (3 in b):
#     print("4");
# if (1 in b):
#     print("2");
# if (6 in b):
#     print("5");
# if (4 in b):
#     print("3");
# if (2 in b):
#     print("1");


#problem4


# cases = int(input("Enter the cases"))
# newarray = []
# secondmax = 0

# for i in range(cases):

#     a,b = map(int,input().split())
# c = b % a
# print(c)

#problem5

# c = int(input())
# for j in range(c):
#     s = input().strip()
#     count = 0
#     for i in s:
#         if i.isupper():
#             count = count + 1

# print(count)

#problem 6

# testcases = int(input())

# for i in range(testcases):
#     string1 = input()
#     a,b = input().split()
#     put = int(a)
#     put1 = int(b)
#     for i in string1[put:put1:1]:
#          print(i,end = "")

#perfect square OYO ROOMS

# testcase = int(input())
# c =[]
# newlist = []
# for i in range(testcase):
#     N = int(input())
#     for i in range(0,100):
#         c.append(i//2)
# for j in c:  
#     if (j not in newlist):
#         newlist.append(j)


# if (N % j == 0):
#     print("1")
# else:
#     print("0")

#section EASY problem 1  matrix //AMAZON

# testcase = int(input())

# string = ""
# for i in range(testcase):

#     N = int(input())
#     rows = input().split()
# a = N*N
# rows = rows[:a]      #limiting the list
# if (len(rows) > a):
#     print("overload")
    
# rows.sort()
# b = ' '.join(rows)
# print(b, end = "\n")

# problem 2

# testcase = int(input())
# a = 100
# d= []
# l = []


# for i in range(testcase):

#     values = int(input())
#     for j in range(1,a):
#         c = j*2
#         d.append(c)
#         if (j in d and j > values):
           
           
#            break

   
#     print(j)


#Printing the max element of array

# arr = [1,4,2,65,2]

# max = 0
# for i in range(len(arr)):
    
#     if arr[i] > max :
#         max = arr[i]
   
# print(max)

#FACTOR OR multiple problem
# c = []
# T = int(input())

# for i in range(T):
#     A,X = map(int,input().split())
#     ar = input().split()
#     # ar = ar[:A]     #limit in  the inputs in int

# for j in range(len(ar)):   
#     if(ar[j] % X == 0):
#         print(ar[j])



# myList = list(input().split())
# myInt = 10
# newList = [x / myInt for x in myList]
# print(newList)

# EXCEPTION # google white board problem

# a = [1,2,3,9]
# b = [1,2,4,4]

# for i in range(0,len(a)):
#     for j in range(1,len(a)):
#         if(a[i] == a[j]):
#             sum = a[i]+a[j]
#             if(sum == '8'):
#                 print("found")
           
# else:
#     print("combination not found")


# Geek for Geeks #Doctors clinic

# T = int(input())
# m = 0
# for i in range(T):
#     N,X = map(int,input().split())

# for j in range(1,N):
#     c = j
# w = (c * X )
# print(w)


# category EASY ARYA STARK problem
# T = int(input())
# for m in range(T):
#     X = int(input())
# c = []
# d = []
# qo = 1      #quotient
# i = 0   
# sum = 0
# count = 0
# q = X // 2
# while  q >= qo:
#     c.append(q)
#     q = q // 2
# c.append(X) 
# c.sort() 
# c.reverse()  
# for i in c:   
#     remainder = (i % 2)
#     d.append(remainder)
# for j in d:
#     if (j == 1):
#      count = count + 1
# print(count)

#Karatsuba Algorithm

# str1 = "1100"
# # d = []
# j= 0

# for i in str1:
#     c = ' '.join([str1[i:i+1] for i in range(0,len(str1))])

# print(c)
# e = list(c.split(" "))

# j = e.remove('')

# print(j)

# a = [1,1,1,1]
# b = ['1','1','1','1']
# d = array("i",b)

# for j in b:
#     print(j)


# Reverse coding
a = 10
b = 10
c = []
d = []
e = []

for i in range(a):
    c.append(i)
for j in c:
    k = d[] + j 
      
print(k)




