


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:59:04 2023

@author: dasar
"""

print("if condtion flow....")
a = 100
#b=int(input("enter b"))
#c = a+b

if a < 20:
    print('its < 20')
elif a > 25:
    print('its > 20')
else:
    print('I dont know')
          
    
print("if condtion flow....")
a = 100
#b=int(input("enter b"))
#c = a+b

if a < 20:
    print('its < 20')
elif a > 25:
    print('its > 20')
else:
    print('I dont know')
          

print("for loop.... iterations")
for l in ('N', 'A', 'R'):
    print(l)

for j in ('NARSIMHA'):
    print(j)

name = "My Name is Narsimha Dasari"
for char in name:
    print(char)

city_pop = [('NewYork', 123444), ('Phily', 3343434), ('California', 999999)]
for city, pop in city_pop:
    print('city is: ', city, ' Population is: ', pop)
    print("\n")
    print('city is %s and its population is %s' %(city, pop))
    

print("*******for loop")
years = [2000, 2001,2002,2003, 2004]

for y in years:
    if y % 4 == 0:
        print(y, " is a leap year")
    else:
        print(y, " is not a leap year")
        
print("*******for loop 2")
names = [['narsimha', 'dasari'], ['smaran', 'dasari']]
for name in names:
    for n in name:
        print(n)
        

print("*******for loop 2")
city = ['NewYork', 'Philly', 'California'] 
pop = [ 3343434,  999999, 838383]

for c in city:
    for p in pop:
        print('city is %s and its population is %s' %(c, p))

print("Range & Tuple")

x = range(10)
print(tuple(x))

print("list ranges")
y = list(range(-5, +5))
print(y)

for i in range(5):
    print(i)
        
for z in range(0, 30, 5):
    print(z, end = " ")
    

print("****Appending/Adding to an empty list***********")
mylist = []

for i in range(0,20,4):
    if(i % 2 or i%4 == 0):
        mylist.append(i)
        
print(mylist)


x=5;
y=6;
x+y;

list_of_lists = [[1,1], [2,2], [3,3]]
int_list = [1,2,3]
print(list_of_lists[0])
print(int_list[0])


print("if condtion flow....")
a = int(input())
#b=int(input("enter b"))
#c = a+b

if a < 20:
    print('its < 20')
elif a > 25:
    print('its > 20')
else:
    print('I dont know')
    

print("****Appending/Adding to an empty list***********")
mylist = []

for i in range(0,20,4):
    if(i % 2 or i%4 == 0):
        mylist.append(i)
        
print(mylist)


print("******WHILE OR DO WHILE******")
i = 1
while i <= 10:
    print(i)
    i = i+ 1


j=1
total = 0
while j <= 50:
    total += 1
    j +=1
    print(f"computed sum upto 50 and total is {total}")
    
