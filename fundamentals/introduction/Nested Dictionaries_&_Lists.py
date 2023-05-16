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
#1
x[1][0]=15
students[0]["last_name"]="Bryant"
sports_directory["soccer"][0]="Andres"
z[0]['y']=30
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#2
def iterateDictionary(some_list):
    for dictionary in some_list:
        for dicta in dictionary:
            print(dicta + "-"+ dictionary[dicta])
iterateDictionary(students)

#3
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students) 
# Miou was here <3

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,value in some_dict.items():
        print(str(len(value))+" "+key.upper())
        for item in value:
            print(item)
printInfo(dojo)