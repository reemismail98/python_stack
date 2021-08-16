#Countdown 
arr=[]
def Countdown(x):
	for x in range(5,-1,-1):
		arr.append(x)
	print(arr)
Countdown(5)

#Print and Return
def print_and_return(arr):
	print(arr[0])
	return arr[1]
arr=[1,2]    
print(print_and_return(arr))

#First Plus Length 
def first_plus_length(arr):
    sum=arr[0]+len(arr)
    return sum
arr=[1,2,3,4,5]
print(first_plus_length(arr))

#Values Greater than Second 
def values_greater_than_second(arr):
	newarr=[]
	for x in range(len(arr)):
		if len(arr)<2:
			return false
		elif arr[x]>arr[1]:
			newarr.append(arr[x])
	print(len(newarr))       
	return newarr
arr=[5,2,3,2,1,4]
print(values_greater_than_second(arr))

# length_and_value(4,7)
def length_and_value(s,v):
    arr=[]
    for x in range(s):
        arr.append(v)
    return arr    
print(length_and_value(4,7))
