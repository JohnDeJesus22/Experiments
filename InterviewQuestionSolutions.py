#Interview Question solutions from question by Jose Portilla's python 
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