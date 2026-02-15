import pandas as pd
csv_1=pd.read_csv("C:\\pandas\\Test_new1.csv")
print(csv_1)
print(type(csv_1))

csv_2=pd.read_csv("C:\\pandas\\Test_new1.csv",nrows=3)
print(csv_2)
print(type(csv_2))

csv_3=pd.read_csv("C:\\pandas\\Test_new1.csv",usecols=["a","c"])
print(csv_3)
print(type(csv_3))

csv_4=pd.read_csv("C:\\pandas\\Test_new1.csv",skiprows=[1])
print(csv_4)
print(type(csv_4))

csv_5=pd.read_csv("C:\\pandas\\Test_new1.csv",index_col="a")
print(csv_5)
print(type(csv_5))

csv_6=pd.read_csv("C:\\pandas\\Test_new1.csv",header=2)
print(csv_6)
print(type(csv_6))

csv_7=pd.read_csv("C:\\pandas\\Test_new1.csv",names=["col1","col2","col3"])
print(csv_7)
print(type(csv_7))

csv_8=pd.read_csv("C:\\pandas\\Test_new1.csv",header=None)
print(csv_8)
print(type(csv_8))

csv_9=pd.read_csv("C:\\pandas\\Test_new1.csv",dtype={"c":"float"})
print(csv_9)
print(type(csv_9))





