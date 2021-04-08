file_name=input("enter the name ")
leng=int(len(file_name))
if (leng-(file_name.rfind('py'))==2):
    print("File extension is python")
else:
    print("Other file extension found")