name= input ('What is your name ?')
birth_month =input('What month were you born in?')

#print greeting 
print(f'Hello,{name}! Great to meet you')

#Option 1. making a variable 
letters_in_name= len(name)
print(f'You have {letters_in_name} letters in your name') #display message 

if birth_month.lower()=='august':

    print('Happy birthday month')
else:
        print('Not your birthday month')


       
       
