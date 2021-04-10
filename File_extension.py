str=input("Enter the string ")
c=int(str.count('.'))
str=str.split('.')
if str[1]=='py' and c==1:
    print('The file extension is python')
else:
    print('The file extension is either incorrect or other')
