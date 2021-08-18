import os
basedir = 'F:/To sort out folder/Music/'
artistname = input('Please enter the artist name: ')
basedir = basedir + artistname
for fn in os.listdir(basedir):
    print(fn)
    b=fn
    f=b
    if fn[-9:] == '- YouTube':
        print('edited:')
        f=f[:-9]
        print(f)
        os.rename(os.path.join(basedir, b),os.path.join(basedir, f))
    else:
        print('\nno edit needed\n')

exitt = input('[Press any key to exit]')
