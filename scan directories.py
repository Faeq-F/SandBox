import os
from os import listdir
import json
# List all files in a directory using os.listdir
dirs2Search = [os.environ['HOME']]
allDirs = []

def mergeSort(alist):

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

for i in dirs2Search:
    #list with all apps
    #all files in portable apps directory
    files = []
    #adding items to above lists
    # r=root, d=list of directories, f = list of files
    for r, d, f in os.walk(Home):
        for file in f:
            #adds the directory to the file to the sublist
            location = os.path.join(r, file)    
            #adds directory to sublist
            item = [['type:','file'],['name:',file],['path:', location]]
            #adds executable to list
            allDirs.append(item)
        for folder in d:
            #adds the directory to the file to the sublist
            location = os.path.join(r, folder)    
            #adds directory to sublist
            item = [['type:','folder'],['name:',folder],['path:', location]]
            #adds executable to list
            allDirs.append(item)


allDirs = mergeSort(allDirs)
json_string = json.dumps(allDirs)
f = open("paths.json", "w")
f.write(json_string)
f.close()
