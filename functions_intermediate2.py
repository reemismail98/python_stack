#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
students[0]['last_name']="Bryant"
sports_directory['soccer'][0]="Andres"
z[0]['y']=30

#Iterate Through a List of Dictionaries
def iterateDictionary(students):
	for dic in students:
		for val,cal in dic.items():
			print(f'{val} - {cal}')
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(first_name, students):
	for x in range(0,len(first_name)):
		print(first_name[x])
    
def iterateDictionary2(last_name, students):
	for x in range(0,len(last_name)):
		print(last_name[x])
        
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
first_name=['Michael','John','Mark','KB']
last_name=['Jordan','Rosales','Guillen','Tonel']
iterateDictionary2(first_name, students)
iterateDictionary2(last_name, students)

#Iterate Through a Dictionary with List Values
def printInfo(dojo):
	for key, values in dojo.items():
		print(len(values), key)
		if(isinstance(values, list)):
			for value in values:
				print(value)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

