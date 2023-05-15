num1 = 42 #variable declaration,intialize integer
num2 = 2.3 #variable declaration,intialize floot
boolean = True #variable declaration,intialize boolean
string = 'Hello World' #variable declaration,intialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration,intialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration,intialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration,intialize tuples
print(type(fruit))#log of type of variable fruit
print(pizza_toppings[1])#log of item in list'pizza_topping' with index 1
pizza_toppings.append('Mushrooms')#adding value to list'pizza_topping'
print(person['name'])# log of value in dictionary'person' with the key 'name'
person['name'] = 'George'#change the value of item in disctionary with the key
person['eye_color'] = 'blue'#add new item key'eye_color' and value'blue'
print(fruit[2])#log of item with index'2' in tuples'fruit'

if num1 > 45: #conditonal if
    print("It's greater")#log statement
else:#confditional else
    print("It's lower")#log statement

if len(string) < 5:#conditional if
    print("It's a short word!")#log statement
elif len(string) > 15:#conditional else if
    print("It's a long word!")#log statement
else:#confditional else
    print("Just right!")#log statement

for x in range(5):#confditional for loop
    print(x)#log statement
for x in range(2,5):#confditional for loop
    print(x)#log statement
for x in range(2,10,3):#confditional for loop
    print(x)#log statement
x = 0#variable declaration,intialize integer
while(x < 5):##confditional while loop
    print(x)#log statement
    x += 1#changing the variable value

pizza_toppings.pop()#delete the last value of list
pizza_toppings.pop(1)#delete value of list with index 1

print(person)#log statement
person.pop('eye_color')#delete item with key eye_color 
print(person)#log statement

for topping in pizza_toppings:#confditional for loop
    if topping == 'Pepperoni':#conditional if
        continue
    print('After 1st if statement')#log statement
    if topping == 'Olives':#conditional if
        break #stop running the code

def print_hello_ten_times():#function
    for num in range(10):#for loop
        print('Hello')#log statement

print_hello_ten_times()#log statement

def print_hello_x_times(x):#function
    for num in range(x):#for loop
        print('Hello')#log statement

print_hello_x_times(4)#run the function

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):#for loop
        print('Hello')#log statement

print_hello_x_or_ten_times()#run the function
print_hello_x_or_ten_times(4)#run the function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)