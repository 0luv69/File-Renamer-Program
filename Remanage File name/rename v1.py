import os

filename = input("Enter your location:\t")
lists = os.listdir(filename)
file_type = input("Enter the extention [without \'.\']:\t")
new_name = input("Enter new name:\t")
o = 1

for i in lists:

    try:
        file_typetype_check = (i.split("."))[-1]
        if file_type.upper() == file_typetype_check.upper():
            os.rename((f"{filename}/{i}"),(f"{filename}/{new_name}_{o}.{file_typetype_check}"))
            print(f"{filename}/{new_name}_{o}.{file_typetype_check}")
            o=o+1
            
    except Exception as error:
        print(error)
        pass
    
input("Hit enter to close:\t")    

