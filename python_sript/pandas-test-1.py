import pandas as pd

df=pd.read_csv("Test_new.csv")

dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}

d=pd.DataFrame(dis)

print(dis)
dis["a"].append(7)
print(dis)

df=pd.concat([df,dis])
d.to_csv("Test_new1.csv")