def most_frequent(name):
    d={}
    name=name.lower()
    for i in range(26):
            y=name.count(chr(i+97))
            d[i]=[chr(i+97),y]
    t=[]
    for i in range(26):
            for j in range(i,26):
                if( d[i][1]<d[j][1]):
                    t=d[i]
                    d[i]=d[j]
                    d[j]=t
            if(d[i][1]>0):
                print(d[i][0], ' = ',d[i][1])
n=input("Please enter a string : ")
most_frequent(n)