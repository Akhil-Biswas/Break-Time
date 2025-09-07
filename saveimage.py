import os

def saveimage(folder,file):
    # verify image ()
    filename =file.filename
    filepath = os.path.join(folder,filename)
    file.save(filepath)
    print("file saved")