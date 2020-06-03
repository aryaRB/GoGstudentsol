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

# total = 0
# power = 0
# sum1 = 0
# j = []
# v =0
# o = []
# d = []

# sum = 0
# T = int(input())
# for z in range(T):
#     str1,str2 = input().split()
# k = len(str1)

# for i in str1:
#     c = ' '.join([str1[i:i+1] for i in range(0,len(str1))])
# for i in str2:
#     f = ' '.join([str1[i:i+1] for i in range(0,len(str1))])

# e = list(c.split(" "))
# for l in e:
#     j.append(int(l))

# h = list(f.split(" "))
# for y in h:
#     o.append(int(y))

# for u in j:
#     if (u == 1):
#         k = k - 1 
#         v = 2 ** k
#         sum = sum + v
# for r in o:
#     if (r == 1):
#         power = power - 1 
#         total = 2 ** power
#         sum1 = sum1 + total
# multiply = sum * sum1

# print(multiply)


# Reverse coding
# v = []
# l = []
# sum = 0
# list1 = 1000
# for o in range(0,list1):
#     l.append(o)

# for i in range(0,len(l)):
#        sum = sum + i
#        v.append(sum)

# T = int(input())
# for k in range(T):
#     n,m = map(int,input().split())


# if (l.index(n) == v.index(m)):
#     print("1")

#mycat exam sample

# T = int(input())
# people = 10;
# for i in range(T):
#     N= int(input()) 
#     dived = people / N
#     if (dived == 2.0 or dived == 0.5):
#        print("yes")
#     else:
#        print("no")




#remove duplicates in a list without creating a new list
# list1 = [1,2,3,3,4,6,8]

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
        
#         if (list1[i] == list1[j]):
#             del list1[i]
#             print(list1)
#             break
#         else:
#             break


#PROBLEMS USING DICTIONARY

# a = {
#        "number" : 10,
#        2 : 20,
#        3 : "cat",
#        4 : 40,
#        5 : "dog"
# }

# if ("number" in a):
#     print("present")

# b = a.sort()
# print(b)

# triangular number EASY

# sum = 0
# a = 10**7
# c = []

# T = int(input())
# for i in range(T):
#     N = int(input())

# for j in range(a):
#     sum = sum + j
#     c.append(sum)
# if (N in c):
#     print("1")
# else:
#     print("0")



# using for loop to reversse a linked list
# T = int(input())
# a = [1,2,5,6]
# c = []
# d = []
# for i in a:
#     c.append(int(i))
# print(c)
# for j in range(len(c)):
#     a = c.pop()
#     d.append(a)
#     print(d)





# Nested Lists

# T = int(input())

# if (T >= 2 and T <=5 ):
#     for i in range(T):
#         N = input()
#         G  = float(input())



# Anshuman's Favourite Number   GOG

# T = int(input())

# d = []

# for i in range(T):
#     N = int(input())

    
#     for j in range(N):
#         c = 5 * j
        
#         d.append(c)
        
        
# if (N in d):
#     print("YES")
            
# else:
#     print("NO")

































































































































































# **** LINKED LIST *******

# creating a node

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # create the linkedlist

# class LinkedList:
#     def __init__(self):
        
#         self.head = None


# if __name__ == '__main__':
#     # assining the value of LinkedList in llist
#     llist = LinkedList()

#     # adding the node to the LinkedList

#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)

#     # connecting the linkedlist
    
#     llist.head.next = third
#     # second.next = third

#     while llist.head != None:
#         print(llist.head.data)
#         llist.head = llist.head.next

# traversing a linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     # adding a new Node before the head node

#     def __init__(self , new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#     #inserting a new node after a node
#     def __init__(self , prev_node ,new_datas):

#         if prev_node is None:
#             print("prev node not present")
#             return

#         new_node = Node(new_datas)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
    
#     #inserting a node at the end
#     def __init__(self,new_data):
#        newnode = Node(new_data)

#        if (self.head == None):

#            self.head = Node
#            return
           
#            last = self.head
#            while (last.next):
#             last = la
           










         
# if __name__ == '__main__':

#     llist = LinkedList()











    
    
    







