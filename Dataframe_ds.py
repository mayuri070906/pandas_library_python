import pandas as pd
l=[1,2,3,4,5,6]
var=pd.DataFrame(l)
print(var)
print(type(var))

list_1=[[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25]]
v1=pd.DataFrame(list_1)
print(v1)
print(type(v1))

d={"x":[1,2,3,4,5],"y":[3,4,5,6,7],"z":[6,7,8,9,9]}
var1=pd.DataFrame(d)
print(var1)
print(type(var1))

var2=pd.DataFrame(d,columns=["x","z"])
print(var2)
print(type(var2))

var3=pd.DataFrame(d,index=["a","b","c","d","e"])
print(var3)
print(type(var3))

#how to get perticular number
dir={"a":[1,2,3,4,5],"b":[3,4,5,6,7],"c":[6,7,8,9,9],"d":[10,5,7,24,3]}
v=pd.DataFrame(dir)
print(v)
print(v["d"][3])

# how to create Dataframe using series ds
sr={"m":pd.Series([1,2,3,4,5]),"d":pd.Series([1,2,3,4,5])}
v2=pd.DataFrame(sr)
print(v2)
print(type(v2))








