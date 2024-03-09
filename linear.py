def search(arr,n,target):
    for j in range(n):
        if(arr[i]==target):
            flag=1
        else :
            flag=0
    return flag


a=[]
n=int(input("enter how many elements"))
for i in range(n):
    o=int(input(f"enter the {i} element"))
    a.append(o)
target=int(input("enter the target element"))
if(search(a,n,target)):
    print(f" { target} is found ")
else :
    print("not found the numbr")