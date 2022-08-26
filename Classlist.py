    
"""THIS PROGRAM IS ASKING USERS FOR CLASSES THEY ARE TAKING """
        
class_list= [] #classlist
class_names =input ('How many Classes will you be taking this semester? ')
class_list = class_names.split(' ') #addtothelist
        
for L in class_list:
  print(L) 