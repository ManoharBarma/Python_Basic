print("hello Barma!!")

print(f"I am learning python!")

###################################
name = 'Barma'
age = 25

print(f"my name is {name} and iam {age}years old")

###################################
name_input = input('input your name : ')

print(f"Hello {name_input}")
###################################
num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))

print(f'sum of input numbers : {num1 + num2}')

###################################
age = int(input("Enter your age : "))

if age >= 18:
    print("eligible to vote")
else :
    gap = 18 - age
    print(f"you still need to wait {gap} more years to vote!!")

###################################
for i in range(1,11):
    print(i)

for j in range(2,21,2):
    print(j)
###################################
servers = ['web01', 'web02', 'db01']

for server in servers:
    print(server)
###################################
def greet(name):
    print(f'hello, {name}')

greet("manu")

def square(num:int):
    print(num * num)

square(77)
###################################
with open("notes.txt", "r+") as file:
    content = file.read()
    file.write(" -- writing something to same file using read+ method in open which goes to the end of read")
print(content)
###################################