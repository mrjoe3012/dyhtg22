import seaborn as sbs
import pandas as pd
import matplotlib.pyplot as plt
from yaml import FlowSequenceStartToken

location = pd.read_csv("./location_data.csv")
logs = pd.read_csv("./security_logs.csv")


print(logs)
#sbs.PairGrid(data = logs, vars=["Student ID", "Name", "Location", "Time"])



logs_time = logs["Time"].values.tolist()
logs_place = logs["Location"].values.tolist()
logs_place1 = location[["Building Name", "Opening Times"]].values.tolist()

enter = []
exit = []
tempy = []
for i in logs_place1:
    print(i)
    temp = i[1].split("-")
    enter.append(int(temp[0]))
    exit.append(int(temp[1]))
    tempy.append(i[0])

df_t = pd.DataFrame({
    "place":tempy,
    "entry time":enter,
    "exit time":exit
})


logs_entry = []
logs_exit = []
count = 0
for i in logs_time:
    temp = i.split("-")
    logs_entry.append(int(temp[0]))
    logs_exit.append(int(temp[1]))
temp = {}

etmp_df = pd.DataFrame({
   "place":logs_place,
   "entry time":logs_entry,
   "exit time":logs_exit
})

sbs.scatterplot(data = etmp_df, x="place", y = "entry time").set(title = "All entry times for the buildings")
sbs.scatterplot(data=df_t, x = "place", y = "entry time", hue = "entry time")
plt.xticks(rotation=45)
plt.savefig("entry_times")
plt.show()

sbs.scatterplot(data = etmp_df, x="place", y = "exit time").set(title= "All exit times for the buildings")
sbs.scatterplot(data=df_t, x = "place", y = "exit time", hue = "exit time")
plt.xticks(rotation=45)
plt.savefig("exit_times")
plt.show()

for j in logs_place:
    temp1 = []












location_only = location["Building Name"].values.tolist()
logs_location = logs["Location"].values.tolist()


count = []
for i in location_only:
    counts = 0
    for j in logs_location:
        if j== i:
            counts +=1
    count.append(counts)

together = pd.DataFrame({
    'Building': location_only,
    'Frequency': count
})


ax = sbs.barplot(data=together, x = "Building", y = "Frequency").set(title = "Attendence Frequency of the Buildings")
plt.xticks(rotation=45)
plt.show()
#plt.savefig("Frequncy")






