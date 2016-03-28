import os;


def rename_files():
    #list all the files
    filenames = os.listdir(r"C:\Users\Dell\Downloads\prank\prank")
    print(filenames)
    x = os.getcwd()
    print(x)
    os.chdir(r"C:\Users\Dell\Downloads\prank\prank")
    for file in filenames:
        os.rename(file,file.translate((str.maketrans('','','0123456789'))))
    #os.chdir(x)

rename_files()
