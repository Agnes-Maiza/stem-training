'''
Create one function (and run it) that does the following:
**For a range of integers between 0 and n (inclusive) if the number is an even number ,half it .
If it is an odd number,double it
**For the output generated in the previous function, write the results to a file.Name the file 'results.txt'
'''
outf=open("results.txt","a")
def even_odd(n):
    for x in range(n+1):
        if x%2==0:
            x/=2
            outf.write(str(x))
            outf.write("\n")
        else:
            x*=2
            outf.write(str(x))
            outf.write("\n")

even_odd(5)
outf.close()
print("the file has been updated succesfuly")