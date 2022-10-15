import numpy as np
import pandas as pd



ppl = pd.read_csv("./security_logs.csv")

ppl_sorted = ppl.sort_values("Student ID")
print(ppl_sorted)

temp = ppl_sorted.groupby("Student ID")["Location"].value_counts()
#print(temp)
temp2 =ppl_sorted.groupby(['Student ID']).apply(lambda x: x['Location'].value_counts().index[0])
#print(temp2)
json_file = temp2.to_json()
print(json_file)
