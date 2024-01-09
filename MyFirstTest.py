x= True
y = False
print('x and y is:', x and y)
print('x and y is:', x or y)
print('x and y is:', not x)


z = 'Narsimha '
print(z)
print('muliple times', z * 2)
print('lenght is:', len(z))



print('Assigning Values to Vairbales')
x = y = z = 'Narsimha'

a,b,c = 'Narsimha ', [1,2,3], True
print('x is: ', x,'y is: ', y,'z is: ', z)
print('a is: ', a,'b is: ', b,'c is: ', c)


print('Updating variables')
a1 = 10
b1 = 20
c1 = 30
total = a1+b1+c1
print('Total is: ', total)
a1 += a1 + 1
total = a1+b1+c1
print('Total is: ', total)

print('****Multiplying time')
d1 = 10
d1 *= 5
print(d1)
print('**********')



print('******DATA TYPES in Python******')
a = True
b = 5
c = [1,2,3]
d = 'Narsimha'

print('type of a: ', type(a),'type of b: ', type(b),'type of c: ', type(c),'type of d: ', type(d) ,'binary should start with 0b: ', 0b111)



print('Questoin and Answer, Inputs')
question = "what did you eat for Dinner?"
answer = input()
print('I had ', answer)



print('*******Quotes vs double Quotes')
print("i'm learning python")
print('double quote vs single quote "Hope this will work!!!"')
print('i\'m learning python')
print("double quote \"vs\" single quote Hope this will work!!!")
print("print a work in \nnext line")



print("**********printing a formatted string")
name = "Narsimha"
print(f'My Name is {name}')


print(13//5)
print("Hellow"+"world")
print("Hellow"*3)
n = 6-4
m=2
print(n,m)
