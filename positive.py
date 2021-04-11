#Program to print all the positive nos. in the range
list=[]
n=int(input('Enter the size : '))
for i in range (n):
    list.append(int(input('Enter the no.: ')))
elist=[]
for i in range(n):
    if list[i]>=0:
        elist.append(list[i])
print(elist)
