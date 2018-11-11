'''Author : Riddhi Gohil
   Date : 11/11/2018
'''

import os,sys
import numpy as np
import matplotlib.pyplot as plt

#count word by directory
def wordcount(path,result,keyword):
    for file in os.listdir(path):
        temp_path = os.path.join(path,file)
        if (os.path.isfile(temp_path) and file.endswith('.txt')):
            file = open(temp_path, "r", encoding="utf-8-sig")
            # increment based on finding
            temp = file.read().count(keyword)
            if(result.get(path) != None) :
                temp += result.get(path)
                result.update({path : temp})
            else:
                result.update({path: temp})

#put all directory in stack
def stack_dir(path,stack):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if (os.path.isdir(file_path)):
            stack.append(file_path)

result = {}
stack = []

#Take argument from command line
root_dir = sys.argv[1]
keyword = sys.argv[2]

#validate input
if(root_dir != None and keyword != None) :

    #find all file which is in text format and itarate over it
    #  for root, dirs in os.walk(root_dir):
    wordcount(root_dir, result, keyword)
    stack.append(root_dir)
    #iterate until all sub dir get visited
    while len(stack) != 0:
        if(len(stack) != 0):
            head = stack.pop()
            stack_dir(head,stack)
            if(head != None):
                    wordcount(head,result,keyword)


#print out put
print(result)

#plot output
if (result != None):
    x = result.keys()
    y = result.values()
    plt.rcParams.update({'font.size': 10})
    plt.plot(x,y)
    plt.show()

#test case

#To check valid case
#python WordCountTree.py /Users/riddhi/Desktop riddhi

#To check invalide input
#python WordCountTree.py
#python WordCountTree.py /Users/riddhi/Desktop

#Few test cases we can by making tree folder stucture and compare flat structure with it








