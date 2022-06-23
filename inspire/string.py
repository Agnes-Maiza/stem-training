#string - can also be indexed as lists.
str = "hello class"
print(str[5])
print(str[6])
print(str[7-3])

strg = ["hello","class","123","51","abc","Hey",'b','a']
print(strg)
print(strg[5])
print(strg[6])
print(strg[7-3])
strg[0] = strg[7-2]
print(strg)

#lists can not be readdressed like this
subjects= ["math","science","religious"]
subjects[2]= "mechanics"
print(subjects)