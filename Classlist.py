    
"""THIS PROGRAM IS ASKING USERS FOR CLASSES THEY ARE TAKING """
        
import string
from tkinter import Y


class_list= [] #classlist
class_num =int(input ('How many Classes will you be taking this semester? '))



for X in range (class_num)     :
  print (f'Class- {X+1};')  
  class_name=string(input())
  classes.append(class_name)

print('Your class this semester are:')
for Y in classes:
 print(Y)