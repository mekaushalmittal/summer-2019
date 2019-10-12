import pandas as pd
import json


data1 = pd.read_csv("train.tsv", sep="\t", header=0)
data2 = pd.read_json("document_passages.json")

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
temp =df1

Q= temp['Question']
DI= temp['DocumentID']
RPs= temp['RelevantPassages']

temp2 =[]
for x in range(len(RPs)):
    # [[dID, [p1ID,p2ID, ...]],  [[344],[0,1,2]], ...]
    temp2.append([DI[x], list(map(int, RPs[x].split(",")))])


T=[]
for x in temp2:
    for y in x[1]:
        t=""
        print(x[0], y)

        t += df2[x[0]][y] 
    T.append(t)


df3 = pd.DataFrame(data={"Question":Q, "Text":T})
df3.to_csv("./train_extracted.csv", sep=",", index=False)
print(df3)