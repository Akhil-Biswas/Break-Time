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
    
def getimage(folder,itemid,default="default.jpg"):
    for ext in [".png", ".jpg", ".jpeg", ".gif"]:
        filename = f"{itemid}{ext}"
        if os.path.exists(os.path.join(folder, filename)):
            return filename
    return default
    
if __name__ == '__main__':
    a =getimage('/storage/emulated/0/Break-Time/static/.images/items',3)
    print (a)