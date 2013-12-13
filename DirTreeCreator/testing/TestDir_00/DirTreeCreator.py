#****************************************************************************************
#
# DirTreeCreator - generating folder tree from given file
#
#****************************************************************************************
import os
import sys

script_name = "Folder tree parser/generator"
script_version = "v1.0"

print
print script_name,script_version
print
    
treeList = []
if (len(sys.argv)<3) :
    print "DirTreeCreator.py -g filename" 
    print "    build a folders list for existing folder tree into the filename file"
    print "DirTreeCreator.py -c filename"
    print "    create folder tree based on folder list given in file filename"
    sys.exit(0)


if (sys.argv[1] == "-c") :
    tree_to_create_file_name = sys.argv[2]
    
    f = open(tree_to_create_file_name,'r')
    tree_to_create_list = []
    for string in f:
        tree_to_create_list.append( string.strip() )
    f.close()
        
    for i in range(0,len(tree_to_create_list)) :
        if not os.path.exists(tree_to_create_list[i]): 
            os.makedirs(tree_to_create_list[i])
    print "Folder tree has been generated at",tree_to_create_list[0]
    print "Done!"
    
elif (sys.argv[1] == "-g") :
    currentPath = os.path.dirname(os.path.abspath(__file__))
    tree_to_create_file_name = sys.argv[2]
    f = open(tree_to_create_file_name,'w')
    
    for root, dirs, files in os.walk(currentPath):
        treeList.append(root)
        #print root
        f.write(root+'\n')
        
    f.close()
    print "File",tree_to_create_file_name, "has been generated."
    print "Done!"
         
else :
    print "DirTreeCreator.py -g filename" 
    print "    build a folders list for existing folder tree into the filename file"
    print "DirTreeCreator.py -c filename"
    print "    create folder tree based on folder list given in file filename"
    sys.exit(0)
