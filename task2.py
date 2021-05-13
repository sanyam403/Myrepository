filename = input("Input the Filename: ")
file_list = filename.split(".")
c = str(file_list[-1])
if c == 'py': 
    print("The extension of the file is: 'python'")
if c == 'cc':
    print("The extension of the file is: 'C++'")
if c == 'c':
    print("The extension of the file is: 'C'")
