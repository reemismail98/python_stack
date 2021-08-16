def skyline(arr):
    min=0
    list=[]
    for x in range(0,len(arr)):
        if arr[x] > min:
            list.append(arr[x])
            min=arr[x] 
    return list        
arr=[1,-1,7,3]
x=skyline(arr)
print(x) 