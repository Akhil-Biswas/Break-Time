import os

def saveimage(folder,file,item):
    # verify image ()
    _, ext = os.path.splitext(file.filename)
    ''' os.path.splitext(file.filename) retutn tuple (filename. ext)
   we need only 2 velue 
     '''
    filename = f"{item}{ext}"
    filepath = os.path.join(folder,filename)
    file.save(filepath)
    print("file saved")