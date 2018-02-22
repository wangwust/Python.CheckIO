#You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. 
#To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
#When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

#non-unique-elements

#Input: A list of integers.

#Output: The list of integers.


#How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. 
#The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

#You can find out more about Python arrays in one of our articles featuring lists, tuples, array.array and numpy.array.

#Precondition:
#0 < len(data) < 1000

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


#-----------------------------------------solution by wangwust------------------------------------------------------------------------------
#from collections import Counter

#def checkio(data):
#    #isinstance() 函数来判断一个对象是否是一个已知的类型
#    count = Counter([x for x in data if isinstance(x, int)])
#    for (k, v) in count.items():
#        if v == 1:
#            data.remove(k)
#    return data

#------------------------------------------other solution 1-----------------------------------------------------------------------------------
#def checkio(data):
#       return [i for i in data if isinstance(i, int) and data.count(i) > 1]

#------------------------------------------other solution 2-----------------------------------------------------------------------------------
def checkio(data):
    for item in data:
        if data.count(item) > 1:
            yield item

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    assert list(checkio([-10,10,0])) == [], "5th example" 
    #assert list(checkio([-10,10,0, 'fdsa', 'fdsa'])) == [], "6th example"
    print("It is all good. Let's check it now")


