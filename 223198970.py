###############################
### EXERCISE 1 30 maks###
###############################

#Given String
s = 'fullstackslp'

#Using indexing to print out the following
#f
print(s[0])

#p
print(s[-1])

#stack
print(s[4:-3])

#slp
print(s[-3:])

print(s[11] + s[10] + s[9] + s[8] + s[7] + s[6] + s[5] + s[4] + s[3] +s[2] + s[1] + s[0])

####################
## Problem 2 - LISTS - 5 Marks##
#####################

#Given this nested list:
l =[3,7,[5,[1,4,'hello']]]

#Reasign 'hello' to 'goodbye'
l[2][1][2] = 'goodbye'
print(l)

#############
## Problem 3 - DICTIONARIES - 6 Marks##
#############

#Using keys and indexing, grap the 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'Hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hellooo']]}]}
print(d3['k1'][0]['nest_key'][1][0])

#################
## Problem 4 -SETS - 4 Marks##
################

#Use a set to find the unique values of the list below:
mylist =[1,1,1,1,1,2,2,2,2,3,3,3,3]

s = set(mylist)
print(s)

################
## Problem 5 - FORMATTING - 5 Marks##
###############

#You are given two variables
age = 45
name = 'Kyle'

print("Hello my dog's name is {} and he looks {} years old".format(name,age))