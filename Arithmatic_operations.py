import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print(var)
var["C"]=var["A"]+var["B"]
print(var)
print(type(var))

var1=pd.DataFrame({"A":[10,20,30,40],"B":[5,16,17,18]})
print(var1)
var1["C"]=var1["A"]-var1["B"]
print(var1)
print(type(var1))

var2=pd.DataFrame({"A":[10,20,30,40],"B":[1,2,3,4]})
print(var2)
var2["C"]=var2["A"]*var2["B"]
print(var2)
print(type(var2))

var3=pd.DataFrame({"A":[10,20,30,40],"B":[1,2,3,4]})
print(var3)
var3["C"]=var3["A"]//var3["B"]
print(var3)
print(type(var3))

var4=pd.DataFrame({"A":[10,17,26,19],"B":[1,2,3,4]})
print(var4)
var4["C"]=var4["A"]%var4["B"]
print(var4)
print(type(var4))

v=pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})
print(v)
v["P"]=v["A"]>=20
print(v)
v["P"]=v["B"]<=20
print(v)








