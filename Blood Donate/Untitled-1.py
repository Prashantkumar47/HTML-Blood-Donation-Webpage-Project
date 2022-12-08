file1 = open("MyFile.txt","a")
file1.close()
file1 = open("myfile.txt","w")
L = ["This is me \n","This is u \n","This is r \n"]
file1.writelines(L)
file1.close()