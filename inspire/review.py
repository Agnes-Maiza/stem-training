str_="19*54"
if "*" in str_:
    y=str_.index("*")
    f_no= float(str_[:y])
    s_no= float(str_[(y+1):])
    res=f_no*s_no
    print(res)
    
