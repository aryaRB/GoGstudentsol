#school #Basic #GFG

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


cases = int(input("Enter the cases"))
newarray = []
secondmax = 0

for i in range(cases):

    a,b = map(int,input().split())
# not completed
    for j in range(0,b):
        product = j * b
        newarray.append(product)
        if (product >= a):
            max = product
            if (max <= a):
           
                c = newarray.index(max) - 1

           
valueofc =  newarray[c]

remainder = (a - valueofc)

            
print(remainder)








