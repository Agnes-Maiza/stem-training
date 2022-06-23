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