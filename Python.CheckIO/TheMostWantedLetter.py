#You are given a text, which contains different english letters and punctuation symbols. 
#You should find the most frequent letter in the text. The letter returned must be in lower case.
#While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". 
#Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

#If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
#For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

#Input: A text for analysis as a string.

#Output: The most frequent letter in lower case as a string.

#Precondition:
#A text contains only ASCII symbols.
#0 < len(text) =< 105



#-----------------------------------------solution by wangwust------------------------------------------------------------------------------
#def checkio(text):
#    text = text.lower()

#    numDic = dict()
#    for s in text:
#        if s.isalpha() == False:
#            continue

#        #for python 2.7
#        if numDic.has_key(s):
#        #for python 3.x
#        #if numDic.__contains__(s):
#            numDic[s] +=1
#        else:
#            numDic[s] = 1

#    list = sort_by_value(numDic)
#    letter = get_letter(list)

#    return letter

#def sort_by_value(dic): 
#    #for python 2.7
#    return [ v for v in sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)] 

#    #for python 3.x
#    #return [ v for v in sorted(dic.items(), key=lambda d:d[1], reverse = True)] 

#def get_letter(list):
#    max = list[0][1]
#    letterList = []

#    for t in list:
#        if t[1] == max:
#            letterList.append(t[0])
    
#    letterList.sort()
#    return letterList[0]

#------------------------------------------other solution 1-----------------------------------------------------------------------------------
#import string

#def checkio(text):
#    """
#    We iterate through latyn alphabet and count each letter in the text.
#    Then 'max' selects the most frequent letter.
#    For the case when we have several equal letter,
#    'max' selects the first from they.
#    """

#    #string.count()用于统计每个字符在字符串中出现的次数
#    #max函数第一个参数是个迭代器，第二个参数是个函数，max函数会把迭代器中每个元素带入到函数中运行，然后将返回结果传给key，再以key为标准进行大小比较
#    text = text.lower()
#    return max(string.ascii_lowercase, key=text.count)

#------------------------------------------other solution 2-----------------------------------------------------------------------------------
from collections import Counter

def checkio(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")