#Interview Question solutions from questions by Jose Portilla's python 
#data structures, algorithms and interviews course.

#get missing number from a given array and the array without the missing value
#(needed some help)
def find_missing(arr1,arr2):
    #edge case
    if len(arr1)-len(arr2)!=1:
        return
    
    arr1.sort()
    arr2.sort()
    
    for num1,num2 in zip(arr1,arr2):
        if num1 !=num2:
            return num1
            
arr1=[1,2,3,4]
arr2=[1,3,4]

find_missing(arr1,arr2)
###############################################################################

#get largest continuous sum from an array of numbers (needed some help)
def largest_sum(arr):
    
    if len(arr)==0:
        return None
    
    max_sum=current_sum = arr[0]
    
    
    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(max_sum,current_sum)
        
    return max_sum

arr=[4,-3,7,-2]

largest_sum(arr)

##############################################################################

#reversing the words of a phrase (own solution)
def phrase_reverse(string):
    
    string=string.strip()
    string=string.split()
    new_string=[]
    for i in range(len(string)):
        new_string.append(string[-1-i])
    
    new_string=' '.join(new_string)
    return new_string

string='testing our the word reversal'

phrase_reverse(string)

#alternate one line solution but cheating using python features
def phrase_rev(string):
    return ' '.join(reversed(string.split()))

##############################################################################

#create a compressed string from a string of repeated letters (own solution)
    
def compressed(string):
    
    #edge case
    if len(string)==0:
        return
    
    count={}
    
    for letter in string:
        if letter not in count:
            count[letter]=1
        else:
            count[letter]+=1
    
    compressed_string=[]
    
    for letter in count:
        compressed_string.append(letter)
        compressed_string.append(str(count[letter]))
        
    return ''.join(compressed_string)

string='AAAaaDDDDD'

compressed(string)

##############################################################################

#given a string: If all characters are unique return true, else return false
#(own solution)
def unique_check(string):
    
    #edge cases
    if len(string)==0:
        return ''
    
    if len(string)==1:
        return True
    
    count ={}
    
    for letter in string:
        if letter not in count:
            count[letter]=1
        else:
            count[letter]+=1
    
    for letter in count:
        if count[letter]!=1:
            return False
    
    return True

string='abcde'
stringTwo='aabcdeee'

unique_check(string)
unique_check(stringTwo)

#instructor solutions

def unique_check2(string):
    return len(set(string))==len(string)

def unique_check3(string):
    
    chars=set()
    
    for letter in string:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    
    return True
##############################################################################
