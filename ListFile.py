# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:15:53 2023

@author: dasar
"""


print("**********BREAK****************")

listN = [5,10,14,12,40,99]

for i in listN:
    print(i)
    if(i==40):
        break
    



print("***************CONTINUE*******************")
cities = ['philly','NewYork','Jersey','Dallas','Austin']

for city in cities:
    #print(city)
    if city == "Dallas":
        continue
    if city == "Jersey":
        break
    
print(city)



y = [x * x for x in range(10) if x % 2 ==0]
print(y)


shapes = ['square','rectangle','triangle']
colors = ['blue','yellow','red']

combined = [(shapes, colors) for shape in shapes for color in colors]
print(combined)



odd_even = [(i, "Even") if i % 2==0 else (i, "Odd") for i in range(20)]
print(odd_even)


print("*************ccnver to upper case***************")
list_words = ['hello','Hi','good','Night']

upper_words = (word.upper() for word in list_words)
for word in upper_words:
    print(word)
    
print("*************split words***************")    
split_word = "Hi how are you doing?"
print(split_word.split())

print("*************print unique words in a string***************")
uniq_word = {w for w in split_word}
uniq_word


