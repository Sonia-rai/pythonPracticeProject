#oh!! soldier Prettify my folder
# Create a function that takes 3 input arguments
# 1.Check all te iles present in whole folder,path are given as an input
# 2.Then capitalize first letter of each word whih are not presnt in file
# 3.The func renames the files to number whoses format is given bu user

import os
def soldier (path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open (file) as f:
        fileslist=f.read().split("\n")

    for filee in files:
        if filee not in fileslist:
            os.rename(filee,filee.capitalize())

        if os.path.splitext(filee)[1]==format:
            os.rename(filee,f"{i}.{format}")
            i=i+1

soldier(r"C:\Users\Dell\OneDrive\Desktop\important hain",
        r"C:\Users\Dell\OneDrive\Desktop\important hain\ext.txt",
        "jpg")
