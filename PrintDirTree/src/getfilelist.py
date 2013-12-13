#****************************************************************************************
#
# PrintDirTree - printout Dir tree and file names
#
#****************************************************************************************
import os
import sys 

currentPath = os.path.dirname(os.path.abspath(__file__))
#print currentPath

#dir2list = "E:\MyPlace\MyDocs\UnSorted"
dir2list = currentPath
'''
files = os.listdir(dir2list); 
for i in range(0,len(files)):
    print files[i]
'''
f = open('filenamelist.txt','w')

for root, dirs, files in os.walk(dir2list):
    print
    f.write("------------------------------------\n")
    
    print root
    f.write(root+'\n')
    
    print "------------------------------------"
    f.write("------------------------------------\n")
    
    for filename in files:
        #if file.endswith(".txt"):
        print os.path.join('', filename)
        f.write(filename+'\n')

f.close()

