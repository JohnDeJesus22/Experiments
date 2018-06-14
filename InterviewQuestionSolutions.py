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

#create a function that takes a natural number n and adds all the numbers of n
#and below up to 1 (own solution)
    
def cum_sum(n):
    
    if n<=0:
        return
    elif n==1:
        return 1
    else:
        return n + cum_sum(n-1)
    
cum_sum(4)
cum_sum(10)

##############################################################################

#function that sums all digits of a number (own solution)

def digit_sum(n):
    
    if len(str(n))==1:
        return n
    else:
        d= n%10
        return d+ digit_sum(n//10)
    
digit_sum(4321)
digit_sum(678)

#############################################################################

#reversing a string using recursion (own solution)

def reverse(s):
    
    if len(s)==1:
        return s
    
    else:
        return s[-1]+reverse(s[:-1])

reverse('hello')

#code for testing provided by instructor
from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print('Passed All Tests')
        
test=TestReverse()
test.test_rev(reverse)

##############################################################################

#given a string, output a list of all permutations (needed some help)
#exceeds limit
def permute(s):
    
    permutations = []
    
    if len(s)==1:
        permutations=[s]
    
    else:
        for i, letter in enumerate(s):
                
            for perm in permute(s[:1]+s[i+1:]):
                    
                permutations+=[letter+perm]
    
    
    return permutations

##############################################################################
    
#fibonaci sequence with recursion (own solution)

def fib_rec(n):
    
    if n == 0 or n==1:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
#fibonaci sequence with iter(from course)
        
def fib_iter(n):
    
    a,b=0,1
    
    for i in range(n):
        a,b=b,a+b

    return a

#fibonaci sequence with memiozation (from course)
n=10
cache=[None]*(n+1)
def fib_dyn(n):
    
    #base case
    if n == 0 or n==1:
        return 1
    
    #check cache
    if cache[n]!= None:
        return cache[n]
    
    #keep cache
    cache[n]=fib_dyn(n-1)+fib_dyn(n-2)
    
    return cache[n]
    
    