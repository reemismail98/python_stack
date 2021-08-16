#Biggie Size
def biggie_size(arr):
    for x in range(len(arr)):
        if arr[x]>0:
            arr[x]="big"
    return arr        
arr=[-1, 3, 5, -5]
print(biggie_size(arr))

#Count Positives
def count_positives(arr):
    count=0
    for x in arr:
        if x>0:
            count=count+1
    arr[-1]=count
    return arr        
arr=[-1,1,1,1]
print (count_positives(arr))  

#Sum Total
def sum_total(arr):
    sum=0
    for x in range(len(arr)):
        sum=sum+arr[x]
    return sum   
arr=[1,2,3,4]     
print (sum_total(arr))  

#Average
def average(arr):
    sum=0
    for x in range(len(arr)):
        sum+=arr[x]
    avg=sum/len(arr)    
    return avg    
arr=[1,2,3,4]     
print(average(arr))     

#Length 
def length(arr):
    if len(arr)==0:
        return False
    else:
        return len(arr)        
arr=[37,2,1,-9]
print(length(arr))

#Minimum
def Min(arr):
	if len(arr)==0:
		return False
	else:
		min=arr[0]
		for x in range(1,len(arr),1):
			if arr[x]<min:
				min=arr[x]
	return min
arr=[37,2,1,-9]
print(Min(arr)) 

#Maximum 
def Max(arr):
	if len(arr)==0:
		return False
	else:
		max=arr[0]
		for x in range(1,len(arr),1):
			if arr[x]>max:
				max=arr[x]
	return max
arr=[37,2,1,-9]
print(Max(arr))

#Ultimate Analysis
def ultimate_analysis(arr,arr2):
	sum=0
	min=0
	max=0
	newarr=[]
	dictOfWords=0    
	for x in range(len(arr)):
		sum+=arr[x]
		avg=sum/len(arr)
		if arr[x]<min:
			min=arr[x]
		if arr[x]>max:
			max=arr[x]
	newarr.append(sum)
	newarr.append(avg)
	newarr.append(min)
	newarr.append(max)
	newarr.append(len(arr))
	zipbObj = zip(arr2, newarr)
	dictOfWords = dict(zipbObj)
	return dictOfWords
arr = [37,2,1,-9,7]
arr2 = ["sumTotal", "average", "minimum", "maximum" ,"length" ]
print(ultimate_analysis(arr,arr2))

def ultimate_analysis1(arr):
    dictionary = {
        "sumTotal": sum(arr),
        "average": sum(arr) / len(arr),
        "minimum": min(arr),
        "maximum": max(arr),
        "length": len(arr)
    }
    return dictionary

arr = [37,2,1,-9]
print(ultimate_analysis1(arr))
print("_" * 30)

def ultimate_analysis2(arr):
    dictionary = dict()  #  dictionary = {}
    sum = 0
    count = 0
    min = max = arr[0]
    for value in arr:
        sum += value
        count += 1
        if min > value:
            min = value
        if max < value:
            max = value
    dictionary["sumTotal"] = sum
    dictionary["average"] = sum / count
    dictionary["minimum"] = min
    dictionary["maximum"] = max
    dictionary["length"] = count
    return dictionary

print("Second solution:")
arr = [37,2,1,-9]
print(ultimate_analysis2(arr))
print("_" * 30)



#Reverse List
def reverse_list():
	arr=[37,2,1,-9][::-1]
	return arr
print(reverse_list())     
