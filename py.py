# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:18:40 2024

@author: m.hawi
"""
" What is 7 to the power of 4?"
 
print("7 to the power of 4 equals to =" , 7**4)

" Split this string: "

s = "Hi there Sam!"

s.split(',')

"Use .format() to print the following string: "
"The diameter of Earth is 12742 kilometers."

planet = "Earth"
diameter = 12742

print(f"The {diameter} of {planet} is 12742 kilometers.")


' Given this nested list, use indexing to grab the word "hello" '

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

lst[3][-3][-1]


'Given this nested dictionary grab the word "hello"'
 
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]

 
"Create a function that grabs the email website domain from a string in the form: "


def domainGet(email): 
   return email.split('@')[1]


domainGet("user@domain.com")



"""Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge
 cases like a punctuation being attached to the word dog, but do account for capitalization."""

def findDog(Input):
    print(Input.lower())
    if "dog" in Input :
      return True

findDog('Is there a dog here?')



" Create a function that counts the number of times the word 'dog' occurs in a string. Again ignore edge cases"

def countDog(Input):
    print(Input.lower())
    return Input.count("dog")

countDog('This dog runs faster than the other dog dude!')



"Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:"

seq = ['soup','dog','salad','cat','great']

start_letter = 's'

with_s = list(filter(lambda x: x.startswith(start_letter), seq))

print("The list with prefix s : " + str(with_s))



"""You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
 If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
 Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.""" 



def caught_speeding(speed, is_birthday):
    speed_limit = speed
    if is_birthday == True:
        speed = speed-5
    else:
        speed = speed_limit       
    if speed <= 60:
        print("No Ticket")
    elif speed>61 and speed<80:
        print ("Small Ticket")
    elif speed>=81:
        print ("Big Ticket")
   
pass



caught_speeding(81,True)
caught_speeding(81,False)

