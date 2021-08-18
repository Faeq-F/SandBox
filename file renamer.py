import os
import time
basedir = 'E:/Music/'
artistname = input('Please enter the artist name: ')
basedir = basedir + artistname
albumname = input('Please enter the album name: ')
if albumname == '':
    time.sleep(0)
else:
    basedir = basedir + '/' + albumname
remove = input('Enter the string you want to remove: ')
for fn in os.listdir(basedir):
    print(fn)
    b = fn
    c = fn
    if remove in fn:
        print('\nedited\n')
        os.rename(os.path.join(basedir,fn),os.path.join(basedir,fn.replace(remove,'')))
    else:
        print('\nno edit needed\n')
