#############################
###Problem 1####
########################
this_list =([0,2, 3,4,1, 2,3])
def list_check(nums):
    for i in range(len(this_list)-1):
        if this_list[i] == 0 and this_list[i+1] == 2 and this_list[i+2] == 3:
           return print(True)

    return print(False)

list_check(this_list)

#####################
### ---Problem 2 --##
#####################
word = "Heeololeo"
def string_bits(str):
    return  str[::2]

print(string_bits(word))




#####################
### ---Problem 3 --##
#####################
def end_other(a,b):
    if a[-3:] == b:
        return print(True)
    else:
        return print(False)

end_other("Hiabb","abc")

#####################
### ---Problem 4 --##
#####################
word='biig'

def double_char(str):
    new_name = ""
    for i in str:
        new_name += i * 2

    return new_name

print(double_char(word))

#####################
### ---Problem 5 --##
#####################

not_teen = {13,14,17,18,19}
def no_teen_sum(a,b,c):
    list_ages = (a,b,c)
    sum = 0
    for i in list_ages:
        if i not in not_teen:
            sum += i
    return sum
print(no_teen_sum(2,3,15))

a =13
def fix_teen(n):
    if n not in not_teen:
        return print(n)
    else:
       return  print(0)

fix_teen(a)

#####################
### ---Problem 6 --##
#####################
nums_list = ([2,7,6])

def count_evens(nums):
    count = 0
    for i in nums_list:
        if i % 2 == 0:
            count = count + 1
    return count


print("Evens is equal to: {}".format(count_evens(nums_list)))