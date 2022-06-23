#Opening and editing files in python
role_file=open("Roles.txt","r")#r-read,w-write,r+-read and write,a-append
print(role_file.readlines())
#close file
role_file.close()
#Append
role_file=open("Roles.txt","a")
role_file.write("I also love gaming")
role_file.close()
#read
role_file=open("Roles.txt","r")
words=role_file.read()
print(words)
role_file.close()
#write
role_file=open("Roles.txt","a")
role_file.write("\nI also love gaming")
role_file.close()
