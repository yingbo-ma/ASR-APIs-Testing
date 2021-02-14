import os
# switch to raw dir
os.chdir("C:\\Users\\Yingbo\\Desktop\\ENGAGE dataset\\ENGAGE Coded Transcriptions\\Previous\\paste_with_values")
# check the current path
print(os.getcwd())
# list all files under current directory
dirs = os.listdir()
# switch dirs to test_ENGAGE path
os.chdir("C:\\Users\\Yingbo\\Desktop\\ENGAGE_test")
# check the current path
print(os.getcwd())
# read each file name
for file in dirs:
    filename = file.split('.')[0]
    os.mkdir(filename)

