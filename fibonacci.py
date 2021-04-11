#Print the fibonacci series
Fn=0
c=1
n=int(input('Enter the no.: '))
print('The fibonacci series : ')
for i in range(n):
    print(Fn, end=' ,')
    c=Fn+c
    Fn=c-Fn